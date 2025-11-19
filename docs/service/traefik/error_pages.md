# Error Pages
Return custom error pages for all service responses and Traefik errors.


## Serving Error Pages
Use [NGINX][a] or a custom server locally on the Traefik proxy to serve error
pages only. [tarampampam/error-pages][b] provide excellent templates.

Install [NGINX][a] and create a static location for error pages.

!!! abstract "/etc/nginx/nginx.conf"
    0644 root:root
    ``` bash
    user nginx;
    worker_processes auto;
    pid /run/nginx.pid;

    events {
      worker_connections 1024;
    }

    # Do not log (Traefik will log) - default to 500 error page.
    http {
      include /etc/nginx/mime.types;
      access_log off;
      error_log /dev/null crit;
      sendfile on;
      tcp_nopush on;
      keepalive_timeout 65;  # Reuse Traefik connections if multiple hits.
      gzip on;
      default_type application/octet-stream;
      server {
        listen 8008;
        server_name localhost;
        location / {
            root /usr/share/nginx;
            index 500.html 500.htm;
        }
      }
    }
    ```

## Routing Error Pages

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
            # Apply error pages to all routed connections.
            - 'default_error_page@file'

    providers:
      file:
        directory: '/etc/traefik/dynamic'
        watch: true
    ```

!!! warning
    Highly recommend enabling [geoblock][c] and [rate limiting][d] when
    responding to ALL URLs requested.

!!! abstract "/etc/traefik/dynamic/routers.yml"
    0640 traefik:traefik
    ``` yaml
    ---
    http:
      routers:
        default_error_page:
          # Use custom error pages for all errors.
          #
          # Using priority 1 ensures that this is the lowest priority rule for
          # any router, effectively creating a fallback route for all services
          # to return an error page.

          # Response to ALL URLs requested, not just defined ones.
          rule: 'HostRegexp(`^.+$`)'

          # Only send custom error pages for requests setting 'host' headers.
          # rule: 'HostRegexp(`{host:.+}`)'

          priority: 1
          entryPoints:
            - 'webs'
          service: 'default_error_page'
    ```

!!! abstract "/etc/traefik/dynamic/middleware.yml"
    0640 traefik:traefik
    ``` yaml
    ---
    http:
      middlewares:
        # Redirect all error status results to NGINX error pages.
        default_error_page:
          errors:
            status: '400-599'
            service: 'default_error_page'
            query: '/{status}.html'
    ```

!!! abstract "/etc/traefik/dynamic/services.yml"
    0640 traefik:traefik
    ``` yaml
    http:
      services:
        # Define NGINX as backend service to handle error pages.
        default_error_page:
          loadbalancer:
            servers:
              - url: 'http://localhost:8008'
    ```

[a]: ../nginx/README.md
[b]: https://github.com/tarampampam/error-pages
[c]: plugins.md
[d]: rate_limiting.md