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

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Disable Allow access to app diagnostic info on this device
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  App Privacy -->
                  Let Windows apps access diagnostic information about other apps
      :option:    ☑,
                  Default for all apps
      :setting:   Enabled,
                  Force Deny
      :no_section:
      :no_caption:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    ``Allow`` enables.

    .. wregedit:: Disable Allow access to app diagnostic info on this device
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
                  CapabilityAccessManager\ConsentStore\appDiagnostics
      :names:     Value
      :types:     SZ
      :data:      Deny
      :no_section:
      :no_caption:
  
  `Reference <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1820-app-diagnostics>`__

Allow apps to access diagnostic info abour your other apps
**********************************************************
.. dropdown:: Disable Allow apps to access diagnostic info abour your other apps
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Disable Allow apps to access diagnostic info abour your other apps
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  App Privacy -->
                  Let Windows apps access diagnostic information about other apps
      :option:    ☑,
                  Default for all apps
      :setting:   Enabled,
                  Force Deny
      :no_section:
      :no_caption:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    ``0`` enables.

    .. wregedit:: Disable Allow apps to access diagnostic info abour your other apps
      :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
      :names:     LetAppsGetDiagnosticInfo
      :types:     DWORD
      :data:      2
      :no_section:
      :no_caption:

  `Reference <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1820-app-diagnostics>`__

Chooose which apps can access diagnostic info about other apps
**************************************************************
See :ref:`w10-20h2-settings-privacy-app-diagnostics`.
