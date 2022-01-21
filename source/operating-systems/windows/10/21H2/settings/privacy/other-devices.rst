.. _w10-21h2-settings-privacy-other-devices:

Other Devices
#############
:cmdmenu:`⌘ + r --> ms-settings:privacy-customdevices`

See :ref:`wbase-determining-app-list` to generate a list of apps for more fine
grained control of app access.

Communicate with unpaired devices
*********************************
.. dropdown:: Disable Communicate with unpaired devices
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  value0 is worded poorly. This prevents apps from sending data
  **automatically** to unpaired / other devices. It does not prevent all
  communication.

  .. gpo::    Disable Communicate with unpaired devices
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              App Privacy -->
              Let Windows apps communicate with unpaired devices
    :value0:  ☑, {ENABLED}
    :value1:  Default for all apps, Force Deny
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1815-other-devices
    :update:  2021-02-19
    :generic:
    :open:

Use trusted devices
*******************
.. dropdown:: Use trusted devices
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. gpo:: Disable communication with unpaired devices
    :path: Computer Configuration -->
                Administrative Templates -->
                Windows Components -->
                App Privacy -->
                Let Windows apps access trusted devices
    :value0:    ☑, {ENABLED}
    :value1:    Default for all apps, Force Deny
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1815-other-devices
    :update: 2021-02-19
    :generic:
    :open:

    Option is worded poorly. This prevents apps from sending data
    **automatically** to **trusted** devices. It does not prevent all
    communication.
