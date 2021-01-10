.. _w10-20h2-xbox-game-bar:

Xbox Game Bar
#############
.. dropdown:: Disable Xbox Game Bar
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in
  :open:

  `Reference <https://www.tenforums.com/tutorials/51180-enable-disable-windows-game-recording-broadcasting-windows-10-a.html>`_

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

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

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Removing ⌘ + g Prompt on Game Launch
      :key_title: HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\
                  GameDVR
      :names:     AppCaptureEnabled
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

    .. wregedit:: `Disable xbox Game DVR`_
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

.. _Disable xbox Game DVR: https://www.tenforums.com/tutorials/8637-turn-off-xbox-game-bar-windows-10-a.html
.. _Disable xbox Game monitoring: https://www.windowscentral.com/how-disable-and-remove-game-bar-windows-10-creators-update
.. _Disable xbox Game DVR for system: https://www.ghacks.net/2019/09/27/disable-windows-10-game-bar-tips-and-notifications/
