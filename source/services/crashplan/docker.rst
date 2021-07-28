.. _service-crashplan-docker:

Crashplan Docker Install
########################
Crashplan Pro (For Small Business) is now the only consumer level option for
crashplan.

`Reference <https://hub.docker.com/r/jlesage/crashplan-pro>`__

Ports
*****
.. ports:: Crashplan Pro Ports
  :value0: 5800, {TCP}, {EXPOSED}, GUI web interface
  :value1: 5900, {TCP}, {EXPOSED}, GUI via VNC
  :open:

Files
*****
.. files:: Crashplan Pro Files
  :value0: /config/var, Crashplan identity certs
  :value1: /storage, Default map for backup location
  :open:

Docker Creation
***************
If first-run, just launch the docker container to generate the correct
configuration directory structure, afterwards you can stop and inject your
current certificates into the configuration directory.

* Crashplan should run as **root** to be able to read/backup all files.
* ``/storage`` is the default location; however, you can mount any directory as
  long as it doesn't overwrite docker image directories. ``/data`` is free to
  use.
* ``/`` is mapped to ``/root-mount`` to enable backup of any files on ``/`` for
  the host that also exist in the docker image.
* Map your backup drives as ``read only``.

.. code-block:: yaml
  :caption: Docker Compose.

  crashplan:
    image: jlesage/crashplan-pro:latest
    restart: unless-stopped
    environment:
      - GROUP_ID=0
      - KEEP_APP_RUNNING=1
      - SECURE_CONNECTION=1
      - TZ=America/Los_Angeles
      - USER_ID=0
    volumes:
      - /:/root-mount:ro
      - /data/services/crashplan:/config:rw
      - /data:/data:ro
      - /etc/localtime:/etc/localtime:ro

* Proxy will forward traffic to the container, so no ports need to be exposed.

Reverse Proxy Setup
*******************
Allows you to isolate your containers as well as wrap connections in SSL. See
:ref:`service-nginx` for more details. See
:ref:`service-nginx-base-proxy-control` for basic proxy configuration.

Using Subdomains
================
.. literalinclude:: source/subdomain.conf
  :caption: **0644 root root** ``nginx/conf.d/reverse-proxy.conf``

`Reference <https://github.com/jlesage/docker-crashplan-pro#routing-based-on-url-path>`__

Using Subpaths
===============
.. literalinclude:: source/subpath.conf
  :caption: **0644 root root** ``nginx/conf.d/reverse-proxy.conf``

* Ensure ``HTTP`` or ``HTTPS`` for underlying service, depending on whether you
  are running it in the container (``SECURE_CONNECTION=``).
* If a **black screen** occurs, remove image and pull a new one. Ensure multiple
  containers are **not** running.
* The docker container uses websockets for the built in GUI display.

`Reference <https://stackoverflow.com/questions/15193743/nginx-reverse-proxy-websockets>`__

Initial Setup
*************
.. code-block:: bash
  :caption: Stop crashplan to configure service.

  docker-compose stop crashplan

Add Existing Certs
==================
If you have a current crashplan installation, you can copy your crashplan
identity to ``/config/var``.

.. code-block:: bash
  :caption: **0750 root root** ``/config/var``

  .identity
  service.pem
  .ui_info

Increase inotify limits to prevent warnings, see:
:ref:`service-crashplan-troublshooting-inotify`.

Import existing backup configuration with :ref:`service-crashplan-adoption`.
