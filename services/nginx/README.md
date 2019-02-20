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
1. [Adding Reverse Proxies](#adding-reverse-proxies)
1. [Configuration Patterns](#configuration-patterns)
1. [Debugging Headers](#debugging-headers)

Docker Ports Exposed
--------------------
Docker Compose

| Docker Port | Protocol | Exposed/Public | Purpose                               |
|-------------|----------|----------------|---------------------------------------|
| 80          | TCP      | Public         | http connection, redirected to https. |
| 443         | TCP      | Public         | https connections.                    |


Important File Locations
------------------------
Relative to docker container

| File                    | Purpose                       |
|-------------------------|-------------------------------|
| /etc/nginx/conf.d       | Proxy configuration settings. |
| /etc/nginx/ssl          | SSL certificate location.     |

Docker Creation
---------------
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

[Automatic generator][13] to generate base configuration templates.

/etc/nginx/conf.d/reverse-proxy.conf
```nginx
# Forward all HTTP IPv4/6 traffic to HTTPS.
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
  ssl_trusted_certificate /etc/nginx/ssl/live/<DOMAIN_NAME>/chain.pem;
  ssl_dhparam /etc/nginx/ssl/ssl-dhparams.pem;
  include /etc/nginx/ssl/options-ssl-nginx.conf;

  # Enable OCSP stapling https://en.wikipedia.org/wiki/OCSP_stapling.
  ssl_stapling on;
  ssl_stapling_verify on;

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

### Rewrite reponses with sub-path
Some applications are not [URI Path aware][11] and will re-write all responses
behind the proxy using a static relative path or hostname; which will cause 404
errors and the app to break. Partially fixed using [http_sub_module][12].

Note: Re-writing the proxy respones generally won't fix a complicated
application as there will be a large number of unknown responses that need to be
re-written. Usually this is resolved using a sub-domain instead.

```nginx
sub_filter https://app:port/ https://reverse-proxy-server/subpath/;
sub_filter 'href="/' 'href="https://reverse-proxy-server/subpath/';
sub_filter_once off;
```
* First rule rewrites responses from the app: `https://app:port/page.html` to
  `https://reverse-proxy-server/subpath/page.html`.
* Second rules rewrites relative responses `href="/other-page.html"` to
  `href="https://reverse-proxy-server/subpath/other-page.html"`.

Configuration Patterns
----------------------
General good configuration practice patterns after using nginx as a reverse
proxy for a while.

### One Site Per Config File
Keep one site per configuration file to focus only on that site. This will help
reduce errors and allow fast lookup / disable of configurations.

1. Create a services directory:

```bash
mkdir /etc/nginx/conf.d/services
```

1. Add each site to `/etc/nginx/conf.d/services/{SITE}.conf`.
1. Modify default config to auto import sites / services:

/etc/nginx/conf.d/default.conf
```nginx
include /etc/nginx/conf.d/services/*.conf;
```

Adding a site in services and restart nginx will now automatically pickup that
site.

### Site-wide Auth File
Keep authentication definitions for different services to one file to maintain
authentication consistency across multiple sites.

1. Create an authentication [block and store in a file][3].

/etc/nginx/conf.d/site-auth.conf
```nginx
# Allow all on 10.1.1.0/24 through, and force auth for everyone else.
satisfy any;
allow 10.1.1.0/24;
deny all;
auth_basic 'Your Site';
auth_basic_user_file /etc/nginx/conf.d/your_site.pass
```

1. Include authentication block where authentication would be required:

/etc/nginx/conf.d/services/my-site.conf
```nginx
location / {
  ...

  include /etc/nginx/conf.d/site-auth.conf;
  proxy_pass ...
  ...
}
```

### Remove Auth Requirement for Docker Containers
For docker containers running with nginx, the docker network or specific IP
would need to be whitelisted. This allows dashboards and services to communicate
using FQDNs without needing basic auth.

#### [Whitelist All Containers][16]
1. Determine network that containers are on:

```bash
docker network ls
docker network inspect docker_default
```

1. Add IP range to the authorization file

/etc/nginx/conf.d/site-auth.conf
```nginx
allow 172.18.0.0/16;
```

#### [Whitelist Single Container][15]
1. Set static IP for docker container (otherwise it is random)

docker-compose.yml
```yaml
container_name:
  ...
  networks:
  agent:
    ipv4_address: 172.18.0.101
```

1. Whitelist specific IP in auth file

/etc/nginx/conf.d/site-auth.conf
```nginx
allow 172.18.0.101;
```

Debugging Headers
-----------------
To validate parameters passed to upstream services, the request should be
dumped by the service or intercepted by another service temporarily. There is a
[docker container to do this][13]. This will dump the recieved headers from both
http and https communication to the upstream service.

docker-compose.yml
```yaml
http-echo:
  image: mendhak/http-https-echo
```

```nginx
location / {
   ...
   proxy_pass http://http-echo/;
}
```
* Headers will be dumped directly to the page.

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
[11]: https://stackoverflow.com/questions/32542282/how-do-i-rewrite-urls-in-a-proxy-response-in-nginx
[12]: http://nginx.org/en/docs/http/ngx_http_sub_module.html
[13]: https://nginxconfig.io
[14]: https://github.com/mendhak/docker-http-https-echo
[15]: https://stackoverflow.com/questions/45358188/restrict-access-to-nginx-server-location-to-a-specific-docker-container-with-al
[16]: https://docs.docker.com/v17.09/engine/userguide/networking/#the-default-bridge-network

[ref1]: proxy-control.conf
[ref2]: ..
[ref3]: site-auth.conf