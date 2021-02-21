.. _service-nzbget:

NZBGet
#######
Usenet downloader.

See `NZBGet Docker and Documentation`_.

Ports
*****
.. ports:: NZBGet Ports
  :value0: 6789, {TCP}, {EXPOSED}, Default NZBGet webservice (http)
  :value1: 6791, {TCP}, {EXPOSED}, Default NZBGet webservice (https)
  :open:

Files
*****
.. files:: NZBGet Files
  :value0: /config, NZBGet main service directory
  :value1: /downloads, NZBGet monitored downloads directory
  :open:

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
