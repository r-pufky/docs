# Basic Auth Dashboard
Force API/Dashboard to be served with Basic Auth on local networks only.

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
      # Enabling insecure will automatically serve the dashboard on :8080.
      insecure: false
      debug: true

    # Skip TLS verification for backend servers.
    serversTransport:
      insecureSkipVerify: true

    # Redirect all HTTP to HTTPS.
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
          # Without parameters auto create self-signed certificate.
          tls: {}

          # Only apply global middleware here. If there are various services
          # with different requirements - it is better to explicitly define
          # each middlewares section on each router - allowing for flexible
          # deployments (e.g. passthrough connections to backends like mail).
          middlewares:
            # Leaving basic_auth_users@file off would require **each**
            # router to explicitly enable it or be unauthenticated.
            - 'basic_auth_users@file'

    # Dynamically load all other configuration.
    providers:
      file:
        directory: '/etc/traefik/dynamic'
        watch: true
    ```

!!! abstract "/etc/traefik/dynamic/routers.yml"
    0640 traefik:traefik
    ``` yaml
    ---
    http:
      routers:
        basic_auth_dashboard:
          # Require basic auth over HTTPS on local network only.
          #
          # Both /api and /dashboard are required to serve the dashboard.
          #
          # api@internal uses dashboard@internal to serve.
          rule: 'Host(`{TRAEFIK_IP}`) && ClientIP(`{CLIENT_CIDR}`) && (PathPrefix(`/api`) || PathPrefix(`/dashboard`))'
          tls: true
          entryPoints:
            - 'webs'
          service: 'api@internal'
    ```

!!! abstract "/etc/traefik/dynamic/middleware.yml"
    0640 traefik:traefik
    ``` yaml
    ---
    # Basic authentication users.
    #
    # Create user/pass with brypt hash:
    #
    #   htpasswd -nB {USER}
    #
    http:
      middlewares:
        basic_auth_users:
          basicAuth:
            users:
              - 'TestUser:$2y$05$kXi9l8LVD3CzwRJpeJ6LwOZzujE/24XppeM.xm0xyT7mWFaBqPK9q'
    ```
