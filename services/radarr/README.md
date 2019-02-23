[Radarr][2k] Server
===================
Movie Management.

1. [Ports](#ports)
1. [Important File Locations](#important-file-locations)
1. [Docker Creation](#docker-creation)
1. [Reverse Proxy Setup](#reverse-proxy-setup)
1. [Add pre-existing series to Radarr](#add-pre-existing-series-to-radarr)
1. [Ensure no Duplicate Plex Updates](#ensure-no-duplicate-plex-updates)

Ports
-----
Docker reverse-proxy.

| Port | Protocol | Exposed/Public | Purpose            |
|------|----------|----------------|--------------------|
| 7878 | TCP      | Exposed        | Radarr webservice. |

Important File Locations
------------------------
Relative to docker container.

| File       | Purpose                               |
|------------|---------------------------------------|
| /config    | Radarr main service directory.        |
| /downloads | Radarr monitored downloads directory. |

Docker Creation
---------------
You can copy your existing configuration to docker _/config_ directory
adjusting for paths.

* The UID/GID should be set to a user/group that has access to your media. All
  media clients should run under the same user to run correctly.
* Your downloader will report the download path **mapped in the downloader
  docker/service**. You need to map this exact path in radarr for it to be able
  to post-process downloads properly.
* See [radarr config example][qp] for example configuration.

Docker Compose:
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

Reverse Proxy Setup
-------------------
Allows you to isolate your containers as well as wrap connections in SSL. See
[nginx][refdi] for more details.

### Using Subdomains
[nginx/conf.d/reverse-proxy.conf][ni] `root:root 0644`
```nginx
server {
  listen 443 ssl http2;
  server_name radarr.{DOMAIN} radarr;

  location / {
    proxy_pass http://radarr:7878;
    include /etc/nginx/conf.d/proxy-control.conf;
  }
}
```
* [proxy-control.conf][refx9] contains default proxy settings. Reload nginx.

### Using Subpaths
[nginx/conf.d/reverse-proxy.conf][ni] `root:root 0644`
```nginx
server {
  location /radarr {
    proxy_pass http://radarr:7878/radarr;
    include /etc/nginx/conf.d/proxy-control.conf;
  }
}
```
* Set URL Base to _/radarr_ in Radarr before enabling the reverse-proxy.
* [proxy-control.conf][refx9] contains default proxy settings. Reload nginx.

radarr/config.yaml `1001:1001 0644`
```xml
<Config>
  <UrlBase>/radarr</UrlBase>
</Config>
```

Add pre-existing series to Radarr
---------------------------------
* Existing files should be in a folder for each movie.
* Import Existing Series On Disk: _/data/movies_.
* Be sure to set appropriate import behavior.
* Be sure to search for correct match for episode if needed.
* Import may timeout if initial import library is large. If this happens, just
  goto `Movies` and run `Update Library`.

Ensure no Duplicate Plex Updates
--------------------------------
Plex will trigger updates on inotify events if configured to do so. If that is
the case, disable `update library` in `Connect > Plex` menu. Otherwise
duplicate items will appear on single files.

[docker-service-template.md|c9067f2][XX]

[qp]: radarr.config.md
[2k]: https://hub.docker.com/r/linuxserver/radarr/
[ni]: https://gist.github.com/IronicBadger/362c408d1f2c27a0503cb9252b508140#file-bash_aliases
[XX]: https://github.com/r-pufky/docs/blob/c9067f2bc3d0aeb0f2915e63f8cd9515c00640a2/services/docker-service-template.md

[refx9]: ../nginx/proxy-control.conf
[refdi]: ../nginx/README.md