.. _w10-20h2-settings-privacy-other-devices:

Other Devices
#############
:cmdmenu:`⌘ + r --> ms-settings:privacy-customdevices`

See :ref:`w10-determining-app-list` to generate a list of apps for more fine
grained control of app access.

Communicate with unpaired devices
*********************************
.. dropdown:: Disable Communicate with unpaired devices
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Option is worded poorly. This prevents apps from sending data
  **automatically** to unpaired / other devices. It does not prevent all
  communication.

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Disable Communicate with unpaired devices
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
      :no_caption:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    ``0`` enables.

    .. wregedit:: Disable Communicate with unpaired devices
      :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
      :names:     LetAppsSyncWithDevices
      :types:     DWORD
      :data:      2
      :no_section:
      :no_caption:

  `Reference <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1815-other-devices>`__

Use trusted devices
*******************
.. dropdown:: Use trusted devices
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Option is worded poorly. This prevents apps from sending data
  **automatically** to **trusted** devices. It does not prevent all communication.

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Disable communication with unpaired devices
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
      :no_caption:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    ``0`` enables communication with unpaired trusted devices.

    .. wregedit:: Disable communication with unpaired trusted devices
      :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
      :names:     LetAppsAccessTrustedDevices
      :types:     DWORD
      :data:      2
      :no_section:
      :no_caption:

  `Reference <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1815-other-devices>`__
