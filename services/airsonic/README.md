[Airsonic][78] Server
=====================
Music streaming.

1. [Ports](#ports)
1. [Important File Locations](#important-file-locations)
1. [Docker Creation](#docker-creation)
1. [Reverse Proxy Setup](#reverse-proxy-setup)

Ports
-----
Docker reverse-proxy.

| Port | Protocol | Exposed/Public | Purpose              |
|------|----------|----------------|----------------------|
| 4040 | TCP      | Exposed        | Airsonic webservice. |

Important File Locations
------------------------
Relative to docker container.

| File       | Purpose                                             |
|------------|-----------------------------------------------------|
| /data      | Airsonic configuration directory.                   |
| /data/airsonic.properties | Global [airsonic configuration.][q0] |
| /playlists | Playlists data.                                     |
| /podcasts  | Podcasts data.                                      |
| /music     | Music data.                                         |

[Docker][8c] Creation
---------------------
You can copy your existing configuration to docker _/data_ directory
adjusting for paths.

Docker Compose:
```yaml
airsonic:
  image: airsonic/airsonic:latest
  restart: unless-stopped
  environment:
    - TZ=America/Los_Angeles
  volumes:
    - /data/services/airsonic/data:/airsonic/data
    - /data/services/airsonic/playlists:/airsonic/playlists
    - /data/media/podcasts:/airsonic/podcasts:ro
    - /data/media/music:/airsonic/music:ro
    - /etc/localtime:/etc/localtime:ro
```
* Proxy will forward traffic to the container, so no ports need to be exposed.

Reverse Proxy Setup
-------------------
Allows you to isolate your containers as well as wrap connections in SSL. See
[nginx][refci] for more details. Site [documentation][8c].

### Enable Forward Headers
Airsonic must be configured to expect requests through a proxy. Enable this and
restart the service before testing proxy configuration.

/data/airsonic.properties `root:root 0644`
```airsonic
server.use-forward-headers=true
```

### Using Subdomains
[nginx/conf.d/reverse-proxy.conf][4j] `root:root 0644`
```nginx
server {
  listen 443 ssl http2;
  server_name airsonic.{DOMAIN} airsonic;

  location / {
    proxy_bind {NGINX PROXY IP};
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto https;
    proxy_set_header X-Forwarded-Host $http_host;
    proxy_set_header Host $http_host;
    proxy_set_header X-Forwarded-Server $host;
    proxy_max_temp_file_size 0;
    proxy_pass http://airsonic:4040;
    add_header Strict-Transport-Security "max-age=15768000; includeSubDomains; preload;";
    add_header X-Content-Type-Options "nosniff";
    add_header X-Frame-Options SAMEORIGIN;
    add_header X-XSS-Protection "1; mode=block";
    add_header X-Robots-Tag none;
  }
}
```

### Using Subpaths
[nginx/conf.d/reverse-proxy.conf][4j] `root:root 0644`
```nginx
server {
  listen 443 ssl http2;
  server_name airsonic.{DOMAIN} airsonic;

  location /airsonic {
    proxy_bind {NGINX PROXY IP};
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto https;
    proxy_set_header X-Forwarded-Host $http_host;
    proxy_set_header Host $http_host;
    proxy_set_header X-Forwarded-Server $host;
    proxy_max_temp_file_size 0;
    proxy_pass http://airsonic:4040;
    add_header Strict-Transport-Security "max-age=15768000; includeSubDomains; preload;";
    add_header X-Content-Type-Options "nosniff";
    add_header X-Frame-Options SAMEORIGIN;
    add_header X-XSS-Protection "1; mode=block";
    add_header X-Robots-Tag none;
  }
}
```

[docker-service-template.md|c9067f2][XX]

[78]: https://airsonic.github.io/
[q0]: https://airsonic.github.io/docs/configure/airsonic-properties/
[8c]: https://hub.docker.com/r/airsonic/airsonic
[6k]: https://airsonic.github.io/docs/proxy/nginx/
[4j]: https://old.reddit.com/r/freenas/comments/b2ft7x/does_anyone_have_a_working_nginx_reverseproxy_for/
[XX]: https://github.com/r-pufky/docs/blob/c9067f2bc3d0aeb0f2915e63f8cd9515c00640a2/services/docker-service-template.md

[ref0p]: ../nginx/proxy-control.conf
[refci]: ../nginx/README.md