.. _service-airsonic:

`Airsonic`_
###########
Music streaming.

See `Airsonic Docker and Documentation`_.

Ports
*****
.. ports:: Ports (Airsonic)
  :value0: 4040, {TCP}, {EXPOSED}, Airsonic webservice
  :open:

Files
*****
.. files:: Airsonic Files
  :value0: /config, Airsonic configuration directory
  :value1: /config/airsonic.properties, Global airsonic configuration
  :value2: /playlists, Playlists data
  :value3: /podcasts, Podcasts data
  :value4: /music, Music data
  :value5: /media, Additional media data (videos; etc)
  :open:

Docker Creation
***************
You can copy your existing configuration to docker ``/config`` directory
adjusting for paths.

.. code-block:: yaml
  :caption: Docker Compose

  airsonic:
    image: linuxserver/airsonic
    restart: unless-stopped
    environment:
      - PUID=1000
      - PGID=1000
      - JAVA_OPTS=-Xmx256m -Xms256m
      - TZ=America/Los_Angeles
    volumes:
      - /data/services/airsonic/config:/config
      - /data/services/airsonic/playlists:/playlists
      - /data/media/podcasts:/podcasts:ro
      - /data/media/music:/music:ro
      - /data/other/media:/media:ro
      - /etc/localtime:/etc/localtime:ro

* Proxy will forward traffic to the container, so no ports need to be exposed.
* Use environment ``CONTEXT_PATH=URL_BASE`` if airsonic is serving from a
  subpath.
* Limit airsonic to 256MB for initial memory size, and heap size. See `Java Xmx
  and Xms options`_.

Reverse Proxy Setup
*******************
Allows you to isolate your containers as well as wrap connections in SSL. See
:ref:`service-nginx` for more details. See
:ref:`service-nginx-base-proxy-control` for basic proxy configuration.

Enable Forward Headers
======================
Airsonic must be configured to expect requests through a proxy otherwise
connections will fail through a reverse proxy. Enable this and restart the
service before testing proxy configuration. Start the service to create a new
file if it doesn't exist.

.. code-block:: bash
  :caption: **0644 root root** ``/data/airsonic.properties``

  server.use-forward-headers=true

Using Subdomains
================
.. literalinclude:: source/subdomain.conf
  :caption: **0644 root root** ``nginx/conf.d/reverse-proxy.conf``

Using Subpaths
==============
.. literalinclude:: source/subpath.conf
  :caption: **0644 root root** ``nginx/conf.d/reverse-proxy.conf``

.. note::
  Use environment ``CONTEXT_PATH=URL_BASE`` if airsonic is serving from a
  subpath.

Postgres Backend
****************
Postgres may be used to store airsonic data in a centralized location. This
assumes that :ref:`service-postgres` is already configured, with an empty
database for airsonic to use (see :ref:`service-postgres-create-database`).

.. code-block:: yaml
  :caption: Docker Compose Add Postgres Network.

  networks:
    db:
      external: True
  airsonic:
    image: linuxserver/airsonic
    networks:
      - db

.. code-block:: bash
  :caption: **0644 root root** ``/data/airsonic.properties``

  DatabaseConfigType=embed
  DatabaseConfigEmbedDriver=org.postgresql.Driver
  DatabaseConfigEmbedUsername={USER}
  DatabaseConfigEmbedPassword={PASS}
  DatabaseConfigEmbedUrl=jdbc:postgresql://{DB IP}:{DB PORT}/airsonic?stringtype=unspecified
  DatabaseUsertableQuote="

.. note::
  Launch airsonic and shutdown after it finishes starting up. The initial DB
  `incorrectly defines two postgres datatypes`_. Correct this by executing the
  following commands below when Airsonic is shutdown.

.. code-block:: psql
  :caption: Set correct datatypes for columns in postgres.

  ALTER TABLE system_avatar ALTER COLUMN data TYPE bytea USING NULL;
  ALTER TABLE custom_avatar ALTER COLUMN data TYPE bytea USING NULL;

Restart Airsonic to complete DB setup.

.. rubric:: References

#. `Airsonic Configuration File <https://airsonic.github.io/docs/configure/airsonic-properties/>`_
#. `Airsonic reverse proxy <https://old.reddit.com/r/freenas/comments/b2ft7x/does_anyone_have_a_working_nginx_reverseproxy_for/>`_
#. `Airsonic nginx reverse proxy <https://airsonic.github.io/docs/proxy/nginx/>`_
#. `Airsonic Database Support <https://airsonic.github.io/docs/database/>`_

.. _Airsonic: https://airsonic.github.io/
.. _Airsonic Docker and Documentation: https://hub.docker.com/r/linuxserver/airsonic
.. _Java Xmx and Xms options: https://codeahoy.com/2019/09/02/java-xmx-vs-xms/
.. _incorrectly defines two postgres datatypes: https://github.com/airsonic/airsonic/issues/1213
