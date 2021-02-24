.. _w10-1903-disable-game-broadcasting:

Disable Game Broadcasting
#########################
Nearly every program on windows now wants to record your games and broadcast
them. This disables the built-in windows game broadcasting and recording
software.

Also removes the :cmdmenu:`⌘ + g` prompt when starting games.

This occurs because of the xbox app on Windows 10. Removing the app will also
fix this. See :ref:`w10-remove-preinstalled-packages`.

.. dropdown:: Disable game broadcasting
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in
  :open:

  Disable xbox Game DVR for system and remove ⌘ + g prompt on game launch.

  .. gpo::    Disable game broadcasting suite
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Windows Game Recording and Broadcasting -->
              Enables or disables Windows Game Recording and Broadcasting
    :value0:  ☑, {DISABLED}
    :ref:     https://www.tenforums.com/tutorials/8637-turn-off-xbox-game-bar-windows-10-a.html
    :update:  2021-02-19
    :generic:

  .. regedit:: Removing ⌘ + g Prompt on Game Launch
    :path:i    HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\
               GameDVR
    :value0:   AppCaptureEnabled, {DWORD}, 0
    :ref:      https://www.tenforums.com/tutorials/8637-turn-off-xbox-game-bar-windows-10-a.html
    :update:   2021-02-19
    :generic:

  .. regedit:: Disable xbox Game DVR
    :path:     HKEY_CURRENT_USER\System\GameConfigStore
    :value0:   GameDVR_Enabled, {DWORD}, 0
    :ref:      https://www.tenforums.com/tutorials/8637-turn-off-xbox-game-bar-windows-10-a.html
    :update:   2021-02-19
    :generic:

  .. regedit:: Disable xbox Game DVR for system
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\GameDVR
    :value0:   AllowgameDVR, {DWORD}, 0
    :ref:      https://www.ghacks.net/2019/09/27/disable-windows-10-game-bar-tips-and-notifications/
    :update:   2021-02-19
    :generic:

  .. regedit:: Disable xbox Game monitoring
    :path:     HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\xbgm
    :value0:   Start, {DWORD}, 4
    :ref:      https://www.windowscentral.com/how-disable-and-remove-game-bar-windows-10-creators-update
    :update:   2021-02-19
    :generic:
