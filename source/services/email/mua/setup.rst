.. _service-email-mua-setup:

MUA
###
Setup roundcube email :term:`MUA` for webmail.

Setup :term:`MTA` and :term:`MDA` before configuration. See
:ref:`service-email-mta-setup`.

Ports
*****
.. ports:: MUA Ports
  :value0: 80, {TCP}, {DISABLE}, Roundcube webface
  :open:

.. gflocation:: Important File Locations (MUA)
  :file:    /var/www/html/config,
            /var/roundcube/db
  :purpose: Roundcube configuration files.,
            Roundcube user data; includes per-user contact information.
  :no_key_title:
  :no_caption:
  :no_launch:

Docker Creation
***************
Configure the mail server before starting the docker container. See
:ref:`service-email-mta-setup`.

* Docker container should be run in an isolated network given the sensitive and
  exposed nature of the data and service.
* Proxy will forward traffic to the container, so no ports need to be exposed.

.. code-block:: yaml
  :caption: Docker Compose

  roundcube:
    image: roundcube/roundcubemail:latest-apache
    restart: "unless-stopped"
    logging:
      driver: syslog
      options:
        tag: roundcube
    environment:
      - "ROUNDCUBEMAIL_DEFAULT_HOST=ssl://mail.{DOMAIN}"
      - "ROUNDCUBEMAIL_DEFAULT_PORT=993"
      - "ROUNDCUBEMAIL_SMTP_SERVER=tls://mail.{DOMAIN}"
      - "ROUNDCUBEMAIL_SMTP_PORT=587"
      - "ROUNDCUBEMAIL_PLUGINS=archive,zipdownload"
      - "ROUNDCUBEMAIL_SKIN=larry"
      - "ROUNDCUBEMAIL_UPLOAD_MAX_FILE_SIZE=10M"
      - "ROUNDCUBEMAIL_DB_TYPE=sqlite"
    volumes:
      - "/data/mail/roundcube/config:/var/www/html/config"
      - "/data/mail/roundcube/db:/var/roundcube/db"

.. warning::
  Use the explicit **Common Name (FQDN)** for ``host`` URI. PHP requires
  `certificate validation`_ by default now; and should match the explicit FQDN
  on the certificate that the mail server uses.

.. note::
  ``ROUNDCUBEMAIL_UPLOAD_MAX_FILE_SIZE`` should match the max file size defined
  on the mail server ``POSTFIX_MESSAGE_SIZE_LIMIT``. See
  :ref:`service-email-mta-docker`.

.. note::
  See `roundcube configuration`_ for configuration guide. See
  `defaults.inc.php`_ for defaults.

Reverse Proxy Setup
*******************
Allows you to isolate your containers as well as wrap connections in SSL. See
:ref:`service-nginx` for more details. See
:ref:`service-nginx-base-proxy-control` for basic proxy configuration.

Using Subdomains
================
.. literalinclude:: source/subdomain.conf
  :caption: **0644 root root** ``nginx/conf.d/reverse-proxy.conf``

Using Subpaths
==============
.. literalinclude:: source/subpath.conf
  :caption: **0644 root root** ``nginx/conf.d/reverse-proxy.conf``

Postgres Backend
****************
Postgres may be used to store roundcube data in a centralized location. This
assumes that :ref:`service-postgres` is already configured, with an empty
database for roundcube to use (see :ref:`service-postgres-create-database`).

.. code-block:: psql
  :caption: Import the Roundcube DB schema.

  psql -U roundcube -f SQL/postgres.initial.sql roundcube

.. note::
  The `roundcube DB schema`_ is defined in the roundcube respository.

.. code-block:: yaml
  :caption: Docker Compose Add Postgres Network.

  networks:
    db:
      external: True
  roundcube:
    image: roundcube/roundcubemail:latest-apache
    networks:
      - db

.. code-block:: php
  :caption: **0600 roundcube roundcube** ``/var/www/html/config/config.inc.php``

  $config[‘db_dsnw’] = ‘pgsql://{USER}:{PASS}@{HOST}/{DB}';

fail2ban Setup
**************
Enable fail2ban for :term:`MTA` and :term:`MDA` services.

Use :ref:`service-fail2ban-docker` for the base fail2ban service setup.

.. code-block:: yaml
  :caption: Add read-only syslog logs to Docker Compose (f2b-docker)

  f2b-system:
    volumes:
      - /var/log/syslog:/var/log/syslog:ro

Enable logging of sucessful user logins.

.. code-block:: php
  :caption: **0644 root root** ``/data/mail/roundcube/config/config.inc.php``

  <?php
    $config['log_logins'] = true

Roundcube Filters
=================
Custom filter to match roundcube log messages in syslog, with roundcube
operating behind a proxy.

.. literalinclude:: source/mail-roundcube.conf
  :caption: **0644 root root** ``/data/filter.d/mail-roundcube.conf``

Roundcube Jails
===============
.. literalinclude:: source/roundcube.conf
  :caption: **0644 root root** ``/data/jail.d/roundcube.conf``

* Restart ``f2b-docker``.

.. _certificate validation: https://github.com/roundcube/roundcubemail/wiki/FAQ
.. _roundcube configuration: https://github.com/roundcube/roundcubemail/wiki/Configuration
.. _defaults.inc.php: https://github.com/roundcube/roundcubemail/blob/master/config/defaults.inc.php
.. _roundcube DB schema: https://github.com/roundcube/roundcubemail/blob/master/SQL/postgres.initial.sql
