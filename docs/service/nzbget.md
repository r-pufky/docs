# NZBGet
NZBGet Server.

!!! example "Migrated to ansible collection"
    Use [r_pufky.arr.nzbget](https://galaxy.ansible.com/ui/repo/published/r_pufky/arr/docs/).

## Reverse Proxy
NZBGet should be run via a Reverse Proxy, allowing you to isolate and wrap
connections in SSL. [See NGINX](nginx/README.md) for more details. [See
Base Proxy Control](nginx/manual/setup.md#setup-base-reverse-proxy) for
basic proxy configuration.

/etc/nginx/conf.d/reverse_proxy.conf (1)
{ .annotate }

1. 0644 root:root

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

/etc/nginx/conf.d/reverse_proxy.conf (1)
{ .annotate }

1. 0644 root:root

``` nginx
server {
  location /nzbget/ {
    proxy_pass            https://nzbget:6791/;
    include               /etc/nginx/conf.d/proxy-control.conf;
    proxy_set_header Host $host;
  }
}
```
