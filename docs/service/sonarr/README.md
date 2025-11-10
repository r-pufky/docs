# Sonarr
Sonarr Server.

!!! example "Migrated to ansible collection"
    Use [r_pufky.arr.sonarr](https://galaxy.ansible.com/ui/repo/published/r_pufky/arr/docs/).

## Reverse Proxy
Sonarr should be run via a Reverse Proxy, allowing you to isolate and wrap
connections in SSL. [See NGINX](../nginx/README.md) for more details. [See
Base Proxy Control](../nginx/manual/setup.md#setup-base-reverse-proxy) for
basic proxy configuration.

/etc/nginx/conf.d/reverse_proxy.conf (1)
{ .annotate }

1. 0644 root:root

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

/etc/nginx/conf.d/reverse_proxy.conf (1)
{ .annotate }

1. 0644 root:root

``` nginx
# Subpath
server {
  location /sonarr {
    proxy_pass http://sonarr:8989/sonarr;
    include    /etc/nginx/conf.d/proxy-control.conf;
  }
}
```
