Nzbget Server
-------------
Usenet downloader.

All media clients should run under the same user to run correctly.

[Dedicated server setup / service notes](nzbget-dedicated.md)

[Docker repository][1]

1. [Docker Ports Exposed](#docker-ports-exposed)
1. [Important File Locations](#important-file-locations)
1. [Docker Creation](#docker-creation)
1. [SSH Tunneling](#ssh-tunneling)

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
 * The UID/GID should be set to a user/group that have access to your media.
 * Map your media directly to where it was before on the docker container to
   prevent needing to modify any libraries. This should be read-only.
 * See [nzbget.conf](nzbget.conf) for example configuration (adjust paths).
 * Use should use [`-t -d`][3] is needed to keep the container in interactive
   mode otherwise as soon as the container is idle it will sleep, which will
   stop background running services.

[1]: https://hub.docker.com/r/linuxserver/nzbget/