.. _w10-21h2-settings-privacy-notifications:

Notifications
#############
:cmdmenu:`⌘ + r --> ms-settings:privacy-notifications`

See :ref:`wbase-determining-app-list` to generate a list of apps for more fine
grained control of app access.

Allow access to user notifications on this device
*************************************************
.. dropdown:: Disable Allow access to user notifications on this device
  :color: primary
  :icon: shield-lock
  :animate: fade-in
  :class-container: sd-shadow-sm

  This disables all notification options. See
  :ref:`w10-21h2-settings-privacy-notifications-apps` to manage access on a
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

.. _w10-21h2-settings-privacy-notifications-apps:

Allow apps to access your notifications
***************************************
.. dropdown:: Disable Allow apps to access your notifications
  :color: primary
  :icon: shield-lock
  :animate: fade-in
  :class-container: sd-shadow-sm

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
