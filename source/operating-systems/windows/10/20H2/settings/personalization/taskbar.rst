.. _w10-20h2-settings-personalization-taskbar:

Taskbar
#######
.. dropdown:: Lock the taskbar 
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Lock the taskbar
      :key_title: User Configuration -->
                  Administrative Templates -->
                  Start Menu and Taskbar -->
                  Lock the Taskbar
      :option:    ☑
      :setting:   Enabled
      :no_section:
      :no_caption:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    Reference is inverted. ``1`` will lock the taskbar.

    .. wregedit:: Lock the taskbar
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion
                  Policies\Explorer
      :names:     LockTaskbar
      :types:     DWORD
      :data:      1
      :no_section:
      :no_caption:

  `Reference <https://www.tenforums.com/tutorials/104265-enable-disable-lock-taskbar-windows-10-a.html>`__

.. dropdown:: Replace Command Prompt with Windows Powershell in the menu when I right-click the start button or press Windows key+X
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Replace Command Prompt with Windows Powershell in the menu when I right-click the start button or press Windows key+X
      :key_title: HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion
                  Explorer\Advanced
      :names:     DontUsePowerShellOnWinX
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

  `Reference <https://blogs.msmvps.com/russel/2016/11/18/defaulting-to-powershell-instead-of-cmd/>`__

.. dropdown:: Disable Show badges on taskbar buttons
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Disable Show badges on taskbar buttons
      :key_title: HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion
                  Explorer\Advanced
      :names:     TaskbarBadges
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

  `Reference <https://www.tenforums.com/tutorials/48186-taskbar-buttons-hide-show-badges-windows-10-a.html>`__

Notification Area
*****************
.. dropdown:: Always show all icons in the notification area
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Lock the taskbar
      :key_title: User Configuration -->
                  Administrative Templates -->
                  Start Menu and Taskbar -->
                  Turn off notification area cleanup
      :option:    ☑
      :setting:   Enabled
      :no_section:
      :no_caption:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Always show all icons in the notification area
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion
                  Explorer
      :names:     EnableAutoTray
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

    .. wregedit:: Always show all icons in the notification area
      :key_title: HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion
                  Explorer
      :names:     EnableAutoTray
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:
      :no_launch:

  `Reference <https://www.tenforums.com/tutorials/5313-hide-show-notification-area-icons-taskbar-windows-10-a.html#option5>`__

.. TODO::
  Manually disable these system icons; there is no current Registry or GPO to
  set these.

  * Location
  * Microphone

.. dropdown:: Disable Input Indicator Icon
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Disable Input Indicator Icon
      :key_title: HKEY_CURRENT_USER\Software\Microsoft\CTF\LangBar
      :names:     ShowStatus
      :types:     DWORD
      :data:      3
      :no_section:
      :no_caption:

  `Reference <https://www.tenforums.com/tutorials/103041-turn-off-language-bar-input-indicator-windows-10-a.html>`__

.. dropdown:: Disable Windows Ink Workspace Icon
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Disable Windows Ink Workspace Icon
      :key_title: HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion
                  PenWorkspace
      :names:     PenWorkspaceButtonDesiredVisibility
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

  `Reference <https://www.tenforums.com/tutorials/48147-hide-show-windows-ink-workspace-button-taskbar-windows-10-a.html>`__

.. dropdown:: Disable Touch Keyboard Icon
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Disable Touch Keyboard Icon
      :key_title: HKEY_CURRENT_USER\SOFTWARE\Microsoft\TabletTip\1.7
      :names:     TipbandDesiredVisibility
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

  `Reference <https://www.tenforums.com/tutorials/28436-hide-show-touch-keyboard-button-taskbar-windows-10-a.html>`__

.. dropdown:: Disable Touchpad Icon
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Disable Touchpad Icon
      :key_title: HKEY_CURRENT_USER\Software\Microsoft\Touchpad
      :names:     TouchpadDesiredVisibility
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

  `Reference <https://www.tenforums.com/tutorials/69380-hide-show-touchpad-button-taskbar-windows-10-a.html>`__

.. dropdown:: Disable Action Center Icon
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Disable Action Center Icon
      :key_title: User Configuration -->
                  Administrative Templates -->
                  Start Menu and Taskbar -->
                  Remove Notifications and Action Center
      :option:    ☑
      :setting:   Enabled
      :no_section:
      :no_caption:

  `Reference <https://www.tenforums.com/tutorials/86601-enable-disable-system-icons-taskbar-windows-10-a.html>`__

.. dropdown:: Disable Meet Now Icon
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Disable Meet Now Icon
      :key_title: User Configuration -->
                  Administrative Templates -->
                  Start Menu and Taskbar -->
                  Remove the Meet Now icon
      :option:    ☑
      :setting:   Enabled
      :no_section:
      :no_caption:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Disable Meet Now Icon
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion
                  Policies\Explorer
      :names:     HideSCAMeetNow
      :types:     DWORD
      :data:      1
      :no_section:
      :no_caption:

  `Reference <https://www.tenforums.com/tutorials/165990-how-add-remove-meet-now-icon-taskbar-windows-10-a.html>`__

People
******
.. dropdown:: Disable Show contacts on the taskbar
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Disable Show contacts on the taskbar
      :key_title: User Configuration -->
                  Administrative Templates -->
                  Start Menu and Taskbar -->
                  Remove the People Bar from the taskbar
      :option:    ☑
      :setting:   Enabled
      :no_section:
      :no_caption:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Disable Show contacts on the taskbar
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows
                  Explorer
      :names:     HidePeopleBar
      :types:     DWORD
      :data:      1
      :no_section:
      :no_caption:

  `Reference <https://www.tenforums.com/tutorials/104877-enable-disable-people-bar-taskbar-windows-10-a.html>`__

.. dropdown:: Disable Show my people notifications
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Disable Show my people notifications
      :key_title: HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion
                  Explorer\Advanced\People\ShoulderTap
      :names:     ShoulderTap
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

  `Reference <https://www.tenforums.com/tutorials/84717-turn-off-show-my-people-pops-windows-10-a.html>`__

.. dropdown:: Disable Play a sound when a My People notification arrives
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Disable Play a sound when a My People notification arrives
      :key_title: HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion
                  Explorer\Advanced\People\ShoulderTap
      :names:     ShoulderTapAudio
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

  `Reference <https://www.tenforums.com/tutorials/84725-turn-off-play-sound-my-people-pop-windows-10-a.html>`__

.. dropdown:: Disable Show My People app suggestions
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Disable Show My People app suggestions
      :key_title: HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion
                  ContentDeliveryManager
      :names:     SubscribedContent-314563Enabled
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

  `Reference <https://www.tenforums.com/tutorials/84725-turn-off-play-sound-my-people-pop-windows-10-a.html>`__
