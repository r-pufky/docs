.. _w10-20h2-settings-update-and-security-find-my-device:

Find my device
##############
.. dropdown:: Disable Find my device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in
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

  .. regedit:: Disable delivery optimization
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Settings\FindMyDevice
    :value0:   LocationSyncEnabled, {DWORD}, 0
    :ref:      https://www.tenforums.com/tutorials/28946-turn-off-find-my-device-windows-10-a.html
    :update:   2021-02-19
    :generic:
    :open:
