[Docker][3n] Service Template
=============================
Background notes on service, VM requirements. TOC is a rought layout adjust as
needed (e.g. docker setups, xen setups, etc).

[Dedicated server setup / service notes][7d].

1. [Ports](#ports)
1. [Docker Capabilities](#docker-capabilities)
1. [Important File Locations](#important-file-locations)
1. [Docker Creation](#docker-creation)
1. [Reverse Proxy Setup](#reverse-proxy-setup)
1. [Service Specific Content Sections](#service-specific-content-sections)

[Ports][u1]
-----------
Docker reverse-proxy.

| Port | Protocol | Exposed/Public | Purpose                        |
|------|----------|----------------|--------------------------------|
| 8337 | TCP      | Exposed        | Web GUI frontend for playback. |
| 9999 | UDP      | Public         | (Optional) some other port.    |

Docker Capabilities
-------------------

| Capability | Action |
|------------|--------|
| NET_ADMIN  | ADD    |

Important File Locations
------------------------
Relative to docker container.

| File         | Purpose        |
|--------------|----------------|
| /config.yaml | configuration. |

Docker Creation
---------------
* The UID/GID should be set to a user/group that have access to your media.
* Map your media directly to where it was before on the docker container to
  prevent needing to modify any libraries.
* Other important points to note while creating docker container.

Docker Compose:
```yaml
beets:
  image: linuxserver/beets:latest
  restart: unless-stopped
  environment:
    - PGID=1001
    - PUID=1001
    - TZ=America/Los_Angeles
  volumes:
    - /data/downloads/complete/music:/data/downloads/complete/music
    - /data/media/music:/data/media/music
    - /data/services/beets:/config
    - /etc/localtime:/etc/localtime:ro
```
* Proxy will forward traffic to the container, so no ports need to be opened.

Reverse Proxy Setup
-------------------
Allows you to isolate your containers as well as wrap connections in SSL. See
[nginx][ref3k] for more details.

{CONTAINER NAME}/important/file/to/modify/for/proxy
```text
example
```

### Using Subdomains
[nginx/conf.d/reverse-proxy.conf][u1] `root:root 0644`
```nginx
server {
  listen 443 ssl http2;
  server_name beets.{DOMAIN} beets;

  location / {
    proxy_pass http://beets:8337;
    include /etc/nginx/conf.d/proxy-control.conf;
    proxy_set_header Host $host;
    proxy_set_header X-Scheme $scheme;
    proxy_set_header X-Script-Name /beets;
  }
}
```
* [proxy-control.conf][refdk] contains default proxy settings. Reload nginx.

### Using Subpaths
[nginx/conf.d/reverse-proxy.conf][ya] `root:root 0644`
```nginx
server {
  location /beets {
    proxy_pass http://beets:8337;
    include /etc/nginx/conf.d/proxy-control.conf;
    proxy_set_header Host $host;
    proxy_set_header X-Scheme $scheme;
    proxy_set_header X-Script-Name /beets;
  }
}
```
* [proxy-control.conf][refdk] contains default proxy settings. Reload nginx.

Service Specific Content Sections
---------------------------------
Add sections as needed for service-specific content.

[docker-service-template.md|XXXXXX][XX]

[3n]: link to the docker container image used.
[u1]: link to all ports a service has if it is avaliable.
[ya]: link to reverse proxy docker setup for container if it exists.
[XX]: link to the commit for the current template used.
[7d]: link to dedicated server setup. Remove line if not used.

[refdk]: ../nginx/proxy-control.conf
[ref3k]: ../nginx/README.md