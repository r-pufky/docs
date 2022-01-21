.. _w10-21h2-settings-privacy-radios:

Radios
######
:cmdmenu:`⌘ + r --> ms-settings:privacy-radios`

Applies to non-OS application controlling radios. Bluetooth and Wifi system
controls will still work properly. Disable all apps access to control radios.

See :ref:`wbase-determining-app-list` to generate a list of apps for more fine
grained control of app access.

Allow access to radios on this device
*************************************
.. dropdown:: Disable Allow access to radios on this device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. gpo::    Disable Allow access to radios on this device
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              App Privacy -->
              Let Windows apps control radios
    :value0:  ☑, {ENABLED}
    :value1:  Default for all apps, Force Deny
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1814-radios
    :update:  2021-02-19
    :generic:
    :open:
