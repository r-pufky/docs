.. _w10-20h2-settings-privacy-app-diagnostics:

App Diagnostics
###############
:cmdmenu:`⌘ + r --> ms-settings:privacy-appdiagnostics`

See :ref:`w10-determining-app-list` to generate a list of apps for more fine
grained control of app access.

Allow access to app diagnostic info on this device
**************************************************
.. dropdown:: Disable Allow access to app diagnostic info on this device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. gpo::    Disable Allow access to app diagnostic info on this device
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              App Privacy -->
              Let Windows apps access diagnostic information about other apps
    :value0:  ☑, {ENABLED}
    :value1:  Default for all apps, Force Deny
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1820-app-diagnostics
    :update:  2021-02-19
    :generic:
    :open:

    ``Allow`` enables.

  .. regedit:: Disable Allow access to app diagnostic info on this device
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
               CapabilityAccessManager\ConsentStore\appDiagnostics
    :value0:   Value, {SZ}, Deny
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1820-app-diagnostics
    :update:   2021-02-19
    :generic:
    :open:

Allow apps to access diagnostic info abour your other apps
**********************************************************
.. dropdown:: Disable Allow apps to access diagnostic info abour your other apps
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. gpo::    Disable Allow apps to access diagnostic info abour your other apps
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              App Privacy -->
              Let Windows apps access diagnostic information about other apps
    :value0:  ☑, {ENABLED}
    :value1:  Default for all apps, Force Deny
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1820-app-diagnostics
    :update:  2021-02-19
    :generic:
    :open:

    ``0`` enables.

  .. regedit:: Disable Allow apps to access diagnostic info abour your other apps
    :path:     HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
    :value0:   LetAppsGetDiagnosticInfo, {DWORD}, 2
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1820-app-diagnostics
    :update:  2021-02-19
    :generic:
    :open:

Chooose which apps can access diagnostic info about other apps
**************************************************************
See :ref:`w10-20h2-settings-privacy-app-diagnostics`.
