# Sonarr
Sonarr Server.

!!! example "Migrated to ansible collection"
    Use [r_pufky.arr.sonarr][a].

!!! tip
    * The UID/GID should be set to a user/group that has access to your media.
      All media clients should run under the same user to run correctly.
    * Your downloader will report the download path **mapped in the downloader
      service**. You need to map this exact path in Sonarr for it to be able to
      post-process downloads properly.

## Reverse Proxy
Sonarr should be run via a Reverse Proxy, allowing you to isolate and wrap
connections in SSL. [See NGINX][b] for more details.
[See Base Proxy Control][c] for basic proxy configuration.

!!! abstract "/etc/nginx/conf.d/reverse_proxy.conf"
    0644 root:root

    ``` nginx
    # Subdomain
    server {
      listen       443 ssl http2;
      server_name  sonarr.{DOMAIN} sonarr;

      location / {
        proxy_pass http://sonarr:8989;
        include    /etc/nginx/conf.d/proxy-control.conf;
      }
    }
    ```

!!! abstract "/etc/nginx/conf.d/reverse_proxy.conf"
    0644 root:root

    ``` nginx
    # Subpath
    server {
      location /sonarr {
        proxy_pass http://sonarr:8989/sonarr;
        include    /etc/nginx/conf.d/proxy-control.conf;
      }
    }
    ```

[a]: https://galaxy.ansible.com/ui/repo/published/r_pufky/arr/docs
[b]: ../../service/nginx/README.md
[c]: ../../service/nginx/manual/setup.md#setup-base-reverse-proxy
