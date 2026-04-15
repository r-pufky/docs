# Troubleshooting

## Refuses to Start
Postgres will refuse to start with any [invalid configuration option][a], which
include deprecated options and version mis-matched options. Default service
does not log configuration errors on startup. This must be done manually to see
what configuration issues are occurring.

``` bash
su - postgres
/usr/lib/postgresql/17/bin/postgres -d 3 \
-D /var/lib/postgresql/17/main \
-c config_file=/etc/postgresql/17/main/postgresql.conf
```

## Collation Version Mismatch
Collation version changed on upgrade. Rebuild indexes.

!!! danger ""
    WARNING:  database "{DB}" has a collation version mismatch
    DETAIL:  The database was created using collation version 2.36, but the operating system provides version 2.41.

``` bash
# Update collation and re-index.
psql -d "{DB}"

ALTER DATABASE "{DB}" REFRESH COLLATION VERSION;
> NOTICE:  changing version from 2.36 to 2.41
> ALTER DATABASE

REINDEX DATABASE "{DB}";
> REINDEX
```

[a]: https://www.postgresql.org/docs/current/config-setting.html
