.. _w10-20h2-settings-privacy-account-info:

Account Info
############
:cmdmenu:`⌘ + r --> ms-settings:privacy-accountinfo`

See :ref:`w10-determining-app-list` to generate a list of apps for more fine
grained control of app access.

Allow access to account info on this device
*******************************************
.. dropdown:: Disable Allow access to account info on this device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  This disables all account info options. See
  :ref:`w10-20h2-settings-privacy-account-info-apps` to manage access on a per
  app basis.

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

    ``Allow`` to enable access to account info.

  .. regedit:: Disable access to account info on this device
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
               CapabilityAccessManager\ConsentStore\userAccountInformation
    :value0:   Value, {SZ}, Deny
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#187-account-info
    :update:   2021-02-19
    :generic:
    :open:

.. _w10-20h2-settings-privacy-account-info-apps:

Allow apps to access your account info
**************************************
.. dropdown:: Disable Allow apps to access your account info
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

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

Choose which apps can access your account info
**********************************************
See :ref:`w10-20h2-settings-privacy-account-info-apps`.
