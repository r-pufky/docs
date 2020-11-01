.. _w10-1903-reasonable-privacy-other-devices:

Other Devices
#############
:cmdmenu:`⌘ + r --> ms-settings:privacy-customdevices`

.. rubric:: Communicate with unpaired devices

.. note::
  Option is worded poorly. This prevents apps from sending data
  **automatically** to unpaired / other devices.

.. wregedit:: Disable communication with unpaired devices via Registry
  :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
  :names:     LetAppsSyncWithDevices
  :types:     DWORD
  :data:      2
  :no_section:

    .. note::
      See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more
      fine grained control of app access.

.. wgpolicy:: Disable communication with unpaired devices via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              App Privacy -->
              Let Windows apps communicate with unpaired devices
  :option:    ☑,
              Default for all apps
  :setting:   Enabled,
              Force Deny
  :no_section:

    .. note::
      See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more
      fine grained control of app access.

.. rubric:: Use trusted devices

.. note::
  Option is worded poorly. This prevents apps from sending data
  **automatically** to trusted devices.

.. wregedit:: Disable communication with unpaired devices via Registry
  :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
  :names:     LetAppsAccessTrustedDevices
  :types:     DWORD
  :data:      2
  :no_section:

    .. note::
      See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more
      fine grained control of app access.

.. wgpolicy:: Disable communication with unpaired devices via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              App Privacy -->
              Let Windows apps access trusted devices
  :option:    ☑,
              Default for all apps
  :setting:   Enabled,
              Force Deny
  :no_section:

    .. note::
      See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more
      fine grained control of app access.

.. rubric:: Rreferences

#. `Other Devices Windows Management Settings <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1815-other-devices>`_