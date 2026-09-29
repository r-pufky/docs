# [Mox][a]
Pass traffic through proxy without modification. This allows the mail server to
change on the backend without needing to changing firewall rules on the router.
See [ACME Behind Traefik][b] for detailed information.

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

[a]: ../../mail/mox/README.md
[b]: acme/behind_traefik.md#http-01
