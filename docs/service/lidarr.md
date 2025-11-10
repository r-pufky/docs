# Lidarr
Lidarr Server.

!!! example "Migrated to ansible collection"
    Use [r_pufky.arr.lidarr](https://galaxy.ansible.com/ui/repo/published/r_pufky/arr/docs/).

## Reverse Proxy
Lidarr should be run via a Reverse Proxy, allowing you to isolate and wrap
connections in SSL. [See NGINX](nginx/README.md) for more details. [See
Base Proxy Control](nginx/manual/setup.md#setup-base-reverse-proxy) for
basic proxy configuration.

/etc/nginx/conf.d/reverse_proxy.conf (1)
{ .annotate }

1. 0644 root:root

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

/etc/nginx/conf.d/reverse_proxy.conf (1)
{ .annotate }

1. 0644 root:root

``` nginx
# Subpath
server {
  location /lidarr {
    proxy_pass http://lidarr:8686/lidarr;
    include    /etc/nginx/conf.d/proxy_control.conf;
  }
}
```
