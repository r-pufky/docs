.. _service-roundcube-basic-configuration:

Basic Configuration
###################

Postgres Backend
****************
Postgres may be used to store roundcube data in a centralized location. This
assumes that :ref:`service-postgres` is already configured, with an empty
database for roundcube to use (see :ref:`service-postgres-create-database`).

The `roundcube DB schema <https://github.com/roundcube/roundcubemail/blob/master/SQL/postgres.initial.sql>`_
is defined in the roundcube respository.

.. code-block:: psql
  :caption: Import the Roundcube DB schema.

  psql -U roundcube -f SQL/postgres.initial.sql roundcube

fail2ban Setup
**************
Enable fail2ban for :term:`MTA` and :term:`MDA` services. Use
:ref:`service-fail2ban` for the base fail2ban service setup.

Enable logging of sucessful user logins ``roundcube_log_logins``.

Roundcube Filters
*****************
Custom filter to match roundcube log messages in syslog, with roundcube
operating behind a proxy.

.. literalinclude:: source/mail-roundcube.conf
  :caption: **0644 root root** ``/data/filter.d/mail-roundcube.conf``

Roundcube Jails
***************
.. literalinclude:: source/roundcube.conf
  :caption: **0644 root root** ``/data/jail.d/roundcube.conf``

Restart fail2ban.
