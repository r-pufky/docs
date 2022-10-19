.. _w10-21h2-settings-system-notifications-and-actions:

Notifications & Actions
#######################
.. note::
  GPO's work in ``Education`` and ``Enterprise``. Apply **both** GPO and
  Registry for all options if available. `Reference <https://social.technet.microsoft.com/Forums/windows/en-US/c39301f4-dcc9-4f2b-a872-98a23bd6d86a/gpo-to-quotturn-off-toast-notifications-on-the-lock-screenquot-does-not-work?forum=win10itprogeneral>`_.

Notifications
*************

.. _w10-21h2-settings-system-get-notifications-from-apps:

.. dropdown:: Disable get notifications from apps and other senders
  :color: primary
  :icon: shield-lock
  :animate: fade-in
  :class-container: sd-shadow-sm

  Global toggle for notifications.

  .. gpo::    Disable get notifications from apps and other windows
    :path:    User Configuration -->
              Administrative Templates -->
              Start Menu and Taskbar -->
              Notifications -->
              Turn off toast notifications
    :value0:  ☑, {ENABLED}
    :ref:     https://www.tenforums.com/tutorials/4111-turn-off-notifications-apps-senders-windows-10-a.html#option2
    :update:  2021-02-19
    :generic:
    :open:

.. dropdown:: Disable show notifications on lock screen
  :color: primary
  :icon: shield-lock
  :animate: fade-in
  :class-container: sd-shadow-sm

  .. gpo:: Disable get notifications from apps and other windows
    :path: User Configuration -->
                Administrative Templates -->
                Start Menu and Taskbar -->
                Notifications -->
                Turn off toast notifications on the lock screen
    :value0:    ☑, {ENABLED}
    :update:   2021-02-19
    :generic:
    :open:

.. regedit:: Disable show reminders and incomign VoIP calls on the lock screen
  :path:     HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\
             Notifications\Settings
  :value0:   NOC_GLOBAL_SETTING_ALLOW_CRITICAL_TOASTS_ABOVE_LOCK, {DWORD}, 0
  :update:   2021-02-19

.. regedit:: Disable allow notifications to play sounds
  :path:     HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\
             Notifications\Settings
  :value0:   NOC_GLOBAL_SETTING_ALLOW_NOTIFICATION_SOUND, {DWORD}, 0
  :update:   2021-02-19

.. dropdown:: Disable show me the windows welcome experience after updates and
              occasionally when I sign in to highlight what's new and suggested
  :color: primary
  :icon: shield-lock
  :animate: fade-in
  :class-container: sd-shadow-sm

  .. gpo::    Disable show me the windows welcome experience after updates
              and occasionally when I sign in to highlight what's new and
              suggested
    :path:    User Configuration -->
              Administrative Templates -->
              Windows Components -->
              Cloud Content -->
              Turn off the Windows Welcome Experience
    :value0:  ☑, {ENABLED}
    :ref:     https://admx.help/?Category=Windows_10_2016&Policy=Microsoft.Policies.CloudContent%3A%3ADisableWindowsSpotlightWindowsWelcomeExperience
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable show me the windows welcome experience after updates
               and occasionally when I sign in to highlight what's new and
               suggested
    :path:     HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\
               ContentDeliveryManager
    :value0:   SubscribedContent-310093Enabled, {DWORD}, 0
    :ref:      https://www.makeuseof.com/tag/disable-windows-welcome-experience-page-windows-10/
    :update:   2021-02-19
    :generic:
    :open:

.. regedit:: Disable suggest ways I can finish setting up my device to get
             the most out of Windows
  :path:     HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\
             UserProfileEngagement
  :value0:   ScoobeSystemSettingEnabled, {DWORD}, 0
  :ref:      https://www.tenforums.com/tutorials/137645-turn-off-get-even-more-out-windows-suggestions-windows-10-a.html
  :update:   2021-02-19

.. dropdown:: Disable get tips, tricks, and suggestions as you use Windows
  :color: primary
  :icon: shield-lock
  :animate: fade-in
  :class-container: sd-shadow-sm

  .. gpo::    Disable get tips, tricks, and suggestions as you use Windows
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Cloud Content -->
              Do not show Windows tips
    :value0:  ☑, {ENABLED}
    :ref:     https://www.tenforums.com/tutorials/30869-turn-off-tip-trick-suggestion-notifications-windows-10-a.html
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable get tips, tricks, and suggestions as you use Windows
    :path:     HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\
               ContentDeliveryManager
    :value0:   SubscribedContent-338389Enabled, {DWORD}, 0
    :ref:      https://www.tenforums.com/tutorials/30869-turn-off-tip-trick-suggestion-notifications-windows-10-a.html
    :update:   2021-02-19
    :generic:
    :open:

Get notifications from these senders
************************************
:ref:`Notifications <w10-21h2-settings-system-get-notifications-from-apps>` must
be enabled for these per-app options to be enabled.

.. regedit:: Notifications can be disabled on a per-app basis
  :path:     HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\
             Notifications\Settings\{APPLICATION}
  :value0:   Enabled, {DWORD}, 0
  :ref: https://community.spiceworks.com/topic/2264044-how-to-manage-windows-10-notifications-via-gpo-for-specific-programs
  :update: 2021-02-19

  Each application will have specific notification settings to set.
