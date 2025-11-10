# Troubleshooting

## Debug NGINX configs
There is no existing logging functionality in NGINX to write directly to logs
from configuration files. Work around by directly injecting debugging headers
in configuration files to dump information to logs. NGINX variables may be used
as well.

``` nginx
add_header X-debug-message "some message to write $ssl_client_s_dn" always;
```

Headers are found in the page response.

![Headers](debug_headers.png)

`Reference <https://serverfault.com/questions/404626/how-to-output-variable-in-nginx-log-for-debugging>`__

## If is Evil
!!! danger "Within a location block the only **safe** operations are"
    If operates as a rewrite and is **inherently misunderstood**.

    * **return**.
    * **rewrite**.

!!! warning "**All** if operations must be explicitly tested for appropriate behavior."

Reference:

* https://www.nginx.com/resources/wiki/start/topics/depth/ifisevil/
* https://agentzh.blogspot.com/2011/03/how-nginx-location-if-works.html
* https://serverfault.com/questions/687033/nginx-use-geo-module-with-allow-deny-directives

## Dump Loaded NGINX Configuration
Dump the currently loaded configuration in config file formatting. Useful to
inspect current nginx state.

``` bash
nginx -T
```

Reference:

* https://stackoverflow.com/questions/12832033/dump-conf-from-running-nginx-process

## NGINX Queries Originate from Wrong Gateway
NGINX express this bug by forwarding/proxying any traffic **over** the default
gateway for the first lexical named network that appears. This results in
non-deterministic source IP routing.

Set an appropriate default gateway in the networking config.

Reference:

* https://github.com/moby/moby/issues/21741
* https://github.com/docker/libnetwork/issues/1141#issuecomment-215522809

## Forward Traffic via Specific Interfaces
NGINX can forward traffic via specific interfaces for *location* definitions.

Use IPv4 address in **proxy_bind** command for specific locations.

``` nginx
location / {
  proxy_bind {NGINX NETWORK IP};
  proxy_pass ...
}
```

Reference:

* https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/#proxy_bind
