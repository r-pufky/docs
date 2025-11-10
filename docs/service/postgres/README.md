# PostgresQL
Postgres is an opensource object-relational database.

!!! example "Migrated to ansible collection"
    Use [r_pufky.srv.postgres](https://galaxy.ansible.com/ui/repo/published/r_pufky/srv/docs/).

## Creating a Database

Create new DB user and database.
``` sql
psql -U {ADMIN USER} -d postgres

CREATE USER {DB USER} PASSWORD '{DB USER PASS}';
CREATE DATABASE {DB USER};

ALTER DATABASE {DB USER} OWNER TO {DB USER};
GRANT ALL PRIVILEGES ON DATABASE {DB USER} TO {DB USER};
```

## Import a Database
Database dumps may be imported, but explicit table permissions need to be set
for the DB user to access the data.

!!! note
    Permissions need to be set if DB is not imported as the DB user. This
    assumes the database has already been created.

Import DB and set appropriate DB permissions ([download](postgres_db_setup.sh)).
``` sql
psql -v ON_ERROR_STOP=1 --username {DB ADMIN} {DB} < {DB DUMP}
psql -U {ADMIN USER} -d postgres

ALTER DATABASE {DB USER} OWNER TO {DB USER};
GRANT ALL PRIVILEGES ON DATABASE {DB USER} TO {DB USER};
\q

for tbl in `psql -U {DB ADMIN} -qAt -c "select tablename from pg_tables where schemaname = 'public';" {DB}`; do psql -U {DB ADMIN} -c "alter table \"$tbl\" owner to {DB USER}" {DB}; done
for tbl in `psql -U {DB ADMIN} -qAt -c "select sequence_name from information_schema.sequences where sequence_schema = 'public';" {DB}`; do psql -U {DB ADMIN} -c "alter sequence \"$tbl\" owner to {DB USER}" {DB}; done
for tbl in `psql -U {DB ADMIN} -qAt -c "select table_name from information_schema.views where table_schema = 'public';" {DB}`; do psql -U {DB ADMIN} -c "alter view \"$tbl\" owner to {DB USER}" {DB}; done
```

Reference:

* https://stackoverflow.com/questions/1348126/postgresql-modify-owner-on-all-tables-simultaneously-in-postgresql

## Database Backup

This will dump all databases, users and permissions. Remember to pull the data
from the instance or the data directory.
``` bash
pg_dumpall > {DUMP FILE}.sql
```

Backup a specific database. Permissions will need to be restored with database.
``` bash
pg_dump -U {DB ADMIN} --no-owner {DB} > {DUMP FILE}.sql
```

## Query Active Connections
Display client sessions that are currently connected to database.

``` sql
select pid as process_id,
     usename as username,
     datname as database_name,
     client_addr as client_address,
     application_name,
     backend_start,
     state,
     state_change
from pg_stat_activity;
```
