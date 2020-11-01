.. _w10-1903-reasonable-privacy-location:

Location
########
:cmdmenu:`⌘ + r --> ms-settings:privacy-location`

.. rubric:: Allow access to location on this device

.. note::
  This disables all location privacy (hardware) options. See
  :ref:`w10-1903-privacy-location` to manage access on a per app basis.

.. wregedit:: Disable access to location on this device via Registry
  :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\
              LocationAndSensors
  :names:     DisableLocation
  :types:     DWORD
  :data:      1
  :no_section:

.. wregedit:: Disable access to location on this device consentstore via
              Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
              CapabilityAccessManager\ConsentStore\location
  :names:     Value
  :types:     SZ
  :data:      Deny
  :no_section:
  :no_launch:

    .. note::
      See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more
      fine grained control of app access.

.. wgpolicy:: Disable access to location on this device via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Location and Sensors -->
              Turn off location
  :option:    ☑
  :setting:   Enabled
  :no_section:

    .. wgpolicy:: Disable Location sensors (hardware) via machine GPO
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Location and Sensors -->
                  Turn off sensors
      :option:    ☑
      :setting:   Enabled
      :no_section:
      :no_launch:

    .. wgpolicy:: Disable Location scripting (hardware) via machine GPO
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Location and Sensors -->
                  Turn off location scripting
      :option:    ☑
      :setting:   Enabled
      :no_section:
      :no_launch:

    .. wgpolicy:: Disable Location provider (hardware) via machine GPO
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Location and Sensors -->
                  Windows Location Provider
                  Turn off Windows Location Provider
      :option:    ☑
      :setting:   Enabled
      :no_section:
      :no_launch:

.. _w10-1903-privacy-location:

.. rubric:: Allow apps to access your location

.. wregedit:: Disable apps to access your location via Registry
  :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
  :names:     LetAppsAccessLocation
  :types:     DWORD
  :data:      2
  :no_section:

    .. note::
      See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more
      fine grained control of app access.

.. wgpolicy:: Disable apps to access your location via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              App Privacy -->
              Let Windows apps access location
  :option:    ☑,
              Default for all apps
  :setting:   Enabled,
              Force Deny
  :no_section:

    .. note::
      See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more
      fine grained control of app access.

.. rubric:: Rreferences

#. `Location Windows Management Settings <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#182-location>`_
