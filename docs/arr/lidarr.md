# Lidarr
Lidarr Server.

!!! example "Migrated to ansible collection"
    Use [r_pufky.arr.lidarr][a].


## Reverse Proxy
Lidarr should be run via a Reverse Proxy, allowing you to isolate and wrap
connections in SSL. [See NGINX][b] for more details.
[See Base Proxy Control][c] for basic proxy configuration.

!!! abstract "/etc/nginx/conf.d/reverse_proxy.conf"
    0644 root:root

    ``` nginx
    # Subdomain
    server {
      listen       443 ssl http2;
      server_name  lidarr.{DOMAIN} lidarr;

      location / {
        proxy_pass http://lidarr:8686;
        include    /etc/nginx/conf.d/proxy_control.conf;
      }
    }
    ```

!!! abstract "/etc/nginx/conf.d/reverse_proxy.conf"
    0644 root:root

    ``` nginx
    # Subpath
    server {
      location /lidarr {
        proxy_pass http://lidarr:8686/lidarr;
        include    /etc/nginx/conf.d/proxy_control.conf;
      }
    }
    ```

[a]: https://galaxy.ansible.com/ui/repo/published/r_pufky/arr/docs
[b]: ../service/nginx/README.md
[c]: ../service/nginx/manual/setup.md#setup-base-reverse-proxy
