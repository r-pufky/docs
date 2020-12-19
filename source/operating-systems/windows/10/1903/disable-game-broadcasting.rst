.. _w10-1903-disable-game-broadcasting:

`Disable Game Broadcasting`_
############################
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

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    `Disable xbox Game DVR for system`_, remove ⌘ + g prompt on game launch.

    .. wregedit:: Removing ⌘ + g Prompt on Game Launch
      :key_title: HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\
                  GameDVR
      :names:     AppCaptureEnabled
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

    .. wregedit:: Disable xbox Game DVR
      :key_title: HKEY_CURRENT_USER\System\GameConfigStore
      :names:     GameDVR_Enabled
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:
      :no_launch:

    .. wregedit:: `Disable xbox Game DVR for system`_
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\GameDVR
      :names:     AllowgameDVR
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:
      :no_launch:

    .. wregedit:: `Disable xbox Game monitoring`_
      :key_title: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\xbgm
      :names:     Start
      :types:     DWORD
      :data:      4
      :no_section:
      :no_caption:
      :no_launch:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

    .. wgpolicy:: Disable game broadcasting suite
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Windows Game Recording and Broadcasting -->
                  Enables or disables Windows Game Recording and Broadcasting
      :option:    ☑
      :setting:   Disabled
      :no_section:
      :no_caption:

.. _Disable Game Broadcasting: https://www.tenforums.com/tutorials/8637-turn-off-xbox-game-bar-windows-10-a.html
.. _Disable xbox Game monitoring: https://www.windowscentral.com/how-disable-and-remove-game-bar-windows-10-creators-update
.. _Disable xbox Game DVR for system: https://www.ghacks.net/2019/09/27/disable-windows-10-game-bar-tips-and-notifications/
