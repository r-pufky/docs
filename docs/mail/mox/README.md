# [Mox][a]
A modern, secure, all-in-one email server.

A single binary simplifying 30+ years of bolt on services for postfix. Most
modern stacks should run this or a hosted solution.

## Key Concepts
A **mox** account is separate from **domain** and **email**. A single account
can have multiple addresses in the domain as well as multiple domains. Accounts
need to have an initial domain.

## Local Machine Resolver
Setup DNSSEC local resolver for Mox. Configure [DNS Mail Hostname][b] before
proceeding.

=== "Unbound"
    ``` bash
    apt install unbound unbound-anchor
    ```

    !!! abstract "/etc/resolv.conf"
        0644 root:root
        ``` bash
        search example.com.

        nameserver 127.0.0.1  # Force DNS resolution through unbound DNSSEC.
        ```

    !!! abstract "/etc/unbound/unbound.conf.d/ede.conf"
        0644 root:root
        ``` bash
        server:
            ede: yes
            val-log-level: 2
        ```

    ``` bash
    # Verify root auto trust anchor was installed.
    cat /etc/unbound/unbound.conf.d/root-auto-trust-anchor-file.conf
    > auto-trust-anchor-file: "/var/lib/unbound/root.key"

    ls /var/lib/unbound/root.key # confirm exists.

    # Run as mox user and confirm mox resolves DNS using DNSSEC.
    mox dns lookup ns com.
    > ns records (13, with dnssec):  # with DNSSEC confirms DNSSEC is working for this system.
    > - &{c.gtld-servers.net.}
    > - &{i.gtld-servers.net.}
    > - &{d.gtld-servers.net.}
    > - &{f.gtld-servers.net.}
    > - &{a.gtld-servers.net.}
    > - &{k.gtld-servers.net.}
    > - &{h.gtld-servers.net.}
    > - &{g.gtld-servers.net.}
    > - &{b.gtld-servers.net.}
    > - &{j.gtld-servers.net.}
    > - &{e.gtld-servers.net.}
    > - &{m.gtld-servers.net.}
    > - &{l.gtld-servers.net.}
    ```

=== "Opportunistic TLS"
    !!! danger "Opportunistic TLS must be used when not using unbound"
        In today's world this is extremely dangerous. Only do this if unbound
        cannot be used.

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

## Generate mail configuration
Configuration and certificates are generated in quickstart. Initial passwords
are logged in **quickstart.log**. 

``` bash
ssh -L 8080:localhost:80 mail.example.com  # Forward ports to access WebUI.
su - mox -s /bin/bash
cd /var/opt/mox
mox quickstart -hostname mail.example.com postmaster@example.com -quickstart -skipdial
```

!!! info
    Mox quickstart will **not** overwrite existing directories and files. All
    options may be configured dynamically via http://localhost:8080/admin or
    **domains.conf** and **mox.conf**.

[Update DNS Records][d] before proceeding.

### Confirm Configuration

!!! warning "NATIPs MUST be updated when IP changes"

!!! abstract "/data/mail/mox/config/mox.config"
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
    ```

## Importing Mail
Mox uses a local per-user database index on top of a maildir like format. 

Destination mailbox will automatically be created if it does not exist for the
Mox user. See [disabling spam and junk filters][f] for import failures.

``` bash
# Maildir must be in a readable location for mox. Typically /var/opt/mox/data.
$ mox import maildir mox_user Archive/import /var/opt/mox/data/import/Maildir
```

Use [recursive Maildir import script][e] to recursively import user Maildir.

## Client Configuration
A webmail interface is provided over localhost by default. Auto client
configuration is enabled by default via DNS entries. This **will** fail if
using test ACME certificates.

  Protocol          | Server           | Port | Exposure | Security
 -------------------|------------------|------|----------|----------
  Submission (SMTP) | mail.example.com | 465  | public   | with TLS
  IMAP              | mail.example.com | 993  | public   | with TLS

Use the first supported encryption option (order of security):

* SCRAM-SHA-256-PLUS
* SCRAM-SHA-1-PLUS
* SCRAM-SHA-256
* SCRAM-SHA-1
* CRAM-MD5

## Reference[^1]
[^1]: https://community.hetzner.com/tutorials/install-and-configure-mailserver-mox-on-debian

[a]: https://www.xmox.nl/
[b]: dns.md#set-mail-hostname
[c]: ../../network/traefik/mox.md
[d]: dns.md#update-dns-records
[e]: https://github.com/r-pufky/import_maildir_mox
[f]: troubleshooting.md#mail-import-fails
