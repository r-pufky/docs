.. _w10-1903-reasonable-privacy-app-diagnostics:

App Diagnostics
###############
:cmdmenu:`⌘ + r --> ms-settings:privacy-appdiagnostics`

.. dropdown:: Allow access to app diagnostic info on this device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. gpo::    Disable apps to access diagnostic info abour your other apps
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              App Privacy -->
              Let Windows apps access diagnostic information about other apps
    :value0:  ☑, {ENABLED}
              Default for all apps, Force Deny
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1820-app-diagnostics
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable access to app diagnostics on this device
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
               CapabilityAccessManager\ConsentStore\appDiagnostics
    :value0:   Value, {SZ}, Deny
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1820-app-diagnostics
    :update:   2021-02-19
    :generic:
    :open:

    ``Allow`` enables access to app diagnostics.

.. dropdown:: Allow apps to access diagnostic info abour your other apps
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more fine
  grained control of app access.

  .. gpo::    Disable apps to access diagnostic info abour your other apps
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              App Privacy -->
              Let Windows apps access diagnostic information about other apps
    :value0:  ☑, {ENABLED}
              Default for all apps, Force Deny
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1820-app-diagnostics
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable apps to access diagnostic info abour your other apps
    :path:     HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
    :value0:   LetAppsGetDiagnosticInfo, {DWORD}, 2
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1820-app-diagnostics
    :update:   2021-02-19
    :generic:
    :open:

    ``0`` enables apps access to diagnostic info.
