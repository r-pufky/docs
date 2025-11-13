# MariaDB
MariaDB is an opensource relational database based on MySQL.

!!! example "Migrated to ansible collection"
    Use [r_pufky.srv.maria][a].


## Creating a Database

Create new DB user and database.
``` sql
mysql -u root -p

CREATE USER IF NOT EXISTS '{USER}'@'{DOMAIN}' IDENTIFIED BY '{PASS}';
CREATE DATABASE IF NOT EXISTS {DB};

GRANT ALL PRIVILEGES ON {DB}.* TO '{USER}'@'{DOMAIN}';
FLUSH PRIVILEGES;
```


## Import a Database

Import DB and set appropriate DB permissions.
``` sql
mysql -u {USER} -p {DATABASE} < database-dump.sql

ALTER DATABASE {DB USER} OWNER TO {DB USER};
GRANT ALL PRIVILEGES ON DATABASE {DB USER} TO {DB USER};
```


## Database Backup

This will dump all databases, users and permissions. Remember to pull the data
from the instance or the data directory.
``` bash
mysqldump --user=root --password --lock-tables --all-databases > {DATABASES}.sql
```

Backup a specific database. Permissions will need to be restored with database.
``` bash
mysql -u root -p {DATABASE} > {DATABASE}.sql
```

[a]: https://galaxy.ansible.com/ui/repo/published/r_pufky/srv/docs