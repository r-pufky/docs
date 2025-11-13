# Deluge
Bittorrent downloader.

!!! example "Migrated to ansible collection"
    Use [r_pufky.arr.deluge][a].


## Reverse Proxy
Deluge should be run via a Reverse Proxy, allowing you to isolate and wrap
connections in SSL. [See NGINX][b] for more details.
[See Base Proxy Control][c] for basic proxy configuration.

!!! abstract "[/etc/nginx/conf.d/reverse_proxy.conf][d]"
    0644 root:root

    ``` nginx
    # Subdomain
    server {
      listen                       443 ssl http2;
      server_name                  deluge.{DOMAIN} deluge;

      location / {
        proxy_pass                 http://deluge:8112;
        include                    /etc/nginx/conf.d/proxy-control.conf;
        add_header X-Frame-Options SAMEORIGIN;
      }
    }
    ```

!!! abstract "[/etc/nginx/conf.d/reverse_proxy.conf][e]"
    0644 root:root

    ``` nginx
    # Subpath
    server {
      location /deluge {
        proxy_pass                     http://deluge:8112/;
        include                        /etc/nginx/conf.d/proxy-control.conf;
        proxy_set_header X-Deluge-Base '/deluge/';
        add_header X-Frame-Options     SAMEORIGIN;
      }
    }
    ```

[a]: https://galaxy.ansible.com/ui/repo/published/r_pufky/arr/docs
[b]: ../service/nginx/README.md
[c]: ../service/nginx/manual/setup.md#setup-base-reverse-proxy
[d]: https://forum.deluge-torrent.org/viewtopic.php?t=35117
[e]: https://dev.deluge-torrent.org/wiki/UserGuide/WebUI/ReverseProxy
