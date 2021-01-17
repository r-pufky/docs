.. _w10-20h2-settings-privacy-eye-tracker:

Eye Tracker
###########
:cmdmenu:`⌘ + r --> ms-settings:privacy-eyetracker`

.. note::
  Only displayed in GUI if eye tracker device is present.

Allow access to eye tracker on this device
******************************************
.. dropdown:: Disable Allow access to eye tracker on this device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in
  :open:

  Disable eye tracking.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Disable Allow access to eye tracker on this device
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
