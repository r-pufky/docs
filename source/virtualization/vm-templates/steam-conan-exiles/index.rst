.. _steam-conan-exiles:

Steam - Conan Exiles (Linux) Dedicated Server
#############################################
Uses :ref:`1804-server-base-install` and assumes post template setup scripts
have been run.

* Memory: 2048MB-8096MB
* Disk: 20GB

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
  :file:    /data/conan-exiles-server/ConanSandbox/Saved/Config/WindowsServer/Engine.ini,
            /data/conan-exiles-server/ConanSandbox/Saved/Config/WindowsServer/ServerSettings.ini,
            /data/conan-exiles-server/ConanSandbox/Saved/game.db
  :purpose: Core engine settings (e.g. ports).,
            Specific game instance settings.,
            Game database and saves.
  :no_key_title:
  :no_caption:
  :no_launch:

    See ``{TARGET}/ConanSandbox/Config/`` for default files with all avaliable
    options.

Server Setup
************
Since the dedicated server only runs on windows, force steam to detect windows
and run under wine.

.. code-block:: bash
  :caption: Install base packages.

  dpkg --add-architecture i386
  apt install --install-recommends steamcmd lib32gcc1 wine-stable wine32 wine64 xvfb

.. code-block:: bash
  :caption: Alternatively, you can install from the more current wineHQ repository.

  dpkg --add-architecture i386
  wget -qO - https://dl.winehq.org/wine-builds/winehq.key | apt-key add -
  apt-add-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ bionic main'
  apt-get  update && apt-get upgrade
  apt-get install --install-recommends steamcmd lib32gcc1 winehq-stable xvfb

.. code-block:: bash
  :caption: Force steam to detect 'windows' platform, download dedicated server to target.

  steamcmd +@sSteamCmdForcePlatformType windows +force_install_dir /data/conan-exiles-server +login anonymous +app_update 443030 validate +quit

.. code-block:: bash
  :caption: Run initial server to create config templates.

  /opt/wine-stable/bin/wine64 /data/conan-exiles-server/ConanSandbox/Binaries/Win64/ConanExilesServer-Win64-Test.exe -nosteamclient -game -server -log

* run for about 5 minutes for all configs to be generated.
* should run through 2 cycles (two report cycles after loading/errors).
* configs should appear in ``/data/conan-exiles-server/ConanSandbox/Saved/Config/WindowsServer``.

.. literalinclude:: source/Engine.ini
  :caption: **0644 conan conan** ``/data/conan-exiles-server/ConanSandbox/Saved/Config/WindowsServer/Engine.ini``
  :emphasize-lines: 9,11-12,15,18,21,23-25

.. note::
  Add sections if they do not exist.

  On initial creation, most options will be removed and stored in the game
  database.

.. literalinclude:: source/ServerSettings.ini
  :caption:  **0644 conan conan** ``/data/conan-exiles-server/ConanSandbox/Saved/Config/WindowsServer/ServerSettings.ini``
  :emphasize-lines: 3,108-109,42,124-125

.. ggui:: Option Values
  :key_title: Option Values
  :option:  MaxNudity,
            IsBattleEyeEnabled,
            IsVACEnabled,
            serverRegion,
            PVPEnabled,
            AdminPassword
  :setting: 2=Full; 1=Partial; 0=None,
            Disable for linux.,
            Disable for linux.,
            3=Asia; 2=Americas; 1/0=Europe. Tested as of 2018-06-19.,
            Boolean player versus player combat.,
            Administrator password.
  :no_key_title:
  :no_caption:
  :no_launch:

    .. note::
      All other settings can be changed in *admin panel* when connected; see
      ``/data/conan-exiles-server/ConanSandbox/Config`` for all options.

Running as a Service
********************
Use ``xvfb`` to emulate correct environment for wine to function as a server.
If it runs correctly in a shell but not as a service, this is why.

