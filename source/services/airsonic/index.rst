.. _service-airsonic:

`Airsonic`_
###########
Music streaming.

See `Airsonic Docker and Documentation`_.

.. gport:: Ports (Airsonic)
  :port:     4040
  :protocol: TCP
  :type:     Exposed
  :purpose:  Airsonic webservice.
  :no_key_title:
  :no_caption:
  :no_launch:

.. gflocation:: Important File Locations (Airsonic)
  :file:    /config,
            /config/airsonic.properties,
            /playlists,
            /podcasts,
            /music,
            /media
  :purpose: Airsonic configuration directory.,
            Global airsonic configuration.,
            Playlists data.,
            Podcasts data.,
            Music data.,
            Additional media data (videos; etc).
  :no_key_title:
  :no_caption:
  :no_launch:

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
===============
.. literalinclude:: source/subpath.conf
  :caption: **0644 root root** ``nginx/conf.d/reverse-proxy.conf``

.. note::
  Use environment ``CONTEXT_PATH=URL_BASE`` if airsonic is serving from a
  subpath.

.. rubric:: References

#. `Airsonic Configuration File <https://airsonic.github.io/docs/configure/airsonic-properties/>`_
#. `Airsonic reverse proxy <https://old.reddit.com/r/freenas/comments/b2ft7x/does_anyone_have_a_working_nginx_reverseproxy_for/>`_
#. `Airsonic nginx reverse proxy <https://airsonic.github.io/docs/proxy/nginx/>`_

.. _Airsonic: https://airsonic.github.io/
.. _Airsonic Docker and Documentation: https://hub.docker.com/r/linuxserver/airsonic
.. _Java Xmx and Xms options: https://codeahoy.com/2019/09/02/java-xmx-vs-xms/
