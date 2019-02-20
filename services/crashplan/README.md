Crashplan Pro
-------------
Crashplan Pro (For Small Business) is now the only 'consumer' level option for
crashplan.

[Dedicated server setup / service notes](crashplan-dedicated.md)

[Docker repository][1]

1. [Docker Ports Exposed](#docker-ports-exposed)
1. [Important File Locations](#important-file-locations)
1. [Docker Creation](#docker-creation)
1. [Initial Setup](#initial-setup)
1. [Reverse Proxy Setup](#reverse-proxy-setup)
1. [Taking over existing backups](#taking-over-existing-backups)

Docker Ports Exposed
--------------------
Docker Compose

| Port | Protocol | Exposed/Public | Purpose           |
|------|----------|----------------|-------------------|
| 5800 | TCP      | Exposed        | GUI web interface |
| 5900 | TCP      | Exposed        | GUI via VNC       |

Important File Locations
------------------------
Relative to docker container

| File        | Purpose                         |
|-------------|---------------------------------|
| /config/var | Crashplan identity certs        |
| /storage    | Default map for backup location |

Docker Creation
---------------
If first-run, just launch the docker container to generate the correct
configuration directory structure, afterwards you can stop and inject your
current certificates into the configuration directory.

* Crashplan should run as root to be able to read/backup all files
* `/storage` is the default location; however, you can mount any directory as
  long as it doesn't overwrite docker image directories. `/data` is free to use
* `/` is mapped to `/root-mount` to enable backup of any files on `/` for the
  host that also exist in the docker image.
* Map your backup drives as *read only*.

### Docker Compose
```yaml
  crashplan:
    image: jlesage/crashplan-pro:latest
    restart: unless-stopped
    ports:
      - "5800:5800"
    environment:
      - GROUP_ID=0
      - KEEP_APP_RUNNING=1
      - SECURE_CONNECTION=1
      - TZ=America/Los_Angeles
      - USER_ID=0
    volumes:
      - /:/root-mount:ro
      - /data/services/crashplan:/config:rw
      - /data:/data:ro
      - /etc/localtime:/etc/localtime:ro
```

Initial Setup
-------------
```bash
docker stop crashplan
```

## Add existing certs
If you have a current crashplan installation, you can copy your crashplan
identity to `/config/var`.

/config/var
```
.identity
service.pem
.ui_info
```

## Bump inotify limits
Increase [inotify max watch limits][2] on host so crashplan can watch monitored
files.

/etc/sysctl.conf
```bash
fs.inotify.max_user_watches=1048576
```

Then reload `sysctl` or `reboot`.
```bash
sysctl -p /etc/sysctl.conf
```

Then restart crashplan
```bash
docker start crashplan
```

Reverse Proxy Setup
-------------------
Allows you to isolate your containers as well as wrap connections in SSL. See
[nginx][ref2] for more details. Recommended.

docker-compose.yml
```yaml
crashplan:
  image: jlesage/crashplan-pro:latest
  restart: unless-stopped
  environment:
    - GROUP_ID=0
    - KEEP_APP_RUNNING=1
    - SECURE_CONNECTION=1
    - TZ=America/Los_Angeles
    - USER_ID=0
  volumes:
    - /:/root-mount:ro
    - /data/services/crashplan:/config:rw
    - /data:/data:ro
    - /etc/localtime:/etc/localtime:ro
```
* Proxy will forward traffic to the container, so no ports need to be exposed.

### Using Subdomains
[nginx/conf.d/reverse-proxy.conf][4]
```nginx
# Websockets: remap http_upgrade to 'upgrade' or 'close' based on
# connection_upgrade being set.
map $http_upgrade $connection_upgrade {
    default upgrade;
    '' close;
}

server {
  listen 443 ssl http2;
  server_name crashplan.<DOMAIN> crashplan;

  location / {
    proxy_pass https://crashplan:5800/;
    include /etc/nginx/conf.d/proxy-control.conf;
  }

  location /websockify {
    proxy_pass https://crashplan:5800;
    include /etc/nginx/conf.d/proxy-control.conf;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection $connection_upgrade;
  }
}
```
* [proxy-control.conf][ref1] contains default proxy settings. Reload nginx.

### Using Subpaths
[nginx/conf.d/reverse-proxy.conf][4]
```nginx
# Websockets: remap http_upgrade to 'upgrade' or 'close' based on
# connection_upgrade being set.
map $http_upgrade $connection_upgrade {
    default upgrade;
    '' close;
}

server {
  listen 443 ssl http2;

  location /crashplan/ {
    proxy_pass https://crashplan:5800/;
    include /etc/nginx/conf.d/proxy-control.conf;

    location /crashplan/websockify {
      proxy_pass https://crashplan:5800/websockify/;
      include /etc/nginx/conf.d/proxy-control.conf;
      proxy_set_header Upgrade $http_upgrade;
      proxy_set_header Connection $connection_upgrade;
    }
  }
}
```
* Ensure `HTTP` or `HTTPS` for underlying service, depending on whether you are
  running it in the container (`SECURE_CONNECTION=`).
* If a _black screen_ occurs, remove image and pull a new one. Ensure multiple
  containers are **not** running.
* [proxy-control.conf][ref1] contains default proxy settings. Reload nginx.
* The docker container uses [websockets][5] for the built in GUI display.

Taking Over Existing Backups
----------------------------
Read [docker container documentation here][3].

Backup tasks will need to migrated if the locations have changed due to running
in a docker container (these are usually `/` based backups like `/etc`).

If identity was imported then no adoption of a backup set is needed.

[1]: https://github.com/jlesage/docker-crashplan-pro
[2]: https://support.code42.com/CrashPlan/4/Troubleshooting/Linux_real-time_file_watching_errors
[3]: https://github.com/jlesage/docker-crashplan-pro#taking-over-existing-backup
[4]: https://hub.docker.com/r/jlesage/crashplan-pro/#routing-based-on-url-path
[5]: https://stackoverflow.com/questions/15193743/nginx-reverse-proxy-websockets

[ref1]: ../nginx/proxy-control.conf
[ref2]: ../nginx/README.md