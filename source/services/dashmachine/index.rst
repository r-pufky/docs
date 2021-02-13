.. _service-dashmachine:

`dashmachine`_
##############
Application Dashboard.

See `dashmachine Docker and Documentation`_

Ports
*****
.. ports:: dashmachine Ports
  :value0: 5000, {TCP}, {EXPOSED}, Webface
  :open:

.. gflocation:: Important File Locations (dashmachine)
  :file:    /dashmachine/dashmachine/user_data
  :purpose: dashmachine main service directory.
  :no_key_title:
  :no_caption:
  :no_launch:

Docker Creation
***************

.. code-block:: yaml
  :caption: Docker Compose

  dashmachine:
    image: rmountjoy/dashmachine:latest
    restart: always
    environment:
      - PGID=1001
      - PUID=1001
      - TZ=America/Los_Angeles
    volumes:
      - /data/services/dashmachine:/dashmachine/dashmachine/user_data
      - /etc/localtime:/etc/localtime:ro

* Proxy will forward traffic to the container, so no ports need to be exposed.

Reverse Proxy Setup
*******************
Allows you to isolate your containers as well as wrap connections in SSL. See
:ref:`service-nginx` for more details. See
:ref:`service-nginx-base-proxy-control` for basic proxy configuration.

dashmachine is **not subpath** aware, and should be hosted from a subdomain.

Using Subdomains
================
.. literalinclude:: source/subdomain.conf
  :caption: **0644 root root** ``nginx/conf.d/reverse-proxy.conf``

Using Subpaths
==============
.. literalinclude:: source/subpath.conf
  :caption: **0644 root root** ``nginx/conf.d/reverse-proxy.conf``

.. _dashmachine: https://www.reddit.com/r/DashMachine
.. _dashmachine Docker and Documentation: https://github.com/rmountjoy92/DashMachine
