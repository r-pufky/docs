.. _w10-20h2-settings-update-and-security-find-my-device:

Find my device
##############
.. dropdown:: Disable Find my device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in
  :open:
  
  GPS information is uploaded to Microsoft if enabled.
    
  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Disable Find my device
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Find My Device -->
                  Turn On/Off Find My Device
      :option:    ☑
      :setting:   Disabled
      :no_section:
      :no_caption:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Disable delivery optimization
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Settings\FindMyDevice
      :names:     LocationSyncEnabled
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

  `Reference <https://www.tenforums.com/tutorials/28946-turn-off-find-my-device-windows-10-a.html>`__
