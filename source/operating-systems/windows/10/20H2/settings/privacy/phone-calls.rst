.. _w10-20h2-settings-privacy-phone-calls:

Phone Calls
###########
:cmdmenu:`⌘ + r --> ms-settings:privacy-phonecalls`

.. note::
  Only displayed in GUI if phone device is present. Can still be disabled.

See :ref:`w10-determining-app-list` to generate a list of apps for more fine
grained control of app access.

Allow phone calls on this device
********************************
.. dropdown:: Disable Allow phone calls on this device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

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

  .. regedit:: Disable Allow phone calls on this device
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
               CapabilityAccessManager\ConsentStore\phoneCall
    :value0:   Value, {SZ}, Deny
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1813-phone-calls
    :update:   2021-02-19
    :generic:
    :open:

    ``Allow`` enables.

Allow apps to make phone calls
******************************
.. dropdown:: Disable Allow apps to make phone calls
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. gpo::    Disable Allow apps to make phone calls
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

  .. regedit:: Disable Allow apps to make phone calls
    :path:i    HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
    :value0:   LetAppsAccessPhone, {DWORD}, 2
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1813-phone-calls
    :update:   2021-02-19
    :generic:
    :open:

    ``0`` enable apps to make phone calls.

Choose which apps can make phone calls
**************************************
See :ref:`w10-20h2-settings-privacy-phone-calls`.
