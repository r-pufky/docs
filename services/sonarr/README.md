Sonarr Server
-------------
Media Management.

[Dedicated server setup](sonarr-dedicated.md)

[Docker repository][1]

1. [Docker Ports Exposed](#docker-ports-exposed)
2. [Important File Locations](#important-file-locations)
3. [Docker Creation](#docker-creation)
4. [Add pre-existing series to Sonarr](#add-pre-existing-series-to-sonarr)
5. [Changing Media Location in Series](#changing-media-location-in-series)

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
docker run -d \
  --name sonarr \
  --network host \
  --restart unless-stopped \
  -e UGID=1001 \
  -e PGID=1001 \
  -e TZ=America/Los_Angeles \
  -e /etc/localtime:/etc/localtime:ro \
  -v /data/services/sonarr:/config \
  -v /data/media/tv:/tv \
  -v /data/downloads:/data/downloads \
  linuxserver/sonarr:latest
```
 * The UID/GID should be set to a user/group that have access to your media.
 * See [sonarr config example](sonarr.config.md) for example configuration.

Add pre-existing series to Sonarr
---------------------------------
 * Import Existing Series On Disk: /data/tv
 * Be sure to set appropriate import behavior
 * Be sure to search for correct match for episode if needed
 * Add all existing shows (even no longer aired), these are all scanned when
   adding shows and will be crufty if not set

Changing Media Location in Series
---------------------------------
If series were imported under a different directory initially, these can be
updated

 * Series -> Series Editor
 * Select all series that had location changes
 * Select `Root Folder` (lower right) and enter new folder location
 * Click `Save`
[1]: https://hub.docker.com/r/linuxserver/sonarr/