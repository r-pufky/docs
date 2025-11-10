# Roundcube

## Setup

### Import the Roundcube DB schema.
``` psql
psql -U roundcube -f SQL/postgres.initial.sql roundcube
```

Reference:

* https://github.com/roundcube/roundcubemail/blob/master/SQL/postgres.initial.sql

### Fail2Ban
Custom filter to match roundcube log messages in syslog, with roundcube
operating behind a proxy.

**/data/filter.d/mail_roundcube.conf** (1)
{ .annotate }

1. 0644 root:root

``` ini
[INCLUDES]

before = common.conf

[Definition]

prefregex = ^\s*(\[\])?(%(__hostname)s\s*(?:roundcube(?:\[(\d*)\])?:)?\s*.*(<[\w]+>)? IMAP Error)?: <F-CONTENT>.+</F-CONTENT>$

failregex = ^(?:FAILED login|Login failed) for <F-USER>.*</F-USER> against .*X-Forwarded-For: <HOST>.*$
            ^(?:<[\w]+> )?Failed login for <F-USER>.*</F-USER> against .*X-Forwarded-For: <HOST> .*$

ignoreregex =

journalmatch = SYSLOG_IDENTIFIER=roundcube
```


**/data/filter.d/mail_roundcube.conf** (1)
{ .annotate }

1. 0644 root:root

``` ini
[mail-roundcube]
enabled  = true
port     = http,https
filter   = mail-roundcube
logpath  = /var/log/syslog
bantime  = -1
findtime = 86400
maxretry = 3
```

## Reverse Proxy
Roundcube should be run via a Reverse Proxy, allowing you to isolate and wrap
connections in SSL. [See NGINX](nginx/README.md) for more details. [See
Base Proxy Control](nginx/manual/setup.md#setup-base-reverse-proxy) for basic
proxy configuration.

Use the explicit **Common Name (FQDN)** for IMAP host URI. PHP requires
certificate validation by default now; and should match the explicit FQDN on
the certificate that the mail server uses. **roundcube_upload_max_filesize**
should match the max file size defined on the mail server
**POSTFIX_MESSAGE_SIZE_LIMIT** - accepted standard is now 25MB.


/etc/nginx/conf.d/reverse_proxy.conf (1)
{ .annotate }

1. 0644 root:root

``` nginx
# Subdomain
server {
  listen       443 ssl http2;
  server_name  roundcube.{DOMAIN} roundcube;

  location / {
    proxy_pass http://roundcube;
    include    /etc/nginx/conf.d/proxy-control.conf;
  }
}
```

/etc/nginx/conf.d/reverse_proxy.conf (1)
{ .annotate }

1. 0644 root:root

``` nginx
# Subpath
server {
  location /roundcube/ {
    proxy_pass http://roundcube;
    include    /etc/nginx/conf.d/proxy-control.conf;
  }
}
```


Reference:

* https://github.com/roundcube/roundcubemail/wiki/FAQ
