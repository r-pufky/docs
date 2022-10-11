.. _w10-21h2-standalone-privacy-location:

Location
########
:cmdmenu:`⌘ + r --> ms-settings:privacy-location`

These location values are not in the GUI. See
:ref:`w10-21h2-settings-privacy-location` for GUI value0s.

.. dropdown:: Allow access to location on this device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in
  :open:

  This disables all location privacy (hardware) options. See
  :ref:`w10-21h2-settings-privacy-location-access` to manage access on a per app
  basis.

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
