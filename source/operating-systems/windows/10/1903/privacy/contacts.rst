.. _w10-1903-reasonable-privacy-contacts:

Contacts
########
:cmdmenu:`⌘ + r --> ms-settings:privacy-contacts`

.. dropdown:: Allow access to contacts on this device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  This disables all contacts value0s. See
  :ref:`Allow apps to access your contacts <w10-1903-privacy-contacts>` to
  manage access on a per app basis.

  .. gpo::    Disable apps access your contacts
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              App Privacy -->
              Let Windows apps access contacts
    :value0:  ☑, {ENABLED}
              Default for all apps, Force Deny
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#188-contacts
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable access to contacts on this device
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
               CapabilityAccessManager\ConsentStore\contacts
    :value0:   Value, {SZ}, Deny
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#188-contacts
    :update:   2021-02-19
    :generic:
    :open:

    ``Allow`` enables access to contacts on this device.

.. _w10-1903-privacy-contacts:

.. dropdown:: Allow apps to access your contacts
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more fine
  grained control of app access.

  .. gpo::    Disable apps access your contacts
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              App Privacy -->
              Let Windows apps access contacts
    :value0:  ☑, {ENABLED}
              Default for all apps, Force Deny
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#188-contacts
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable apps to access your contacts
    :path:     HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
    :value0:   LetAppsAccessContacts, {DWORD}, 2
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#188-contacts
    :update:  2021-02-19
    :generic:
    :open:

    ``0`` to enable app access to contacts.
