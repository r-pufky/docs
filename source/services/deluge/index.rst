.. _service-deluge:

Deluge
######
Bittorrent downloader.

See `Deluge Docker and Documentation`_.

.. gport:: Ports (Deluge)
  :port:     49160,
             8112
  :protocol: UDP/TCP,
             TCP
  :type:     Public,
             Exposed
  :purpose:  Peer Port for transfers.,
             Webface.
  :no_key_title:
  :no_caption:
  :no_launch:

.. gflocation:: Important File Locations (Deluge)
  :file:    /config/core.conf,
            /config/web.conf,
            /watch,
            /downloads
  :purpose: Daemon Settings.,
            WebUI Settings.,
            Watch directory.,
            Downloads direcory.
  :no_key_title:
  :no_caption:
  :no_launch:

Docker Creation
***************
If first-run, just launch the docker container to generate the correct
configuration directory structure, afterwards you can re-create with mapped
directories.

* The UID/GID should be set to a user/group that have access to your media. All
  media clients should run under the same user to run correctly.

.. code-block:: yaml
  :caption: Docker Compose

  deluge:
    image: linuxserver/deluge:latest
    restart: unless-stopped
    ports:
      - "49160:49160"
      - "49160:49160/udp"
    environment:
      - PGID=1001
      - PUID=1001
      - TZ=America/Los_Angeles
    volumes:
      - /data/downloads/watched:/watch
      - /data/downloads:/data/downloads
      - /data/services/deluge:/config
      - /etc/localtime:/etc/localtime:ro

.. note::
  Port ``49160`` needs to be exposed for transfers.

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

Using Subpaths
==============
.. literalinclude:: source/subpath.conf
  :caption: **0644 root root** ``nginx/conf.d/reverse-proxy.conf``

See `subpath reference`_.

Modifying Settings
******************
Deluge **must** be connected to the Daemon to write configuration changes.
Ensure you select ``Connect`` on ``Connection Manager``.

Required changes to minimally secure your configuration.

.. literalinclude:: source/core.conf
  :caption: **0644 user user** ``/config/core.conf``
  :emphasize-lines: 6-7,8,9,14,19,21,23,27,33,47,51,54-58,59,62,99

.. tip::
  ``max_upload_speed`` should be set to a non-zero number to enable downloads.

Reset Password
**************
Stop Deluge and remove ``pwd_sh1`` pasword line in ``web.conf``, restart.

.. literalinclude:: source/web.conf
  :caption: **0644 user user** ``/config/web.conf``
  :emphasize-lines: 7

.. note::
  The default username/password is ``admin`` / ``deluge``.

.. _Deluge Docker and Documentation: https://hub.docker.com/r/linuxserver/deluge/
.. _subdomain reference: https://forum.deluge-torrent.org/viewtopic.php?t=35117
.. _subpath reference: https://dev.deluge-torrent.org/wiki/UserGuide/WebUI/ReverseProxy