# Mail

!!! note
    All examples use **example.com** replace with your DNS domain name.

## DNS
Setup DNS with [DNSSEC/DANE][a] using Google Cloud DNS.

!!! warning
    Captive DNS services must be configured to handle DNSSEC verification or
    validation will break.

    **Disable** captive DNS for mail server to test DNSSEC verification works.

### Static DNS Resolvers
!!! abstract "/etc/resolv.conf"
    0644 root:root
    ``` bash
    search example.com.

    # Use cloudflare - does not sell user data.
    nameserver 1.1.1.1
    nameserver 1.0.0.1

    # Enable extended DNS attributes and propagate authenticated domain trust.
    options edns0 trust-ad
    ```

### Set Mail Hostname
Mail servers are generally hosted on a **mail** subdomain to enable transparent
backend changes as well as main domain separation. A mail hostname does **not**
need to match the machine hostname to server mail.

!!! example "console.cloud.google.com ➔ ctrl + o ➔ {DNS} ➔ Network Services ➔ Cloud DNS ➔ {DOMAIN} ➔ Edit"
    * DNSSEC: **On**

!!! example "console.cloud.google.com ➔ ctrl + o ➔ {DNS} ➔ Network Services ➔ Cloud DNS ➔ {DOMAIN}"
    * Add standard:
        * DNS name: **mail.example.com**
        * Resource control type: **A**
        * TTL: **5**
        * TTL Unit: **minutes**
        * IPv4 Address: **{PUBLIC_IP}**

    See [r_pufky.srv.gcp_ddns][b] for automatically updating your public IP.

``` bash
# Verify DNSSEC from mail server.

# RRSIG must appear for DNSSEC/DANE mail configuration.
delv mail.example.com.
> ; fully validated
> mail.example.com.		300	IN	A	50.39.134.131
> mail.example.com.		300	IN	RRSIG	A 8 3 300 20251210160823 20251118160823 59571 example.com. {HASH}/c {HASH}/fb k4w=

# AD (authenticated domain) must appear for DNS entry.
dig mail.example.com

# Additionally test local DNS resolver if running.
dig @127.0.0.1 mail.example.com

# ad must appear in flags.
> ; <<>> DiG 9.20.15-1~deb13u1-Debian <<>> mail.example.com
> ;; global options: +cmd
> ;; Got answer:
> ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 53402
> ;; flags: qr rd ra ad; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1
>
> ;; OPT PSEUDOSECTION:
> ; EDNS: version: 0, flags:; udp: 512
> ;; QUESTION SECTION:
> ;mail.example.com.			IN	A
>
> ;; ANSWER SECTION:
> mail.example.com.		300	IN	A	50.39.134.131
>
> ;; Query time: 88 msec
> ;; SERVER: 1.1.1.1#53(1.1.1.1) (UDP)
> ;; WHEN: Thu Nov 20 21:09:44 UTC 2025
> ;; MSG SIZE  rcvd: 59
```

Verify Mox resolves the same.
``` bash
mox -loglevel debug dns lookup a mail.example.com

# authentic=true and 'with dnssec' must be returned to validate.
> debug: dns lookup result; pkg=dns; type=ip; network=ip4; host=mail.example.com.; resp=[X.X.X.X]; authentic=true; duration=81.866448ms
> records (1, with dnssec):
> - X.X.X.X
```

[a]: https://galaxy.ansible.com/ui/repo/published/r_pufky/srv/docs
[b]: https://stackoverflow.com/questions/1348126/postgresql-modify-owner-on-all-tables-simultaneously-in-postgresql

## Traefik
Pass traffic through proxy without modification. This allows the mail server to
change on the backend without needing to changing firewall rules on the router.
See [ACME Behind Traefik][e] for detailed information.

Forward ports to traefik TCP: 25, 465, 587, 143, 993


!!! abstract "/etc/traefik/traefik.yml"
    0644 root:root
    ``` yaml
    entryPoints:
      # Defer TLS requirements to routers.
      web:
        address: ':80'
      webs:
        address: ':443'
        asDefault: true
      # Passthrough mail routing.
      smtp:
        address: ':25'
      smtps:
        address: ':465'
      submission:
        address: ':587'
      imap:
        address: ':143'
      imaps:
        address: ':993'
    ```

