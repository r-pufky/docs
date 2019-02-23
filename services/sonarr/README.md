[Sonarr][78] Server
===================
TV Management.

1. [Ports](#ports)
1. [Important File Locations](#important-file-locations)
1. [Docker Creation](#docker-creation)
1. [Reverse Proxy Setup](#reverse-proxy-setup)
1. [Add pre-existing series to Sonarr](#add-pre-existing-series-to-sonarr)
1. [Changing Media Location in Series](#changing-media-location-in-series)
1. [Ensure no Duplicate Plex Updates](#ensure-no-duplicate-plex-updates)

Ports
-----
Docker reverse-proxy.

| Port | Protocol | Exposed/Public | Purpose            |
|------|----------|----------------|--------------------|
| 8989 | TCP      | Exposed        | Sonarr webservice. |

Important File Locations
------------------------
Relative to docker container.

| File       | Purpose                               |
|------------|---------------------------------------|
| /config    | Sonarr main service directory.        |
| /downloads | Sonarr monitored downloads directory. |

Docker Creation
---------------
You can copy your existing configuration to docker _/config_ directory
adjusting for paths.

* The UID/GID should be set to a user/group that has access to your media. All
  media clients should run under the same user to run correctly.
* Your downloader will report the download path **mapped in the downloader
  docker/service**. You need to map this exact path in sonarr for it to be able
  to post-process downloads properly.
* See [sonarr config example][jh] for example configuration.

Docker Compose:
```yaml
sonarr:
  image: linuxserver/sonarr:latest
  restart: unless-stopped
  depends_on:
    - nzbget
  environment:
    - PGID=1001
    - PUID=1001
    - TZ=America/Los_Angeles
  volumes:
    - /data/downloads:/data/downloads
    - /data/media/tv:/data/media/tv
    - /data/services/sonarr:/config
    - /etc/localtime:/etc/localtime:ro
```
* Proxy will forward traffic to the container, so no ports need to be exposed.

Reverse Proxy Setup
-------------------
Allows you to isolate your containers as well as wrap connections in SSL. See
[nginx][refci] for more details.

### Using Subdomains
[nginx/conf.d/reverse-proxy.conf][do] `root:root 0644`
```nginx
server {
  listen 443 ssl http2;
  server_name sonarr.{DOMAIN} sonarr;

  location / {
    proxy_pass http://sonarr:8989;
    include /etc/nginx/conf.d/proxy-control.conf;
  }
}
```
* [proxy-control.conf][ref0p] contains default proxy settings. Reload nginx.

### Using Subpaths
[nginx/conf.d/reverse-proxy.conf][do] `root:root 0644`
```nginx
server {
  location /sonarr {
    proxy_pass http://sonarr:8989/sonarr;
    include /etc/nginx/conf.d/proxy-control.conf;
  }
}
```
* Set URL Base to _/sonarr_ in Sonarr before enabling the reverse-proxy.
* [proxy-control.conf][ref0p] contains default proxy settings. Reload nginx.

sonarr/config.yaml `1001:1001 0640`
```xml
<Config>
  <UrlBase>/sonarr</UrlBase>
</Config>
```

Add pre-existing series to Sonarr
---------------------------------
* Import Existing Series On Disk: _/data/tv_.
* Be sure to set appropriate import behavior.
* Be sure to search for correct match for episode if needed.
* Add all existing shows (even no longer aired), these are all scanned when
  adding shows and will be crufty if not set.

Changing Media Location in Series
---------------------------------
If series were imported under a different directory initially, these can be
updated.

* `Series > Series Editor`
  * Select all series that had location changes.
  * Select `Root Folder` (lower right) and enter new folder location.
  * `Click Save`

Ensure no Duplicate Plex Updates
--------------------------------
Plex will trigger updates on inotify events if configured to do so. If that is
the case, disable `update library` in `Connect > Plex` menu. Otherwise
duplicate items will appear on single files.

[docker-service-template.md|c9067f2][XX]

[jh]: sonarr.config.md
[78]: https://hub.docker.com/r/linuxserver/sonarr/
[do]: https://gist.github.com/IronicBadger/362c408d1f2c27a0503cb9252b508140#file-bash_aliases
[XX]: https://github.com/r-pufky/docs/blob/c9067f2bc3d0aeb0f2915e63f8cd9515c00640a2/services/docker-service-template.md

[ref0p]: ../nginx/proxy-control.conf
[refci]: ../nginx/README.md