.. _w10-21h2-settings-privacy-phone-calls:

Phone Calls
###########
:cmdmenu:`⌘ + r --> ms-settings:privacy-phonecalls`

.. note::
  Only displayed in GUI if phone device is present. Can still be disabled.

See :ref:`wbase-determining-app-list` to generate a list of apps for more fine
grained control of app access.

Allow phone calls on this device
********************************
.. dropdown:: Disable Allow phone calls on this device
  :color: primary
  :icon: shield-lock
  :animate: fade-in
  :class-container: sd-shadow-sm

  .. gpo::    Disable Allow phone calls on this device
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              App Privacy -->
              Let Windows apps make phone calls
    :value0:  ☑, {ENABLED}
    :value1:  Default for all apps, Force Deny
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1813-phone-calls
    :update:  2021-02-19
    :generic:
    :open:
