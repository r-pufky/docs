.. _w10-20h2-settings-search-searching-windows:

Searching Windows
#################
.. dropdown:: Classic Find My Files
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  `Reference <https://www.tenforums.com/tutorials/120447-turn-off-enhanced-mode-search-indexer-windows-10-a.html>`_
    
  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    ``1`` enhanced.

    .. wregedit:: Classic Find My Files
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Search\Gather
                  Windows\SystemIndex
      :names:     EnableFindMyFiles
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

Indexer Performance
*******************
.. dropdown:: Enable Respect Device Power Mode Settings
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  `Reference <https://www.tenforums.com/tutorials/139198-turn-off-search-indexer-respect-device-power-mode-settings.html>`_
    
  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Enable Respect Device Power Mode Settings
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Search\Gather
                  Windows\SystemIndex
      :names:     RespectPowerModes
      :types:     DWORD
      :data:      1
      :no_section:
      :no_caption:
