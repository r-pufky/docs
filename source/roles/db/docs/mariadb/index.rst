.. _service-mariadb:

`MariaDB`_
##########
MariaDB is an opensource relational database based on MySQL.

.. toctree::
   :hidden:
   :maxdepth: -1

   basic-configuration

.. role:: db.maria
  :galaxy:      https://galaxy.ansible.com/r_pufky/db
  :source:      https://github.com/r-pufky/ansible_db
  :service_doc: https://mariadb.org/
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
.. literalinclude:: ../../defaults/main/maria.yml
