.. _windows-10-reasonable-privacy-notifications:

Notifications
#############
:cmdmenu:`⌘ + r --> ms-settings:privacy-notifications`

.. rubric:: Allow access to user notifications on this device

.. note::
  This disables all notification options. See
  :ref:`windows-10-privacy-notifications` to manage access on a per app basis.

.. wregedit:: Disable access to user notifications on this device via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\
              CurrentVersion\PushNotifications
  :names:     NoCloudApplicationNotification
  :types:     DWORD
  :data:      1
  :no_section:

.. wregedit:: Disable access to user notifications listner on this device via
              Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
              CapabilityAccessManager\ConsentStore\userNotificationListener
  :names:     Value
  :types:     SZ
  :data:      Deny
  :no_section:

.. wgpolicy:: Disable access to user notifications on this device via machine
              GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Start Menu and Taskbar -->
              Notifications -->
              Turn off Notifications network usage
  :option:    ☑
  :setting:   Enabled
  :no_section:

.. _windows-10-privacy-notifications:

.. rubric:: Allow apps to access your notifications

.. wregedit:: Disable apps to access your notifications via Registry
  :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
  :names:     LetAppsAccessNotifications
  :types:     DWORD
  :data:      2
  :no_section:

    .. note::
      See :ref:`windows-10-privacy-app-list` to generate a list of apps for more
      fine grained control of app access.

.. wgpolicy:: Disable apps to access your notifications via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              App Privacy -->
              Let Windows apps access location
  :option:    ☑,
              Default for all apps
  :setting:   Enabled,
              Force Deny
  :no_section:

    .. note::
      See :ref:`windows-10-privacy-app-list` to generate a list of apps for more
      fine grained control of app access.

.. rubric:: Rreferences

#. `Notification Windows Management Settings <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#185-notifications>`_