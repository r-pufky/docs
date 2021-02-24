.. _w10-1903-reasonable-privacy-eye-tracker:

Eye Tracker
###########
:cmdmenu:`⌘ + r --> ms-settings:privacy-eyetracker`

.. gpo::   Disable access to eye tracker on this device
  :path:   Computer Configuration -->
           Administrative Templates -->
           Windows Components -->
           App Privacy -->
           Let Windows apps access an eye tracker device
  :value0: ☑, {ENABLED}
  :value1: Default for all apps, Force Deny
  :update: 2021-02-19

  Only displayed in GUI if eye tracker is installed. Can still be disabled.
