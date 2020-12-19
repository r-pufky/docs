.. _w10-1903-reasonable-privacy-notifications:

Notifications
#############
:cmdmenu:`⌘ + r --> ms-settings:privacy-notifications`

.. dropdown:: Allow access to user notifications on this device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  This disables all notification options. See
  :ref:`Allow apps to access your notifications
  <w10-1903-privacy-notifications>` to manage access on a per app basis.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    ``0`` to enable user notifications. ``Allow`` to enable notification
    listener. 

    .. wregedit:: Disable access to user notifications on this device
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\
                  CurrentVersion\PushNotifications
      :names:     NoCloudApplicationNotification
      :types:     DWORD
      :data:      1
      :no_section:
      :no_caption:

    .. wregedit:: Disable access to user notifications listener on this device
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
                  CapabilityAccessManager\ConsentStore\userNotificationListener
      :names:     Value
      :types:     SZ
      :data:      Deny
      :no_section:
      :no_caption:
      :no_launch:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

    .. wgpolicy:: Disable access to user notifications on this device
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Start Menu and Taskbar -->
                  Notifications -->
                  Turn off Notifications network usage
      :option:    ☑
      :setting:   Enabled
      :no_section:
      :no_caption:

.. _w10-1903-privacy-notifications:

.. dropdown:: Allow apps to access your notifications
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more fine
  grained control of app access.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    ``0`` enables app access to notifications.

    .. wregedit:: Disable apps to access your notifications
      :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
      :names:     LetAppsAccessNotifications
      :types:     DWORD
      :data:      2
      :no_section:
      :no_caption:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

    .. wgpolicy:: Disable apps to access your notifications
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  App Privacy -->
                  Let Windows apps access notifications
      :option:    ☑,
                  Default for all apps
      :setting:   Enabled,
                  Force Deny
      :no_section:
      :no_caption:

.. rubric:: Rreferences

#. `Notification Windows Management Settings <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#185-notifications>`_
