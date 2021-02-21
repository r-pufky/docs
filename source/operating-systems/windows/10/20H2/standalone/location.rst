.. _w10-20h2-standalone-privacy-location:

Location
########
:cmdmenu:`⌘ + r --> ms-settings:privacy-location`

These location options are not in the GUI. See
:ref:`w10-20h2-settings-privacy-location` for GUI options.

.. dropdown:: Allow access to location on this device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in
  :open:

  This disables all location privacy (hardware) options. See
  :ref:`w10-20h2-settings-privacy-location-access` to manage access on a per app
  basis.

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

  `Reference <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#182-location>`__
