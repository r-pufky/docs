.. _service-lidarr-setup:

Lidarr Setup
############
Music Management.

See `Lidarr Docker and Documentation`_.

Ports
*****
.. ports:: Lidarr Ports
  :value0: 8686, {TCP}, {EXPOSED}, Webface
  :open:

.. gflocation:: Important File Locations (Lidarr)
  :file:    /config,
            /downloads
  :purpose: Lidarr main service directory.,
            Lidarr monitored downloads directory.
  :no_key_title:
  :no_caption:
  :no_launch:

Docker Creation
***************
You can copy your existing configuration to docker ``/config`` directory
adjusting for paths.

* The UID/GID should be set to a user/group that has access to your media. All
  media clients should run under the same user to run correctly.
* Your downloader will report the download path **mapped in the downloader
  docker/service**. You need to map this exact path in lidarr for it to be able
  to post-process downloads properly.
* See :ref:`service-lidarr-basic-configuration` for example configuration.

.. code-block:: yaml
  :caption: Docker Compose

  lidarr:
    image: linuxserver/lidarr:latest
    restart: unless-stopped
    depends_on:
      - nzbget
    environment:
      - PGID=1001
      - PUID=1001
      - TZ=America/Los_Angeles
    volumes:
      - /data/downloads:/data/downloads
      - /data/media/music:/data/media/music
      - /data/services/lidarr:/config
      - /etc/localtime:/etc/localtime:ro

* Proxy will forward traffic to the container, so no ports need to be exposed.

Reverse Proxy Setup
*******************
Allows you to isolate your containers as well as wrap connections in SSL. See
:ref:`service-nginx` for more details. See
:ref:`service-nginx-base-proxy-control` for basic proxy configuration.

See `Lidarr reverse proxy reference`_.

Using Subdomains
================
.. literalinclude:: source/subdomain.conf
  :caption: **0644 root root** ``nginx/conf.d/reverse-proxy.conf``

Using Subpaths
==============
.. literalinclude:: source/subpath.conf
  :caption: **0644 root root** ``nginx/conf.d/reverse-proxy.conf``

.. note::
  Set URL Base to ``/lidarr`` in Lidarr before enabling the reverse-proxy.

  .. code-block:: xml
    :caption: **0640 user user** ``/config/config.yaml``

    <Config>
      <UrlBase>/lidarr</UrlBase>
    </Config>

.. _Lidarr Docker and Documentation: https://hub.docker.com/r/linuxserver/lidarr/
.. _Lidarr reverse proxy reference: https://gist.github.com/IronicBadger/362c408d1f2c27a0503cb9252b508140#file-bash_aliases
