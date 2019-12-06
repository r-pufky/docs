.. _steam-7-days-to-die:

Steam - 7 Days to Die Dedicated Server
######################################
Uses :ref:`1804-server-base-install` and assumes post template setup scripts
have been run.

* Memory: 2048MB-8096MB.
* Disk: 20GB encrypted (see :ref:`create-an-encrypted-volume-ubuntu`).

.. gport:: Ports Exposed (7 Days to Die)
  :port:     8080,
             8081,
             26900,
             26900-26902
  :protocol: TCP,
             TCP,
             TCP,
             UDP
  :type:     External,
             External,
             External,
             External
  :purpose:  Control Panel (Disabled).,
             Telnet Port (Disabled).,
             Dedicated Server (steam).,
             Dedicated Server (clients).
  :no_key_title:
  :no_caption:
  :no_launch:

    .. note::
      Control Panel and Telnet are insecure. **Disable** and **block**.

Server Setup
************
Install ``steamCMD`` and dedicated server; then migrate data to secondary disk.

.. code-block:: bash
  :caption: Install steamcmd and migrated to encrypted volume.

  sudo apt install steamcmd
  steamcmd
  exit
  mv ~/.steam /data/steam
  mv ~/.local /data/local
  ln -s /data/steam .steam
  ln -s /data/local .local
  mkdir /data/saves /data/config

.. code-block:: bash
  :caption: From steamcmd, install the server.

  steam
  login anonymous
  app_update 294420

.. note::
  ``-beta latest_experimental`` will load beta channels.

.. literalinclude:: source/7days.service
  :caption: Create a systemd service (assumes server directory is symlinked to steam server location).

.. code-block:: bash
  :caption: Enable the 7days service.

  systemctl enable 7days

.. gflocation:: Important File Locations (7 days)
  :file:    .local/share/7DaysToDie/Saves/[gametype]/[gameseed]/serveradmin.xml,
            .steam/SteamApps/common/7 Days to Die Dedicated Server/serverconfig.xml,
            .steam/SteamApps/common/7 Days to Die Dedicated Server/startserver.sh,
            .steam/SteamApps/common/7 Days to Die Dedicated Server/7DaysToDieServer_Data
  :purpose: Defines user bans; whitelists; admins and server commands.,
            Server configuration.,
            Starts server.,
            Server logs.
  :no_key_title:
  :no_caption:
  :no_launch:

    .. note::
      ``serveradmin.xml`` does not exist by default in game saves, and needs to
      be created. :download:`serveradmin.xml template <source/serveradmin.xml>`

      It might be pertinient to link directories to home directory.

Disable Insecure 7 Day Services
*******************************
Disable these insecure services that 7 Days uses, and set long random passwords.

:download:`serverconfig.xml template <source/serverconfig.xml>`

.. literalinclude:: source/serverconfig.xml
  :caption: **0644 7days 7days** ``{SERVER}/.steam/SteamApps/common/7 Days to Die Dedicated Server/serverconfig.xml``
  :emphasize-lines: 1,3,5,7
  :lines: 27-33

Starting the Server
*******************

.. code-block:: bash
  :caption: Use systemd to start the service.

  service 7days start

.. code-block:: bash
  :caption: Manually starting the server.

  src
  cd {SERVER}/.steam/SteamApps/common/7 Days to Die Dedicated Server/
  ./startserver.sh -configfile=serverconfig.xml

.. rubric:: References

#. `7 Days to Die Dedicated Server <https://developer.valvesoftware.com/wiki/7_Days_to_Die_Dedicated_Server#Installation>`_
#. `SteamCMD Reference <https://developer.valvesoftware.com/wiki/SteamCMD>`_