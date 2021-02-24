.. _w10-1903-reasonable-privacy-account-info:

Account Info
############
:cmdmenu:`⌘ + r --> ms-settings:privacy-accountinfo`

.. dropdown:: Allow access to account info on this device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  This disables all account info value0s. See
  :ref:`Allow apps to access your account info <w10-1903-privacy-account-info>`
  to manage access on a per app basis.

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

  .. regedit:: Disable access to account info on this device
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
               CapabilityAccessManager\ConsentStore\userAccountInformation
    :value0:   Value, {SZ}, Deny
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#187-account-info
    :update:   2021-02-19
    :generic:
    :open:

    ``Allow`` to enable access to account info.

.. _w10-1903-privacy-account-info:

.. dropdown:: Allow apps to access your account info
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more fine
  grained control of app access.

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

  .. regedit:: Disable apps to access your account info
    :path:     HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
    :value0:   LetAppsAccessAccountInfo, {DWORD}, 2
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#187-account-info
    :update:   2021-02-19
    :generic:
    :open:

    ``0`` enables apps access to account info.
