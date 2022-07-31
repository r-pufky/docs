.. _wbase-reinstall-checklist:

Reinstall Checklist
###################
Common things to remember when reinstalling a Windows machine.

Use Robocopy
************
Fast, multi-threaded, stateful copy. Faster that GUI copy.

.. code-block:: powershell
  :caption: Copy with robocopy (powershell as admin)

  robocopy "{SOURCE} " "{DESTINATION} " /copyall /mt /z /e

.. note::
  There is an escaping issue with ``\`` at the end of a path. Paths with
  trailing ``\`` (e.g. ``"c:\Program Files (x86)\ "``) require an extra space
  to parse the path correctly based on how the strings are passed internally.

  Add extra space to all paths as it does not affect outcome and ensures no
  path errors. **Always** quote paths.

`Reference <https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy>`__

`Reference <https://www.ubackup.com/synchronization/windows-sync-two-folders-command-line-5740.html>`__

#. Remove any existing junctions, otherwise copy with halt on them.
#. Backup any wanted data from the following default locations:

   * ``c:\Users\*``
   * ``c:\Programs\``
   * ``c:\ProgramData\``
   * ``c:\Program Files (x86)\``

Dump Existing Registry
**********************
Backup the existing registry in case anything is missed after reinstall.

:cmdmenu:`⌘ --> regedit --> Computer --> {RMB} --> Export`

Gamesave Manager
****************
Backup the installation directory and games database:

* ``c:\Program Files (x86)GameSave Manager v3``
* ``%appdata%\roaming\GameSave Manager 3``

Putty
*****
.. code-block:: powershell
  :caption: Dump putty settings to reg file (powershell as admin).

  regedit /e '%userprofile%\Desktop\putty.reg' 'HKEY_CURRENT_USER\Software\SimonTatham'

WinSCP
******
:cmdmenu:`⌘ --> winscp --> Tools --> Export/Backup Configuration ...`

.. code-block:: powershell
  :caption: Dump winscp settings to reg file (powershell as admin).

  regedit /e '%userprofile%\Desktop\winscp.reg' 'HKEY_CURRENT_USER\Software\Martin Prikryl\WinSCP 2'

MusicBee
********
* Copy any special files from installation directory (e.g. plugins, etc). These
  are located in ``c:\Program Files (x86)/MusicBee``.
* Copy configuration data from `%appdata%/roaming/musicbee`.

Mumble
******
Backup the client settings, certificates, and database:
* ``%appdata%\Mumble\mumble.sqlite``
* ``%appdata%\roaming\Mumble``

.. code-block:: powershell
  :caption: Dump mumble client settings to reg file (powershell as admin).

  regedit /e '%userprofile%\Desktop\putty.reg' 'HKEY_CURRENT_USER\Software\Mumble\Mumble'

Claws-mail
**********
Default installation directory includes configuration and mail data:
``c:\Program Files (x86)\claws``.

Gaming
******
Backup saves and game data from game services.

Origin
======
Directory contains configuration and saves: ``c:\Program Files (x86)\Origin``.

Uplay
=====
Directory contains configuration and saves: ``c:\Program Files (x86)\Ubisoft``.

.. warning::
  Older ubisoft games do **not** back up to their servers even though they say
  they do.

Steam
=====
Directory contains configuration and saves:
``c:\Program Files (x86)\Steam\userdata``.
