.. _game-conan-setup:

Conan Exiles Setup
##################
Conan Exiles dedicated server on steam.

See `Conan Docker and Documentation`_.

.. gtable:: Conan Exiles Requirements
  :header: Players,
           CPU,
           Memory,
           Disk
  :c0:     10,
           35,
           50,
           70
  :c1:     2c/2t @3.0Ghz,
           4c/4t @3.1Ghz,
           4c/8t @3.5Ghz,
           4c/8t @4.0Ghz
  :c2:     8GB,
           8GB,
           12GB,
           12GB
  :c3:     35Gb,
           35Gb,
           35Gb,
           35Gb
  :no_key_title:
  :no_caption:
  :no_launch:

    See `Conan Exiles Dedicated Server`_.

.. gport:: Ports Exposed (Conan Exiles)
  :port:     27015,
             27016,
             7777,
             7778
  :protocol: UDP,
             UDP,
             UDP,
             UDP
  :type:     External,
             External,
             External,
             External
  :purpose:  Dedicated Server (steam).,
             Dedicated Server (steam announce).,
             Dedicated Server (clients direct).,
             Dedicated Server (client via steam).
  :no_key_title:
  :no_caption:
  :no_launch:

    * ``7778`` and ``27016`` should be opened for server to appear in steam
      public lists or in player's history. Public lists are buggy and will not
      always appear. Can take up to 15 minutes.
    * If connecting on local network, use the private IP of the server, not the
      public IP address.

.. gflocation:: Important File Locations (Conan Exiles)
  :file:    /data/server/ConanSandbox/Saved/Config/WindowsServer/Engine.ini,
            /data/server/ConanSandbox/Saved/Config/WindowsServer/ServerSettings.ini,
            /data/server/ConanSandbox/Saved/game.db
  :purpose: Core engine settings (e.g. ports).,
            Specific game instance settings.,
            Game database and saves.
  :no_key_title:
  :no_caption:
  :no_launch:

    See ``/data/server/ConanSandbox/Config/`` for default files with all
    avaliable options.

Docker Creation
***************
You can copy your existing state to docker ``/data`` directory adjusting for
paths.

* The UID/GID should be set to a user/group that has access to your media. All
  media clients should run under the same user to run correctly.
* See :ref:`game-conan-configuration` for example configuration.

.. code-block:: yaml
  :caption: Docker Compose

  conan:
    image: rpufky/steam:winehq
    restart: unless-stopped
    stop_grace_period: 1m
    ports:
      - '27015:27015'
      - '27015:27015/udp'
      - '27016:27016/udp'
      - '7777:7777/udp'
      - '7778:7778/udp'
    environment:
      - PUID=1001
      - PGID=1001
      - UPDATE_OS=1
      - UPDATE_STEAM=1
      - UPDATE_SERVER=1
      - PLATFORM=windows
      - STEAM_APP_ID=443030
      - TZ=America/Los_Angeles
    volumes:
      - '/data/conan:/data'
      - '/etc/localtime:/etc/localtime:ro'

Create ``custom_server`` script to manage server, per `Conan Docker and
Documentation`_ requirements.

.. literalinclude:: source/custom_server
  :caption: **0755 conan conan** ``/data/custom_server``
  :emphasize-lines: 6-7,26

.. note::
  * ``PROCESS_WAIT_TIME``: amount of time allocated to shutdown wine.
  * ``WATCHDOG_TIME``: amount of time between checking server heartbeat.

  Game options specified will launch a dedicated server visible on steam
  clients. The game server will check for updates on boot and reboot.

.. code-block:: bash
  :caption: Run container to create base configuration.

  docker-compose up -d conan

.. note::
  Conan will autogenerate default configuration files if they are missing. Make
  sure the server gets to a running state before shutting down.

  See :ref:`game-conan-troublshooting-wine` if wine takes multiple minutes to
  start.

.. _Conan Docker and Documentation: https://hub.docker.com/r/rpufky/steam
.. _Conan Exiles Dedicated Server: https://conanexiles.gamepedia.com/Dedicated_server_system_requirements>