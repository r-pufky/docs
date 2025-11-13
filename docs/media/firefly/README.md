# Firefly III
Self-hosted financial manager.

!!! example "Migrated to ansible collection"
    Use [r_pufky.srv.firefly][a].


## Reverse Proxy
Firefly should be run via a Reverse Proxy, allowing you to isolate and wrap
connections in SSL. [See NGINX][b] for more details.
[See Base Proxy Control][c] for basic proxy configuration.

Set **firefly_trusted_proxies** to ** or specific proxy IP before enabling the
reverse-proxy. **firefly_app_url** should remain localhost as it does not
affect proxied or non-proxied connections.

!!! abstract "/etc/nginx/conf.d/reverse_proxy.conf"
    0644 root:root

    ``` nginx
    # Subdomain
    server {
      listen                               443 ssl http2;
      server_name                          firefly.{DOMAIN} firefly;

      location / {
        proxy_bind                         {PROXY IP ON FIREFLY NETWORK};
        proxy_pass                         http://firefly/;
        proxy_set_header Host              $http_host;
        proxy_set_header X-Real-IP         $remote_addr;
        proxy_set_header X-Forwarded-For   $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_buffering                    off;
      }
    }
    ```

!!! abstract "/etc/nginx/conf.d/reverse_proxy.conf"
    0644 root:root

    ``` nginx
    # Subpath
    location ^~ /firefly/ {
       deny all;
    }

    location ^~ /budget {
       alias /var/www/html/firefly-iii/public;
       try_files $uri $uri/ @budget;

       location ~* \.php(?:$|/) {
          include snippets/fastcgi-php.conf;
          fastcgi_param SCRIPT_FILENAME $request_filename;
          fastcgi_param modHeadersAvailable true; #Avoid sending the security headers twice
          fastcgi_pass unix:/run/php/php8.0-fpm.sock;
       }
    }

    location @budget {
       rewrite ^/budget/(.*)$ /budget/index.php/$1 last;
    }
    ```

[a]: https://jamielinux.com/docs/openssl-certificate-authority/create-the-intermediate-pair.html
[b]: ../../service/nginx/README.md
[c]: ../../service/nginx/manual/setup.md#setup-base-reverse-proxy
