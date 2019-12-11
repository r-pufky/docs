.. _service-firefly:

`Firefly III`_
##############
Self-hosted financial manager.

This setup will focus on creating a docker-based reverse proxy, enforcing SSL
for all connections to docker containers using Let's Encrypt.

See `Firefly Docker and Documentation`_.

.. gport:: Ports (Firefly)
  :port:     443,
             80,
             5432
  :protocol: TCP,
             TCP,
             TCP
  :type:     Public,
             Private,
             Private
  :purpose:  https connections.,
             Firefly web UI.,
             Postgres SQL.
  :no_key_title:
  :no_caption:
  :no_launch:

.. gflocation:: Important File Locations (Firefly)
  :file:    /var/www/firefly-iii/storage/export,
            /var/www/firefly-iii/storage/upload,
            /var/lib/postgresql/data
  :purpose: Exported data location.,
            Uploaded docs location.,
            Postgres DB.
  :no_key_title:
  :no_caption:
  :no_launch:

`Docker Creation`_
******************
Firefly runs a frontend webservice with a backend postgres SQL database. Local
storage should be locked down to prevent sensitive data from leaking.

.. code-block:: yaml
  :caption: Docker Compose

  firefly:
    image: jc5x/firefly-iii
    restart: unless-stopped
    environment:
      - FF_DB_HOST=firefly_iii_db
      - FF_DB_NAME=firefly
      - FF_DB_USER={DB USER}
      - FF_DB_PASSWORD={DB PASS}
      - FF_APP_KEY={32 CHAR APP KEY WITHOUT %*#$&}
      - FF_APP_ENV=local
      - FF_DB_CONNECTION=pgsql
      - TZ=America/Los_Angeles
      - APP_URL=https://firefly.{DOMAIN}
      - TRUSTED_PROXIES={PROXY IP ADDRESS}
      - APP_LOG_LEVEL=debug
    volumes:
      - /data/services/firefly/export:/var/www/firefly-iii/storage/export
      - /data/services/firefly/upload:/var/www/firefly-iii/storage/upload
      - /etc/localtime:/etc/localtime:ro

  firefly_db:
    image: postgres:10
    restart: unless-stopped
    environment:
      - POSTGRES_PASSWORD={DB PASS}
      - POSTGRES_USER={DB USER}
      - TZ=America/Los_Angeles
    volumes:
      - /data/services/firefly/db:/var/lib/postgresql/data
      - /etc/localtime:/etc/localtime:ro

* Docker container should be run in an isolated network given the sensitive
  nature of the data.
* ``TRUSTED_PROXIES`` should be set to the known proxy IP address so all other
  connections are denied by default. Setting to ``**`` will enable all
  connections (insecure).
* Additional `environment settings here`_.

Reverse Proxy Setup
*******************
Allows you to isolate your containers as well as wrap connections in SSL. See
:ref:`service-nginx` for more details. See
:ref:`service-nginx-base-proxy-control` for basic proxy configuration.

Using Subdomains
================
.. literalinclude:: source/subdomain.conf
  :caption: **0644 root root** ``nginx/conf.d/reverse-proxy.conf``

See `subdomain reference`_.

Initial Setup
*************
Start firefly and setup the initial database. This only needs to be done on
initial container creation.

.. code-block:: bash
  :caption: Initialize the DB.

  docker-compose up -d
  docker-compose exec firefly php artisan migrate --seed
  docker-compose exec firefly php artisan firefly:upgrade-database
  docker-compose exec firefly php artisan firefly:verify
  docker-compose exec firefly php artisan cache:clear

Login to Site, first user created is an **administrator**.

.. ggui:: Verify Password Security
  :option:  ☑
  :setting: Verify password security
  :no_key_title:
  :no_section:
  :no_caption:
  :no_launch:

.. note::
  `Verifying password security`_ checks that the password used is not in known
  password dumps. See linked documentation for more details.

Firefly Gotchas
***************

Attachment Disappears
=====================
There is a hard ``2MB`` limit from ``lavarel``. This will be displayed as
uploading successfully but will be `sliently dropped`_.

.. rubric:: References

#. `Firefly with NGINX reverse proxy <https://docs.firefly-iii.org/support/faq#i-am-using-nginx-and-want-to-expose-firefly-iii-under-budget>`_

.. _Firefly III: https://firefly-iii.org/
.. _Firefly Docker and Documentation: https://hub.docker.com/r/jc5x/firefly-iii
.. _Docker Creation: https://docs.firefly-iii.org/installation/docker#docker-hub-with-automatic-updates-via-docker-compose
.. _environment settings here: https://github.com/firefly-iii/firefly-iii/blob/master/.env.example
.. _subdomain reference: https://github.com/firefly-iii/firefly-iii/issues/2109
.. _Verifying password security: https://github.com/firefly-iii/help/wiki/Secure-password
.. _sliently dropped: https://github.com/firefly-iii/firefly-iii/issues/960