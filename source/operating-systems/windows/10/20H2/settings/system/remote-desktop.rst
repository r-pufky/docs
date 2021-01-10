.. _w10-20h2-settings-system-remote-desktop:

Remote Desktop
##############
.. dropdown:: Disable Remote Desktop
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in
  :open:

  Remote desktop is easily exploited and should never be enabled.
  
  `Reference <https://www.tenforums.com/tutorials/92433-enable-disable-remote-desktop-connections-windows-10-pc.html>`_

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Disable Remote Desktop
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Remote Desktop Services -->
                  Remote Desktop Session Host -->
                  Connections -->
                  Allow users to connect remotely by using Remote Desktop Services
      :option:    ☑
      :setting:   Disabled
      :no_section:
      :no_caption:

    .. wgpolicy:: Require network authentication
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Remote Desktop Services -->
                  Remote Desktop Session Host -->
                  Security -->
                  Require user authentication for remote connections by using network level authentication
      :option:    ☑
      :setting:   Enabled
      :no_section:
      :no_caption:
      :no_launch:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Disable Remote Desktop
      :key_title: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\
                  Terminal Server
      :names:     fDenyTSConnections
      :types:     DWORD
      :data:      1
      :no_section:
      :no_caption:
    
    .. wregedit:: Require network authentication
      :key_title: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\
                  Terminal Server\WinStations\RDP-Tcp
      :names:     UserAuthentication
      :types:     DWORD
      :data:      1
      :no_section:
      :no_caption:
      :no_launch:
