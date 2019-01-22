Nzbget Server
-------------
Usenet downloader.

All media clients should run under the same user to run correctly.

[Dedicated server setup / service notes](nzbget-dedicated.md)

[Docker repository][1]

1. [Docker Ports Exposed](#docker-ports-exposed)
1. [Important File Locations](#important-file-locations)
1. [Docker Creation](#docker-creation)
1. [Reverse Proxy Setup](#reverse-proxy-setup)

Docker Ports Exposed
--------------------

| Port | Protocol | Purpose                           |
|------|----------|-----------------------------------|
| 6789 | TCP      | Default nzbget webservice (http)  |
| 6791 | TCP      | Default nzbget webservice (https) |
 * If https is enabled, http is disabled

Important File Locations
------------------------
Relative to docker container

| File       | Purpose                         |
|------------|---------------------------------|
| /config    | Nzbget main service directory   |
| /downloads | Nzbget main downloads directory |

Docker Creation
---------------
You can copy your existing configuration to docker `/config` directory
adjusting for paths.

* The UID/GID should be set to a user/group that have access to your media.
* Map your media directly to where it was before on the docker container to
  prevent needing to modify any libraries. This should be read-only.
* See [nzbget.conf](nzbget.conf) for example configuration (adjust paths).

### Independent Container
```bash
docker run -t -d \
  --name nzbget \
  --network host \
  --restart unless-stopped \
  -e PUID=1001 \
  -e PGID=1001 \
  -e TZ=America/Los_Angeles \
  -e /etc/localtime:/etc/localtime:ro \
  -v /data/services/nzbget:/config \
  -v /data/downloads:/downloads \
  linuxserver/nzbget:latest
```
* Use `-t -d` is needed to keep the container in interactive mode otherwise as
  soon as the container is idle it will sleep, which will stop background
  running services.

### Docker Compose
```yaml
nzbget:
  image: linuxserver/nzbget:latest
  restart: unless-stopped
  ports:
    - "6791:6791"
  environment:
    - PGID=1001
    - PUID=1001
    - TZ=America/Los_Angeles
  volumes:
    - /data/downloads:/data/downloads
    - /data/services/nzbget:/config
    - /etc/localtime:/etc/localtime:ro
```

Reverse Proxy Setup
-------------------
Allows you to isolate your containers as well as wrap connections in SSL. See
[nginx][ref2] for more details. Recommended.

docker-compose.yml
```yaml
nzbget:
  image: linuxserver/nzbget:latest
  restart: unless-stopped
  environment:
    - PGID=1001
    - PUID=1001
    - TZ=America/Los_Angeles
  volumes:
    - /data/downloads:/data/downloads
    - /data/services/nzbget:/config
    - /etc/localtime:/etc/localtime:ro
```
* Proxy will forward traffic to the container, so no ports need to be exposed.

### Using Subdomains
[nginx/conf.d/reverse-proxy.conf][2]
```nginx
server {
  listen 443 ssl http2;
  server_name nzbget.<DOMAIN> nzbget;

  location / {
    proxy_pass http://nzbget:6791;
    include /etc/nginx/conf.d/proxy-control.conf;
    proxy_set_header Host $host;
  }
}
```
* [proxy-control.conf][ref1] contains default proxy settings. Reload nginx.

### Using Subpaths
[nginx/conf.d/reverse-proxy.conf][2]
```nginx
server {
  location /nzbget/ {
    proxy_pass https://nzbget:6791/;
    include /etc/nginx/conf.d/proxy-control.conf;
    proxy_set_header Host $host;
  }
}
```
* [proxy-control.conf][ref1] contains default proxy settings. Reload nginx.

[1]: https://hub.docker.com/r/linuxserver/nzbget/
[2]: https://nzbget.net/behind-other-web-server

[ref1]: ../nginx/proxy-control.conf
[ref2]: ../nginx/README.md