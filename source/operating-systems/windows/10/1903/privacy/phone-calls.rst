.. _w10-1903-reasonable-privacy-phone-calls:

Phone Calls
###########
:cmdmenu:`⌘ + r --> ms-settings:privacy-phonecalls`

.. note::
  Only displayed in GUI if phone device is present. Can still be disabled.

.. dropdown:: Allow phone calls on this device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more fine
  grained control of app access.

  .. gpo::    Disable apps make phone calls
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

  .. regedit:: Disable apps make phone calls
    :path:     HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
    :value0:   LetAppsAccessPhone, {DWORD}, 2
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1813-phone-calls
    :update:   2021-02-19
    :generic:
    :open:

    ``0`` enable apps to make phone calls.

.. regedit:: Disable consent for phone calls
  :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
             CapabilityAccessManager\ConsentStore\phoneCall
  :value0:   Value, {SZ}, Deny
  :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1813-phone-calls
  :update:   2021-02-19

  See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more fine
  grained control of app access.

  ``Allow`` enable consent for phone calls.

