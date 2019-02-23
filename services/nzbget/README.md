[Nzbget][sy] Server
===================
Usenet downloader.

1. [Ports](#ports)
1. [Important File Locations](#important-file-locations)
1. [Docker Creation](#docker-creation)
1. [Reverse Proxy Setup](#reverse-proxy-setup)

Ports
-----
Docker reverse-proxy.

| Port | Protocol | Exposed/Public | Purpose                            |
|------|----------|----------------|------------------------------------|
| 6789 | TCP      | Exposed        | Default nzbget webservice (http).  |
| 6791 | TCP      | Exposed        | Default nzbget webservice (https). |
* If https is enabled, http is disabled.

Important File Locations
------------------------
Relative to docker container.

| File       | Purpose                          |
|------------|----------------------------------|
| /config    | Nzbget main service directory.   |
| /downloads | Nzbget main downloads directory. |

Docker Creation
---------------
You can copy your existing configuration to docker _/config_ directory
adjusting for paths.

* The UID/GID should be set to a user/group that have access to your media. All
  media clients should run under the same user to run correctly.
* Map your media directly to where it was before on the docker container to
  prevent needing to modify any libraries. This should be read-only.
* See [nzbget.conf][af] for example configuration (adjust paths).

Docker Compose:
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

Reverse Proxy Setup
-------------------
Allows you to isolate your containers as well as wrap connections in SSL. See
[nginx][refc8] for more details.

### Using Subdomains
[nginx/conf.d/reverse-proxy.conf][ui] `root:root 0644`
```nginx
server {
  listen 443 ssl http2;
  server_name nzbget.{DOMAIN} nzbget;

  location / {
    proxy_pass http://nzbget:6791;
    include /etc/nginx/conf.d/proxy-control.conf;
    proxy_set_header Host $host;
  }
}
```
* [proxy-control.conf][refjk] contains default proxy settings. Reload nginx.

### Using Subpaths
[nginx/conf.d/reverse-proxy.conf][ui] `root:root 0644`
```nginx
server {
  location /nzbget/ {
    proxy_pass https://nzbget:6791/;
    include /etc/nginx/conf.d/proxy-control.conf;
    proxy_set_header Host $host;
  }
}
```
* [proxy-control.conf][refjk] contains default proxy settings. Reload nginx.

[docker-service-template.md|c9067f2][XX]

[sy]: https://hub.docker.com/r/linuxserver/nzbget/
[ui]: https://nzbget.net/behind-other-web-server
[af]: nzbget.conf
[XX]: https://github.com/r-pufky/docs/blob/c9067f2bc3d0aeb0f2915e63f8cd9515c00640a2/services/docker-service-template.md

[refjk]: ../nginx/proxy-control.conf
[refc8]: ../nginx/README.md