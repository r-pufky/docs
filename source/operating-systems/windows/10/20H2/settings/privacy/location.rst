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

  .. gpo::    Disable access to location on this device
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Location and Sensors -->
              Turn off location
    :value0:  ☑, {ENABLED}
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#182-location>
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable access to location on this device
    :path:     HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\
               LocationAndSensors
    :value0:   DisableLocation, {DWORD}, 1
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#182-location>
    :update:  2021-02-19
    :generic:
    :open:

.. _w10-20h2-settings-privacy-location-access:

Allow apps to access your location
**********************************
.. dropdown:: Disable Allow apps to access your location
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Disable apps access to location.

  .. gpo::    Disable apps to access your location
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              App Privacy -->
              Let Windows apps access location
    :value0:  ☑, {ENABLED}
    :value1:  Default for all apps, Force Deny
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#182-location
    :update:  2021-02-19
    :generic:
    :open:

    ``0`` enables location.

  .. regedit:: Disable apps to access your location
    :path:     HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
    :value0:   LetAppsAccessLocation, {DWORD}, 2
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#182-location
    :update:   2021-02-19
    :generic:
    :open:

Allow desktop apps to access your location
******************************************
.. regedit:: Disable Allow desktop apps to access your location
  :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion
             CapabilityAccessManager\ConsentStore\location
  :value0:   Value, {SZ}, Deny
  :ref:      https://www.tenforums.com/tutorials/138191-turn-off-location-access-desktop-apps-windows-10-a.html
  :update:   2021-02-19

  Disable desktop apps access to location. ``Allow`` enables location.
