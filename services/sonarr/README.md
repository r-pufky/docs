Sonarr Server
-------------
TV Management.

All media clients should run under the same user to run correctly.

[Dedicated server setup / service notes](sonarr-dedicated.md)

[Docker repository][1]

1. [Docker Ports Exposed](#docker-ports-exposed)
1. [Important File Locations](#important-file-locations)
1. [Docker Creation](#docker-creation)
1. [Add pre-existing series to Sonarr](#add-pre-existing-series-to-sonarr)
1. [Ensure no Duplicate Plex Updates](#ensure-no-duplicate-plex-updates)
1. [Changing Media Location in Series](#changing-media-location-in-series)

Docker Ports Exposed
--------------------

| Port | Protocol | Purpose           |
|------|----------|-------------------|
| 8989 | TCP      | Sonarr webservice |

Important File Locations
------------------------
Relative to docker container

| File       | Purpose                              |
|------------|--------------------------------------|
| /config    | Sonarr main service directory        |
| /downloads | Sonarr monitored downloads directory |

Docker Creation
---------------
You can copy your existing configuration to docker `/config` directory
adjusting for paths.

```bash
docker run -t -d \
  --name sonarr \
  --network host \
  --restart unless-stopped \
  -e PUID=1001 \
  -e PGID=1001 \
  -e TZ=America/Los_Angeles \
  -e /etc/localtime:/etc/localtime:ro \
  -v /data/services/sonarr:/config \
  -v /data/media/tv:/tv \
  -v /data/downloads:/downloads \
  linuxserver/sonarr:latest
```
 * The UID/GID should be set to a user/group that has access to your media.
 * Your downloader will report the download path **mapped in the downloader
   docker/service**. You need to map this exact path in sonarr for it to be
   able to post-process downloads properly.
 * See [sonarr config example](sonarr.config.md) for example configuration.

[1]: https://hub.docker.com/r/linuxserver/sonarr/