??? abstract "/etc/traefik/dynamic/mail.yml"
    0644 root:root
    ``` yaml
    http:
      routers:
        mail_http01:
          rule: 'PathPrefix(`/.well-known/acme-challenge/`) && (Host(`mail.example.com`) || Host(`autoconfig.example.com`) || Host(`mta-sts.example.com`))'
          entryPoints:
            - 'web'
          priority: 1000
          service: 'mail_http01_service'

        mail_webmail:
          rule: 'ClientIP(`10.2.2.80`) && Host(`mail.example.com`) && PathPrefix(`/webmail`)'
          entryPoints:
            - 'webs'
          tls:
            certResolver: 'lets_encrypt'
            domains:
              - main: 'example.com'
                sans: '*.example.com'
          middlewares:
            - 'redirect_to_https'
          service: 'mail_webmail_service'

        mail_admin:
          rule: 'ClientIP(`10.2.2.80`) && Host(`mail.example.com`) && PathPrefix(`/admin`)'
          entryPoints:
            - 'webs'
          tls:
            certResolver: 'lets_encrypt'
            domains:
              - main: 'example.com'
                sans: '*.example.com'
          middlewares:
            - 'redirect_to_https'
          service: 'mail_admin_service'

      middlewares:
        redirect_to_https:
          redirectScheme:
            scheme: 'https'
            permanent: true

      services:
        mail_http01_service:
          loadBalancer:
            servers:
              - url: 'http://10.5.5.240:80'

        mail_webmail_service:
          loadbalancer:
            servers:
              - url: 'https://10.5.5.240/webmail'

        mail_admin_service:
          loadbalancer:
            servers:
              - url: 'https://10.5.5.240/admin'

    tcp:
      routers:
        mail_smtp:
          rule: 'HostSNI(`*`)'
          entryPoints:
            - 'smtp'
          service: 'mail_smtp_service'

        mail_smtps:
          rule: 'HostSNI(`*`)'
          entryPoints:
            - 'smtps'
          service: 'mail_smtps_service'

        mail_submission:
          rule: 'HostSNI(`*`)'
          entryPoints:
            - 'submission'
          service: 'mail_submission_service'

        mail_imap:
          rule: 'HostSNI(`*`)'
          entryPoints:
            - 'imap'
          service: 'mail_imap_service'

        mail_imaps:
          rule: 'HostSNI(`*`)'
          entryPoints:
            - 'imaps'
          service: 'mail_imaps_service'

      services:
        mail_smtp_service:
          loadbalancer:
            servers:
              - address: '10.5.5.240:25'

        mail_smtps_service:
          loadbalancer:
            servers:
              - address: '10.5.5.240:465'

        mail_submission_service:
          loadbalancer:
            servers:
              - address: '10.5.5.240:587'

        mail_imap_service:
          loadbalancer:
            servers:
              - address: '10.5.5.240:143'

        mail_imaps_service:
          loadbalancer:
            servers:
              - address: '10.5.5.240:993'
    ```

## Mox
!!! tip
    Increase **TTL** for configured entries after mail service is confirmed to
    work.

!!! warning
    Mox quickstart will not overwrite existing directories and files. If
    regenerating a quickstart configuration all directories and files must be
    deleted.

### Generate mail configuration
Configuration and certificates are generated in quickstart. Initial passwords
are logged in **quickstart.log**.
``` bash
mox quickstart -hostname mail.example.com postmaster@example.com
```
See [troubleshooting][c] to resolve quickstart issues.

### Update DNS Records
Use the generated mox certificates to configure DNS.

#### DANE TLS Associations
These only need to be created for the first hosted domain (machine based).

!!! example "console.cloud.google.com ➔ ctrl + o ➔ {DNS} ➔ Network Services ➔ Cloud DNS ➔ {DOMAIN}"
    * Add standard:
        * DNS name: **_25._tcp.mail.example.com.**
        * Resource control type: **TLSA**
        * TTL: **5**
        * TTL Unit: **minutes**
        * DANE TLS Association 1: **3 1 1 {HASH}**
        * DANE TLS Association 2: **3 1 1 {HASH}**

#### Relax DMARC SPF for postmaster messages
These only need to be created for the first hosted domain (machine based).

!!! example "console.cloud.google.com ➔ ctrl + o ➔ {DNS} ➔ Network Services ➔ Cloud DNS ➔ {DOMAIN}"
    * Add standard:
        * DNS name: **mail.example.com.**
        * Resource control type: **TXT**
        * TTL: **5**
        * TTL Unit: **minutes**
        * TXT data: **"v=spf1 a -all"**

    **Must** use double quotes for TXT data.

