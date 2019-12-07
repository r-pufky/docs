.. _service-crashplan:

Crashplan Pro
#############
Crashplan Pro (For Small Business) is now the only consumer level option for
crashplan.

See `Crashplan Docker and Documentation`_.

.. gport:: Ports (Crashplan Pro)
  :port:     5800,
             5900
  :protocol: TCP,
             TCP
  :type:     Exposed,
             Exposed
  :purpose:  GUI web interface.,
             GUI via VNC.
  :no_key_title:
  :no_caption:
  :no_launch:

.. gflocation:: Important File Locations (Crashplan Pro)
  :file:    /config/var,
            /storage
  :purpose: Crashplan identity certs.,
            Default map for backup location.
  :no_key_title:
  :no_caption:
  :no_launch:

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

See `subdomain reference`_.

Using Subpaths
===============
.. literalinclude:: source/subpath.conf
  :caption: **0644 root root** ``nginx/conf.d/reverse-proxy.conf``

* Ensure ``HTTP`` or ``HTTPS`` for underlying service, depending on whether you
  are running it in the container (``SECURE_CONNECTION=``).
* If a **black screen** occurs, remove image and pull a new one. Ensure multiple
  containers are **not** running.
* The docker container uses `websockets`_ for the built in GUI display.

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

Bump Inotify Limits
===================
Increase `inotify max watch limits`_ on host so crashplan can watch monitored
files.

.. code-block:: bash
  :caption: **0644 root root** ``/etc/sysctl.conf``

  fs.inotify.max_user_watches=1048576

.. code-block:: bash
  :caption: Reload sysctl (or reboot):

  sysctl -p /etc/sysctl.conf

.. code-block:: bash
  :caption: Restart crashplan.

  docker-compose start crashplan

Taking Over Existing Backups
============================
Read `docker container documentation here`_.

Backup tasks will need to migrated if the locations have changed due to running
in a docker container (these are usually ``/`` based backups like ``/etc``).

If identity imported then no adoption of a backup set is needed.

.. _Crashplan Docker and Documentation: https://github.com/jlesage/docker-crashplan-pro
.. _inotify max watch limits: https://support.code42.com/CrashPlan/4/Troubleshooting/Linux_real-time_file_watching_errors
.. _docker container documentation here: https://github.com/jlesage/docker-crashplan-pro#taking-over-existing-backup
.. _subdomain reference: https://hub.docker.com/r/jlesage/crashplan-pro/#routing-based-on-url-path
.. _websockets: https://stackoverflow.com/questions/15193743/nginx-reverse-proxy-websockets