[OMBI][ek]
==========
Media request management.

1. [Ports](#ports)
1. [Important File Locations](#important-file-locations)
1. [Docker Creation](#docker-creation)
1. [Reverse Proxy Setup](#reverse-proxy-setup)
1. [Plex SSL Errors](#plex-ssl-errors)

Ports
-----
Docker reverse-proxy.

| Port | Protocol | Exposed/Public | Purpose       |
|------|----------|----------------|---------------|
| 3579 | TCP      | Exposed        | OMBI Webface. |

Important File Locations
------------------------
Relative to docker container.

| File       | Purpose                      |
|------------|------------------------------|
| /config    | OMBI main service directory. |

Docker Creation
---------------
You can copy your existing configuration to docker _/config_ directory
adjusting for paths.

* The UID/GID should be set to a user/group that is restricted.

Docker Compose:
```yaml
sonarr:
  image: linuxserver/ombi:latest
  restart: unless-stopped
  environment:
    - PGID=1001
    - PUID=1001
    - TZ=America/Los_Angeles
  volumes:
    - /data/services/sonarr:/config
    - /etc/localtime:/etc/localtime:ro
```

Reverse Proxy Setup
-------------------
Allows you to isolate your containers as well as wrap connections in SSL. See
[nginx][refhu] for more details.

### Using Subdomains
[nginx/conf.d/reverse-proxy.conf][vb] `root:root 0644`
```nginx
server {
  listen 443 ssl http2;
  server_name ombi.{DOMAIN} ombi;

  location / {
    proxy_pass http://ombi:3579;

    proxy_set_header Host $host;
    proxy_set_header X-Forwarded-Host $server_name;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Ssl on;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_read_timeout 90;
    proxy_redirect http://ombi:3759 https://$host;
  }
}
```
* [proxy-control.conf][refio] contains default proxy settings. Reload nginx.

### Using Subpaths
[nginx/conf.d/reverse-proxy.conf][vb] `root:root 0644`
```nginx
server {
  location /ombi/ {
    proxy_pass http://ombi:3579/;

    proxy_set_header Host $host;
    proxy_set_header X-Forwarded-Host $server_name;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Ssl on;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_read_timeout 90;
  }
}
```
* [proxy-control.conf][refio] contains default proxy settings. Reload nginx.

Plex SSL Errors
---------------
OMBI may fail to connect to plex containers on the same machine in which SSL is
being used. This is due to the internal container IP not matching the SSL
certificate issued by Plex that is used by default for connections. Workaround
is to continue to require SSL, but disable SSL validation.

OMBI does not save [all settings on save][bugdk]. Some require the container to
be restarted (for whatever reason, requiring SSL for connections is one of
them).

1. `Settings > Ombi`
  * Check `Ignore any certificate errors`
1. Restart OMBI container
  * `docker stop ombi; docker start ombi`
1. `Settings > Media Server > Plex`
  - [x] `SSL`
  * Use Plex container external IP.
  * Auto generated token is fine.

[docker-service-template.md|c9067f2][XX]

[ek]: https://github.com/linuxserver/docker-ombi
[vb]: https://github.com/tidusjar/Ombi/wiki/Reverse-Proxy-Examples
[XX]: https://github.com/r-pufky/docs/blob/c9067f2bc3d0aeb0f2915e63f8cd9515c00640a2/services/docker-service-template.md

[bugdk]: https://github.com/tidusjar/Ombi/issues/2762

[refio]: ../nginx/proxy-control.conf
[refhu]: ../nginx/README.md