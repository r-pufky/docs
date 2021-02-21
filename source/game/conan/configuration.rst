.. _game-conan-configuration:

Configuration
#############
Minimal options need to be change directly in the configuration files. Other
options can be changed directly via the admin panel in game.

.. literalinclude:: source/Engine.ini
  :caption: **0644 conan conan** ``/data/server/ConanSandbox/Saved/Config/WindowsServer/Engine.ini``
  :emphasize-lines: 9,11-12,15,18,21,23-25

.. note::
  Add sections if they do not exist.

  On initial creation, most options will be removed and stored in the game
  database.

.. literalinclude:: source/ServerSettings.ini
  :caption:  **0644 conan conan** ``/data/server/ConanSandbox/Saved/Config/WindowsServer/ServerSettings.ini``
  :emphasize-lines: 3,108-109,42,124-125

.. gui::   Option Values
  :path:   Option Values
  :value0: MaxNudity; 2=Full, 1=Partial, 0=None
  :value1: IsBattleEyeEnabled; Disable for linux
  :value2: IsVACEnabled; Disable for linux
  :value3: serverRegion; 3=Asia, 2=Americas, 1/0=Europe
  :value4: PVPEnabled; Boolean player versus player combat
  :value5: AdminPassword; {PASS}
  :delim: ;
  :update: 2018-06-19

  .. note::
    All other settings can be changed in **admin panel** when connected; see
    ``/data/server/ConanSandbox/Config`` for all options.

Installing Mods
***************
Mods can be used for conan running on linux; installing these mods automatically
from the workshop with wine doesn't work consistently.

Obtain workshop mods
====================
* Download the mods using the steam workshop and your game client.
* These should appear in ``{STEAM}/content/440900/{MOD ID}/{MOD NAME}.pak``.
* Copy all ``pak`` files to linux server.

.. code-block:: bash
  :caption: Create a ``Mods`` folder within ``ConanSandbox`` and place all ``pak`` files within.

  mkdir /data/server/ConanSandbox/Mods
  cp *.pak /data/server/ConanSandbox/Mods

Enable modlist
==============
Place each mod on a separate line, prefaced with ``*``, which will enable the
mod in this directory.

.. code-block:: bash
  :caption: **0644 conan conan** ``/data/server/ConanSandbox/Mods/modlist.txt``

  *MyAwesomeMod.pak
  *MyAwesomeOtherMod.pak

.. code-block:: bash
  :caption: Ensure permissions are correct and start server.

  chown -R conan /data/server

Backup
******
Server DB is a SQLite database, which can be backed up while running.

.. literalinclude:: source/conan-backup
  :caption: **0755 root root** ``/root/cron/conan-backup``
  :emphasize-lines: 5-6

.. code-block:: bash
  :caption: ``sudo crontab -e``

  @weekly /root/cron/conan-backup
