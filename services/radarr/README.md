Radarr Server
-------------
Movie Management.

All media clients should run under the same user to run correctly.

[Dedicated server setup / service notes](radarr-dedicated.md)

[Docker repository][1]

1. [Docker Ports Exposed](#docker-ports-exposed)
1. [Important File Locations](#important-file-locations)
1. [Docker Creation](#docker-creation)
1. [Reverse Proxy Setup](#reverse-proxy-setup)

Docker Ports Exposed
--------------------

| Port | Protocol | Purpose           |
|------|----------|-------------------|
| 7878 | TCP      | Radarr webservice |

Important File Locations
------------------------
Relative to docker container

| File       | Purpose                              |
|------------|--------------------------------------|
| /config    | Radarr main service directory        |
| /downloads | Radarr monitored downloads directory |

Docker Creation
---------------
You can copy your existing configuration to docker `/config` directory
adjusting for paths.

* The UID/GID should be set to a user/group that has access to your media.
* Your downloader will report the download path **mapped in the downloader
  docker/service**. You need to map this exact path in radarr for it to be able
  to post-process downloads properly.
* See [radarr config example](radarr.config.md) for example configuration.

### Independent Container
```bash
docker run -t -d \
  --name radarr \
  --network host \
  --restart unless-stopped \
  -e PUID=1001 \
  -e PGID=1001 \
  -e TZ=America/Los_Angeles \
  -e /etc/localtime:/etc/localtime:ro \
  -v /data/services/radarr:/config \
  -v /data/media/movies:/movies \
  -v /data/downloads:/downloads \
  linuxserver/radarr:latest
```
* Use `-t -d` is needed to keep the container in interactive mode otherwise as
  soon as the container is idle it will sleep, which will stop background
  running services.

### Docker Compose
```yaml
lidarr:
  image: linuxserver/lidarr:latest
  restart: unless-stopped
  ports:
    - "7878:7878"
  environment:
    - PGID=1001
    - PUID=1001
    - TZ=America/Los_Angeles
  volumes:
    - /data/downloads:/data/downloads
    - /data/media/music:/data/media/music
    - /data/services/lidarr:/config
    - /etc/localtime:/etc/localtime:ro
```

Reverse Proxy Setup
-------------------
Allows you to isolate your containers as well as wrap connections in SSL. See
[nginx][ref2] for more details. Recommended.


docker-compose.yml
```yaml
lidarr:
  image: linuxserver/radarr:latest
  restart: unless-stopped
  depends_on:
    - nzbget
  environment:
    - PGID=1001
    - PUID=1001
    - TZ=America/Los_Angeles
  volumes:
    - /data/downloads:/data/downloads
    - /data/media/movies:/data/media/movies
    - /data/services/radarr:/config
    - /etc/localtime:/etc/localtime:ro
```
* Proxy will forward traffic to the container, so no ports need to be exposed.

### Using Subdomains
[nginx/conf.d/reverse-proxy.conf][2]
```nginx
server {
  listen 443 ssl http2;
  server_name radarr.<DOMAIN> radarr;

  location / {
    proxy_pass http://radarr:7878;
    include /etc/nginx/conf.d/proxy-control.conf;
  }
}
```
* [proxy-control.conf][ref1] contains default proxy settings. Reload nginx.

### Using Subpaths
[nginx/conf.d/reverse-proxy.conf][2]
```nginx
server {
  location /radarr {
    proxy_pass http://radarr:7878/radarr;
    include /etc/nginx/conf.d/proxy-control.conf;
  }
}
```
* Set URL Base to `/radarr` in Radarr before enabling the reverse-proxy.
* [proxy-control.conf][ref1] contains default proxy settings. Reload nginx.

radarr/config.yaml
```xml
<Config>
  <UrlBase>/radarr</UrlBase>
</Config>
```

[1]: https://hub.docker.com/r/linuxserver/radarr/
[2]: https://gist.github.com/IronicBadger/362c408d1f2c27a0503cb9252b508140#file-bash_aliases

[ref1]: ../nginx/proxy-control.conf
[ref2]: ../nginx/README.md