[firefly III][f8]
=================
Self-hosted financial manager.

This setup will focus on creating a docker-based reverse proxy, enforcing SSL
for all connections to docker containers using Let's Encrypt.

1. [Ports](#ports)
1. [Important File Locations](#important-file-locations)
1. [Docker Creation](#docker-creation)
1. [Adding Reverse Proxies](#adding-reverse-proxies)
1. [Initial Setup](#initial-setup)

Ports
-----
Docker reverse-proxy.

| Docker Port | Protocol | Exposed/Public | Purpose            |
|-------------|----------|----------------|--------------------|
| 443         | TCP      | Public         | https connections. |
| 80          | TCP      | Private        | Firefly web UI.    |
| 5432        | TCP      | Private        | Postgres SQL.      |

Important File Locations
------------------------
Relative to docker container.

| File                                | Purpose                 |
|-------------------------------------|-------------------------|
| /var/www/firefly-iii/storage/export | Exported data location. |
| /var/www/firefly-iii/storage/upload | Uploaded docs location. |
| /var/lib/postgresql/data            | Postgres DB.            |

[Docker Creation][3m]
---------------------
Firefly runs a frontend webservice with a backend postgres SQL database.

* Local storage should be locked down to prevent sensitive data from leaking.

Docker Compose:
```yaml
firefly:
  environment:
    - FF_DB_HOST=firefly_iii_db
    - FF_DB_NAME=firefly
    - FF_DB_USER={DB_USER}
    - FF_DB_PASSWORD={DB_PASS}
    - FF_APP_KEY={32_CHAR_APP_KEY_WITHOUT_%*#$&}
    - FF_APP_ENV=local
    - FF_DB_CONNECTION=pgsql
    - TZ=America/Los_Angeles
    - APP_URL=https://firefly.{DOMAIN}
    - TRUSTED_PROXIES=172.41.1.1
    - APP_LOG_LEVEL=debug
  image: jc5x/firefly-iii
  volumes:
    - /data/services/firefly/export:/var/www/firefly-iii/storage/export
    - /data/services/firefly/upload:/var/www/firefly-iii/storage/upload
    - /etc/localtime:/etc/localtime:ro
firefly_db:
  environment:
    - POSTGRES_PASSWORD={DB_PASS}
    - POSTGRES_USER={DB_USER}
    - TZ=America/Los_Angeles
  image: "postgres:10"
  volumes:
    - /data/services/firefly/db:/var/lib/postgresql/data
    - /etc/localtime:/etc/localtime:ro
```
* Docker container should be run in an isolated network given the sensitive
  nature of the data.
* `TRUSTED_PROXIES` should be set to the known proxy IP address so all other
  connections are denied by default. Setting to `**` will enable all
  connections.
* Additional [environment settings here][3k].

Reverse Proxy Setup
-------------------
Allows you to isolate your containers as well as wrap connections in SSL. See
[nginx][refci] for more details. Firefly is intended to be used from a
subdomain.

### Using Subdomains
[nginx/conf.d/reverse-proxy.conf][El] `root:root 0644`
```nginx
server {
  listen 443 ssl http2;
  server_name firefly.{DOMAIN} firefly;

  location / {
    proxy_bind {PROXY_IP_ON_FIREFLY_NET};
    proxy_pass http://firefly/;
    proxy_set_header Host $http_host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_buffering off;
  }
}

```

Initial Setup
-------------
Start firefly and setup the initial database. This only needs to be done on
initial container creation.

```bash
docker-compose up -d
docker-compose exec firefly php artisan migrate --seed
docker-compose exec firefly php artisan firefly:upgrade-database
docker-compose exec firefly php artisan firefly:verify
docker-compose exec firefly php artisan cache:clear
```

[docker-service-template.md|c9067f2][XX]

[f8]: https://firefly-iii.org/
[3m]: https://docs.firefly-iii.org/en/latest/installation/docker.html#docker-hub-with-automatic-updates-via-docker-compose
[di]: https://firefly-iii.readthedocs.io/en/latest/support/faq.html#i-am-using-nginx-and-want-to-expose-firefly-iii-under-budget
[3k]: https://github.com/firefly-iii/firefly-iii/blob/master/.deploy/docker/.env.docker
[El]: https://github.com/firefly-iii/firefly-iii/issues/2109
[XX]: https://github.com/r-pufky/docs/blob/c9067f2bc3d0aeb0f2915e63f8cd9515c00640a2/services/docker-service-template.md

[ref0p]: ../nginx/proxy-control.conf
[refci]: ../nginx/README.md