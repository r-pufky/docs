.. _service-radarr-setup:

Radarr Setup
############
Movie Management.

See `Radarr Docker and Documentation`_.

.. gport:: Ports (Radarr)
  :port:     7878
  :protocol: TCP
  :type:     Exposed
  :purpose:  Webface.
  :no_key_title:
  :no_caption:
  :no_launch:

.. gflocation:: Important File Locations (Radarr)
  :file:    /config,
            /downloads
  :purpose: Radarr main service directory.,
            Radarr monitored downloads directory.
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
  docker/service**. You need to map this exact path in radarr for it to be able
  to post-process downloads properly.
* See :ref:`service-radarr-basic-configuration` for example configuration.

.. code-block:: yaml
  :caption: Docker Compose

  ridarr:
    image: linuxserver/radarr:latest
    restart: unless-stopped
    depends_on:
      - nzbget
    environment:
      - PGID=1001
      - PUID=1001
      - TZ=America/Los_Angeles
    volumes:
      - /data/downloads:/data/downloads
      - /data/media/movies:/data/media/movies
      - /data/services/radarr:/config
      - /etc/localtime:/etc/localtime:ro

* Proxy will forward traffic to the container, so no ports need to be exposed.

Reverse Proxy Setup
*******************
Allows you to isolate your containers as well as wrap connections in SSL. See
:ref:`service-nginx` for more details. See
:ref:`service-nginx-base-proxy-control` for basic proxy configuration.

See `Radarr reverse proxy reference`_.

Using Subdomains
================
.. literalinclude:: source/subdomain.conf
  :caption: **0644 root root** ``nginx/conf.d/reverse-proxy.conf``

Using Subpaths
==============
.. literalinclude:: source/subpath.conf
  :caption: **0644 root root** ``nginx/conf.d/reverse-proxy.conf``

.. note::
  Set URL Base to ``/radarr`` in Lidarr before enabling the reverse-proxy.

  .. code-block:: xml
    :caption: **0644 user user** ``/config/config.yaml``

    <Config>
      <UrlBase>/radarr</UrlBase>
    </Config>

Add Pre-existing Series to Radarr
*********************************

#. Existing files should be in a folder for each movie.
#. :cmdmenu:`Movie --> Bulk Import Movies --> /data/movies`
#. Be sure to set appropriate import behavior.
#. Be sure to search for correct match for episode if needed.
#. Import may timeout if initial import library is large. Restart import.

   :cmdmenu:`Movies --> Update Library`.

Ensure no Duplicate Plex Updates
********************************
Plex will trigger updates on ``inotify`` events if configured to do so. If that
is the case:

:cmdmenu:`Connect --> Plex --> Update Library --> Disable`

Otherwise duplicate items will appear on single files.

.. _Radarr Docker and Documentation: https://hub.docker.com/r/linuxserver/radarr/
.. _Radarr reverse proxy reference: https://gist.github.com/IronicBadger/362c408d1f2c27a0503cb9252b508140#file-bash_aliases