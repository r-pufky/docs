nginx
-----
[Reverse proxy and load balancer][1] This provides a way to place services
behind a proxy and enforce SSL for those applications, as well as being able to
offer a clean namespace for multiple microservices.

This setup will focus on creating a docker-based reverse proxy, enforcing SSL
for all connections to docker containers using Let's Encrypt.

[Docker repository][5]

1. [Docker Ports Exposed](#docker-ports-exposed)
1. [Important File Locations](#important-file-locations)
1. [Docker Creation](#docker-creation)
1. [Initial Setup](#initial-setup)
1. [Importing Git Repositories](#importing-git-epositories)
1. [Other Options](#other-options)

Docker Ports Exposed
--------------------

| Docker Port | Protocol |Purpose                                |
|-------------|----------|---------------------------------------|
| 80          | TCP      | http connection, redirected to https. |
| 443         | TCP      | https connections.                    |


Important File Locations
------------------------
Relative to docker container

| File                    | Purpose                       |
|-------------------------|-------------------------------|
| /etc/nginx/conf.d       | Proxy configuration settings. |
| /etc/nginx/ssl          | SSL certificate location.     |

Docker Creation
---------------
### Independant Container
```bash
docker run -t -d \
  --name=nginx-proxy \
  --net=host \
  --restart=unless-stopped \
  -p 80:80 \
  -p 443:443 \
  -e /etc/localtime:/etc/localtime:ro \
  -v /data/services/nginx/conf.d:/etc/nginx/conf.d:ro \
  -v /data/services/letsencrypt:/etc/nginx/ssl:ro \
  -v /etc/localtime:/etc/localtime:ro
  nginx
```
* Use `-t -d` is needed to keep the container in interactive mode otherwise as
  soon as the container is idle it will sleep, which will stop background
  running services.

### Docker Compose
```yaml
nginx-proxy:
  image: nginx
  restart: unless-stopped
  ports:
    - '80:80'
    - '443:443'
  volumes:
    - /data/services/nginx/conf.d:/etc/nginx/conf.d:ro
    - /data/services/letsencrypt:/etc/nginx/ssl:ro
    - /etc/localtime:/etc/localtime:ro
```
* Let's Encrypt local mount should just point the install location of let's
  encrypt, typically `/etc/letsencrypt`.

Initial Setup
-------------
### Setup Base Reverse Proxy
This will setup a basic reverse-proxy that:

* Force HTTP to HTTPS connections for IPv4/6 with a permenant redirect.
* Serve traffic only over SSL (443).
* Enable HTTP2 if the service behind the proxy supports it.
* Ability to upgrade a connection to a websocket if a service requires it.
* Direct requests to the proxy cannot contain data.
* Import SSL certificate settings used in Let's Encrypt for strong validation of
  certifcate usage.

/etc/nginx/conf.d/reverse-proxy.conf
```nginx
# Forward all HTTP/HTTPS IPv4/6 traffic to HTTPS.
server {
  listen 80 default_server;
  listen [::]:80 default_server;
  server_name <SERVER_DNS_NAME>;
  return 301 https://$server_name$request_uri;
}

# Websockets: remap http_upgrade to 'upgrade' or 'close' based on
# connection_upgrade being set.
map $http_upgrade $connection_upgrade {
    default upgrade;
    '' close;
}

server {
  listen 443 ssl http2;

  # Import SSL certificate options from letsencrypt
  ssl_certificate /etc/nginx/ssl/live/<DOMAIN_NAME>/fullchain.pem;
  ssl_certificate_key /etc/nginx/ssl/live/<DOMAIN_NAME>/privkey.pem;
  ssl_dhparam /etc/nginx/ssl/ssl-dhparams.pem;
  include /etc/nginx/ssl/options-ssl-nginx.conf;

  client_max_body_size 0;
}
```
* The `SERVER_DNS_NAME` should be in the SSL certificate; a [wildcard
  certificate][5] will work.
* `ssl-dhparams.pem` may be generated with `sudo openssl dhparam -out
  ssl-dhparams.pem 4096`.

### Setup Base Proxy Control
A proxy control template will enable complex proxy configurations to be applied
easily to proxies.

[/etc/nginx/conf.d/proxy-control.conf][ref1]
```nginx
client_max_body_size 10m;
client_body_buffer_size 128k;

#Timeout if the real server is dead
proxy_next_upstream error timeout invalid_header http_500 http_502 http_503;

# Advanced Proxy Config
send_timeout 5m;
proxy_read_timeout 240;
proxy_send_timeout 240;
proxy_connect_timeout 240;

# Basic Proxy Config
proxy_set_header Host $host:$server_port;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
proxy_set_header X-Forwarded-Proto https;
proxy_redirect  http://  $scheme://;
proxy_http_version 1.1;
proxy_set_header Connection '';
proxy_cache_bypass $cookie_session;
proxy_no_cache $cookie_session;
proxy_buffers 32 4k;
```

### Reload Configuration
nginx can update the proxy configuration without downtime.

```bash
docker exec -it nginx-proxy nginx -s reload
```
* If underlying services have changed `expose` or `ports`, those containers
  will need to be restarted.

Adding Reverse Proxies
----------------------
This will cover the basic usage of nginx as a reverse proxy; covering services
on the URI path, not as a custom subdomain. See [subdomain reverse proxy][6] for
setting up subdomains.

See [services][ref2] for specific details as well as [reference
documentation][3] and [location block][4] reference.

`location` blocks should be placed in the `server` block.

### Service Gotchas
Ensure the services running behind the proxy are in a known configuration.

* Running on expected protocols (http or https).
* Externally accessible ports (e.g. non-proxied external requests) are setup as
  `ports`.
* Internally accessible ports (e.g. proxied external requests) are setup as
  `expose` ports.

See [expose versus ports][10].

### [Trailing Slash Gotchas][7]
See [proxy_pass reference documentation][9].

In Short:

* Services already using URI paths for the services should leaving **off**
  trailing slashes in `location` and `proxy_pass`.
* Services using **no** additional URI paths for services should use trailing
  slashes in `location` and `proxy_pass`.

Explanation:
If the proxy_pass directive is specified with a URI, then when a request is
passed to the server, the part of a _normalized request URI matching the
location is replaced by a URI specified in the directive_:

```nginx
location /name/ {
  proxy_pass http://app/remote/;
}
```
* Assume request: http://proxy/name/path?params=1
* http://app/remote/ sees request as https://app/remote/path?params=1
* Essentially, the matched URI path is remove and the rest is passed as though
  it was called from app's page.

If proxy_pass is specified without a URI, the request URI is passed to the
server in the same form as sent by a client when the original request is
processed, or the full normalized request URI is passed when processing the
changed URI:

```nginx
location /name/ {
    proxy_pass http://app/remote;
}
```
* Assume request: http://proxy/name/path?params=1
* http://app/remote/ sees request as https://app/remote/name/path?params=1
* Essentially, the URI path is concatenated to the end of the remote path.

### Regex Versus Trailing Slashes
Most examples on the web use regex, but regex is generally [slow, error prone
and hard to read][8]. In nginx most regexes may be replaced with trailing slash
ability to replace the matched URI path instead. It's cleaner and easier to
read, and usually covers the regex case.

Web Regex Example (bad) that proxies /nzbget to https://nzbget:6791/
```nginx
location ~ ^/nzbget$ {
  return 302 $scheme://$host$request_uri/;
}
location ~ ^/nzbget($|./*) {
  rewrite /nzbget/(.*) /$1 break;
  proxy_pass https://nzbget:6791;
  include /etc/nginx/conf.d/proxy.conf;
  proxy_set_header Host $host;
}
```
* First rule regex matches `nzbget` and returns a 302 to the same URI with a
  trailing slash.
* Second rule accepts `/nzbget` with parameters and proxies to the service.
* This results in two proxy hits and two regex comprehensions; it's also hard to
  understand what the regex is doing immediately.

Using trailing slashes (good) that proxies /nzbget to https://nzbget:6791/
```nginx
location /nzbget/ {
  proxy_pass https://nzbget:6791/;
  include /etc/nginx/conf.d/proxy.conf;
  proxy_set_header Host $host;
}
```

### Redirect path to base URI
For applications that serve https://app/

```nginx
location /gogs/ {
  proxy_pass https://gogs:3000/;
}
```
* Note trailing slashes.

### Redirect path to service URI path
For applications that serve https://app/path

```nginx
location /sonarr {
  proxy_pass http://sonarr:8989/sonarr;
  include /etc/nginx/conf.d/proxy-control.conf;
}
```
* Note **no** trailing slashes.

### Custom Path for Service
This will allow you to hit the same service using shortcuts, `tv` & `sonarr`.

```nginx
location /tv {
  return 301 $scheme://$host/sonarr/;
}
location /sonarr {
  proxy_pass http://sonarr:8989/sonarr;
  include /etc/nginx/conf.d/proxy-control.conf;
}
```
* `tv` will automatically redirect to `sonarr`.

### Enable Websockets
This will allow for apps requiring websockets to be used.

```nginx
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
```
* Upgrade and Connection must be used, and pass values through the websocket map
  to enable the connection upgrade or close the connection.
* `proxy_http_version 1.1` is required, but included in `proxy-control.conf`.

[1]: https://www.nginx.com/
[2]: https://hub.docker.com/_/nginx
[3]: https://docs.nginx.com/nginx/admin-guide/installing-nginx/installing-nginx-open-source/
[4]: https://www.digitalocean.com/community/tutorials/understanding-nginx-server-and-location-block-selection-algorithms
[5]: https://medium.com/@utkarsh_verma/how-to-obtain-a-wildcard-ssl-certificate-from-lets-encrypt-and-setup-nginx-to-use-wildcard-cfb050c8b33f
[6]: https://community.home-assistant.io/t/nginx-reverse-proxy-set-up-guide-docker/54802
[7]: https://stackoverflow.com/questions/22759345/nginx-trailing-slash-in-proxy-pass-url
[8]: https://stackoverflow.com/questions/764247/why-are-regular-expressions-so-controversial
[9]: http://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_pass
[10]: https://medium.freecodecamp.org/expose-vs-publish-docker-port-commands-explained-simply-434593dbc9a3

[ref1]: proxy-control.conf
[ref2]: ..