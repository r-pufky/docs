# Sonarr
Sonarr Server.

!!! example "Migrated to ansible collection"
    Use [r_pufky.arr.sonarr][a].

!!! tip
    * The UID/GID should be set to a user/group that has access to your media.
      All media clients should run under the same user to run correctly.
    * Your downloader will report the download path **mapped in the downloader
      service**. You need to map this exact path in Sonarr for it to be able to
      post-process downloads properly.

## Migrate to PostgreSQL
Complete [authoritative migration instructions are here][d].

Manual Migration Overview:

1. Install [pgloader][f] on postgres server.
2. Create postgres databases

    ``` bash
    systemctl stop sonarr
    sqlite3 sonarr.db vacuum
    ```

3. Update config.xml with [postgres settings][e] (or apply role with postgres).
4. Confirm sonarr running (appears empty).
5. Migrate Database.

    ``` bash
    # Starting sonarr will initialize the Postgres DB but Sonarr appears empty.
    # This is expected until we migrate actual data.
    systemctl stop sonarr
    cp sonarr.db postgres:/tmp

    # Login to postgres and clear any pre-existing metadata.
    psql -d sonarr
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
    pgloader --with "quote identifiers" --with "data only" sonarr.db 'postgresql://qstick:qstick@localhost/sonarr-main' --with "prefetch rows = 100" --with "batch size = 1MB"

    # Restart Sonarr. Existing data should appear.
    systemctl start sonarr
    ```

## Reverse Proxy
Sonarr should be run via a Reverse Proxy, allowing you to isolate and wrap
connections in SSL. [See NGINX][b] for more details.
[See Base Proxy Control][c] for basic proxy configuration.

!!! abstract "/etc/nginx/conf.d/reverse_proxy.conf"
    0644 root:root

    ``` nginx
    # Subdomain
    server {
      listen       443 ssl http2;
      server_name  sonarr.{DOMAIN} sonarr;

      location / {
        proxy_pass http://sonarr:8989;
        include    /etc/nginx/conf.d/proxy-control.conf;
      }
    }
    ```

!!! abstract "/etc/nginx/conf.d/reverse_proxy.conf"
    0644 root:root

    ``` nginx
    # Subpath
    server {
      location /sonarr {
        proxy_pass http://sonarr:8989/sonarr;
        include    /etc/nginx/conf.d/proxy-control.conf;
      }
    }
    ```

[a]: https://galaxy.ansible.com/ui/repo/published/r_pufky/arr/docs
[b]: ../../service/nginx/README.md
[c]: ../../service/nginx/manual/setup.md#setup-base-reverse-proxy
[d]: https://wiki.servarr.com/en/sonarr/postgres-setup
[e]: https://github.com/r-pufky/ansible_sonarr/blob/main/files/postgres/config.xml
[f]: https://github.com/Roxedus/Pgloader-bin