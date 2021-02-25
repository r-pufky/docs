.. _w10-20h2-settings-privacy-eye-tracker:

Eye Tracker
###########
:cmdmenu:`⌘ + r --> ms-settings:privacy-eyetracker`

.. note::
  Only displayed in GUI if eye tracker device is present.

Allow access to eye tracker on this device
******************************************
.. gpo::   Disable Allow access to eye tracker on this device
  :path:   Computer Configuration -->
           Administrative Templates -->
           Windows Components -->
           App Privacy -->
           Let Windows apps access an eye tracker device
  :value0: ☑, {ENABLED}
  :value1: Default for all apps, Force Deny
  :update: 2021-02-19
  :open:

  Disable eye tracking.
