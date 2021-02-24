.. _w10-1903-reasonable-privacy-messaging:

Messaging
#########
:cmdmenu:`⌘ + r --> ms-settings:privacy-messaging`

.. rubric:: Allow access to messaging on this device

.. dropdown:: Allow access to messaging on this device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  This disables all messaging value0s. See
  :ref:`Allow apps to read or send messages <w10-1903-privacy-messaging>` to
  manage access on a per app basis.

  .. gpo::    Disable apps access your messaging
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

  .. regedit:: Disable access to messaging on this device
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
               CapabilityAccessManager\ConsentStore\chat
    :value0:   Value, {SZ}, Deny
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1812-messaging
    :update:   2021-02-19
    :generic:
    :open:

    ``Allow`` enables access to messaging on this device.

.. _w10-1903-privacy-messaging:

.. dropdown:: Allow apps to read or send messages
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more fine
  grained control of app access.

  .. gpo::    Disable apps access your messaging
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              App Privacy -->
              Let Windows apps access messaging
    :value0:  ☑, {ENABLED}
              Default for all apps, Force Deny
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1812-messaging
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable apps to access your messaging
    :path:     HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
    :value0:   LetAppsAccessMessaging, {DWORD}, 2
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1812-messaging
    :update:   2021-02-19
    :generic:
    :open:

    ``0`` enables apps access to messaging.

.. dropdown:: Turn off message sync
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  This is not available in the GUI.

  .. gpo::    Disable message sync
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Messaging -->
              Allow Message Service Cloud Sync
    :value0:  ☑, {DISABLED}
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1812-messaging
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable message sync
    :path:     HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\Messaging
    :value0:   AllowMessageSync, {DWORD}, 0
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1812-messaging
    :update:   2021-02-19
    :generic:
    :open:

    ``1`` enable message sync.
