# Lidarr
Lidarr Server.

!!! example "Migrated to ansible collection"
    Use [r_pufky.arr.lidarr][a].

!!! tip
    * The UID/GID should be set to a user/group that has access to your media.
      All media clients should run under the same user to run correctly.
    * Your downloader will report the download path **mapped in the downloader
      service**. You need to map this exact path in Radarr for it to be able to
      post-process downloads properly.


## Migrate to PostgreSQL
Complete [authoritative migration instructions are here][d].

Manual Migration Overview:

1. Install [pgloader][f] on postgres server.
2. Create postgres databases

    ``` bash
    systemctl stop lidarr
    sqlite3 lidarr.db vacuum
    ```

3. Update config.xml with [postgres settings][e] (or apply role with postgres).
4. Confirm lidarr running (appears empty).
5. Migrate Database.

    ``` bash
    # Starting lidarr will initialize the Postgres DB but Lidarr appears empty.
    # This is expected until we migrate actual data.
    systemctl stop lidarr
    cp lidarr.db postgres:/tmp

    # Login to postgres and clear any pre-existing metadata.
    psql -d lidarr
    DELETE FROM "QualityProfiles";
    DELETE FROM "QualityDefinitions";
    DELETE FROM "DelayProfiles";
    DELETE FROM "Metadata";
    DELETE FROM "Config";
    DELETE FROM "VersionInfo";
    DELETE FROM "ScheduledTasks";
    \q

    # Load the SQLite DB into Postgres.
    # Many WARNINGS may appear; these can be ignored.
    pgloader --with "quote identifiers" --with "data only" lidarr.db 'postgresql://qstick:qstick@localhost/lidarr-main' --with "prefetch rows = 100" --with "batch size = 1MB"

    # Restart Sonarr. Existing data should appear.
    systemctl start lidarr
    ```


## Reverse Proxy
Lidarr should be run via a Reverse Proxy, allowing you to isolate and wrap
connections in SSL. [See NGINX][b] for more details.
[See Base Proxy Control][c] for basic proxy configuration.

!!! abstract "/etc/nginx/conf.d/reverse_proxy.conf"
    0644 root:root

    ``` nginx
    # Subdomain
    server {
      listen       443 ssl http2;
      server_name  lidarr.{DOMAIN} lidarr;

      location / {
        proxy_pass http://lidarr:8686;
        include    /etc/nginx/conf.d/proxy_control.conf;
      }
    }
    ```

!!! abstract "/etc/nginx/conf.d/reverse_proxy.conf"
    0644 root:root

    ``` nginx
    # Subpath
    server {
      location /lidarr {
        proxy_pass http://lidarr:8686/lidarr;
        include    /etc/nginx/conf.d/proxy_control.conf;
      }
    }
    ```

[a]: https://galaxy.ansible.com/ui/repo/published/r_pufky/arr/docs
[b]: ../service/nginx/README.md
[c]: ../service/nginx/manual/setup.md#setup-base-reverse-proxy
[d]: https://wiki.servarr.com/en/lidarr/postgres-setup
[e]: https://github.com/r-pufky/ansible_lidarr/blob/main/files/postgres/config.xml
[f]: https://github.com/Roxedus/Pgloader-bin