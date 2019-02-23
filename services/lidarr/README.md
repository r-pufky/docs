[Lidarr][ef] Server
===================
Music Management.

1. [Ports](#ports)
1. [Important File Locations](#important-file-locations)
1. [Docker Creation](#docker-creation)
1. [Reverse Proxy Setup](#reverse-proxy-setup)

Ports
-----
Docker reverse-proxy.

| Port | Protocol | Exposed/Public | Purpose            |
|------|----------|----------------|--------------------|
| 8686 | TCP      | Exposed        | Lidarr webservice. |

Important File Locations
------------------------
Relative to docker container.

| File       | Purpose                               |
|------------|---------------------------------------|
| /config    | Lidarr main service directory.        |
| /downloads | Lidarr monitored downloads directory. |

Docker Creation
---------------
You can copy your existing configuration to docker `/config` directory
adjusting for paths.

* The UID/GID should be set to a user/group that has access to your media. All
  media clients should run under the same user to run correctly.
* Your downloader will report the download path **mapped in the downloader
  docker/service**. You need to map this exact path in lidarr for it to be able
  to post-process downloads properly.
* See [lidarr config example][id] for example configuration.

### Docker Compose
```yaml
lidarr:
  image: linuxserver/lidarr:latest
  restart: unless-stopped
  depends_on:
    - nzbget
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
* Proxy will forward traffic to the container, so no ports need to be exposed.

Reverse Proxy Setup
-------------------
Allows you to isolate your containers as well as wrap connections in SSL. See
[nginx][ref8d] for more details.

### Using Subdomains
[nginx/conf.d/reverse-proxy.conf][je] `root:root 0644`
```nginx
server {
  listen 443 ssl http2;
  server_name lidarr.{DOMAIN} lidarr;

  location / {
    proxy_pass http://lidarr:8686;
    include /etc/nginx/conf.d/proxy-control.conf;
  }
}
```
* [proxy-control.conf][refci] contains default proxy settings. Reload nginx.

### Using Subpaths
[nginx/conf.d/reverse-proxy.conf][je] `root:root 0644`
```nginx
server {
  location /lidarr {
    proxy_pass http://lidarr:8686/lidarr;
    include /etc/nginx/conf.d/proxy-control.conf;
  }
}
```
* Set URL Base to _/lidarr_ in Lidarr before enabling the reverse-proxy.
* [proxy-control.conf][refci] contains default proxy settings. Reload nginx.

lidarr/config.yaml `1001:1001 0644`
```xml
<Config>
  <UrlBase>/lidarr</UrlBase>
</Config>
```

[docker-service-template.md|c9067f2][XX]

[ef]: https://hub.docker.com/r/linuxserver/lidarr/
[id]: lidarr.config.md
[je]: https://gist.github.com/IronicBadger/362c408d1f2c27a0503cb9252b508140#file-bash_aliases
[XX]: https://github.com/r-pufky/docs/blob/c9067f2bc3d0aeb0f2915e63f8cd9515c00640a2/services/docker-service-template.md

[refci]: ../nginx/proxy-control.conf
[ref8d]: ../nginx/README.md