.. code-block:: bash
  :caption: Create conan system user and set permissions.

  adduser --system --home /data/conan-exiles-server conan
  cp -av ~/.wine /data/conan-exiles-server/.wine
  chown -R conan /data/conan-exiles-server

.. literalinclude:: source/conan.service
  :caption: **0644 root root** ``/etc/systemd/system/conan.service``

.. code-block:: bash
  :caption: Reload the service, start and watch the logs.

  systemctl daemon-reload
  systemctl enable conan.service
  systemctl start conan
  journalctl -f -u conan

Installing Mods
***************
Mods can be used for conan running on linux; though installing these mods
automatically from the workshop with wine doesn't work consistently.

Obtain workshop mods
====================
* Download the mods wanted using the steam workshop and your game client.
* These should appear in ``{STEAM}/content/440900/{MOD ID}/MOD_NAME.pak``.
* Copy all ``pak`` files to linux server.

.. code-block:: bash
  :caption: Create a ``Mods`` folder within ``ConanSandbox`` and place all ``pak`` files within.

  mkdir /data/conan-exiles-server/ConanSandbox/Mods
  cp *.pak /data/conan-exiles-server/ConanSandbox/Mods

Enable modlist
==============
Place each mod on a separate line, prefaced with ``*``, which will enable the
server to find the mod in this directory.

.. code-block:: bash
  :caption: **0644 conan conan** ``/data/conan-exiles/server/ConanSandbox/Mods/modlist.txt``

  *MyAwesomeMod.pak
  *MyAwesomeOtherMod.pak

.. code-block:: bash
  :caption: Ensure permissions are correct and start server.

  chown -R conan /data/conan-exiles-server
  systemctl start conan

Updating Server
***************
The server may be updated by stopping it, and running the update command. You will
need permissions to the directory to do the update.

It's a good idea to backup the install incase something goes wrong.

.. code-block:: bash

  systemctl stop conan
  su - conan
  cp -av /data/conan-exiles-server /data/backups/<date>-conan-exiles-server
  steamcmd +@sSteamCmdForcePlatformType windows +force_install_dir /data/conan-exiles-server +login anonymous +app_update 443030 validate +quit
  systemctl start conan

.. note::
  If you get ``0x0`` or ``disk write errors``, you need to explicitly own the
  files to modify them via steamcmd. ``su`` to the user or temporarily chown
  them.

Wine Taking Long Time for First Start
*************************************
``winehq`` may potentially take ~5 minutes on first boot to launch, due to
blocking on boot events:

.. pull-quote::
  *0014:err:ole:get_local_server_stream Failed: 80004002*

.. pull-quote::
  *__wine_kernel_init boot event wait timed out*

Subsequent boots will not see the delay. Mitigate this by updating wine before
our first use.

.. code-block:: bash

  wineboot --update
  xvfb-run --autoservernum wineboot --update

This is a suspected issue with the GCC build toolchain, but has not been
resolved yet. See `GCC breaks 64bit wine`_ and `wait timeout`_.

.. rubric:: References

#. `Conan Exiles Dedicated Server <https://conanexiles.gamepedia.com/Dedicated_server_system_requirements>`_
#. `Conan Exiles CentOS <https://steamcommunity.com/sharedfiles/filedetails/?id=858035949>`_
#. `Installing wine on Ubuntu <https://tecadmin.net/install-wine-on-ubuntu/>`_
#. `Conan Exiles multi-server Docker <https://hub.docker.com/r/alinmear/docker-conanexiles/>`_
#. `Conan Exiles Ports <https://old.reddit.com/r/ConanExiles/comments/5tgbsh/lets_discuss_ports/>`_
#. `Running Conan Exiles with wine on Ubuntu <https://steamcommunity.com/sharedfiles/filedetails/?id=858035949>`_

.. _GCC breaks 64bit wine: https://bugs.winehq.org/show_bug.cgi?id=38653
.. _wait timeout: https://ubuntuforums.org/archive/index.php/t-1499348.html
