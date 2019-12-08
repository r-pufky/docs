.. _service-nzbget:

NZBGet
#######
Usenet downloader.

See `NZBGet Docker and Documentation`_.

.. gport:: Ports (NZBGet)
  :port:     6789,
             6791
  :protocol: TCP,
             TCP
  :type:     Exposed,
             Exposed
  :purpose:  Default NZBGet webservice (http).,
             Default NZBGet webservice (https).
  :no_key_title:
  :no_caption:
  :no_launch:

.. gflocation:: Important File Locations (NZBGet)
  :file:    /config,
            /downloads
  :purpose: NZBGet main service directory.,
            NZBGet monitored downloads directory.
  :no_key_title:
  :no_caption:
  :no_launch:

Docker Creation
***************
You can copy your existing configuration to docker ``/config`` directory
adjusting for paths.

* The UID/GID should be set to a user/group that have access to your media. All
  media clients should run under the same user to run correctly.
* Map your media directly to where it was before on the docker container to
  prevent needing to modify any libraries. This should be read-only.

.. code-block:: yaml
  :caption: Docker Compose

  nzbget:
    image: linuxserver/nzbget:latest
    restart: unless-stopped
    environment:
      - PGID=1001
      - PUID=1001
      - TZ=America/Los_Angeles
    volumes:
      - /data/downloads:/data/downloads
      - /data/services/nzbget:/config
      - /etc/localtime:/etc/localtime:ro

* Proxy will forward traffic to the container, so no ports need to be exposed.

Reverse Proxy Setup
*******************
Allows you to isolate your containers as well as wrap connections in SSL. See
:ref:`service-nginx` for more details. See
:ref:`service-nginx-base-proxy-control` for basic proxy configuration.

See `NZBGet reverse proxy reference`_.

Using Subdomains
================
.. literalinclude:: source/subdomain.conf
  :caption: **0644 root root** ``nginx/conf.d/reverse-proxy.conf``

Using Subpaths
==============
.. literalinclude:: source/subpath.conf
  :caption: **0644 root root** ``nginx/conf.d/reverse-proxy.conf``

Basic Configuration
*******************
Example NZBGet configuration. Adjust as needed.

:download:`nzbget.conf <source/nzbget.conf>`

.. literalinclude:: source/nzbget.conf
  :caption: **0640 user user** ``/config/nzbget.conf``
  :emphasize-lines: 17-20

.. _NZBGet Docker and Documentation: https://hub.docker.com/r/linuxserver/nzbget/
.. _NZBGet reverse proxy reference: https://nzbget.net/behind-other-web-server