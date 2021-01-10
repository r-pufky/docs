.. _w10-20h2-settings-system-notifications-and-actions:

Notifications & Actions
#######################

Notifications
*************
.. note::
  GPO's are currently broken. Apply **both** GPO and Registry for all options
  if available. `Reference <https://social.technet.microsoft.com/Forums/windows/en-US/c39301f4-dcc9-4f2b-a872-98a23bd6d86a/gpo-to-quotturn-off-toast-notifications-on-the-lock-screenquot-does-not-work?forum=win10itprogeneral>`_.

.. _w10-20h2-settings-system-get-notifications-from-apps:

.. dropdown:: Disable get notifications from apps and other windows
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Global toggle for notifications.

  `Reference <https://www.tenforums.com/tutorials/4111-turn-off-notifications-apps-senders-windows-10-a.html#option2>`_

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    Working.

    .. wgpolicy:: Disable get notifications from apps and other windows
      :key_title: User Configuration -->
                  Administrative Templates -->
                  Start Menu and Taskbar -->
                  Notifications -->
                  Turn off toast notifications
      :option:    ☑
      :setting:   Enabled
      :no_section:
      :no_caption:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Disable get notifications from apps and other windows
      :key_title: HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\
                  PushNotifications
      :names:     ToastEnabled
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

.. dropdown:: Disable show notifications on lock screen
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    Broken. Will enforce if it is already disabled, but will not force disable.
    Use registry keys to force disable.

    .. wgpolicy:: Disable get notifications from apps and other windows
      :key_title: User Configuration -->
                  Administrative Templates -->
                  Start Menu and Taskbar -->
                  Notifications -->
                  Turn off toast notifications on the lock screen
      :option:    ☑
      :setting:   Enabled
      :no_section:
      :no_caption:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Disable show notifications on lock screen
      :key_title: HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\
                  Notifications\Settings
      :names:     NOC_GLOBAL_SETTING_ALLOW_TOASTS_ABOVE_LOCK
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

    .. wregedit:: Disable show notifications on lock screen
      :key_title: HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\
                  PushNotifications
      :names:     LockScreenToastEnabled
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:
      :no_launch:

.. dropdown:: Disable show reminders and incomign VoIP calls on the lock screen
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Disable show reminders and incomign VoIP calls on the lock screen
      :key_title: HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\
                  Notifications\Settings
      :names:     NOC_GLOBAL_SETTING_ALLOW_CRITICAL_TOASTS_ABOVE_LOCK
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

.. dropdown:: Disable allow notifications to play sounds
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Disable allow notifications to play sounds
      :key_title: HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\
                  Notifications\Settings
      :names:     NOC_GLOBAL_SETTING_ALLOW_NOTIFICATION_SOUND
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

.. dropdown:: Disable show me the windows welcome experience after updates and 
              occasionally when I sign in to highlight what's new and suggested
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    `Reference <https://www.makeuseof.com/tag/disable-windows-welcome-experience-page-windows-10/>`_

    .. wregedit:: Disable show me the windows welcome experience after updates
                  and occasionally when I sign in to highlight what's new and
                  suggested
      :key_title: HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\
                  ContentDeliveryManager
      :names:     SubscribedContent-310093Enabled
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

    Broken.

    `Reference <https://admx.help/?Category=Windows_10_2016&Policy=Microsoft.Policies.CloudContent%3A%3ADisableWindowsSpotlightWindowsWelcomeExperience>`_

    .. wgpolicy:: Disable show me the windows welcome experience after updates
                  and occasionally when I sign in to highlight what's new and
                  suggested
      :key_title: User Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Cloud Content -->
                  Turn off the Windows Welcome Experience
      :option:    ☑
      :setting:   Enabled
      :no_section:
      :no_caption:

.. dropdown:: Disable suggest ways I can finish setting up my device to get the
              most out of Windows
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    `Reference <https://www.tenforums.com/tutorials/137645-turn-off-get-even-more-out-windows-suggestions-windows-10-a.html>`_

    .. wregedit:: Disable suggest ways I can finish setting up my device to get
                  the most out of Windows
      :key_title: HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\
                  UserProfileEngagement
      :names:     ScoobeSystemSettingEnabled
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

.. dropdown:: Disable get tips, tricks, and suggestions as you use Windows
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in
  
  `Reference <https://www.tenforums.com/tutorials/30869-turn-off-tip-trick-suggestion-notifications-windows-10-a.html>`_

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Disable get tips, tricks, and suggestions as you use Windows
      :key_title: HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\
                  ContentDeliveryManager
      :names:     SubscribedContent-338389Enabled
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

    Only works in ``Enterprise`` and ``Education`` Windows versions.

    .. wgpolicy:: Disable get tips, tricks, and suggestions as you use Windows
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Cloud Content -->
                  Do not show Windows tips
      :option:    ☑
      :setting:   Enabled
      :no_section:
      :no_caption:

Get notifications from these senders
************************************
:ref:`w10-20h2-settings-system-get-notifications-from-apps` must be enabled for
these per-app options to be enabled.

.. dropdown:: Notifications can be disabled on a per-app basis
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Each application will have specific notification settings to set.

  `Reference <https://community.spiceworks.com/topic/2264044-how-to-manage-windows-10-notifications-via-gpo-for-specific-programs>`_
  
  .. wregedit:: Notifications can be disabled on a per-app basis
    :key_title: HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\
                Notifications\Settings\{APPLICATION}
    :names:     Enabled
    :types:     DWORD
    :data:      0
    :no_section:
    :no_caption:
