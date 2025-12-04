# Troubleshooting


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
