[Heimdall][4j]
==============
[Application Dashboard][tm].

1. [Ports](#ports)
1. [Important File Locations](#important-file-locations)
1. [Docker Creation](#docker-creation)
1. [Reverse Proxy Setup](#reverse-proxy-setup)
1. [Add Password Authentication](#add-password-authentication)

Docker Ports Exposed
--------------------
Docker reverse-proxy.

| Port | Protocol | Exposed/Public | Purpose           |
|------|----------|----------------|-------------------|
| 443  | TCP      | Exposed        | Heimdall webface. |

Important File Locations
------------------------
Relative to docker container.

| File       | Purpose                              |
|------------|--------------------------------------|
| /config    | Heimdall main service directory.     |

Docker Creation
---------------
Docker Compose:
```yaml
heimdall:
  image: linuxserver/heimdall:latest
  restart: unless-stopped
  environment:
    - PGID=1001
    - PUID=1001
    - TZ=America/Los_Angeles
  volumes:
    - /data/services/heimdall:/config
    - /etc/localtime:/etc/localtime:ro
```
* Proxy will forward traffic to the container, so no ports need to be exposed.

Reverse Proxy Setup
-------------------
Allows you to isolate your containers as well as wrap connections in SSL. See
[nginx][ref7v] for more details.

Heimdall is not subpath aware, and should be hosted from a subdomain.

nginx/conf.d/reverse-proxy.conf
```nginx
server {
  listen 443 ssl http2;
  server_name heimdall.{DOMAIN} heimdall;

  location / {
    proxy_pass https://heimdall/;
    include /etc/nginx/conf.d/proxy-control.conf;
  }
}
```
* [proxy-control.conf][ref4c] contains default proxy settings. Reload nginx.

Add [Password Authentication][3]
--------------------------------
A reverse proxy setup is **required**.

Install password utilities and generate a user/password:
```bash
apt install apache2-utils
sudo htpasswd -c /data/services/nginx/heimdall.pass <user>
```

nginx/conf.d/reverse-proxy.conf
```nginx
server {
  listen 443 ssl http2;
  server_name heimdall.{DOMAIN} heimdall;

  location / {
    allow {TRUSTED NETWORK}/{TRUSTED NETWORK MASK};
    allow {TRUSTED IP};
    deny all;
    auth_basic 'Heimdall';
    auth_basic_user_file /etc/nginx/heimdall.pass;

    proxy_pass https://heimdall/;
    include /etc/nginx/conf.d/proxy-control.conf;
  }
}
```
* Restrict to specific IP / subnets and deny rest of traffic.
* [proxy-control.conf][ref4c] contains default proxy settings. Reload nginx.

[docker-service-template.md@248d10f][XX]

[tm]: https://heimdall.site/
[4j]: https://github.com/linuxserver/Heimdall
[3]: https://docs.nginx.com/nginx/admin-guide/security-controls/configuring-http-basic-authentication/#pass
[XX]: ../docker-service-template.md@248d10f

[ref4c]: ../nginx/proxy-control.conf
[ref7v]: ../nginx/README.md