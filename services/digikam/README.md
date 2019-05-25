[digiKam][f8]
=============
digiKam is an advanced open-source digital photo management application that
runs on Linux, Windows, and MacOS. The application provides a comprehensive set
of tools for importing, managing, editing, and sharing photos and raw files.

This setup will focus on creating a docker-based reverse proxy, enforcing SSL
for all connections to docker containers using Let's Encrypt.

1. [Ports](#ports)
1. [Important File Locations](#important-file-locations)
1. [Docker Creation](#docker-creation)
1. [Adding Reverse Proxies](#adding-reverse-proxies)
1. [Initial Setup](#initial-setup)
1. [Usage Gotchas](#usage-gotchas)

Ports
-----
Docker reverse-proxy.

| Docker Port | Protocol | Exposed/Public | Purpose            |
|-------------|----------|----------------|--------------------|
| 443         | TCP      | Public         | https connections. |
| 5800        | TCP      | Private        | websocket webGUI.  |
| 5900        | TCP      | Private        | VNC server.        |

Important File Locations
------------------------
Relative to docker container.

| File    | Purpose                    |
|---------|----------------------------|
| /config | All digiKam configuration. |
| /data   | Media location.            |

[Docker Creation][3m]
---------------------
digiKam runs a web GUI and a VNC server. We will only access the web GUI through
the reverse proxy with authentication.

* Local storage should be locked down to prevent sensitive data from leaking.

Docker Compose:
```yaml
digiKam:
  image: rpufky/digiKam:6.1.0
  environment:
    - USER_ID=1000
    - GROUP_ID=1000
    - UMASK=022
    - TZ=America/Los_Angeles
    - KEEP_APP_RUNNING=1
    - DISPLAY_WIDTH=1920
    - DISPLAY_HEIGHT=1080
    - ENABLE_CJK_FONT=1
  volumes:
    - /my/docker/service/config:/config
    - /my/photo/location:/data
    - /etc/localtime:/etc/localtime:ro
```
* Docker container should be run in an isolated network given the sensitive
  nature of the data and to prevent VNC server access.
* Additional [environment settings here][ne].

Reverse Proxy Setup
-------------------
Allows you to isolate your containers as well as wrap connections in SSL. See
[nginx][refci] for more details. digiKam is intended to be used from a
subdomain.

### Using Subdomains
nginx/conf.d/reverse-proxy.conf `root:root 0644`
```nginx
server {
  listen 443 ssl http2;
  server_name digiKam.{DOMAIN} digiKam;

  location / {
    proxy_bind {PROXY_IP_ON_DIGIKAM_NET};
    include /etc/nginx/conf.d/site-auth.conf;
    proxy_pass http://digiKam:5800/;
    include /etc/nginx/conf.d/proxy-control.conf;
  }

  location /websockify {
    proxy_bind {PROXY_IP_ON_DIGIKAM_NET};
    include /etc/nginx/conf.d/site-auth.conf;
    proxy_pass http://digiKam:5800;
    include /etc/nginx/conf.d/proxy-control.conf;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection $connection_upgrade;
  }
}
```
* [proxy-control.conf][ref0p] contains default proxy settings. Reload nginx.
* [site-auth.conf][ref5g] contain basic auth settings. Reload nginx.

[Initial Setup][ks]
-------------------
Start digiKam and setup the initial configuration location and database. This
only needs to be done on initial container creation. Only two sections are
required for basic functionality:


Configure where you keep your images
- Location: `/data`

Configure where you will store databases
- Type: `SQLite`
- Location: `/config`


[docker-service-template.md|c9067f2][XX]

[f8]: https://www.digikam.org/
[3m]: https://github.com/r-pufky/digikam
[ne]: https://hub.docker.com/r/jlesage/baseimage-gui/#environment-variables
[ks]: https://github.com/r-pufky/digikam#digikam-setup
[XX]: https://github.com/r-pufky/docs/blob/c9067f2bc3d0aeb0f2915e63f8cd9515c00640a2/services/docker-service-template.md

[ref5g]: ../nginx/site-auth.conf
[ref0p]: ../nginx/proxy-control.conf
[refci]: ../nginx/README.md
