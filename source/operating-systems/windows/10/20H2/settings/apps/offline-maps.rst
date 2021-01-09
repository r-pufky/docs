.. _w10-20h2-offline-maps:

Offline maps
############
.. dropdown:: Disable Metered connections
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in
  
  `Reference <https://www.tenforums.com/tutorials/83220-turn-off-download-maps-over-metered-connections-windows-10-a.html>`_
    
  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Disable Metered connections
      :key_title: HKEY_LOCAL_MACHINE\SYSTEM\Maps
      :names:     UpdateOnlyOnWifi
      :types:     DWORD
      :data:      1
      :no_section:
      :no_caption:

.. dropdown:: Disable Automatically update maps
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in
  :open:
  
  `Reference <https://www.tenforums.com/tutorials/106248-enable-disable-automatic-updates-offline-maps-windows-10-a.html>`_
    
  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Disable Automatically update maps
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Maps -->
                  Turn off Automatic Download and Update of Map Data
      :option:    ☑
      :setting:   Enabled
      :no_section:
      :no_caption:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Disable Automatically update maps
      :key_title: KEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Maps
      :names:     AutoDownloadAndUpdateMapData
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:
