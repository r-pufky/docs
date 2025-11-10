# Deluge
Bittorrent downloader.

!!! example "Migrated to ansible collection"
    Use [r_pufky.arr.deluge](https://galaxy.ansible.com/ui/repo/published/r_pufky/arr/docs/).

## Reverse Proxy
Deluge should be run via a Reverse Proxy, allowing you to isolate and wrap
connections in SSL. [See NGINX](nginx/README.md) for more details. [See
Base Proxy Control](nginx/manual/setup.md#setup-base-reverse-proxy) for
basic proxy configuration.


/etc/nginx/conf.d/reverse_proxy.conf (1)
{ .annotate }

1. 0644 root:root

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

Reference:

* https://forum.deluge-torrent.org/viewtopic.php?t=35117

/etc/nginx/conf.d/reverse_proxy.conf (1)
{ .annotate }

1. 0644 root:root

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

Reference:

* https://dev.deluge-torrent.org/wiki/UserGuide/WebUI/ReverseProxy
