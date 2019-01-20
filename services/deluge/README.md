Deluge
------
Deluge docker instalation.

All media clients should run under the same user to run correctly.

[Docker repository][1]

1. [Docker Ports Exposed](#docker-ports-exposed)
1. [Important File Locations](#important-file-locations)
1. [Docker Creation](#docker-creation)
1. [Reverse Proxy Setup](#reverse-proxy-setup)
1. [Modifying Settings](#modifying-settings)
1. [Reset Password](#reset-password)

Docker Ports Exposed
--------------------

| Port  | Protocol | Purpose                                    |
|-------|----------|--------------------------------------------|
| 49160 | UDP      | UDP Peer Port (standalone & reverse-proxy) |
| 49160 | TCP      | Peer Port (standalone & reverse-proxy)     |
| 8112  | TCP      | webface                                    |

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

* The UID/GID should be set to a user/group that have access to your media.

### Independent Container
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
* Use `-t -d` is needed to keep the container in interactive mode otherwise as
  soon as the container is idle it will sleep, which will stop background
  running services.

### Docker Compose
```yaml
deluge:
  image: linuxserver/deluge:latest
  restart: unless-stopped
  ports:
    - "49160:49160"
    - "49160:49160/udp"
  environment:
    - PGID=1001
    - PUID=1001
    - TZ=America/Los_Angeles
  volumes:
    - /data/downloads/watched:/watch
    - /data/downloads:/data/downloads
    - /data/services/deluge:/config
    - /etc/localtime:/etc/localtime:ro
```
* Port `49160` needs to be exposed for transfers.

Reverse Proxy Setup
-------------------
Allows you to isolate your containers as well as wrap connections in SSL. See
[nginx][ref2] for more details. Recommended.

[nginx/conf.d/reverse-proxy.conf][3]
```nginx
server {
  location /deluge {
    proxy_pass http://deluge:8112/;
    include /etc/nginx/conf.d/proxy-control.conf;
    proxy_set_header X-Deluge-Base '/deluge/';
    add_header X-Frame-Options SAMEORIGIN;
  }
}
```
* [proxy-control.conf][ref1] contains default proxy settings. Reload nginx.

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

[ref1]: ../nginx/proxy-control.conf
[ref2]: ../nginx/README.md