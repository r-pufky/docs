.. _windows-10-reasonable-privacy-radios:

Radios
######
:cmdmenu:`⌘ + r --> ms-settings:privacy-radios`

Leave Radios enabled -- usually required for Bluetooth and wifi applications to
work properly. Disable all apps access to control radios.

.. rubric:: Allow access to radios on this device

.. wregedit:: Enable access to radios on this device via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
              CapabilityAccessManager\ConsentStore\radios
  :names:     Value
  :types:     SZ
  :data:      Allow
  :no_section:

.. rubric:: Allow apps to control device radios

.. wregedit:: Disable apps to access your radios via Registry
  :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
  :names:     LetAppsAccessRadios
  :types:     DWORD
  :data:      2
  :no_section:

    .. note::
      See :ref:`windows-10-privacy-app-list` to generate a list of apps for more
      fine grained control of app access.

.. wgpolicy:: Disable apps access your radios via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              App Privacy -->
              Let Windows apps control radios
  :option:    ☑,
              Default for all apps
  :setting:   Enabled,
              Force Deny
  :no_section:

    .. note::
      See :ref:`windows-10-privacy-app-list` to generate a list of apps for more
      fine grained control of app access.

.. rubric:: Rreferences

#. `Radios Windows Management Settings <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1814-radios>`_