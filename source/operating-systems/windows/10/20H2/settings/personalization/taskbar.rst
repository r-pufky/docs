.. _w10-20h2-settings-personalization-taskbar:

Taskbar
#######
.. dropdown:: Lock the taskbar
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. gpo:: Lock the taskbar
    :path: User Configuration -->
                Administrative Templates -->
                Start Menu and Taskbar -->
                Lock the Taskbar
    :value0:    ☑, {ENABLED}
    :ref:       https://www.tenforums.com/tutorials/104265-enable-disable-lock-taskbar-windows-10-a.html
    :update:    2021-02-19
    :generic:
    :open:

  .. regedit:: Lock the taskbar
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion
               Policies\Explorer
    :value0:   LockTaskbar, {DWORD}, 1
    :ref:      https://www.tenforums.com/tutorials/104265-enable-disable-lock-taskbar-windows-10-a.html
    :update:   2021-02-19
    :generic:
    :open:

    Reference is inverted. ``1`` will lock the taskbar.

.. regedit:: Replace Command Prompt with Windows Powershell in the menu when I right-click the start button or press Windows key+X
  :path:     HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion
             Explorer\Advanced
  :value0:   DontUsePowerShellOnWinX, {DWORD}, 0
  :ref:      https://blogs.msmvps.com/russel/2016/11/18/defaulting-to-powershell-instead-of-cmd/
  :update:   2021-02-19

.. regedit:: Disable Show badges on taskbar buttons
  :path:     HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion
             Explorer\Advanced
  :value0:   TaskbarBadges, {DWORD}, 0
  :ref:      https://www.tenforums.com/tutorials/48186-taskbar-buttons-hide-show-badges-windows-10-a.html
  :update:   2021-02-19

Notification Area
*****************
.. dropdown:: Always show all icons in the notification area
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. gpo::    Lock the taskbar
    :path:    User Configuration -->
              Administrative Templates -->
              Start Menu and Taskbar -->
              Turn off notification area cleanup
    :value0:  ☑, {ENABLED}
    :ref:     https://www.tenforums.com/tutorials/5313-hide-show-notification-area-icons-taskbar-windows-10-a.html#option5
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Always show all icons in the notification area
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion
               Explorer
    :value0:   EnableAutoTray, {DWORD}, 0
    :ref:      https://www.tenforums.com/tutorials/5313-hide-show-notification-area-icons-taskbar-windows-10-a.html#option5
    :update:   2021-02-19
    :generic:
    :open:

  .. regedit:: Always show all icons in the notification area
    :path:     HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion
               Explorer
    :value0:   EnableAutoTray, {DWORD}, 0
    :ref:      https://www.tenforums.com/tutorials/5313-hide-show-notification-area-icons-taskbar-windows-10-a.html#option5
    :update:   2021-02-19
    :generic:
    :open:

.. todo::
  Manually disable these system icons; there is no current Registry or GPO to
  set these.

  * Location
  * Microphone

.. regedit:: Disable Input Indicator Icon
  :path:     HKEY_CURRENT_USER\Software\Microsoft\CTF\LangBar
  :value0:   ShowStatus, {DWORD}, 3
  :ref:      https://www.tenforums.com/tutorials/103041-turn-off-language-bar-input-indicator-windows-10-a.html
  :update:   2021-02-19

.. regedit:: Disable Windows Ink Workspace Icon
  :path:     HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion
             PenWorkspace
  :value0:   PenWorkspaceButtonDesiredVisibility, {DWORD}, 0
  :ref:      https://www.tenforums.com/tutorials/48147-hide-show-windows-ink-workspace-button-taskbar-windows-10-a.html
  :update:   2021-02-19

.. regedit:: Disable Touch Keyboard Icon
  :path:     HKEY_CURRENT_USER\SOFTWARE\Microsoft\TabletTip\1.7
  :value0:   TipbandDesiredVisibility, {DWORD}, 0
  :ref:      https://www.tenforums.com/tutorials/28436-hide-show-touch-keyboard-button-taskbar-windows-10-a.html
  :update:   2021-02-19

.. regedit:: Disable Touchpad Icon
  :path:     HKEY_CURRENT_USER\Software\Microsoft\Touchpad
  :value0:   TouchpadDesiredVisibility, {DWORD}, 0
  :ref:      https://www.tenforums.com/tutorials/69380-hide-show-touchpad-button-taskbar-windows-10-a.html
  :update:   2021-02-19

.. gpo::   Disable Action Center Icon
  :path:   User Configuration -->
           Administrative Templates -->
           Start Menu and Taskbar -->
           Remove Notifications and Action Center
  :value0: ☑, {ENABLED}
  :ref:    https://www.tenforums.com/tutorials/86601-enable-disable-system-icons-taskbar-windows-10-a.html
  :update: 2021-02-19

.. dropdown:: Disable Meet Now Icon
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. gpo::    Disable Meet Now Icon
    :path:    User Configuration -->
              Administrative Templates -->
              Start Menu and Taskbar -->
              Remove the Meet Now icon
    :value0:  ☑, {ENABLED}
    :ref:     https://www.tenforums.com/tutorials/165990-how-add-remove-meet-now-icon-taskbar-windows-10-a.html
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable Meet Now Icon
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion
               Policies\Explorer
    :value0:   HideSCAMeetNow, {DWORD}, 1
    :ref:      https://www.tenforums.com/tutorials/165990-how-add-remove-meet-now-icon-taskbar-windows-10-a.html
    :update:   2021-02-19
    :generic:
    :open:

People
******
.. dropdown:: Disable Show contacts on the taskbar
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. gpo::    Disable Show contacts on the taskbar
    :path:    User Configuration -->
              Administrative Templates -->
              Start Menu and Taskbar -->
              Remove the People Bar from the taskbar
    :value0:  ☑, {ENABLED}
    :ref:     https://www.tenforums.com/tutorials/104877-enable-disable-people-bar-taskbar-windows-10-a.html
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable Show contacts on the taskbar
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows
               Explorer
    :value0:   HidePeopleBar, {DWORD}, 1
    :ref:      https://www.tenforums.com/tutorials/104877-enable-disable-people-bar-taskbar-windows-10-a.html
    :update:   2021-02-19
    :generic:
    :open:

.. regedit:: Disable Show my people notifications
  :path:     HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion
             Explorer\Advanced\People\ShoulderTap
  :value0:   ShoulderTap, {DWORD}, 0
  :ref:      https://www.tenforums.com/tutorials/84717-turn-off-show-my-people-pops-windows-10-a.html
  :update:   2021-02-19

.. regedit:: Disable Play a sound when a My People notification arrives
  :path:     HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion
             Explorer\Advanced\People\ShoulderTap
  :value0:   ShoulderTapAudio, {DWORD}, 0
  :ref:      https://www.tenforums.com/tutorials/84725-turn-off-play-sound-my-people-pop-windows-10-a.html
  :update:   2021-02-19

.. regedit:: Disable Show My People app suggestions
  :path:     HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion
             ContentDeliveryManager
  :value0:   SubscribedContent-314563Enabled, {DWORD}, 0
  :ref: https://www.tenforums.com/tutorials/84725-turn-off-play-sound-my-people-pop-windows-10-a.html
  :update:   2021-02-19
