.. _service-radarr-network:

Network
#######
Radarr should be run via a Reverse Proxy, allowing you to isolate and wrap
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
  server_name  radarr.{DOMAIN} radarr;

  location / {
    proxy_pass http://radarr:7878;
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
  location /radarr {
    proxy_pass http://radarr:7878/radarr;
    include    /etc/nginx/conf.d/proxy-control.conf;
  }
}
```
