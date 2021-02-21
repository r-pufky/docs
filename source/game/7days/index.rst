.. _game-7days:

7 Days to Die
#############
`7 Days to Die`_ dedicated server on steam.

See `7 Days Docker and Documentation`_.

.. gtable:: 7 Days to Die Requirements
  :header: Minimum,
           Recommended
  :c0:     2c/4t @2.4Ghz,
           6GB RAM,
           4GB Disk
  :c1:     4c/8t @3.0Ghz,
           12GB RAM,
           4GB Disk
  :no_key_title:
  :no_caption:
  :no_launch:

    See `7 Days to Die Dedicated Server`_.

Ports
*****
.. ports:: 7 Days to Die Ports
  :value0:        8080, {TCP}, {DISABLE}, Control Panel
  :value1:        8081, {TCP}, {DISABLE}, Telnet Port
  :value2:       26900, {TCP},  {PUBLIC}, Dedicated Server (Steam Server)
  :value3: 26900-26902, {UDP},  {PUBLIC}, Dedicated Server (Steam Clients)
  :open:

  .. note::
    Control Panel and Telnet are insecure. **Disable** and **block**.

Files
*****
.. files:: 7 Days to Die Files
  :value0: /data/saves/serveradmin.xml;
           Defines user bans, whitelists, admins and server commands
  :value1: /data/server/serverconfig.xml; Server configuration
  :value2: /data/server/startserver.sh; Starts server
  :value3: /data/server/7DaysToDieServer_Data; Server logs
  :delim: ;
  :open:

Docker Creation
***************
You can copy your existing state to docker ``/data`` directory adjusting for
paths.

* The UID/GID should be set to a user/group that has access to your media. All
  media clients should run under the same user to run correctly.

.. code-block:: yaml
  :caption: Docker Compose

  7days:
    image: rpufky/steam:winehq
    restart: unless-stopped
    stop_grace_period: 1m
    environment:
      - PUID=1001
      - PGID=1001
      - UPDATE_OS=1
      - UPDATE_STEAM=1
      - UPDATE_SERVER=1
      - PLATFORM=linux
      - STEAM_APP_ID=294420
      - TZ=America/Los_Angeles
    volumes:
      - '/d/7days:/data'
      - '/etc/localtime:/etc/localtime:ro'

Create ``custom_server`` script to manage server, per `7 Days Docker and
Documentation`_ requirements.

.. literalinclude:: source/custom_server
  :caption: **0755 7days 7days** ``/data/custom_server``
  :emphasize-lines: 6-7,21

.. note::
  * ``PROCESS_WAIT_TIME``: amount of time allocated to shutdown wine.
  * ``WATCHDOG_TIME``: amount of time between checking server heartbeat.

  Game options specified will launch a dedicated server visible on steam
  clients. The game server will check for updates on boot and reboot.

.. _game-7days-initial-startup:

Initial Startup
***************
7 Days needs to be started twice to generate the basic files in the correct
locations for server configuration.

.. code-block:: bash
  :caption: Start 7 Days server to generate configuration files.

  docker-compose up -d 7days

.. note::
  Wait until you see the message:

  *Using config file: /data/server/serverconfig.xml*

  This means that the server has started.

.. code-block:: bash
  :caption: Stop 7 Days server and configure it.

  docker-compose stop 7days

.. code-block:: xml
  :caption: **0644 7days 7days** ``/data/server/serverconfig.xml``
  :lineno-start: 40
  :emphasize-lines: 2

  # Uncomment this line and redirect saves to container data store.
  <property name="SaveGameFolder" value="/data/saves" />

.. code-block:: bash
  :caption: Start 7 Days server to generate server admin files.

  docker-compose up -d 7days

.. note::
  Wait until you see the message:

  *Using config file: /data/server/serverconfig.xml*

  This means that the server has started.

.. code-block:: bash
  :caption: Stop 7 Days server and configure it.

  docker-compose stop 7days

Disable Insecure 7 Day Services
*******************************
Disable these insecure services that 7 Days uses, and set long random passwords.

See `7 Days to Die server configuration reference`_ for all potential settings.

.. literalinclude:: source/serverconfig.xml
  :caption: **0644 7days 7days** ``/data/server/serverconfig.xml``
  :emphasize-lines: 26,28,30,32,41

Access to administrative commands is granted based on SteamID, in
``serveradmin.xml``. A server restart is needed to apply changes.

.. literalinclude:: source/serveradmin.xml
  :caption: **0644 7days 7days** ``/data/saves/serveradmin.xml``
  :lines: 31-66

.. _7 Days to Die: https://7daystodie.com/
.. _7 Days Docker and Documentation: https://hub.docker.com/r/rpufky/steam
.. _7 Days to Die Dedicated Server: https://7daystodie.gamepedia.com/System_Requirements
.. _7 Days to Die server configuration reference: https://developer.valvesoftware.com/wiki/7_Days_to_Die_Dedicated_Server#Installation
