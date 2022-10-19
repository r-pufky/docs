.. _service-postgres-basic-configuration:

Basic Configuration
###################

.. _service-postgres-create-database:

Creating A Database
*******************

.. code-block:: psql
  :caption: Create new DB user and database.

  psql -U {ADMIN USER} -d postgres

  CREATE USER {DB USER} PASSWORD '{DB USER PASS}';
  CREATE DATABASE {DB USER};

  ALTER DATABASE {DB USER} OWNER TO {DB USER};
  GRANT ALL PRIVILEGES ON DATABASE {DB USER} TO {DB USER};

Import A Database
*****************
Database dumps may be imported, but explicit table permissions need to be set
for the DB user to access the data.

.. note::
  Permissions need to be set if DB is not imported as the DB user. This assumes
  the database has already been created.

.. code-block:: psql
  :caption: Import DB and set appropriate DB permissions.

  psql -v ON_ERROR_STOP=1 --username {DB ADMIN} {DB} < {DB DUMP}
  psql -U {ADMIN USER} -d postgres

  ALTER DATABASE {DB USER} OWNER TO {DB USER};
  GRANT ALL PRIVILEGES ON DATABASE {DB USER} TO {DB USER};
  \q

  for tbl in `psql -U {DB ADMIN} -qAt -c "select tablename from pg_tables where schemaname = 'public';" {DB}`; do psql -U {DB ADMIN} -c "alter table \"$tbl\" owner to {DB USER}" {DB}; done
  for tbl in `psql -U {DB ADMIN} -qAt -c "select sequence_name from information_schema.sequences where sequence_schema = 'public';" {DB}`; do psql -U {DB ADMIN} -c "alter sequence \"$tbl\" owner to {DB USER}" {DB}; done
  for tbl in `psql -U {DB ADMIN} -qAt -c "select table_name from information_schema.views where table_schema = 'public';" {DB}`; do psql -U {DB ADMIN} -c "alter view \"$tbl\" owner to {DB USER}" {DB}; done

:download:`postgres-db-setup-script.sh <source/postgres-db-setup.sh>`

`Reference <https://stackoverflow.com/questions/1348126/postgresql-modify-owner-on-all-tables-simultaneously-in-postgresql>`__

Database Backup
***************

Backup Entire Instance
======================
This will dump all databases, users and permissions. Remember to pull the data
from the instance or the data directory.

.. code-block:: bash

  pg_dumpall > {DUMP FILE}.sql

Backup A Specific Database
==========================
Backup a specific database. Permissions will need to be restored with database.

.. code-block:: bash

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
