.. _w10-1903-reasonable-privacy-other-devices:

Other Devices
#############
:cmdmenu:`⌘ + r --> ms-settings:privacy-customdevices`

.. dropdown:: Communicate with unpaired devices
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Option is worded poorly. This prevents apps from sending data
  **automatically** to unpaired / other devices. It does not prevent all
  communication.

  See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more fine
  grained control of app access.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    ``0`` enables communication with unpaired devices.

    .. wregedit:: Disable communication with unpaired devices
      :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
      :names:     LetAppsSyncWithDevices
      :types:     DWORD
      :data:      2
      :no_section:
      :no_caption:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

    .. wgpolicy:: Disable communication with unpaired devices
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

.. dropdown:: Use trusted devices
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Option is worded poorly. This prevents apps from sending data
  **automatically** to trusted devices. It does not prevent all communication.

  See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more fine
  grained control of app access.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    ``0`` enables communication with unpaired trusted devices.

    .. wregedit:: Disable communication with unpaired trusted devices
      :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
      :names:     LetAppsAccessTrustedDevices
      :types:     DWORD
      :data:      2
      :no_section:
      :no_caption:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

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

.. rubric:: Rreferences

#. `Other Devices Windows Management Settings <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1815-other-devices>`_
