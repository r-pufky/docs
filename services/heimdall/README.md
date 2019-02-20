Heimdall
--------
[Application Dashboard][1].

[Docker repository][2]

1. [Docker Ports Exposed](#docker-ports-exposed)
1. [Important File Locations](#important-file-locations)
1. [Docker Creation](#docker-creation)
1. [Reverse Proxy Setup](#reverse-proxy-setup)
1. [Add Password Authentication](#add-password-authentication)

Docker Ports Exposed
--------------------
Docker Compose

| Port | Protocol | Exposed/Public | Purpose             |
|------|----------|----------------|---------------------|
| 443  | TCP      | Exposed        | Heimdall webservice |

Important File Locations
------------------------
Relative to docker container

| File       | Purpose                              |
|------------|--------------------------------------|
| /config    | Heimdall main service directory      |

Docker Creation
---------------
You can copy your existing configuration to docker `/config` directory
adjusting for paths.

* The UID/GID should be set to a user/group that has access to your media.
* Your downloader will report the download path **mapped in the downloader
  docker/service**. You need to map this exact path in sonarr for it to be able
  to post-process downloads properly.

### Docker Compose
```yaml
heimdall:
  image: linuxserver/heimdall:latest
  restart: unless-stopped
  ports:
    - "443:443"
  environment:
    - PGID=1001
    - PUID=1001
    - TZ=America/Los_Angeles
  volumes:
    - /data/services/heimdall:/config
    - /etc/localtime:/etc/localtime:ro
```

Reverse Proxy Setup
-------------------
Allows you to isolate your containers as well as wrap connections in SSL. See
[nginx][ref2] for more details. Recommended.

Heimdall is not subpath aware, and should be hosted from a subdomain.

nginx/conf.d/reverse-proxy.conf
```nginx
server {
  listen 443 ssl http2;
  server_name heimdall.<DOMAIN> heimdall;

  location / {
    proxy_pass https://heimdall/;
    include /etc/nginx/conf.d/proxy-control.conf;
  }
}
```
* [proxy-control.conf][ref1] contains default proxy settings. Reload nginx.

docker-compose.yml
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

Add [Password Authentication][3]
--------------------------------
A reverse proxy setup is **required**.

Install password utilities and generate a user/password.
```bash
apt install apache2-utils
sudo htpasswd -c /data/services/nginx/heimdall.pass <user>
```

nginx/conf.d/reverse-proxy.conf
```nginx
server {
  listen 443 ssl http2;
  server_name heimdall.<SUBDOMAIN>.<DOMAIN>;

  location / {
    allow x.x.x.x/24;
    allow x.x.x.x;
    deny all;
    auth_basic 'Heimdall';
    auth_basic_user_file /etc/nginx/heimdall.pass;

    proxy_pass https://heimdall/;
    include /etc/nginx/conf.d/proxy-control.conf;
  }
}
```
* Restrict to specific IP / subnets and deny rest of traffic.
* [proxy-control.conf][ref1] contains default proxy settings. Reload nginx.

[1]: https://heimdall.site/
[2]: https://github.com/linuxserver/Heimdall
[3]: https://docs.nginx.com/nginx/admin-guide/security-controls/configuring-http-basic-authentication/#pass

[ref1]: ../nginx/proxy-control.conf
[ref2]: ../nginx/README.md