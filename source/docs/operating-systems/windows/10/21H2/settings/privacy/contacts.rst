.. _w10-21h2-settings-privacy-contacts:

Contacts
########
:cmdmenu:`⌘ + r --> ms-settings:privacy-contacts`

See :ref:`wbase-determining-app-list` to generate a list of apps for more fine
grained control of app access.

Allow access to contacts on this device
***************************************
.. dropdown:: Disable Allow access to contacts on this device
  :color: primary
  :icon: shield-lock
  :animate: fade-in
  :class-container: sd-shadow-sm

  This disables all contacts options.

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
