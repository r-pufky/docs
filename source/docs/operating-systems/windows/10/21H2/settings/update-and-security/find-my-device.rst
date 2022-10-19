.. _w10-21h2-settings-update-and-security-find-my-device:

Find my device
##############
.. dropdown:: Disable Find my device
  :color: primary
  :icon: shield-lock
  :animate: fade-in
  :class-container: sd-shadow-sm
  :open:

  GPS information is uploaded to Microsoft if enabled.

  .. gpo::    Disable Find my device
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Find My Device -->
              Turn On/Off Find My Device
    :value0:  ☑, {DISABLED}
    :ref:     https://www.tenforums.com/tutorials/28946-turn-off-find-my-device-windows-10-a.html
    :update:  2021-02-19
    :generic:
    :open:
