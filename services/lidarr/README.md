Lidarr Server
-------------
Music Management.

All media clients should run under the same user to run correctly.

[Dedicated server setup / service notes](lidarr-dedicated.md)

[Docker repository][1]

1. [Docker Ports Exposed](#docker-ports-exposed)
1. [Important File Locations](#important-file-locations)
1. [Docker Creation](#docker-creation)
1. [Add pre-existing series to Lidarr](#add-pre-existing-series-to-lidarr)
1. [Ensure no Duplicate Plex Updates](#ensure-no-duplicate-plex-updates)
1. [Changing Media Location in Series](#changing-media-location-in-series)

Docker Ports Exposed
--------------------

| Port | Protocol | Purpose           |
|------|----------|-------------------|
| 8686 | TCP      | Lidarr webservice |

Important File Locations
------------------------
Relative to docker container

| File       | Purpose                              |
|------------|--------------------------------------|
| /config    | Lidarr main service directory        |
| /downloads | Lidarr monitored downloads directory |

Docker Creation
---------------
You can copy your existing configuration to docker `/config` directory
adjusting for paths.

```bash
docker run -t -d \
  --name lidarr \
  --network host \
  --restart unless-stopped \
  -e PUID=1001 \
  -e PGID=1001 \
  -e TZ=America/Los_Angeles \
  -e /etc/localtime:/etc/localtime:ro \
  -v /data/services/lidarr:/config \
  -v /data/media/music:/music \
  -v /data/downloads:/downloads \
  linuxserver/lidarr:latest
```
 * The UID/GID should be set to a user/group that has access to your media.
 * Your downloader will report the download path **mapped in the downloader
   docker/service**. You need to map this exact path in lidarr for it to be
   able to post-process downloads properly.
 * See [lidarr config example](lidarr.config.md) for example configuration.

[1]: https://hub.docker.com/r/linuxserver/lidarr/