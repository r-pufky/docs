.. _w10-1903-reasonable-privacy-location:

Location
########
:cmdmenu:`⌘ + r --> ms-settings:privacy-location`

.. dropdown:: Allow access to location on this device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  This disables all location privacy (hardware) value0s. See
  :ref:`Allow apps to access your location <w10-1903-privacy-location>` to
  manage access on a per app basis.

  .. gpo::    Disable access to location on this device
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Location and Sensors -->
              Turn off location
    :value0:  ☑, {ENABLED}
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#182-location
    :update:  2021-02-19
    :generic:
    :open:

  .. gpo::    Disable Location sensors (hardware)
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Location and Sensors -->
              Turn off sensors
    :value0:  ☑, {ENABLED}
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#182-location
    :update:  2021-02-19
    :generic:
    :open:

  .. gpo::    Disable Location scripting (hardware)
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Location and Sensors -->
              Turn off location scripting
    :value0:  ☑, {ENABLED}
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#182-location
    :update:  2021-02-19
    :generic:
    :open:

  .. gpo::    Disable Location provider (hardware)
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Location and Sensors -->
              Windows Location Provider -->
              Turn off Windows Location Provider
    :value0:  ☑, {ENABLED}
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#182-location
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable access to location on this device
    :path:     HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\
               LocationAndSensors
    :value0:   DisableLocation, {DWORD}, 1
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#182-location

    :update:   2021-02-19
    :generic:
    :open:

    See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more
    fine grained control of app access.

  .. regedit:: Disable access to location on this device consentstore
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
               CapabilityAccessManager\ConsentStore\location
    :value0:   Value, {SZ}, Deny
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#182-location
    :update:   2021-02-19
    :generic:
    :open:

.. _w10-1903-privacy-location:

.. dropdown:: Allow apps to access your location
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Disable app access to location.

  .. gpo::    Disable apps to access your location
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              App Privacy -->
              Let Windows apps access location
    :value0:  ☑, {ENABLED}
              Default for all apps, Force Deny
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#182-location
    :update:  2021-02-19
    :generic:
    :open:
    
    See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more
    fine grained control of app access.

  .. regedit:: Disable apps to access your location
    :path:     HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
    :value0:   LetAppsAccessLocation, {DWORD}, 2
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#182-location
    :update:   2021-02-19
    :generic:
    :open:

    See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more
    fine grained control of app access.

    ``0`` enables location.
