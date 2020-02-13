#!/bin/bash
set -e
PSQL_ADMIN={{ psql_admin }}
DB={{ db }}
DB_USER={{ db_user }}
DB_DUMP_LATEST={{ db_dump_latest }}

echo "Creating $DB_USER user account ..."
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
  CREATE USER $DB_USER PASSWORD '{{ db_pass }}';
  CREATE DATABASE $DB;
EOSQL

if [ -f "$DB_DUMP_LATEST" ]; then
  echo "Importing $DB_DUMP_LATEST to $DB database ..."
  psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" $DB < "$DB_DUMP_LATEST"
fi

echo "Setting database $DB permissions ..."
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
  ALTER DATABASE $DB OWNER TO $DB_USER;
  GRANT ALL PRIVILEGES ON DATABASE $DB TO $DB_USER;
EOSQL

# https://stackoverflow.com/questions/1348126/modify-owner-on-all-tables-simultaneously-in-postgresql
for tbl in `psql -U $PSQL_ADMIN -qAt -c "select tablename from pg_tables where schemaname = 'public';" $DB` ; do
  psql -U $PSQL_ADMIN -c "alter table \"$tbl\" owner to $DB_USER" $DB;
done
for tbl in `psql -U $PSQL_ADMIN -qAt -c "select sequence_name from information_schema.sequences where sequence_schema = 'public';" $DB` ; do
  psql -U $PSQL_ADMIN -c "alter sequence \"$tbl\" owner to $DB_USER" $DB;
done
for tbl in `psql -U $PSQL_ADMIN -qAt -c "select table_name from information_schema.views where table_schema = 'public';" $DB` ; do
  psql -U $PSQL_ADMIN -c "alter view \"$tbl\" owner to $DB_USER" $DB ;
done

echo "done."
