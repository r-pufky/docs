.. _w10-21h2-settings-gaming-xbox-game-bar:

Xbox Game Bar
#############
.. dropdown:: Disable Xbox Game Bar
  :color: primary
  :icon: shield-lock
  :animate: fade-in
  :class-container: sd-shadow-sm
  :open:

  .. gpo::    Disable game broadcasting suite
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Windows Game Recording and Broadcasting -->
              Enables or disables Windows Game Recording and Broadcasting
    :value0:  ☑, {DISABLED}
    :ref:     https://www.tenforums.com/tutorials/51180-enable-disable-windows-game-recording-broadcasting-windows-10-a.html
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable Open Xbox Game Bar using this button on a controller
    :path:     HKEY_CURRENT_USER\SOFTWARE\Microsoft\GameBar
    :value0:   UseNexusForGameBarEnabled, {DWORD}, 0
    :ref:      https://www.tenforums.com/tutorials/51180-enable-disable-windows-game-recording-broadcasting-windows-10-a.html
    :update:   2021-02-19
    :generic:
    :open:

  .. regedit:: Remove ⌘ + g Prompt on Game Launch
    :path:     HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\
               GameDVR
    :value0:   AppCaptureEnabled, {DWORD}, 0
    :ref:      https://www.tenforums.com/tutorials/51180-enable-disable-windows-game-recording-broadcasting-windows-10-a.html
    :update:   2021-02-19
    :generic:
    :open:

  .. regedit:: Disable xbox Game DVR
    :path:     HKEY_CURRENT_USER\System\GameConfigStore
    :value0:   GameDVR_Enabled, {DWORD}, 0
    :ref:      https://www.tenforums.com/tutorials/8637-turn-off-xbox-game-bar-windows-10-a.html
    :update:   2021-02-19
    :generic:
    :open:

  .. regedit:: Disable xbox Game DVR for system
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\GameDVR
    :value0:   AllowgameDVR, {DWORD}, 0
    :ref:      https://www.ghacks.net/2019/09/27/disable-windows-10-game-bar-tips-and-notifications/
    :update:   2021-02-19
    :generic:
    :open:
