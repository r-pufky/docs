Radarr Server
-------------
Media Management.

All media clients should run under the same user to run correctly.

[Dedicated server setup / service notes](radarr-dedicated.md)

[Docker repository][1]

1. [Docker Ports Exposed](#docker-ports-exposed)
1. [Important File Locations](#important-file-locations)
1. [Docker Creation](#docker-creation)
1. [Add pre-existing series to Radarr](#add-pre-existing-series-to-radarr)
1. [Ensure no Duplicate Plex Updates](#ensure-no-duplicate-plex-updates)
1. [Changing Media Location in Series](#changing-media-location-in-series)

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
 * The UID/GID should be set to a user/group that has access to your media.
 * Your downloader will report the download path **mapped in the downloader
   docker/service**. You need to map this exact path in radarr for it to be
   able to post-process downloads properly.
 * See [radarr config example](radarr.config.md) for example configuration.

[1]: https://hub.docker.com/r/linuxserver/radarr/