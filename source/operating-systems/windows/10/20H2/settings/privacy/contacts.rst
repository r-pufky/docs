.. _w10-20h2-settings-privacy-contacts:

Contacts
########
:cmdmenu:`⌘ + r --> ms-settings:privacy-contacts`

See :ref:`w10-determining-app-list` to generate a list of apps for more fine
grained control of app access.

Allow access to contacts on this device
***************************************
.. dropdown:: Disable Allow access to contacts on this device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  This disables all contacts options. See
  :ref:`w10-20h2-settings-privacy-contacts-apps` to manage access on a per app
  basis.

  .. gpo::    Disable apps access your contacts
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              App Privacy -->
              Let Windows apps access contacts
    :value0:  ☑, {ENABLED}
    :value1:  Default for all apps, Force Deny
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#188-contacts
    :update:  2021-02-19
    :generic:
    :open:

    ``Allow`` enables access to contacts on this device.

  .. regedit:: Disable access to contacts on this device
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
               CapabilityAccessManager\ConsentStore\contacts
    :value0:   Value, {SZ}, Deny
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#188-contacts
    :update:   2021-02-19
    :generic:
    :open:

.. _w10-20h2-settings-privacy-contacts-apps:

Allow apps to access your contacts
**********************************
.. dropdown:: Disable Allow apps to access your contacts
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. gpo::    Disable apps access your contacts
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              App Privacy -->
              Let Windows apps access contacts
    :value0:  ☑, {ENABLED}
    :value1:  Default for all apps, Force Deny
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#188-contacts
    :update:  2021-02-19
    :generic:
    :open:

    ``0`` to enable app access to contacts.

  .. regedit:: Disable apps to access your contacts
    :path:     HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
    :value0:   LetAppsAccessContacts, {DWORD}, 2
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#188-contacts
    :update:   2021-02-19
    :generic:
    :open:

Choose which apps can access your contacts
******************************************
See :ref:`w10-20h2-settings-privacy-contacts-apps`
