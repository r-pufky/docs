# Troubleshooting


## [Debug NGINX configs][a]
There is no existing logging functionality in NGINX to write directly to logs
from configuration files. Work around by directly injecting debugging headers
in configuration files to dump information to logs. NGINX variables may be used
as well.

``` nginx
add_header X-debug-message "some message to write $ssl_client_s_dn" always;
```

Headers are found in the page response.

![Headers](debug_headers.png)


## [If is Evil][b]
!!! danger "Within a location block the only **safe** operations are"
    If operates as a rewrite and is [**inherently misunderstood**][c].

    * **return**.
    * **rewrite**.

!!! warning "**All** if operations must be [explicitly tested][d] for appropriate behavior."


## [Dump Loaded NGINX Configuration][e]
Dump the currently loaded configuration in config file formatting. Useful to
inspect current nginx state.

``` bash
nginx -T
```


## [NGINX Queries Originate from Wrong Gateway][f]
NGINX express this bug by forwarding/proxying any traffic **over** the default
gateway for the first lexical named network that appears. This results in
non-deterministic source IP routing.

Set an appropriate default gateway in the networking config.


## [Forward Traffic via Specific Interfaces][g]
NGINX can forward traffic via specific interfaces for *location* definitions.

Use IPv4 address in **proxy_bind** command for specific locations.

``` nginx
location / {
  proxy_bind {NGINX NETWORK IP};
  proxy_pass ...
}
```

[a]: https://serverfault.com/questions/404626/how-to-output-variable-in-nginx-log-for-debugging
[b]: https://www.nginx.com/resources/wiki/start/topics/depth/ifisevil
[c]: https://agentzh.blogspot.com/2011/03/how-nginx-location-if-works.html
[d]: https://serverfault.com/questions/687033/nginx-use-geo-module-with-allow-deny-directives
[e]: https://stackoverflow.com/questions/12832033/dump-conf-from-running-nginx-process
[f]: https://github.com/moby/moby/issues/21741
[g]: https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/#proxy_bind