#### Enable TLS Failure Reporting
These only need to be created for the first hosted domain (machine based).

!!! example "console.cloud.google.com ➔ ctrl + o ➔ {DNS} ➔ Network Services ➔ Cloud DNS ➔ {DOMAIN}"
    * Add standard:
        * DNS name: **_smtp._tls.mail.example.com.**
        * Resource control type: **TXT**
        * TTL: **5**
        * TTL Unit: **minutes**
        * TXT data: **"v=TLSRPTv1; rua=mailto:tlsreports@mail.example.com"**

    **Must** use double quotes for TXT data.

#### Email delivery host (this mail server)
!!! example "console.cloud.google.com ➔ ctrl + o ➔ {DNS} ➔ Network Services ➔ Cloud DNS ➔ {DOMAIN}"
    * Add standard:
        * DNS name: **example.com.**
        * Resource control type: **MX**
        * TTL: **5**
        * TTL Unit: **minutes**
        * Preference and mail server 1: **10 mail.example.com.**

    Additional secondary mail servers may be added (e.g.
    **aspmx.l.google.com.**) to continue to accept mail on Google hosted mail
    until service is setup.

#### DKIM outgoing message signing keys
!!! example "console.cloud.google.com ➔ ctrl + o ➔ {DNS} ➔ Network Services ➔ Cloud DNS ➔ {DOMAIN}"
    * Add standard:
        * DNS name: **2025a._domainkey.example.com.**
        * Resource control type: **TXT**
        * TTL: **5**
        * TTL Unit: **minutes**
        * TXT data: **"{2025A_KEY}"**

    * Add standard:
        * DNS name: **2025a._domainkey.example.com.**
        * Resource control type: **TXT**
        * TTL: **5**
        * TTL Unit: **minutes**
        * TXT data: **"{2025B_KEY}"**

    Add all quoted lines to TXT field.

TODO - this record MUST be updated when IP changes.

#### [SPF Softfail][d]
Tag any email failing SPF checks (accept mail from old mail servers).

!!! example "console.cloud.google.com ➔ ctrl + o ➔ {DNS} ➔ Network Services ➔ Cloud DNS ➔ {DOMAIN}"
    * Add standard:
        * DNS name: **example.com.**
        * Resource control type: **TXT**
        * TTL: **5**
        * TTL Unit: **minutes**
        * TXT data: **"v=spf1 ip4:{IP} mx ~all"**

#### Reject DMARC failures and Request Reports
!!! example "console.cloud.google.com ➔ ctrl + o ➔ {DNS} ➔ Network Services ➔ Cloud DNS ➔ {DOMAIN}"
    * Add standard:
        * DNS name: **_dmarc.example.com.**
        * Resource control type: **TXT**
        * TTL: **5**
        * TTL Unit: **minutes**
        * TXT data: **"v=DMARC1;p=reject;rua=mailto:dmarcreports@example.com!10m"**

#### Enable MTA-STS TLS Certificate Validation
!!! example "console.cloud.google.com ➔ ctrl + o ➔ {DNS} ➔ Network Services ➔ Cloud DNS ➔ {DOMAIN}"
    * Add standard:
        * DNS name: **mta-sts.example.com.**
        * Resource control type: **CNAME**
        * TTL: **5**
        * TTL Unit: **minutes**
        * Canonical name: **mail.example.com.**

!!! example "console.cloud.google.com ➔ ctrl + o ➔ {DNS} ➔ Network Services ➔ Cloud DNS ➔ {DOMAIN}"
    * Add standard:
        * DNS name: **_mta-sts.example.com.**
        * Resource control type: **TXT**
        * TTL: **5**
        * TTL Unit: **minutes**
        * TXT data: **"v=STSv1; id=20251120T223212"**

#### Enable Client Autodiscovery
!!! example "console.cloud.google.com ➔ ctrl + o ➔ {DNS} ➔ Network Services ➔ Cloud DNS ➔ {DOMAIN}"
    * Add standard:
        * DNS name: **autoconfig.example.com.**
        * Resource control type: **CNAME**
        * TTL: **5**
        * TTL Unit: **minutes**
        * Canonical name: **mail.example.com.**

    * Add standard:
        * DNS name: **_autodiscover._tcp.example.com.**
        * Resource control type: **SRV**
        * TTL: **5**
        * TTL Unit: **minutes**
        * SRV data 1: **0 1 443 mail.example.com.**

