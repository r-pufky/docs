.. _service-postgres:

`Postgresql`_
#############
Postgres is an opensource object-relational database.

See `Postgres Docker and Documentation`_.

.. gport:: Ports (postgres)
  :port:     5432
  :protocol: TCP
  :type:     Exposed
  :purpose:  postgres DB port.
  :no_key_title:
  :no_caption:
  :no_launch:

.. gflocation:: Important File Locations (postgres)
  :file:    /docker-entrypoint-initdb.d,
            /var/lib/postgresql/data,
            /var/lib/postgresql/data/postgres.conf
  :purpose: DB initalization scripts if DB is empty.,
            DB file storage location.,
            DB configuration file.
  :no_key_title:
  :no_caption:
  :no_launch:

Docker Creation
***************

.. code-block:: yaml
  :caption: Docker Compose

  postgres:
    image: postgres:12-alpine
    restart: "always"
    networks:
      db:
        ipv4_address: {IP}
    environment:
      - POSTGRES_PASSWORD={ADMIN PASS}
      - POSTGRES_USER={ADMIN USER}
      - POSTGRES_DB=postgres
      - TZ=America/Los_Angeles
    volumes:
      - /data/services/postgres/initdb.d:/docker-entrypoint-initdb.d:ro
      - /data/services/postgres/data:/var/lib/postgresql/data
      - /etc/localtime:/etc/localtime:ro

* Container should **not** be mapped via proxy. Don't expose container.
* ``postgres`` used as the default DB since this DB is automatically created and
  offers no additional security with a name change if the container is
  compromised.
* Postgres runs internally as the ``postgres`` user, UID/GID of ``70``. Create
  a system account with this UID/GID and ``chown`` postgres files with it.

.. _service-postgres-create-database:

Creating A Database
*******************
Create a new database for each service that will use this DB backend. This
includes user accounts for the specific database.

.. code-block:: psql
  :caption: Create DB user and database.

  docker -exec -ti db /bin/bash
  psql -U {ADMIN USER} -d postgres

  CREATE USER {DB USER} PASSWORD '{DB USER PASS}';
  CREATE DATABASE {DB USER};

  ALTER DATABASE {DB USER} OWNER TO {DB USER};
  GRANT ALL PRIVILEGES ON DATABASE {DB USER} TO {DB USER};

Import A Database
*****************
Database dumps may be imported, but `explicit table permissions`_ need to be set
for the DB user to access the data.

.. note::
  Permissions need to be set if DB is not imported as the DB user. This assumes
  the database has already been created.

.. code-block:: psql
  :caption: Import DB and set appropriate DB permissions.

  docker -exec -ti db /bin/bash
  psql -v ON_ERROR_STOP=1 --username {DB ADMIN} {DB} < {DB DUMP}
  psql -U {ADMIN USER} -d postgres

  ALTER DATABASE {DB USER} OWNER TO {DB USER};
  GRANT ALL PRIVILEGES ON DATABASE {DB USER} TO {DB USER};
  \q

  for tbl in `psql -U {DB ADMIN} -qAt -c "select tablename from pg_tables where schemaname = 'public';" {DB}`; do psql -U {DB ADMIN} -c "alter table \"$tbl\" owner to {DB USER}" {DB}; done
  for tbl in `psql -U {DB ADMIN} -qAt -c "select sequence_name from information_schema.sequences where sequence_schema = 'public';" {DB}`; do psql -U {DB ADMIN} -c "alter sequence \"$tbl\" owner to {DB USER}" {DB}; done
  for tbl in `psql -U {DB ADMIN} -qAt -c "select table_name from information_schema.views where table_schema = 'public';" {DB}`; do psql -U {DB ADMIN} -c "alter view \"$tbl\" owner to {DB USER}" {DB}; done

``initdb.d`` Scripts
********************
These scripts will be run if the Postgres DB does not exist on first startup.
Useful for creating initial DB's for services automatically. An example script
is below, which creates user accounts, imports a database dump if it exists, and
ensures permissions are set properly.

.. literalinclude:: source/postgres-db-setup.sh
  :caption: **0500 postgres postgres** ``/docker-entrypoint-initdb.d/example.sh``

Database Backup
***************
Backup Entire Instance
======================
This will dump all databases, users and permissions. Remember to pull the data
from the instance or the data directory.

.. code-block:: bash
  :caption: Dump Entire Instance.

  docker -exec -ti db /bin/bash
  pg_dumpall > {DUMP FILE}.sql

Backup A Specific Database
==========================
Backup a specific database. Permissions will need to be restored with database.

.. code-block:: bash
  :caption: Dump specific DB.

  docker -exec -ti db /bin/bash
  pg_dump -U {DB ADMIN} --no-owner {DB} > {DUMP FILE}.sql

Query Active Connections
************************
Display client sessions that are currently connected to database.

.. code-block:: sql

  select pid as process_id,
       usename as username,
       datname as database_name,
       client_addr as client_address,
       application_name,
       backend_start,
       state,
       state_change
  from pg_stat_activity;

.. _Postgres: https://www.postgresql.org/
.. _Postgres Docker and Documentation: https://hub.docker.com/_/postgres
.. _incorrectly defines two postgres datatypes: https://github.com/postgres/postgres/issues/1213
.. _explicit table permissions: https://stackoverflow.com/questions/1348126/postgresql-modify-owner-on-all-tables-simultaneously-in-postgresql
