.. _w10-1903-disable-game-broadcasting:

`Disable Game Broadcasting`_
############################
Nearly every program on windows now wants to record your games and broadcast
them. This disables the built-in windows game broadcasting and recording
software.

Also removes the :cmdmenu:`⌘ + g` prompt when starting games.

This occurs because of the xbox app on Windows 10. Removing the app will also
fix this. See :ref:`w10-1903-remove-preinstalled-packages`.

:term:`Registry` User
*********************
.. wregedit:: Removing ⌘ + g Prompt on Game Launch via Registry
  :key_title: HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\
              GameDVR
  :names:     AppCaptureEnabled
  :types:     DWORD
  :data:      0
  :no_section:

.. wregedit:: Disable xbox Game DVR via Registry
  :key_title: HKEY_CURRENT_USER\System\GameConfigStore
  :names:     GameDVR_Enabled
  :types:     DWORD
  :data:      0
  :no_section:
  :no_launch:

:term:`Registry` Machine
************************
.. wregedit:: `Disable xbox Game DVR for system`_ via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\GameDVR
  :names:     AllowgameDVR
  :types:     DWORD
  :data:      0
  :no_section:
  :no_launch:

.. wregedit:: `Disable xbox Game monitoring`_ via Registry
  :key_title: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\xbgm
  :names:     Start
  :types:     DWORD
  :data:      4
  :no_section:
  :no_launch:

:term:`GPO` Computer
********************
.. wgpolicy:: Disable game broadcasting suite policy via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Windows Game Recording and Broadcasting -->
              Enables or disables Windows Game Recording and Broadcasting
  :option:    ☑
  :setting:   Disabled
  :no_section:

.. _Disable Game Broadcasting: https://www.tenforums.com/tutorials/8637-turn-off-xbox-game-bar-windows-10-a.html
.. _Disable xbox Game monitoring: https://www.windowscentral.com/how-disable-and-remove-game-bar-windows-10-creators-update
.. _Disable xbox Game DVR for system: https://www.ghacks.net/2019/09/27/disable-windows-10-game-bar-tips-and-notifications/
