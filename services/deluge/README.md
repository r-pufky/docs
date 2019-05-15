[Deluge][8v]
============
Deluge docker instalation.

1. [Ports](#ports)
1. [Important File Locations](#important-file-locations)
1. [Docker Creation](#docker-creation)
1. [Reverse Proxy Setup](#reverse-proxy-setup)
1. [Modifying Settings](#modifying-settings)
1. [Reset Password](#reset-password)

Ports
-----
Docker reverse-proxy.

| Port  | Protocol | Exposed/Public | Purpose                  |
|-------|----------|----------------|--------------------------|
| 49160 | UDP/TCP  | Public         | Peer Port for transfers. |
| 8112  | TCP      | Exposed        | Webface.                 |

Important File Locations
------------------------
Relative to docker container.

| File                  | Purpose              |
|-----------------------|----------------------|
| /config/core.conf     | Daemon Settings.     |
| /config/web.conf      | WebUI Settings.      |
| /watch                | Watch direcotry.     |
| /downloads            | Downloads directory. |

Docker Creation
---------------
If first-run, just launch the docker container to generate the correct
configuration directory structure, afterwards you can re-create with a mapped
directories.

* The UID/GID should be set to a user/group that have access to your media. All
  media clients should run under the same user to run correctly.

Docker Compose:
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
* Port _49160_ needs to be exposed for transfers.

Reverse Proxy Setup
-------------------
Allows you to isolate your containers as well as wrap connections in SSL. See
[nginx][refek] for more details.

### Using Subdomains
[nginx/conf.d/reverse-proxy.conf][ui] `root:root 0644`
```nginx
server {
  listen 443 ssl http2;
  server_name deluge.{DOMAIN} deluge;

  location / {
    proxy_pass http://deluge:8112;
    include /etc/nginx/conf.d/proxy-control.conf;
    add_header X-Frame-Options SAMEORIGIN;
  }
}
```
* [proxy-control.conf][refof] contains default proxy settings. Reload nginx.

### Using Subpaths
[nginx/conf.d/reverse-proxy.conf][kl] `root:root 0644`
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
* [proxy-control.conf][refof] contains default proxy settings. Reload nginx.

Modifying Settings
------------------
Deluge **must** be connected to the Daemon to [write configuration changes][ui].
Ensure you select `Connect` on `Connection Manager`.

Required changes to minimally secure your configuration.
[/config/core.conf][kl] `1001:1001 0644`
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
> :thought_balloon:  
> _Max upload speed_ should be set to a non-zero number to enable downloads.


Reset Password
--------------
Stop Deluge and remove _pwd_sh1_ pasword line in _web.conf_, restart.

Default username/password is `admin` / `deluge`.

[docker-service-template.md|c9067f2][XX]

[8v]: https://hub.docker.com/r/linuxserver/deluge/
[ui]: https://forum.deluge-torrent.org/viewtopic.php?t=35117
[kl]: https://dev.deluge-torrent.org/wiki/UserGuide/WebUI/ReverseProxy
[XX]: https://github.com/r-pufky/docs/blob/c9067f2bc3d0aeb0f2915e63f8cd9515c00640a2/services/docker-service-template.md

[refof]: ../nginx/proxy-control.conf
[refek]: ../nginx/README.md