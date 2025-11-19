# Plugins
Traefik may expand base capabilities through plugins.

!!! warning
    Be sure to carefully look at plugins before installing, including source
    code. Many plugins are copied and slightly modified for specific use cases.
    In most cases the plugin with the most stars is the one to use.

    https://plugins.traefik.io/plugins

!!! tip
    Plugins must always be defined in the **install** configuration. Each
    plugin beyond enablement requires different setup.

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
            - 'basic_auth_users@file'
            - 'default_error_page@file'
            # Block Russia and China IP address at entrypoint.
            - 'geoblock_cn_ru@file'
    providers:
      file:
        directory: '/etc/traefik/dynamic'
        watch: true

    experimental:
      plugins:
        # Enable IP blocking by country.
        geoblock:
          moduleName: 'github.com/PascalMinder/geoblock'
          version: 'v0.3.3'
    ```

!!! abstract "/etc/traefik/dynamic/middleware.yml"
    0640 traefik:traefik
    ``` yaml
    ---
    http:
      middlewares:
        geoblock_cn_ru:
          plugin:
            geoblock:
              silentStartUp: false
              allowLocalRequests: true
              logLocalRequests: false
              logAllowedRequests: false
              logApiRequests: false
              api: 'https://get.geojs.io/v1/ip/country/{ip}'
              apiTimeoutMs: 750
              cacheSize: 15
              forceMonthlyUpdate: false
              allowUnknownCountries: false
              unknownCountryApiResponse: "nil"
              blackListMode: true
              addCountryHeader: false
              countries:
                - 'RU'
                - 'CN'
    ```
