# Let's Encrypt DNS-01
DNS-01 Challenge with Google Cloud DNS and Traefik.

Traefik uses [LEGO][a] internally to configure certificates. Certificates will
be auto provisioned based on configured routers and base domains.

!!! warning
    Traefik **must** be able to directly query authoritative DNS servers to
    validate record change **before** issuing a ACME certificate request.
    Otherwise "Waiting for DNS record propagation" will run until it times out.

    Disable **destination/source/captive DNS** for proxy host **or** disable
    propagation check and delay the required SLA time for DNS record update.

## Create Google Cloud Service Account

Create service account with DNS administrator privileges.
!!! abstract "console.cloud.google.com ➔ ctrl + o ➔ {PROJECT} ➔ APIs & Services ➔ Credentials ➔ Create credentials ➔ Service account"
    * Create service account:
        * Service account name: **traefik acme**
        * Service account ID: **{AUTO_GENERATED}**
        * Service account description: **Traefik DNS-01 ACME Challenges**
    * Permissions: **DNS Administrator**
    * Principals with access: **None**

Generate JSON keys
!!! abstract "console.cloud.google.com ➔ ctrl + o ➔ {PROJECT} ➔ IAM & Admin ➔ Service accounts ➔ traefik acme ➔ ⋮ ➔ Manage keys"
    * Add key ➔ Create new key: JSON

    Download JSON key as **traefik_acme.json**.


## Add LEGO environment variables to service
!!! tip
    This can be done through **r_pufky.srv.traefik** with:

    ``` bash
    traefik_srv_env:
      - var: 'GCE_PROJECT'
        value: '{PROJECT_ID}'
      - var: 'GCE_SERVICE_ACCOUNT_FILE'
        value: '/etc/traefik/traefik_acme.json'
    ```

!!! abstract "/etc/systemd/system/traefik.service"
    0644 root:root
    ``` bash
    [service]
    ...
    Environment="GCE_PROJECT={PROJECT_ID}"
    Environment="GCE_SERVICE_ACCOUNT_FILE=/etc/traefik/traefik_acme.json"
    ...
    ```


## Configure DNS-01 Certificate challenge with Google Cloud DNS

!!! abstract "/etc/traefik/traefik.yml"
    0640 traefik:traefik
    ``` yaml
    ---
    log:
      level: 'DEBUG'
      format: 'json'
    accessLog:
      format: 'json'
    api:
      dashboard: true
      disableDashboardAd: true
      insecure: false
      debug: true
    serversTransport:
      insecureSkipVerify: true
    entryPoints:
      web:
        address: ':80'
        http:
          redirections:
            entryPoint:
              to: 'webs'
              scheme: 'https'
              permanent: true
      webs:
        address: ':443'
        asDefault: true
        http:
          # Use Let's Encrypt with DNS-01 Challenges.
          tls:
            certResolver: 'lets_encrypt'
          domains:
          - main: 'example.com'  # Main domain.
            sans: '*.example.com'  # Wildcard certificates.
          middlewares:
            - 'global_rate_limit@file'
            - 'basic_auth_users@file'
            - 'default_error_page@file'
    providers:
      file:
        directory: '/etc/traefik/dynamic'
        watch: true

    # Use gcloud DNS with LEGO for ACME certificates.
    certificatesResolvers:
      lets_encrypt:
        acme:
          email: 'contact@example.com'
          storage: '/var/lib/traefik/acme_staging.json'  # For staging certs.
          # Initial configuration with staging server.
          # Only 50 certificates may be issued in a week.
          # caServer: 'https://acme-v02.api.letsencrypt.org/directory'
          caServer: 'https://acme-staging-v02.api.letsencrypt.org/directory'
          # LEGO environment configured in traefik_srv_env.
          dnsChallenge:
            provider: 'gcloud'
            # Set to DNS authoritative name servers for your domain.
            # Found in Cloud DNS ➔ Registrar Setup
            resolvers:
              - 'ns-cloud-e1.googledomains.com.'
              - 'ns-cloud-e2.googledomains.com.'
              - 'ns-cloud-e3.googledomains.com.'
              - 'ns-cloud-e4.googledomains.com.'
            propagation:
              delayBeforeChecks: '120s'  # 120 is SLA for gcloud DNS update.
              # Only disable if caching or captive DNS upstream servers
              # interfere with proxy host resolving DNS updates for ACME
              # challenges.
              disableChecks: true
    ```

## Validate Configuration.
Start Traefik and search logs.

Google cloud DNS console may be checked for **_acme-challenge.{DOMAIN}** change
which indicates that the service account works correctly.

!!! abstract "journalctl -u traefik"
    ``` bash
    [INFO] acme: Registering account for contact@example.com"}
    "message":"Using DNS Challenge provider: gcloud"}
    [INFO] [example.com, *.example.com] acme: Obtaining bundled SAN certificate"}
    [INFO] [*.example.com] AuthURL: https://acme-staging-v02.api.letsencrypt.org/acme/authz/243572763/20286930863"}
    [INFO] [example.com] AuthURL: https://acme-staging-v02.api.letsencrypt.org/acme/authz/243572763/20286930873"}
    [INFO] [*.example.com] acme: use dns-01 solver"}
    [INFO] [example.com] acme: Could not find solver for: tls-alpn-01"}
    [INFO] [example.com] acme: Could not find solver for: http-01"}
    [INFO] [example.com] acme: use dns-01 solver"}
    [INFO] [*.example.com] acme: Preparing to solve DNS-01"}
    [INFO] [*.example.com] acme: Trying to solve DNS-01"}
    [INFO] [*.example.com] acme: Checking DNS record propagation. [nameservers=ns-cloud-e1.googledomains.com.:53,ns-cloud-e2.googledomains.com.:53,ns-cloud-e3.googledomains.com.:53,ns-cloud-e4.googledomains.com.:53]"}
    [INFO] Wait for propagation [timeout: 3m0s, interval: 5s]"}
    [INFO] [*.example.com] The server validated our request"}
    ```


## Set Live Certificates
Once confirmed swap to the live certificate server.

!!! abstract "/etc/traefik/traefik.yml"
    0640 traefik:traefik
    ``` yaml
    certificatesResolvers:
      lets_encrypt:
        acme:
          email: 'contact@example.com'
          storage: '/var/lib/traefik/acme.json'  # For live certs.
          # Live cert server.
          caServer: 'https://acme-v02.api.letsencrypt.org/directory'
          dnsChallenge:
            provider: 'gcloud'
            resolvers:
              - 'ns-cloud-e1.googledomains.com.'
              - 'ns-cloud-e2.googledomains.com.'
              - 'ns-cloud-e3.googledomains.com.'
              - 'ns-cloud-e4.googledomains.com.'
            propagation:
              delayBeforeChecks: '120s'
              disableChecks: true
    ```

``` bash
systemctl restart traefik
```

## Reference[^1][^2][^3][^4]

[a]: https://go-acme.github.io/lego/dns/gcloud/index.html

[^1]: https://doc.traefik.io/traefik/reference/install-configuration/tls/certificate-resolvers/acme
[^2]: https://old.reddit.com/r/Actualfixes/comments/wgdd1n/fix_traefik_dns_certificate_time_limit_exceeded
[^3]: https://medium.com/@svenvanginkel/traefik-letsencrypt-dns01-challenge-with-ovhcloud-52f2a2c6d08a
[^4]: https://betatim.github.io/posts/traefik-config-bare-metal
[^5]: https://old.reddit.com/user/germanpickles/comments/1i07bw9/enable_mtls_for_traefik