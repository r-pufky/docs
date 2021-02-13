.. _service-sonarr-setup:

Sonarr Setup
############
TV Management.

See `Sonarr Docker and Documentation`_.

Ports
*****
.. ports:: Sonarr Ports
  :value0: 8989, {TCP}, {EXPOSED}, Webface
  :open:

.. gflocation:: Important File Locations (Sonarr)
  :file:    /config,
            /downloads
  :purpose: Sonarr main service directory.,
            Sonarr monitored downloads directory.
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
  docker/service**. You need to map this exact path in Sonarr for it to be able
  to post-process downloads properly.
* See :ref:`service-sonarr-basic-configuration` for example configuration.

.. code-block:: yaml
  :caption: Docker Compose

  sonarr:
    image: linuxserver/sonarr:latest
    restart: unless-stopped
    depends_on:
      - nzbget
    environment:
      - PGID=1001
      - PUID=1001
      - TZ=America/Los_Angeles
    volumes:
      - /data/downloads:/data/downloads
      - /data/media/tv:/data/media/tv
      - /data/services/sonarr:/config
      - /etc/localtime:/etc/localtime:ro

* Proxy will forward traffic to the container, so no ports need to be exposed.

Reverse Proxy Setup
*******************
Allows you to isolate your containers as well as wrap connections in SSL. See
:ref:`service-nginx` for more details. See
:ref:`service-nginx-base-proxy-control` for basic proxy configuration.

See `Sonarr reverse proxy reference`_.

Using Subdomains
================
.. literalinclude:: source/subdomain.conf
  :caption: **0644 root root** ``nginx/conf.d/reverse-proxy.conf``

Using Subpaths
==============
.. literalinclude:: source/subpath.conf
  :caption: **0644 root root** ``nginx/conf.d/reverse-proxy.conf``

.. note::
  Set URL Base to ``/sonarr`` in Sonarr before enabling the reverse-proxy.

  .. code-block:: xml
    :caption: **0640 user user** ``/config/config.yaml``

    <Config>
      <UrlBase>/sonarr</UrlBase>
    </Config>

Add Pre-existing Series to Sonarr
*********************************

#. Existing files should be in a folder for each movie.
#. :cmdmenu:`Movie --> Bulk Import Movies --> /data/tv`
#. Be sure to set appropriate import behavior.
#. Be sure to search for correct match for episode if needed.
#. Add all existing shows (even no longer aired), these are all scanned when
   adding shows and will be crufty if not set.

Changing Media Location in Series
*********************************
If series were imported under a different directory initially, these can be
updated.

#. :cmdmenu:`Series --> Series Editor`
#. Select all series that had location changes.
#. :cmdmenu:`Root Folder` (lower right) and enter new folder location.
#. :cmdmenu:`Save`

Ensure no Duplicate Plex Updates
********************************
Plex will trigger updates on ``inotify`` events if configured to do so. If that
is the case:

:cmdmenu:`Connect --> Plex --> Update Library --> Disable`

Otherwise duplicate items will appear on single files.

.. _Sonarr Docker and Documentation: https://hub.docker.com/r/linuxserver/sonarr/
.. _Sonarr reverse proxy reference: https://gist.github.com/IronicBadger/362c408d1f2c27a0503cb9252b508140#file-bash_aliases
