# MariaDB
MariaDB is an opensource relational database based on MySQL.

!!! example "Migrated to ansible collection"
    Use [r_pufky.srv.maria][a].


## [Encrypted Databases][b]
MariaDB 11+ now support encrypted databases.

### Generate Encryption Keys

``` bash
cd /etc/mysql/secure.conf.d

# Create random entropy source.
echo -n "1;`openssl rand -hex 32`" > keyfile

# Generate random password file.
openssl rand -hex 128 > keyfile.key

# Pack key and password into PFX certificate.
openssl enc -aes-256-cbc -md sha1 -pass file:keyfile.key -in keyfile -out keyfile.enc

# Restrict access.
chmod 0640 keyfile*
```

### Configure mariadb
!!! abstract "/etc/mysql/cond.d/50-server.cnf"
    0644 root:root

    ``` ini
    [mariadbd]
    basedir=/usr
    bind_address=127.0.0.1
    expire_logs_days=10
    file_key_management_encryption_algorithm=AES_CTR
    file_key_management_filekey=FILE:/etc/mysql/secure.conf.d/keyfile.key
    file_key_management_filename=/etc/mysql/secure.conf.d/keyfile.enc
    pid_file=/run/mysqld/mysqld.pid
    ```

!!! abstract "/etc/mysql/mariadb.cnf"
    0644 root:root

    ``` ini
    [client-server]
    socket=/run/mysqld/mysqld.sock
    !includedir /etc/mysql/conf.d/
    !includedir /etc/mysql/mariadb.conf.d/
    !includedir /etc/mysql/secure.conf.d/

    [mariadb]
    plugin_load_add = file_key_management
    aria-encrypt-tables
    encrypt-binlog
    encrypt-tmp-disk-tables
    encrypt-tmp-files
    loose-innodb-encrypt-log
    loose-innodb-encrypt-tables
    ```


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
[b]: https://mariadb.com/kb/en/file-key-management-encryption-plugin
