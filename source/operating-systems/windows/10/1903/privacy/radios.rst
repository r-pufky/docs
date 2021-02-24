.. _w10-1903-reasonable-privacy-radios:

Radios
######
:cmdmenu:`⌘ + r --> ms-settings:privacy-radios`

Leave radios enabled -- usually required for Bluetooth and Wifi applications to
work properly. Disable all apps access to control radios; Windows controls will
still work to manage radios.

.. dropdown:: Allow access to radios on this device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

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

  .. regedit:: Enable access to radios on this device
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
               CapabilityAccessManager\ConsentStore\radios
    :value0:   Value, {SZ}, Allow
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1814-radios
    :update:   2021-02-19
    :generic:
    :open:

    ``Deny`` disables access to radios on this device.

.. dropdown:: Allow apps to control device radios
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more fine
  grained control of app access.

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

  .. regedit:: Disable apps to access your radios
    :path:     HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
    :value0:   LetAppsAccessRadios, {DWORD}, 2
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1814-radios
    :update:   2021-02-19
    :generic:
    :open:

    ``0`` enables apps access to radios.
