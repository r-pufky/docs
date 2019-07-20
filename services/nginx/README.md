[nginx][3k]
==========
[Reverse proxy and load balancer][co] This provides a way to place services
behind a proxy and enforce SSL for those applications, as well as being able to
offer a clean namespace for multiple microservices.

This setup will focus on creating a docker-based reverse proxy, enforcing SSL
for all connections to docker containers using Let's Encrypt.

A detailed [Nginx Administration Handbook is here][ls].

1. [Ports](#ports)
1. [Important File Locations](#important-file-locations)
1. [Docker Creation](#docker-creation)
1. [Initial Setup](#initial-setup)
1. [Adding Reverse Proxies](#adding-reverse-proxies)
1. [Custom Error Pages](#custom-error-pages)
1. [Configuration Patterns](#configuration-patterns)
1. [Debugging](#debugging)

Ports
-----
Docker reverse-proxy.

| Docker Port | Protocol | Exposed/Public | Purpose                               |
|-------------|----------|----------------|---------------------------------------|
| 80          | TCP      | Public         | http connection, redirected to https. |
| 443         | TCP      | Public         | https connections.                    |

Important File Locations
------------------------
Relative to docker container.

| File                    | Purpose                       |
|-------------------------|-------------------------------|
| /etc/nginx/conf.d       | Proxy configuration settings. |
| /etc/nginx/ssl          | SSL certificate location.     |

Docker Creation
---------------
Docker Compose:
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
  encrypt, typically _/etc/letsencrypt_.

Initial Setup
-------------
### Setup Base Reverse Proxy
This will setup a basic reverse-proxy that:
* Forces HTTP to HTTPS connections for IPv4/6 with a permenant redirect.
* Serves traffic only over SSL (443).
* Enables HTTP2 if the service behind the proxy supports it.
* Ability to upgrade a connection to a websocket if a service requires it.
* Direct requests to the proxy cannot contain data.
* Import SSL certificate settings used in Let's Encrypt for strong validation of
  certifcate usage.

[Automatic generator][v9] to generate base configuration templates.

/etc/nginx/conf.d/reverse-proxy.conf `root:root 0644`
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
  resolver 127.0.0.1;

  client_max_body_size 0;
}
```
* The `SERVER_DNS_NAME` should be in the SSL certificate; a [wildcard
  certificate][3l] will work.
* _ssl-dhparams.pem_ may be generated with `openssl dhparam -out
  ssl-dhparams.pem 4096`.
* _resolver_ should be set to a [DNS resolver][rm]. localhost, gateway or pihole
  are all viable options. Check logs to ensure resolution works.

### Setup Base Proxy Control
A proxy control template will enable complex proxy configurations to be
consistenly applied to multiple proxy sites.

[/etc/nginx/conf.d/proxy-control.conf][refss]
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
* If underlying services have changed _expose_ or _ports_, those containers will
  need to be restarted.

Adding Reverse Proxies
----------------------
This will cover the basic usage of nginx as a reverse proxy; covering services
on the URI path, not as a custom subdomain. See [subdomain reverse proxy][kd]
for setting up subdomains.

See [services][refew] for specific details as well as [reference
documentation][io] and [location block][ff] reference.

_location_ blocks should be placed in the _server_ block.

### Service Gotchas
Ensure the services running behind the proxy are in a known configuration.
* Running on expected protocols (http or https).
* Externally accessible ports (e.g. non-proxied external requests) are setup as
  _ports_.
* Internally accessible ports (e.g. proxied external requests) are setup as
  _expose_ ports.

See [expose versus ports][dj].

### [Trailing Slash Gotchas][ik]
See [proxy_pass reference documentation][op].

In Short:
* Services already using URI paths for the services should leave **off**
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
* Assume request: _http://proxy/name/path?params=1_
* http://app/remote/ sees request as _https://app/**remote**/path?params=1_
* Essentially, the matched URI path is removed and the rest is passed as though
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
* Assume request: _http://proxy/name/path?params=1_
* http://app/remote/ sees request as _https://app/**remote**/name/path?params=1_
* Essentially, the URI path is concatenated to the end of the remote path.

### Regex Versus Trailing Slashes
Most examples on the web use regex, but regex is generally [slow, error prone
and hard to read][xv]. In nginx most regexes may be replaced with trailing slash
ability to replace the matched URI path instead. It's cleaner and easier to
read, and usually covers the regex case.

Web Regex Example (_bad_) that proxies /nzbget to https://nzbget:6791/:
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
* First rule regex matches `nzbget` and returns a _302_ to the same URI with a
  trailing slash.
* Second rule accepts `/nzbget` with parameters and proxies to the service.
* This results in two proxy hits and two regex comprehensions; it's also hard to
  understand what the regex is doing immediately.

Using trailing slashes (_good_) that proxies /nzbget to https://nzbget:6791/:
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
This will allow you to hit the same service using shortcuts, _tv_ & _sonarr_.

```nginx
location /tv {
  return 301 $scheme://$host/sonarr/;
}
location /sonarr {
  proxy_pass http://sonarr:8989/sonarr;
  include /etc/nginx/conf.d/proxy-control.conf;
}
```
* _tv_ will automatically redirect to _sonarr_.

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
Some applications are not [URI Path aware][wm] and will re-write all responses
behind the proxy using a static relative path or hostname; which will cause 404
errors and the app to break. Partially fixed using [http_sub_module][o3].

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

Custom Error Pages
------------------
Setup a custom [error page][v7] to serve [all errors][9x].

> :warning:  
> The _root_ for web serving must be set for both the http and https server,
> otherwise it will default to what nginx was built with. This will produce
> hard to debug errors with the page not loading.

Set root web folder for http server:
```bash
server {
  ...
  root /www;
  ...
}
```
* This assumes _http_ is redirected to _https_; so no error block needed.

Set root web folder for https server, and redirect all errors to custom page.
```bash
server {
  root /www;
  error_page 400 401 402 403 404 405 406 407 408 409 410 411 412 413 414 415 416 417 418 421 422 423 424 426 428 429 431 451 500 501 502 503 504 505 506 507 508 510 511 /error.html;
  location = /error.html {
    allow all;
    internal;
    root /www;
  }
}
```
* This _must_ be defined for each server block.
* `internal` marks the location as internal redirect only.
* root is defined to enable image file serving for the error. Static error pages
  do not need this, but a root should be defined regardless for predicatable
  behavior.
* This should be defined in the server block before other rules.

/www/error.html `root:root 0644`
```bash
<html>
<head>
<style type=text/css>
div {
  text-align: center;
  font-family: sans-serif;
  font-weight: bold;
  font-size: 3em;
  position: absolute;
  top: 410px;
  width: 100%;
}
body {
  background-repeat: no-repeat;
  background-position: center top;
  background-image: 1.png;
}
</style>
<script type='text/javascript'>
function background(){
  var BG = Math.ceil(Math.random() * 12);
  document.body.background = 'img/' + BG + '.png';
}
</script>
</head>
</html>
<body onload='background();'>
<div>Whoops.</div>
</html>
```
* this example randomly loads a background image when the page is loaded.

Configuration Patterns
----------------------
General good configuration practice patterns after using nginx as a reverse
proxy for a while.

### One Site Per Config File
Keep one site per configuration file to focus only on that site. This will help
reduce errors and allow fast lookup / disable of configurations.

Create a services directory:
```bash
mkdir /etc/nginx/conf.d/services
```

Add each site to `/etc/nginx/conf.d/services/{SITE}.conf`. Then modify default
config to auto import sites / services.

/etc/nginx/conf.d/default.conf `root:root 0644`
```nginx
include /etc/nginx/conf.d/services/*.conf;
```

Adding a site in services and restarting nginx will now automatically pickup
that site.

### Site-wide Auth File
Keep authentication definitions for different services to one file to maintain
authentication consistency across multiple sites.

Create an authentication [block and store in a file][io].

/etc/nginx/conf.d/site-auth.conf `root:root 0644`
```nginx
# Allow all on 10.1.1.0/24 through, and force auth for everyone else.
satisfy any;
allow 10.1.1.0/24;
deny all;
auth_basic 'Your Site';
auth_basic_user_file /etc/nginx/conf.d/your_site.pass
```

Include authentication block where authentication would be required.

/etc/nginx/conf.d/services/my-site.conf `root:root 0644`
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

#### [Whitelist All Containers][7m]
Determine network that containers are on:
```bash
docker network ls
docker network inspect docker_default
```

Add IP range to the authorization file.

/etc/nginx/conf.d/site-auth.conf `root:root 0644`
```nginx
allow 172.18.0.0/16;
```

#### [Whitelist Single Container][0f]
Set static IP for docker container (otherwise it is random).

docker-compose.yml
```yaml
container_name:
  ...
  networks:
  agent:
    ipv4_address: 172.18.0.101
```

Whitelist specific IP in auth file.

/etc/nginx/conf.d/site-auth.conf
```nginx
allow 172.18.0.101;
```

### Disable Auth for a specific location
Explicitly disable auth and allow all to remove any auth enforcement for a
specific location. This is for proxied sites that do their own authentication
(e.g. git) or for specific locations which shouldn't be auth'ed.

Explicitly set no authentication and allow all to prevent any configuration
carried over from the default site.

/etc/nginx/conf.d/services/my-site.conf `root:root 0644`
```nginx
location / {
  ...
  auth_basic off;
  allow all;
  proxy_pass ...
  ...
}
```

### Accessing Networks from Other Compose Containers
Custom networks may be explicitly accessed by other containers (e.g. a
reverse-proxy) by explicitly defining them within the compose definition.

_service-name_/docker-compose.yml `root:staff 0640`
```yaml
networks:
  custom_net_name:
    external: true
...
services:
  my_proxy:
    networks:
      my_proxy_network:
      custom_net_name:
```
* _custom_net_name_ is a network defined in another container. Once this is
  added, the proxy container will be able to do DNS resolution of container
  names as usual, including proxying traffic to that network.

### Show Loaded nginx Configuration
This will show the loaded configuration files, what ordered they were loaded in
and any issues loading them.

```bash
sudo nginx -T
```

Debugging
---------

### Validating upstream parameters
To validate parameters passed to upstream services, the request should be
dumped by the service or intercepted by another service temporarily. There is a
[docker container to do this][8k]. This will dump the recieved headers from both
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

### Debug nginx configs
There is no existing logging functionality in nginx to write directly to logs
from configuration files. This can be worked aorund by directly injecting
[debugging headers][h5] in configuration files to dump information to logs.

```nginx
add_header X-debug-message "some message to write" always;
```

### If is Evil
If operates as a rewrite and is [inherently misunderstood][h6].

Within a location block the only **safe** operations are
* `return`
* `rewrite`

All if operations must be explicitly tested for [appropropriate behavior.][h7]

Nginx queries Originate from Wrong Gateway
------------------------------------------
[Docker does not provide a way][bugdx] to set the [appropriate default
gateway][bugfk] for multi-network containers. This results in
[non-deterministic][bugsf] source IP [routing][buge9].

Per [documentation][bugdx]:
> :warning:
> When a container is connected to multiple networks, its external connectivity
> is provided via the first non-internal network, in lexical order.

Nginx expresses this bug by forwarding/proxying any traffic _over_ the default
gateway for the first lexical named network that appears.

The current fix is to inspect the container and find the first _gateway_ listed
in the connected networks. This will be the _default gateway_ for the container.

There is currently no clean way to set a default gateway via compose.

```bash
docker inspect proxy_nginx_1
```

### Forward Traffic via Specific Interfaces
Nginx can forward traffic via [specific interfaces][dm] for _location_
definitions.

_service-name_/docker-compose.yml `root:staff 0640`
```yaml
networks:
  custom_net_name:
    external: true
...
services:
  my_proxy:
    networks:
      my_proxy_network:
        ipv4_address: 172.1.1.1
      custom_net_name:
        ipv4_address: 172.2.1.1
```
* _custom_net_name_ is a network defined in another container. Once this is
  added, the proxy container will be able to do DNS resolution of container
  names as usual, including proxying traffic to that network.
* Use IPv4 address for _proxy_bind_ command for specific locations.

```nginx
location / {
  proxy_bind {NGINX NETWORK IP};
  proxy_pass ...
}
```

[docker-service-template.md|c9067f2][XX]

[co]: https://www.nginx.com/
[3k]: https://hub.docker.com/_/nginx
[io]: https://docs.nginx.com/nginx/admin-guide/installing-nginx/installing-nginx-open-source/
[ff]: https://www.digitalocean.com/community/tutorials/understanding-nginx-server-and-location-block-selection-algorithms
[3l]: https://medium.com/@utkarsh_verma/how-to-obtain-a-wildcard-ssl-certificate-from-lets-encrypt-and-setup-nginx-to-use-wildcard-cfb050c8b33f
[kd]: https://community.home-assistant.io/t/nginx-reverse-proxy-set-up-guide-docker/54802
[ik]: https://stackoverflow.com/questions/22759345/nginx-trailing-slash-in-proxy-pass-url
[xv]: https://stackoverflow.com/questions/764247/why-are-regular-expressions-so-controversial
[op]: http://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_pass
[dj]: https://medium.freecodecamp.org/expose-vs-publish-docker-port-commands-explained-simply-434593dbc9a3
[wm]: https://stackoverflow.com/questions/32542282/how-do-i-rewrite-urls-in-a-proxy-response-in-nginx
[o3]: http://nginx.org/en/docs/http/ngx_http_sub_module.html
[v9]: https://nginxconfig.io
[8k]: https://github.com/mendhak/docker-http-https-echo
[0f]: https://stackoverflow.com/questions/45358188/restrict-access-to-nginx-server-location-to-a-specific-docker-container-with-al
[7m]: https://docs.docker.com/v17.09/engine/userguide/networking/#the-default-bridge-network
[rm]: https://community.letsencrypt.org/t/no-resolver-defined-to-resolve-ocsp-int-x3-letsencrypt-org-while-requesting-certificate-status-responder-ocsp-int-x3-letsencrypt-org/21427
[dm]: https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/#proxy_bind
[v7]: https://stackoverflow.com/questions/27610979/nginx-custom-error-page-502-with-css-and-image-files
[9x]: https://blog.adriaan.io/one-nginx-error-page-to-rule-them-all.html
[ls]: https://github.com/trimstray/nginx-admins-handbook/blob/master/README.md
[h5]: https://serverfault.com/questions/404626/how-to-output-variable-in-nginx-log-for-debugging
[h6]: https://www.nginx.com/resources/wiki/start/topics/depth/ifisevil/
[h7]: https://serverfault.com/questions/687033/nginx-use-geo-module-with-allow-deny-directives

[bugdx]: https://github.com/docker/libnetwork/issues/1141#issuecomment-215522809
[bugsf]: https://dustymabe.com/2016/05/25/non-deterministic-docker-networking-and-source-based-ip-routing/
[bugfk]: https://stackoverflow.com/questions/36882945/change-default-route-in-docker-container
[buge9]: https://github.com/moby/moby/issues/21741

[refss]: proxy-control.conf
[refew]: ..