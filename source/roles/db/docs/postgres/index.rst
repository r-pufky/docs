.. _service-postgres:

Postgresql
##########
Postgres is an opensource object-relational database.

.. toctree::
   :hidden:
   :maxdepth: -1

   basic-configuration

.. role:: db.postgres
  :galaxy:      https://galaxy.ansible.com/r_pufky/db
  :source:      https://github.com/r-pufky/ansible_db
  :service_doc: https://www.postgresql.org/
  :blocking:    Requires upstream source repo update.
  :update:      2022-10-09
  :open:

  Manage MariaDB.

  * Role handles all steps that are provided in this documentation.

  ..  collapse:: README.md

    .. literalinclude:: ../../README.md

Ports
*****
.. literalinclude:: ../../defaults/main/ports.yml

Defaults
********
.. literalinclude:: ../../defaults/main/postgres.yml
