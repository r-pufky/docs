.. _w10-20h2-settings-privacy-radios:

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
  :color: primary
  :icon: note
  :animate: fade-in
  :class-container: sd-shadow-sm

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

    ``Allow`` enables.

  .. regedit:: Disable Allow access to radios on this device
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
               CapabilityAccessManager\ConsentStore\radios
    :value0:   Value, {SZ}, Deny
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1814-radios
    :update:   2021-02-19
    :generic:
    :open:

Allow apps to control device radios
***********************************
.. dropdown:: Allow apps to control device radios
  :color: primary
  :icon: note
  :animate: fade-in
  :class-container: sd-shadow-sm

  .. gpo::    Disable apps access your radios
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

    ``0`` enables apps access to radios.

  .. regedit:: Disable apps to access your radios
    :path:     HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
    :value0:   LetAppsAccessRadios, {DWORD}, 2
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1814-radios
    :update:   2021-02-19
    :generic:
    :open:

Choose which apps can control your device radios
************************************************
See :ref:`w10-20h2-settings-privacy-radios`.
