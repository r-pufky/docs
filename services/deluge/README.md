Deluge
------
Deluge docker instalation.

All media clients should run under the same user to run correctly.

[Docker repository][1]

1. [Docker Ports Exposed](#docker-ports-exposed)
1. [Important File Locations](#important-file-locations)
1. [Docker Creation](#docker-creation)
1. [Modifying Settings](#modifying-settings)
1. [Reset Password](#reset-password)

Docker Ports Exposed
--------------------

| Port  | Protocol | Purpose       |
|-------|----------|---------------|
| 49160 | UDP      | UDP Peer Port |
| 49160 | TCP      | Peer Port     |
| 8112  | TCP      | webface       |

Important File Locations
------------------------
Relative to docker container

| File                  | Purpose             |
|-----------------------|---------------------|
| /config/core.conf     | Daemon Settings     |
| /config/web.conf      | WebUI Settings      |
| /watch                | Watch direcotry     |
| /downloads            | Downloads directory |

Docker Creation
---------------
If first-run, just launch the docker container to generate the correct
configuration directory structure, afterwards you can re-create with a mapped
directories.

```bash
docker run -t -d \
  --name=deluge \
  --net=host \
  --restart=unless-stopped \
  -p 8112:8112 \
  -p 49160:49160 \
  -p 49160:49160/udp \
  -e PGID=1001 \
  -e PUID=1001 \
  -e TZ=America/Los_Angeles \
  -v /etc/localtime:/etc/localtime:ro \
  -v /data/services/deluge:/config \
  -v /data/downloads:/downloads \
  -v /data/downloads/watched:/watch \
  linuxserver/deluge:latest
```
 * This assumes that the docker container is running as 1001:1001.
 * Use should use [`-t -d`][3] is needed to keep the container in interactive
   mode otherwise as soon as the container is idle it will sleep, which will
   stop background running services.

Modifying Settings
------------------
Deluge **must** be connected to the Daemon to [write configuration changes][2].
Ensure you select `Connect` on `Connection Manager`.

Required changes to minimally secure your configuration.
[/config/core.conf][3]
```vim
  "enc_in_policy": 1,
  "enc_level": 1,
  "enc_out_policy": 1,
  "enc_prefer_rc4": true,

  "random_port": false,
  "listen_ports": [
    49160,
    49160
  ],
  "dht": true,
  "upnp": false,
  "natpmp": false,
  "lsd": false,
  "send_info": false,
  "allow_remote": false,
  "max_upload_speed_per_torrent": 0,
  "max_upload_speed": 0.0,
  "move_completed_path": "/downloads/complete/deluge",
  "download_location": "/downloads/incomplete",
  "autoadd_location": "/watched",
```

Reset Password
--------------
Stop Deluge, remove `pwd_sh1` pasword line in `web.conf`, restart.

Default username/password is `admin` / `deluge`.

[1]: https://hub.docker.com/r/linuxserver/deluge/
[2]: https://forum.deluge-torrent.org/viewtopic.php?t=35117
[3]: https://dev.deluge-torrent.org/wiki/UserGuide/WebUI/ReverseProxy