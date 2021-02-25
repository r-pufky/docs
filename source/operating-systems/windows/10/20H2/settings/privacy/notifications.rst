.. _w10-20h2-settings-privacy-notifications:

Notifications
#############
:cmdmenu:`⌘ + r --> ms-settings:privacy-notifications`

See :ref:`w10-determining-app-list` to generate a list of apps for more fine
grained control of app access.

Allow access to user notifications on this device
*************************************************
.. dropdown:: Disable Allow access to user notifications on this device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  This disables all notification options. See
  :ref:`w10-20h2-settings-privacy-notifications-apps` to manage access on a
  per app basis.

  .. gpo::    Disable access to user notifications on this device
    :path:    Computer Configuration -->
              Administrative Templates -->
              Start Menu and Taskbar -->
              Notifications -->
              Turn off Notifications network usage
    :value0:  ☑, {ENABLED}
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#185-notifications
    :update:  2021-02-19
    :generic:
    :open:

    ``0`` to enable user notifications. ``Allow`` to enable notification
    listener. 

  .. regedit:: Disable access to user notifications on this device
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\
               CurrentVersion\PushNotifications
    :value0:   NoCloudApplicationNotification, {DWORD}, 1
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#185-notifications
    :update:   2021-02-19
    :generic:
    :open:

  .. regedit:: Disable access to user notifications listener on this device
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
               CapabilityAccessManager\ConsentStore\userNotificationListener
    :value0:   Value, {SZ}, Deny
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#185-notifications
    :update:   2021-02-19
    :generic:
    :open:

.. _w10-20h2-settings-privacy-notifications-apps:

Allow apps to access your notifications
***************************************
.. dropdown:: Disable Allow apps to access your notifications
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. gpo::    Disable apps to access your notifications
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              App Privacy -->
              Let Windows apps access notifications
    :value0:  ☑, {ENABLED}
    :value1:  Default for all apps, Force Deny
    :update:  2021-02-19
    :generic:
    :open:

  ``0`` enables app access to notifications.

  .. regedit:: Disable apps to access your notifications
    :path:     HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
    :value0:   LetAppsAccessNotifications, {DWORD}, 2
    :update:   2021-02-19
    :generic:
    :open:

Choose which apps can access your location
******************************************
See :ref:`w10-20h2-settings-privacy-notifications-apps`.
