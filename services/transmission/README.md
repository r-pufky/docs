Transmission
------------
Transmission docker instalation.

All media clients should run under the same user to run correctly.

[Dedicated server setup / service notes](transmission-dedicated.md)

[Docker repository][1]

1. [Docker Ports Exposed](#docker-ports-exposed)
1. [Important File Locations](#important-file-locations)
1. [Docker Creation](#docker-creation)
1. [Modifying Settings](#modifying-settings)

Docker Ports Exposed
--------------------

| Port  | Protocol | Purpose       |
|-------|----------|---------------|
| 49160 | UDP      | UDP Peer Port |
| 49160 | TCP      | Peer Port     |
| 9092  | TCP      | webface       |

Important File Locations
------------------------
Relative to docker container

| File                  | Purpose             |
|-----------------------|---------------------|
| /config/settings.json | Settings            |
| /watch                | Watch direcotry     |
| /downloads            | Downloads directory |

Docker Creation
---------------
If first-run, just launch the docker container to generate the correct
configuration directory structure, afterwards you can re-create with a mapped
directories.

```bash
docker run -t -d \
  --name=transmission \
  --net=host \
  --restart=unless-stopped \
  -p 9092:9092 \
  -p 49160:49160 \
  -p 49160:49160/udp \
  -e PGID=1001 \
  -e PUID=1001 \
  -e TZ=America/Los_Angeles \
  -v /etc/localtime:/etc/localtime:ro \
  -v /data/services/transmission:/config \
  -v /data/downloads:/downloads \
  -v /data/downloads/watched:/watch \
  linuxserver/transmission:latest
```
 * This assumes that the docker container is running as 1001:1001.
 * Use should use [`-t -d`][3] is needed to keep the container in interactive
   mode otherwise as soon as the container is idle it will sleep, which will
   stop background running services.

Modifying Settings
------------------
Transmission needs to be stopped to modify settings, as it overwrites the config
on shutdown. Stop the container then modify settings. Passwords will
automatically be encrypted when started.

```bash
docker stop transmission
```

Required changes
[/config/settings.json][2]
```vim
  "bind-address-ipv4": "<YOUR-SERVER-IP>",
  "download-dir": "/downloads/complete/transmission",
  "incomplete-dir": "/downloads/incomplete",
  "peer-port": 49160,
  "peer-port-random-on-start": false,
  "port-forwarding-enabled": true,
  "rpc-enabled": true,
  "rpc-password": "<WEBFACE_PASSWORD",
  "rpc-port": 9092,
  "rpc-username": "<WEBFACE_USERNAME",
  "rpc-whitelist": "<ALLOWED COMPUTERS>,127.0.0.1",
  "watch-dir": "/watch",
```

Restart transmission
```bash
docker start transmission
```

[1]: https://hub.docker.com/r/linuxserver/transmission/
[2]: settings.json