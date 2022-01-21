.. _w10-20h2-settings-privacy-messaging:

Messaging
#########
:cmdmenu:`⌘ + r --> ms-settings:privacy-messaging`

See :ref:`wbase-determining-app-list` to generate a list of apps for more fine
grained control of app access.

Allow access to messaging on this device
****************************************
.. dropdown:: Disable Allow access to messaging on this device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  This disables all messaging options. See
  :ref:`w10-20h2-settings-privacy-messaging-apps` to manage access on a per app
  basis.

  .. gpo::    Disable Allow access to messaging on this device
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              App Privacy -->
              Let Windows apps access messaging
    :value0:  ☑, {ENABLED}
    :value1:  Default for all apps, Force Deny
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1812-messaging
    :update:  2021-02-19
    :generic:
    :open:

    ``Allow`` enables.

  .. regedit:: Disable Allow access to messaging on this device
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
               CapabilityAccessManager\ConsentStore\chat
    :value0:   Value, {SZ}, Deny
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1812-messaging
    :update:   2021-02-19
    :generic:
    :open:

.. _w10-20h2-settings-privacy-messaging-apps:

Allow apps to read or send messages
***********************************
.. dropdown:: Disable Allow apps to read or send messages
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. gpo::    Disable Allow apps to read or send messages
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              App Privacy -->
              Let Windows apps access messaging
    :value0:  ☑, {ENABLED}
    :value1:  Default for all apps, Force Deny
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1812-messaging
    :update:  2021-02-19
    :generic:
    :open:

    ``0`` enables apps access to messaging.

  .. regedit:: Disable Allow apps to read or send messages
    :path:     HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
    :value0:   LetAppsAccessMessaging, {DWORD}, 2
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1812-messaging
    :update:   2021-02-19
    :generic:
    :open:

Choose which apps can read or send messages
*******************************************
See :ref:`w10-20h2-settings-privacy-messaging-apps`.
