# NZBGet
NZBGet Server.

!!! example "Migrated to ansible collection"
    Use [r_pufky.arr.nzbget][a].

!!! tip
    * The UID/GID should be set to a user/group that has access to your media.
      All media clients should run under the same user to run correctly.
    * Your downloader will report the download path **mapped in the downloader
      service**. You need to map this exact path in NZBGet for it to be able to
      post-process downloads properly.


## Reverse Proxy
NZBGet should be run via a Reverse Proxy, allowing you to isolate and wrap
connections in SSL. [See NGINX][b] for more details.
[See Base Proxy Control][c] for basic proxy configuration.

!!! abstract "/etc/nginx/conf.d/reverse_proxy.conf"
    0644 root:root

    ``` nginx
    server {
      listen                  443 ssl http2;
      server_name             nzbget.{DOMAIN} nzbget;

      location / {
        proxy_pass            http://nzbget:6791;
        include               /etc/nginx/conf.d/proxy-control.conf;
        proxy_set_header Host $host;
      }
    }
    ```

!!! abstract "/etc/nginx/conf.d/reverse_proxy.conf"
    0644 root:root

    ``` nginx
    server {
      location /nzbget/ {
        proxy_pass            https://nzbget:6791/;
        include               /etc/nginx/conf.d/proxy-control.conf;
        proxy_set_header Host $host;
      }
    }
    ```

[a]: https://galaxy.ansible.com/ui/repo/published/r_pufky/arr/docs
[b]: ../service/nginx/README.md
[c]: ../service/nginx/manual/setup.md#setup-base-reverse-proxy
