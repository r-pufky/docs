.. _w10-1903-reasonable-privacy-location:

Location
########
:cmdmenu:`⌘ + r --> ms-settings:privacy-location`

.. dropdown:: Allow access to location on this device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  This disables all location privacy (hardware) options. See
  :ref:`Allow apps to access your location <w10-1903-privacy-location>` to
  manage access on a per app basis.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more
    fine grained control of app access.

    .. wregedit:: Disable access to location on this device
      :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\
                  LocationAndSensors
      :names:     DisableLocation
      :types:     DWORD
      :data:      1
      :no_section:
      :no_caption:

    .. wregedit:: Disable access to location on this device consentstore
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
                  CapabilityAccessManager\ConsentStore\location
      :names:     Value
      :types:     SZ
      :data:      Deny
      :no_section:
      :no_caption:
      :no_launch:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

    .. wgpolicy:: Disable access to location on this device
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Location and Sensors -->
                  Turn off location
      :option:    ☑
      :setting:   Enabled
      :no_section:
      :no_caption:

    .. wgpolicy:: Disable Location sensors (hardware)
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Location and Sensors -->
                  Turn off sensors
      :option:    ☑
      :setting:   Enabled
      :no_section:
      :no_caption:
      :no_launch:

    .. wgpolicy:: Disable Location scripting (hardware)
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Location and Sensors -->
                  Turn off location scripting
      :option:    ☑
      :setting:   Enabled
      :no_section:
      :no_caption:
      :no_launch:

    .. wgpolicy:: Disable Location provider (hardware)
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Location and Sensors -->
                  Windows Location Provider -->
                  Turn off Windows Location Provider
      :option:    ☑
      :setting:   Enabled
      :no_section:
      :no_caption:
      :no_launch:

.. _w10-1903-privacy-location:

.. dropdown:: Allow apps to access your location
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Disable app access to location.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more
    fine grained control of app access.

    ``0`` enables location.

    .. wregedit:: Disable apps to access your location
      :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
      :names:     LetAppsAccessLocation
      :types:     DWORD
      :data:      2
      :no_section:
      :no_caption:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    
    See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more
    fine grained control of app access.

    .. wgpolicy:: Disable apps to access your location
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
      :no_caption:

.. rubric:: Rreferences

#. `Location Windows Management Settings <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#182-location>`_
