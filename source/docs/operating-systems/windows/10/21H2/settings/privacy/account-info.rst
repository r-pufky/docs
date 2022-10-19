.. _w10-21h2-settings-privacy-account-info:

Account Info
############
:cmdmenu:`⌘ + r --> ms-settings:privacy-accountinfo`

See :ref:`wbase-determining-app-list` to generate a list of apps for more fine
grained control of app access.

Allow access to account info on this device
*******************************************
.. dropdown:: Disable Allow access to account info on this device
  :color: primary
  :icon: shield-lock
  :animate: fade-in
  :class-container: sd-shadow-sm

  This disables all account info options.

  .. gpo::    Disable apps access your account info
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              App Privacy -->
              Let Windows apps access account information
    :value0:  ☑, {ENABLED}
    :value1:  Default for all apps, Force Deny
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#187-account-info
    :update:  2021-02-19
    :generic:
    :open:
