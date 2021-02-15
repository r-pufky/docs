.. _service-plex-setup:

`Plex`_ Setup
#############
Media streaming service.

See `Plex Docker and Documentation`_.

Ports
*****
.. ports:: Plex Ports
  :value0: 32400, {TCP},   {PUBLIC}, Plex Media Server Access
  :value1:  1900, {UDP}, {OPTIONAL}, Plex DLNA Server
  :value2:  3005, {TCP}, {OPTIONAL}, Control Plex Home Theater w/ Plex Companion
  :value3:  5353, {UDP}, {OPTIONAL}, Bonjour/Avahi discovery
  :value4:  8324, {TCP}, {OPTIONAL}, Control Plex for Roku w/ Plex Companion
  :value5: 32410, {UDP}, {OPTIONAL}, GDM network discovery
  :value6: 32412, {UDP}, {OPTIONAL}, GDM network discovery
  :value7: 32413, {UDP}, {OPTIONAL}, GDM network discovery
  :value8: 32414, {UDP}, {OPTIONAL}, GDM network discovery
  :value9: 32469, {TCP}, {OPTIONAL}, Plex DLNA Server
  :open:

  .. note::
    Using host networking will expose all of these ports. It may be better to
    specify just ``32400``.

    See `Plex port usage`_.

Files
*****
.. files:: Plex Files
  :value0: /config, Server configuration
  :value1: /transcode, Transcoding directory
  :value2: /tmp, Temp directory for transcoding
  :value3: /data/media, Plex media server library
  :open:

Docker Creation
***************
You can copy your existing library from ``/var/lib/plexmediaserver/*`` to docker
``/config`` directory to auto-import your existing plex library.

* The UID/GID should be set to a user/group that have access to your media. All
  media clients should run under the same user to run correctly.
* Map your media directly to where it was before on the docker container to
  prevent needing to modify any libraries. This should be read-only.
* ``/transcode`` needs to be mapped to a **fast** drive. See
  :ref:`service-plex-transcode-tmpfs` to run transcoding in memory.
* We additionally map the plex ``/tmp`` directory to a subdirectory for the
  transcoding directory. Plex updated transcoding to split video encoding to
  ``/transcode`` while the audio encoding is transcoded in ``/tmp``. This causes the
  *EAE timeout! EAE not running, or wrong folder? Could not read* Error. Moving
  ``/tmp`` fixes this.
* ``PLEX_CLAIM`` token is used to identify the server for your account. This is
  only used on initial startup without a pre-existing config. Generate a token
  here: https://www.plex.tv/claim.

.. code-block:: yaml
  :caption: Docker Compose

  plex:
    image: plexinc/pms-docker:plexpass
    restart: unless-stopped
    network_mode: host
    environment:
      - CHANGE_CONFIG_DIR_OWNERSHIP=False
      - PLEX_GID=1001
      - PLEX_UID=1001
      - PLEX_CLAIM={CLAIM TOKEN}
      - TZ=America/Los_Angeles
    volumes:
      - /data/media:/data/media:ro
      - /data/services/plexmediaserver:/config
      - /etc/localtime:/etc/localtime:ro
      - /tmp/Transcode/tmp:/tmp
      - /tmp:/transcode

.. code-block:: bash
  :caption: Stop Plex to finish configuration.

  docker-compose stop plex

.. _service-plex-transcode-tmpfs:

Setup ``/transcode`` with tmpfs
*******************************
Transcoding is disk intensive and requires a fast (SSD or better) drive to make
latencies transparent. This will setup ``/tmp`` with tmpfs (running in memory)
to do transcoding in RAM, which will make playback and seeks nearly
instantanenous.

Create tmpfs on the docker host.

.. code-block:: bash
  :caption: **0644 root root** ``/etc/fstab``

  tmpfs  /tmp  tmpfs  defaults,size=4G  0  0

.. note::
  Setup ``/tmp`` to use at most ``4GB`` of RAM for storage (tmpfs only allocates
  space from actual items stored).

  Ensure that ``/transcode`` is set on the plex server to properly map to the
  docker host ``/tmp`` directory.

Reboot to enable.

Enable Secure Server Connection
*******************************
* Ensure ``32400`` is forwarded from the router.
* Enable `DNS Rebinding`_ on router.

If not using a plex claim token or manual port forwarding you may need to setup
plex manually from the machine.

.. code-block:: bash
  :caption: Setup SSH port forward.

  ssh -L 32400:{DOCKER HOST}:32400 -N {USER}@{DOCKER HOST}

.. code-block:: bash
  :caption: Then nagivate to http://localhost:32400/web/index.html to finish
            setup.

  docker-compose up -d plex

.. _Plex: https://www.plex.tv/
.. _Plex Docker and Documentation: https://hub.docker.com/r/plexinc/pms-docker/
.. _Plex port usage: https://support.plex.tv/articles/201543147-what-network-ports-do-i-need-to-allow-through-my-firewall/
.. _DNS Rebinding: https://support.plex.tv/articles/206225077-how-to-use-secure-server-connections/
