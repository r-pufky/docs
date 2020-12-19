.. _w10-1903-reasonable-privacy-motion:

Motion
######
:cmdmenu:`⌘ + r --> ms-settings:privacy-motion`

.. note::
  Only displayed in GUI if motion detection device is present (e.g. phone,
  pedometer, etc.). Can still be disabled.

.. dropdown:: Let Windows and your apps use your motion data and collect motion
              history
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in
  :open:

  Disable access to motion data.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    ``0`` enable apps usage of motion data.

    .. wregedit:: Disable apps use your motion data and collect motion history
      :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
      :names:     LetAppsAccessMotion
      :types:     DWORD
      :data:      2
      :no_section:
      :no_caption:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

    .. wgpolicy:: Disable apps use your motion data and collect motion history
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  App Privacy -->
                  Let Windows apps access motion
      :option:    ☑,
                  Default for all apps
      :setting:   Enabled,
                  Force Deny
      :no_section:
      :no_caption:

.. rubric:: Rreferences

#. `Motion Windows Management Settings <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1818-motion>`_