#### Enable IMAP Autodiscovery
!!! example "console.cloud.google.com ➔ ctrl + o ➔ {DNS} ➔ Network Services ➔ Cloud DNS ➔ {DOMAIN}"
    * Add standard:
        * DNS name: **_imaps._tcp.example.com.**
        * Resource control type: **SRV**
        * TTL: **5**
        * TTL Unit: **minutes**
        * SRV data 1: **0 1 993 mail.example.com.**

    * Add standard:
        * DNS name: **_submissions._tcp.example.com.**
        * Resource control type: **SRV**
        * TTL: **5**
        * TTL Unit: **minutes**
        * SRV data 1: **0 1 465 mail.example.com.**

    Note trailing **S** signifies encryption.

#### Disable Unencrypted Submission Discovery
Extend DNS lifetimes as these services should never be enabled again.

!!! example "console.cloud.google.com ➔ ctrl + o ➔ {DNS} ➔ Network Services ➔ Cloud DNS ➔ {DOMAIN}"
    * Add standard:
        * DNS name: **_imap._tcp.example.com.**
        * Resource control type: **SRV**
        * TTL: **1**
        * TTL Unit: **weeks**
        * SRV data 1: **0 0 0 .**

    * Add standard:
        * DNS name: **_submission._tcp.example.com.**
        * Resource control type: **SRV**
        * TTL: **1**
        * TTL Unit: **weeks**
        * SRV data 1: **0 0 0 .**
    * Add standard:
        * DNS name: **_pop3._tcp.example.com.**
        * Resource control type: **SRV**
        * TTL: **1**
        * TTL Unit: **weeks**
        * SRV data 1: **0 0 0 .**
    * Add standard:
        * DNS name: **_pop3s._tcp.example.com.**
        * Resource control type: **SRV**
        * TTL: **1**
        * TTL Unit: **weeks**
        * SRV data 1: **0 0 0 .**

#### Require Let's Encrypt Certificates for TLS Signatures
!!! example "console.cloud.google.com ➔ ctrl + o ➔ {DNS} ➔ Network Services ➔ Cloud DNS ➔ {DOMAIN}"
    * Add standard:
        * DNS name: **example.com.**
        * Resource control type: **CAA**
        * TTL: **5**
        * TTL Unit: **minutes**
        * Certificate Authority Authorization 1: **0 issue "letsencrypt.org"**

### Verify DNS Records
``` bash
# Confirm DNS propagated for DNSSEC/DANE.
dig +dnssec +noall +answer +multi _25._tcp.mail.example.com. TLSA
_25._tcp.mail.example.com. 300 IN	TLSA 3 1 1 (
				{HASH}
        )
_25._tcp.mail.example.com. 300 IN	TLSA 3 1 1 (
				{HASH}
        )
_25._tcp.mail.example.com. 300 IN	RRSIG TLSA 8 5 300 (
				20251210160823 20251118160823 59571 example.com.
				{HASH}
        )
```

### Confirm Configuration

TODO - setup letsencrypt

!!! abstract **/data/mail/mox/config/mox.config**
    0660 mox:mox
    ``` yaml
    Listeners:
	    internal:
        # Internal/Private IP's only.
		    IPs:
		    	- 127.0.0.1
		    	- ::1
public:
    IPs:
      # Use 0.0.0.0 and :: for all IPv4/IPv6 addresses.
      #
      # This should be your host IP.
      - {IP}

    # Update whenever public IP changes.
		NATIPs:
			- {EXTERNAL_IP}

		# Use HTTP
		WebserverHTTP:
			Enabled: true

		# Use HTTPS
		WebserverHTTPS:
			Enabled: true

TODO: /data/mail/mox/mox.config NEEDS TO BE UPDATED WHEN PUBLIC IP CHANGES!.


## Reference[^1]

[^1]: https://community.hetzner.com/tutorials/install-and-configure-mailserver-mox-on-debian

[a]: https://datatracker.ietf.org/doc/html/rfc7671
[b]: https://galaxy.ansible.com/ui/repo/published/r_pufky/srv
[c]: troubleshooting.md
[d]: https://en.wikipedia.org/wiki/Sender_Policy_Framework
[e]: ../traefik/acme/behind_traefik.md#http-01
