.. _service-heimdall:

`Heimdall`_
###########
Application Dashboard.

See `Heimdall Docker and Documentation`_

.. gport:: Ports (Heimdall)
  :port:     443
  :protocol: TCP
  :type:     Exposed
  :purpose:  Webface.
  :no_key_title:
  :no_caption:
  :no_launch:

.. gflocation:: Important File Locations (Heimdall)
  :file:    /config
  :purpose: Heimdall main service directory.
  :no_key_title:
  :no_caption:
  :no_launch:

Docker Creation
***************

.. code-block:: yaml
  :caption: Docker Compose

  heimdall:
    image: linuxserver/heimdall:latest
    restart: unless-stopped
    environment:
      - PGID=1001
      - PUID=1001
      - TZ=America/Los_Angeles
    volumes:
      - /data/services/heimdall:/config
      - /etc/localtime:/etc/localtime:ro

* Proxy will forward traffic to the container, so no ports need to be exposed.

Reverse Proxy Setup
*******************
Allows you to isolate your containers as well as wrap connections in SSL. See
:ref:`service-nginx` for more details. See
:ref:`service-nginx-base-proxy-control` for basic proxy configuration.

Heimdall is **not subpath** aware, and should be hosted from a subdomain.

Using Subdomains
================
.. literalinclude:: source/subdomain.conf
  :caption: **0644 root root** ``nginx/conf.d/reverse-proxy.conf``

Add Password Authentication
***************************
A reverse proxy setup is **required**. See :ref:`service-nginx-basic-auth`.

.. _Heimdall: https://heimdall.site/
.. _Heimdall Docker and Documentation: https://github.com/linuxserver/Heimdall