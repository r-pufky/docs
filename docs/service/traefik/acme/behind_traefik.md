# Behind Traefik
Traefik will intercept and block ACME certificate resolvers behind it unless
explicitly enabled.

!!! danger "Here Be Dragons"
    Requires pushing TLS enforcement from the entrypoint to each router. All
    routers **must** ensure TLS is enforced if required.

## HTTP-01
Enables host and prefix matching to direct ACME challenges to the correct
backend to validate challenges.

!!! tip "Highly Recommended"
    Use **DNS-01** challenges for Traefik configuration and **HTTP-01**
    challenges for backend service ACME challenges.

    HTTP-01 challenges [may be used for Traefik][c] with some additional
    configuration.

!!! abstract "/etc/traefik/traefik.yml"
    0644 traefik:traefik
    ``` bash
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
      # Disable HTTP redirection - HTTP may be redirected to HTTPS after ACME
      # challenge using priorities and broad router rule matching.
      web:
        address: ':80'

      # Move TLS requirements to routers.
      webs:
        address: ':443'
        asDefault: true

    providers:
      file:
        directory: '/etc/traefik/dynamic'
        watch: true

    certificatesResolvers:
      lets_encrypt:
        acme:
          email: 'contact@example.com'
          storage: '/var/lib/traefik/acme_staging.json'
          caServer: 'https://acme-staging-v02.api.letsencrypt.org/directory'
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

!!! abstract "/etc/traefik/dynamic.yml"
    0644 traefik:traefik
    ``` bash
    http:
      routers:
        # Match ACME challenge prefix as well as hostnames. Route requests to
        # backend service expecting the ACME HTTP-01 challenge.
        mail_http01:
          rule: 'PathPrefix(`/.well-known/acme-challenge/`) && (Host(`mail.example.com`) || Host(`autoconfig.example.com`) || Host(`mta-sts.example.com`))'
          entryPoints:
            - 'web'
          priority: 1000
          service: 'mail_http01_service'

        # Another service using HTTPS with certificates obtained with DNS-01
        # challenge from Traefik.
        mail_webmail:
          rule: 'Host(`mail.example.com`) && PathPrefix(`/webmail`)'
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

      middlewares:
        redirect_to_https:
          redirectScheme:
            scheme: 'https'
            permanent: true

      services:
        # Backend service hanlding ACME HTTP-01 challenges for
        # {mail,autoconfig,mta-sts}.example.com.
        mail_http01_service:
          loadBalancer:
            servers:
              - url: 'http://10.5.5.240:80'

        mail_webmail_service:
          loadbalancer:
            servers:
              - url: 'https://10.5.5.240/webmail'
    ```

## TLS-APLN-01

!!! warning "Not Recommended"
    TLS-APLN-01 challenges **require** TCP passthrough over TLS connections. As
    TLS must be terminated (decrypted) to introspect hostnames,
    [only * can be used][b] to match and route incoming requests to backend
    services. [TCP is evaluated **before** HTTP][a] and therefore can
    **easily** break or redirect unexpected (or all) traffic to this backend.


!!! abstract "/etc/traefik/traefik.yml"
    0644 traefik:traefik
    ``` bash
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
      # Disable HTTP redirection - HTTP may be redirected to HTTPS after ACME
      # challenge using priorities and broad router rule matching.
      web:
        address: ':80'

      # Move TLS requirements to routers.
      webs:
        address: ':443'
        asDefault: true

    providers:
      file:
        directory: '/etc/traefik/dynamic'
        watch: true

    certificatesResolvers:
      lets_encrypt:
        acme:
          email: 'contact@example.com'
          storage: '/var/lib/traefik/acme_staging.json'
          caServer: 'https://acme-staging-v02.api.letsencrypt.org/directory'
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

!!! abstract "/etc/traefik/traefik.yml"
    0644 traefik:traefik
    ``` bash
    tcp:
      routers:
        # Send all traffic to backend.
        mail_apln_challenge:
          rule: 'HostSNI(`*`)'
          entryPoints:
            - 'webs'
          # Forward packet without modification.
          tls:
            passthrough: true
          service: 'mail_alpn_service'

      services:
        mail_alpn_service:
          loadbalancer:
            servers:
              - address: '10.5.5.240:443'
    ```


## Reference[^1][^2]

[^1]: https://github.com/traefik/traefik/issues/8992
[^2]: https://github.com/traefik/traefik/issues/10684

[a]: https://doc.traefik.io/traefik/reference/routing-configuration/tcp/routing/rules-and-priority/
[b]: https://doc.traefik.io/traefik/reference/routing-configuration/tcp/routing/rules-and-priority/#hostsni-and-hostsniregexp
[c]: https://gist.github.com/micw/67faf5cd3d4a6f64568ca2bb9a051230
