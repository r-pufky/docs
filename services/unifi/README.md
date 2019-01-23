Unifi Controller
-------------
Manage Ubiquity Unifi APs.

[Docker repository][1]

1. [Docker Ports Exposed](#docker-ports-exposed)
1. [Important File Locations](#important-file-locations)
1. [Docker Creation](#docker-creation)
1. [Reverse Proxy Setup](#reverse-proxy-setup)
1. [Configuration](#configuration)

Docker [Ports Exposed][2]
--------------------
| Port | Protocol | Purpose                                                    |
|------|----------|------------------------------------------------------------|
| 3478 | UDP      | Port used for STUN.                                        |
| 8080 | TCP      | Port used for device and controller communication.         |
| 8443 | TCP      | Port used for controller GUI/API as seen in a web browser. |
| 8880 | TCP      | Port used for HTTP portal redirection.                     |
| 8843 | TCP      | Port used for HTTPS portal redirection.                    |

These ports are disabled in this configuration.
| Port      | Protocol | Purpose                                                                            |
|-----------|----------|------------------------------------------------------------------------------------|
| 6789      | TCP      | Port used for UniFi mobile speed test.                                             |
| 27117     | TCP      | Port used for local-bound database communication.                                  |
| 5656-5699 | UDP      | Ports used by AP-EDU broadcasting.                                                 |
| 10001     | UDP      | Port used for AP discovery                                                         |
| 1900      | UDP      | Port used for "Make controller discoverable on L2 network" in controller settings. |

Important File Locations
------------------------
Relative to docker container

| File       | Purpose                              |
|------------|--------------------------------------|
| /config    | Unifi main service directory.        |

Docker Creation
---------------
You can copy your existing configuration to docker `/config` directory
adjusting for paths.

* `unstable` is the current release branch. `latest` is 5.6.x branch.

### Independent Container
```bash
docker run -t -d \
  --name unifi \
  --restart unless-stopped \
  -p 3478:3478/udp \
  -p 8080:8080 \
  -p 8443:8443 \
  -p 8880:8880 \
  -p 8843:8843 \
  -e PUID=1001 \
  -e PGID=1001 \
  -e TZ=America/Los_Angeles \
  -v /etc/localtime:/etc/localtime:ro \
  -v /data/services/unifi:/config \
  linuxserver/unifi:unstable
```
* Use `-t -d` is needed to keep the container in interactive mode otherwise
  as soon as the container is idle it will sleep, which will stop background
  running services.

### Docker Compose
```yaml
unifi:
  image: linuxserver/unifi:unstable
  restart: unless-stopped
  ports:
    - '3478:3478/udp'
    - '8080:8080'
    - '8443:8443'
    - '8880:8880'
    - '8843:8843'
  environment:
    - TZ=America/Los_Angeles
  volumes:
    - /data/services/unifi:/config
    - /etc/localtime:/etc/localtime:ro
```

Reverse Proxy Setup
-------------------
Allows you to isolate your containers as well as wrap connections in SSL. See
[nginx][ref2] for more details. Recommended.

docker-compose.yml
```yaml
sonarr:
  image: linuxserver/sonarr:latest
  restart: unless-stopped
  depends_on:
    - nzbget
  environment:
    - PGID=1001
    - PUID=1001
    - TZ=America/Los_Angeles
  volumes:
    - /data/downloads:/data/downloads
    - /data/media/tv:/data/media/tv
    - /data/services/sonarr:/config
    - /etc/localtime:/etc/localtime:ro
```
* Proxy will forward traffic to the container, so no ports need to be exposed.

### Using Subdomains
nginx/conf.d/reverse-proxy.conf
```nginx
# Websockets: remap http_upgrade to 'upgrade' or 'close' based on
# connection_upgrade being set.
map $http_upgrade $connection_upgrade {
    default upgrade;
    '' close;
}

server {
  listen 443 ssl http2;
  server_name unifi.<DOMAIN> unifi;

  location / {
    proxy_pass https://unifi:8443;

    proxy_cache off;
    proxy_store off;
    proxy_buffering off;
    proxy_http_version 1.1;
    proxy_read_timeout 36000s;

    proxy_set_header Host $http_host;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection $connection_upgrade;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header Referer '';

    client_max_body_size 0;
  }
}
```
* [proxy-control.conf][ref1] contains default proxy settings. Reload nginx.

### Using Subpaths
nginx/conf.d/reverse-proxy.conf
```nginx
# Websockets: remap http_upgrade to 'upgrade' or 'close' based on
# connection_upgrade being set.
map $http_upgrade $connection_upgrade {
    default upgrade;
    '' close;
}

server {
  location /sonarr/ {
    proxy_pass https://unifi:8443/;

    proxy_cache off;
    proxy_store off;
    proxy_buffering off;
    proxy_http_version 1.1;
    proxy_read_timeout 36000s;

    proxy_set_header Host $http_host;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection $connection_upgrade;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header Referer '';

    client_max_body_size 0;
  }
}
```
* [proxy-control.conf][ref1] contains default proxy settings. Reload nginx.

Configuration
-------------
Ensure DNS/hosts is setup for unifi controller.

### Router Configuration
Forward traffic to Unifi Controller for AP to be managed - will be located
slightly differently for each server.

1. `Firewall Policies`
  1. `<AP IP> <UNIFI CONTROLLER IP> 8443,8080 tcp` (AP Management)
  1. `<AP IP> <UNIFI CONTROLLER IP> 3478` (AP STUN)

### Enable Unifi Controller Assignment in EdgeOS or DHCP Option 43
This should be enable for subnets in which the AP will reside. This will enable
the AP to be auto-detected by the controller.

#### EdgeOS
* `Services > DNS > Subnet > Details > Unifi Controller`
  * IP of Unifi controller.

#### DHCP Option 43
For non-EdgeOS routers, this can be enabled in using [option 43][3].

dhcpd.conf
```dhcpd
option space ubnt;
option ubnt.unifi-address code 1 = ip-address;

class "ubnt" {
        match if substring (option vendor-class-identifier, 0, 4) = "ubnt";
        option vendor-class-identifier "ubnt";
        vendor-option-space ubnt;
}

subnet 10.10.10.0 netmask 255.255.255.0 {
        range 10.10.10.100 10.10.10.160;
        option ubnt.unifi-address 201.10.7.31;  ### UniFi Controller IP ###
        option routers 10.10.10.2;
        option broadcast-address 10.10.10.255;
        option domain-name-servers 168.95.1.1, 8.8.8.8;
        # ...
}
```
* Example IP's used.

[1]: https://hub.docker.com/r/linuxserver/unifi/
[2]: https://help.ubnt.com/hc/en-us/articles/218506997-UniFi-Ports-Used
[3]: https://help.ubnt.com/hc/en-us/articles/204909754-UniFi-Device-Adoption-Methods-for-Remote-UniFi-Controllers#7

[ref1]: ../nginx/proxy-control.conf
[ref2]: ../nginx/README.md