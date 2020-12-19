.. _w10-1903-reasonable-privacy-eye-tracker:

Eye Tracker
###########
:cmdmenu:`⌘ + r --> ms-settings:privacy-eyetracker`

.. dropdown:: Allow access to eye tracker on this device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in
  :open:

  Only displayed in GUI if eye tracker is installed. Can still be disabled.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wgpolicy:: Disable access to eye tracker on this device
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  App Privacy -->
                  Let Windows apps access an eye tracker device
      :option:    ☑,
                  Default for all apps
      :setting:   Enabled,
                  Force Deny
      :no_section:
      :no_caption:
