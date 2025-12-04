# Best Practices


## One Proxy File Per Site
Minimizes errors by keeping proxy configuration in one location. Useful when
needing the same proxy config multiple times in a site.

Create a proxy directory.
``` bash
mkdir /etc/nginx/conf.d/include/proxy
```

Add each site proxy config to **/etc/nginx/conf.d/include/proxy/{SITE}**. These
can be imported in server/location blocks as needed.

!!! abstract "/etc/nginx/conf.d/include/server/{SITE}"
    0644 root:root

    ``` nginx
    server {
      include /etc/nginx/conf.d/include/proxy/{SITE};
    }
    ```


## One Server Site Per Config File
Keep one site per configuration file to focus only on that site. This will help
reduce errors and allow fast lookup / disable of configurations.

Create a server directory.
``` bash
mkdir /etc/nginx/conf.d/include/server
```

Add each site to **/etc/nginx/conf.d/include/server/{SITE}**. Then modify
default config to auto import sites / services.

!!! abstract "/etc/nginx/conf.d/default.conf"
    0644 root:root

    ``` nginx
    include /etc/nginx/conf.d/include/server/*;
    ```

Adding a site in services and restarting NGINX will now automatically pickup
that site.

## [Password Authentication (Basic Auth)][a]
Basic auth uses a file to authenticate users for NGINX locations.

Install password utilities and generate a user/password.
``` bash
apt install apache2-utils
sudo htpasswd -c /etc/nginx/{SITE}.pass {USER}
```

!!! abstract "nginx/conf.d/reverse_proxy.conf"
    0644 root:root

    ``` nginx
    server {
      listen 443 ssl http2;
      server_name {SITE}.{DOMAIN} {SITE};

      location / {
        allow {TRUSTED NETWORK}/{TRUSTED NETWORK MASK};
        allow {TRUSTED IP};
        deny all;
        auth_basic '{SITE}';
        auth_basic_user_file /etc/nginx/{SITE}.pass;

        proxy_pass https://{SITE}/;
        include /etc/nginx/conf.d/proxy-control.conf;
      }
    }
    ```

!!! note
    This will allow specific subnets and trusted IP's to access location
    without authentication, and force all others to authenticate, prompting
    with **{SITE}**.


## [Site-wide Auth File][b]
Keep authentication definitions for different services to one file to maintain
authentication consistency across multiple sites.

Create an authentication block, and store in a file.

!!! abstract "/etc/nginx/conf.d/site_auth.conf"
    0644 root:root

    ``` nginx
    # Allow all on 10.1.1.0/24 through, and force auth for everyone else.
    satisfy              any;
    allow                10.1.1.0/24;
    deny                 all;
    auth_basic           'Your Site';
    auth_basic_user_file /etc/nginx/conf.d/your_site.pass
    ```

Include authentication block where authentication would be required.

!!! abstract "/etc/nginx/conf.d/service/my_site.conf"
    0644 root:root

    ``` nginx
    location / {
      include    /etc/nginx/conf.d/site_auth.conf;
      proxy_pass ...
    }
    ```


## Remove Auth Requirement for Proxies
NGINX may be whitelisted to allow dashboards and services to communicate with
each other using FQDNs without needing basic auth.

### [Whitelist All Containers][c]
Add IP range to the authorization file.

!!! abstract "/etc/nginx/conf.d/site_auth.conf"
    0644 root:root

    ``` nginx
    allow 172.18.0.0/16;
    ```

### [Whitelist Single Container][d]
Whitelist specific IP in the authorization file.

!!! abstract "/etc/nginx/conf.d/site_auth.conf"
    0644 root:root

    ``` nginx
    allow 172.18.0.101;
    ```


## Disable Auth for a specific location
Explicitly disable auth and allow all to remove any auth enforcement for a
specific location. This is for proxied sites that do their own authentication
(e.g. git) or for specific locations which shouldn't be auth'ed.

Explicitly set **no** authentication and **allow all** to prevent any
configuration carried over from the default site.

!!! abstract "/etc/nginx/conf.d/service/my_site.conf"
    0644 root:root

    ``` nginx
    location / {
      auth_basic off;
      allow      all;
      proxy_pass ...
    }
    ```


## [Classify Networks to Variables][e]
Determine remote address subnet / IP and set variable specifically for match.
Enables use of logic within NGINX to make decisions based on remote IP address.

``` nginx
geo $client {
  default        default;
  172.1.1.1      nginx-proxy-host;
  172.10.0.0/16  subnet-one;
  172.11.0.0/16  subnet-two;
}
```

* **$client** will store a value based on the most specific match and can be
  checked in other sections.
* There is essentially no cost for a large list of matches; only evaluated when
  used.

``` nginx
server {
  location / {
    if ($client = subnet-one) {
      return 403;
      break;
    }
  }
}
```


## [Rate Limiting][f]
Restrict the amount of requests a user can simultaneously issue to the NGINX
proxy and determine how to throttle or drop requests over that limit. Read
in-depth documentation reference to fully understand rate limiting.

``` nginx
limit_req_zone $binary_remote_addr zone=binip:10m rate=10r/s;
```

* Place this in the **http** context block, outside of **server** blocks.
* **10 MB** of memory is reserved in the zone **binip** to match the binary ip
  address requests. This is shared across all threads.
* The rate limit specified is **10 requests / second**. (1 request every 100
  milliseconds). No bursting is defined here so requests between 100 millisecond
  increments will be dropped.

``` nginx
location / {
    limit_req zone=binip burst=20 nodelay;
}
```

* Enable bursting of up to 20 requests a second and immediate queue those
  requests without delay. This will handle requests between 100 millisecond
  increments, however, the 21st request will be delayed until the queue has
  space.
* **delay=10** will enable bursting of up to 10 requests a second, then delay
  any request amount over 10 until the queue is cleared. Excessive queries will
  be dropped.

[a]: https://docs.nginx.com/nginx/admin-guide/security-controls/configuring-http-basic-authentication/#pass
[b]: https://docs.nginx.com/nginx/admin-guide/installing-nginx/installing-nginx-open-source
[c]: https://docs.docker.com/network/bridge/#differences-between-user-defined-bridges-and-the-default-bridge
[d]: https://stackoverflow.com/questions/45358188/restrict-access-to-nginx-server-location-to-a-specific-docker-container-with-al
[e]: http://nginx.org/en/docs/http/ngx_http_geo_module.html
[f]: https://www.nginx.com/blog/rate-limiting-nginx
