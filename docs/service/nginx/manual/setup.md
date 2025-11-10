# Setup

!!! abstract "This will setup a basic reverse-proxy that"
    * Forces HTTP to HTTPS connections for IPv4/6 with a permanent redirect.
    * Serves traffic only over SSL (443).
    * Enables HTTP2 if the service behind the proxy supports it.
    * Ability to upgrade a connection to a websocket if a service requires it.
    * Direct requests to the proxy cannot contain data.
    * Import SSL certificate settings used in Let's Encrypt for strong
      validation of certificate usage.

[Automatic generator](https://www.digitalocean.com/community/tools/nginx) to
generate base configuration templates.

## Setup Base Reverse Proxy
/etc/nginx/conf.d/reverse_proxy.conf (1)
{ .annotate }

1. 0644 root:root

``` nginx
# Forward all HTTP IPv4/6 traffic to HTTPS.
server {
  listen                 80 default_server;
  listen                 [::]:80 default_server;
  server_name            {SERVER DNS NAME};
  return                 301 https://$server_name$request_uri;
}

# Websockets: remap http_upgrade to 'upgrade' or 'close' based on
# connection_upgrade being set.
map $http_upgrade $connection_upgrade {
  default                upgrade;
  ''                     close;
}

server {
  listen                  443 ssl http2;

  # Import SSL certificate options from letsencrypt
  ssl_certificate         /etc/nginx/ssl/live/{DOMAIN NAME}/fullchain.pem;
  ssl_certificate_key     /etc/nginx/ssl/live/{DOMAIN NAME}/privkey.pem;
  ssl_trusted_certificate /etc/nginx/ssl/live/{DOMAIN NAME}/chain.pem;
  ssl_dhparam             /etc/nginx/ssl/ssl-dhparams.pem;
  include                 /etc/nginx/ssl/options-ssl-nginx.conf;

  # Enable OCSP stapling https://en.wikipedia.org/wiki/OCSP_stapling.
  ssl_stapling            on;
  ssl_stapling_verify     on;
  resolver                127.0.0.1;

  client_max_body_size    0;
}
```

* The **SERVER DNS NAME** should be in the SSL certificate; a wildcard
  certificate will work.
* **ssl-dhparams.pem** may be generated with `openssl dhparam -out
  ssl-dhparams.pem 4096`.
* **resolver** should be set to a DNS resolver. localhost, gateway or pihole
  are all viable options. Check logs to ensure resolution works.

Reference:

* https://medium.com/@utkarsh_verma/how-to-obtain-a-wildcard-ssl-certificate-from-lets-encrypt-and-setup-nginx-to-use-wildcard-cfb050c8b33f
* https://community.letsencrypt.org/t/no-resolver-defined-to-resolve-ocsp-int-x3-letsencrypt-org-while-requesting-certificate-status-responder-ocsp-int-x3-letsencrypt-org/21427

## Setup Base Proxy Control
A proxy control template will enable complex proxy configurations to be
consistently applied to multiple proxy sites.

/etc/nginx/conf.d/proxy_control.conf (1)
{ .annotate }

1. 0644 root:root

``` nginx
client_max_body_size               10m;
client_body_buffer_size            128k;

#Timeout if the real server is dead
proxy_next_upstream                error timeout invalid_header http_500 http_502 http_503;

# Advanced Proxy Config
send_timeout                       5m;
proxy_read_timeout                 240;
proxy_send_timeout                 240;
proxy_connect_timeout              240;

# Basic Proxy Config
proxy_set_header Host              $host:$server_port;
proxy_set_header X-Real-IP         $remote_addr;
proxy_set_header X-Forwarded-For   $proxy_add_x_forwarded_for;
proxy_set_header X-Forwarded-Proto https;
proxy_redirect                     http://  $scheme://;
proxy_http_version                 1.1;
proxy_set_header Connection        '';
proxy_cache_bypass                 $cookie_session;
proxy_no_cache                     $cookie_session;
proxy_buffers                      32 4k;
```

Reload nginx configuration while running.
``` bash
nginx -s reload
```
