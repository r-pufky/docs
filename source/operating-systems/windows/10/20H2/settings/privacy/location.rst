.. _w10-20h2-settings-privacy-location:

Location
########
:cmdmenu:`⌘ + r --> ms-settings:privacy-location`

See :ref:`w10-determining-app-list` to generate a list of apps for more fine
grained control of app access.

Allow access to location on this device
***************************************
.. dropdown:: Disable Allow access to location on this device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  This disables all location privacy (hardware) options. See
  :ref:`Allow apps to access your location <w10-20h2-settings-privacy-location-access>`
  to manage access on a per app basis.

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

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

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Disable access to location on this device
      :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\
                  LocationAndSensors
      :names:     DisableLocation
      :types:     DWORD
      :data:      1
      :no_section:
      :no_caption:

  `Reference <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#182-location>`__

.. _w10-20h2-settings-privacy-location-access:

Allow apps to access your location
**********************************
.. dropdown:: Disable Allow apps to access your location
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Disable apps access to location. 

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:
    
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

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    ``0`` enables location.

    .. wregedit:: Disable apps to access your location
      :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
      :names:     LetAppsAccessLocation
      :types:     DWORD
      :data:      2
      :no_section:
      :no_caption:

  `Reference <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#182-location>`__

Allow desktop apps to access your location
******************************************
.. dropdown:: Disable Allow desktop apps to access your location
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Disable desktop apps access to location. 

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    ``Allow`` enables location.

    .. wregedit:: Disable desktop apps to access your location
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion
                  CapabilityAccessManager\ConsentStore\location
      :names:     Value
      :types:     SZ
      :data:      Deny
      :no_section:
      :no_caption:

  `Reference <https://www.tenforums.com/tutorials/138191-turn-off-location-access-desktop-apps-windows-10-a.html>`__
