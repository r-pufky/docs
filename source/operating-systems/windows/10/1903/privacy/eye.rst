.. _w10-1903-reasonable-privacy-eye:

Eye Tracker
###########
:cmdmenu:`⌘ + r --> ms-settings:privacy-eyetracker`

.. note::
  Only displayed in GUI if eye tracker is installed. Can still be disabled.

.. rubric:: Allow access to eye tracker on this device

.. wgpolicy:: Disable access to eye tracker on this device via machine GPO
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
  :no_launch: