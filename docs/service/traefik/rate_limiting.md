# Rate Limiting
[Rate limit][a] traffic through Traefik.

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
          tls: {}
          middlewares:
            # See comment in middlewares for chaining.
            # - 'basic_geoblock_errorpages'

            # Rate limiting applied here will apply to ALL traffic through this
            # entrypoint. Instead rate limit on the router.
            # - 'global_rate_limit@file'
            - 'basic_auth_users@file'
            - 'default_error_page@file'
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
        # Serve all URLs requested with a global rate limit.
        default_error_page:
          rule: 'HostRegexp(`(.*?)`)'
          priority: 1
          entryPoints:
            - 'webs'
          middlewares:
            # See comment in middlewares for chaining.
            # - 'basic_geoblock_errorpages'
            - 'global_rate_limit_error_page'
          service: 'default_error_page'
    ```

!!! abstract "/etc/traefik/dynamic/middleware.yml"
    0640 traefik:traefik
    ``` yaml
    ---
    http:
      middlewares:
        # A middleware chain creates a 'group' of middleware to apply to a
        # given entryPoint or router.
        basic_geoblock_errorpages:
          chain:
            middlewares:
              - 'basic_auth_users'  # @file only needed if not in this file.
              - 'default_error_page'
              - 'global_rate_limit_error_page'

        global_rate_limit_error_page:
          # Global rate limit for error pages (100r/s, burst to 200r/s).
          rateLimit:
            average: 100
            period: '1s'
            burst: 200
    ```

[a]: https://doc.traefik.io/traefik/reference/routing-configuration/http/middlewares/ratelimit
