.. _service-digikam:

`digiKam`_
##########
digiKam is an advanced open-source digital photo management application that
runs on Linux, Windows, and MacOS. The application provides a comprehensive set
of tools for importing, managing, editing, and sharing photos and raw files.

This setup will focus on creating a docker-based reverse proxy, enforcing SSL
for all connections to docker containers using Let's Encrypt.

See `digiKam Docker and Documentation`_

.. gport:: Ports (digiKam)
  :port:     443,
             5800,
             5900
  :protocol: TCP,
             TCP,
             TCP
  :type:     Public,
             Private,
             Private
  :purpose:  https connections.,
             websocket webGUI.,
             VNC server.
  :no_key_title:
  :no_caption:
  :no_launch:

.. gflocation:: Important File Locations (digiKam)
  :file:    /config,
            /data
  :purpose: All digiKam configuration.,
            Media location.
  :no_key_title:
  :no_caption:
  :no_launch:

Docker Creation
***************
digiKam runs a web GUI and a VNC server. We will only access the web GUI through
the reverse proxy with authentication.

* Local storage should be locked down to prevent sensitive data from leaking.

.. code-block:: yaml
  :caption: Docker Compose

  digiKam:
   image: rpufky/digiKam:stable
   restart: unless-stopped
   environment:
     - USER_ID=1000
     - GROUP_ID=1000
     - UMASK=022
     - TZ=America/Los_Angeles
     - KEEP_APP_RUNNING=1
     - DISPLAY_WIDTH=1920
     - DISPLAY_HEIGHT=1080
     - ENABLE_CJK_FONT=1
   volumes:
     - /my/docker/service/config:/config
     - /my/photo/location:/data
     - /etc/localtime:/etc/localtime:ro

* Docker container should be run in an isolated network given the sensitive
  nature of the data and to prevent VNC server access.
* Additional `environment settings here`_.

Reverse Proxy Setup
*******************
Allows you to isolate your containers as well as wrap connections in SSL. See
:ref:`service-nginx` for more details. See
:ref:`service-nginx-base-proxy-control` for basic proxy configuration.

Using Subdomains
================
.. literalinclude:: source/subdomain.conf
  :caption: **0644 root root** ``nginx/conf.d/reverse-proxy.conf``

`Initial Setup`_
****************
Start digiKam and setup the initial configuration location and database. This
only needs to be done on initial container creation. Only two sections are
required for basic functionality:

.. ggui:: Image Location
  :option:  Configure where you keep your images
  :setting: /data
  :no_key_title:
  :no_section:
  :no_launch:

.. gtable:: Database Location
  :header: Option,
           Type,
           Location
  :c0:     Configure where you will store databases
  :c1:     SQLLite
  :c2:     /config
  :no_key_title:
  :no_section:
  :no_launch:

.. _digiKam: https://www.digikam.org/
.. _digiKam Docker and Documentation: https://github.com/r-pufky/digikam
.. _environment settings here: https://github.com/jlesage/docker-baseimage-gui#environment-variables
.. _Initial Setup: https://github.com/r-pufky/digikam#digikam-setup
