.. _w10-21h2-settings-search-searching-windows:

Searching Windows
#################
.. regedit:: Classic Find My Files
  :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Search\Gather
             Windows\SystemIndex
  :value0:   EnableFindMyFiles, {DWORD}, 0
  :ref:      https://www.tenforums.com/tutorials/120447-turn-off-enhanced-mode-search-indexer-windows-10-a.html
  :update:   2021-02-19

  ``1`` enhanced.

Indexer Performance
*******************
.. regedit:: Enable Respect Device Power Mode Settings
  :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Search\Gather
             Windows\SystemIndex
  :value0:   RespectPowerModes, {DWORD}, 1
  :ref:      https://www.tenforums.com/tutorials/139198-turn-off-search-indexer-respect-device-power-mode-settings.html
  :update:   2021-02-19
