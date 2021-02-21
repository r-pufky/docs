.. _service-mariadb:

`MariaDB`_
##########
MariaDB is an opensource relational database.

See `MariaDB Docker and Documentation`_.

Ports
*****
.. ports:: MariaDB Ports
  :value0: 3306, {TCP}, {EXPOSED}, MariaDB DB port
  :open:

Files
*****
.. files:: MariaDB Files
  :value0: /config, DB configuration files and databases
  :value1: /config/initdb.d, DB initalization scripts if DB is empty
  :open:

Docker Creation
***************

.. code-block:: yaml
  :caption: Docker Compose

  mariadb:
    image: linuxserver/mariadb
    restart: "always"
    networks:
      db:
        ipv4_address: {IP}
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=America/Los_Angeles
    volumes:
      - /data/services/mariadb/data:/config
      - /data/services/mariadb/initdb.d:/config/initdb.d
      - /etc/localtime:/etc/localtime:ro

* Container should **not** be mapped via proxy. Don't expose container.
* ``initdb.d`` will execute all ``.sql`` scripts if there is no pre-existing
  database.
* Container **requires** `initdb.d scripts to be run without setting a root
  password`_.
* Setting a **root** password during ``initdb.d`` setup will cause setup failure
  Set root password after the initial DB creation happens.

.. _service-mariadb-create-database:

Creating A Database
*******************
Create a new database for each service that will use this DB backend. This
includes user accounts for the specific database.

.. code-block:: mysql
  :caption: Create DB user and database.

  docker -exec -ti mariadb /bin/bash
  mysql -u root -p

  CREATE USER IF NOT EXISTS '{USER}'@'{DOMAIN}' IDENTIFIED BY '{PASS}';
  CREATE DATABASE IF NOT EXISTS {DB};

  GRANT ALL PRIVILEGES ON {DB}.* TO '{USER}'@'{DOMAIN}';
  FLUSH PRIVILEGES;

Import A Database
*****************
Database dumps may be imported when the container is first initialized via
``initdb.d``.

.. code-block:: mysql
  :caption: Import DB and set appropriate DB permissions.

  docker -exec -ti mariadb /bin/bash
  mysql -u {USER} -p {DATABASE} < database-dump.sql
  ALTER DATABASE {DB USER} OWNER TO {DB USER};
  GRANT ALL PRIVILEGES ON DATABASE {DB USER} TO {DB USER};

``initdb.d`` Scripts
********************
These scripts will be run if the MariaDB DB does not exist on first startup.
Useful for creating initial DB's for services automatically. An example script
is below, which creates user accounts, imports a database dump if it exists, and
ensures permissions are set properly.

.. literalinclude:: source/maria-db-setup.sql
  :caption: **0500 root root** ``/config/initdb.d/example.sql``

Database Backup
***************
Backup Entire Instance
======================
This will dump all databases, users and permissions. Remember to pull the data
from the instance or the data directory.

.. code-block:: bash
  :caption: Dump Entire Instance.

  docker -exec -ti mariadb /bin/bash
  mysqldump --user=root --password --lock-tables --all-databases > {DATABASES}.sql

Backup A Specific Database
==========================
Backup a specific database. Permissions will need to be restored with database.

.. code-block:: bash
  :caption: Dump specific DB.

  docker -exec -ti mariadb /bin/bash
  mysql -u root -p {DATABASE} > {DATABASE}.sql

.. _initdb.d scripts to be run without setting a root password: https://github.com/linuxserver/docker-mariadb/issues/44
.. _MariaDB: https://mariadb.org/
.. _MariaDB Docker and Documentation: https://hub.docker.com/r/linuxserver/mariadb
