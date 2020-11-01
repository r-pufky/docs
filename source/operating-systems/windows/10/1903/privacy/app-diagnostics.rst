.. _w10-1903-reasonable-privacy-app-diagnostics:

App Diagnostics
###############
:cmdmenu:`⌘ + r --> ms-settings:privacy-appdiagnostics`

.. rubric:: Allow access to app diagnostic info on this device

.. wregedit:: Disable access to app diagnostics on this device via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
              CapabilityAccessManager\ConsentStore\appDiagnostics
  :names:     Value
  :types:     SZ
  :data:      Deny
  :no_section:

.. rubric:: Allow apps to access diagnostic info abour your other apps

.. wregedit:: Disable apps to access diagnostic info abour your other apps via
              Registry
  :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
  :names:     LetAppsGetDiagnosticInfo
  :types:     DWORD
  :data:      2
  :no_section:

    .. note::
      See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more
      fine grained control of app access.

.. wgpolicy:: Disable apps to access diagnostic info abour your other apps via
              machine GPO
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

    .. note::
      See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more
      fine grained control of app access.

.. rubric:: Rreferences

#. `App Diagnostics Windows Management Settings <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1820-app-diagnostics>`_