.. _w10-20h2-settings-apps-offline-maps:

Offline maps
############
.. regedit:: Disable Metered connections
  :path:     HKEY_LOCAL_MACHINE\SYSTEM\Maps
  :value0:   UpdateOnlyOnWifi, {DWORD}, 1
  :ref:      https://www.tenforums.com/tutorials/83220-turn-off-download-maps-over-metered-connections-windows-10-a.html
  :update:   2021-02-19

.. dropdown:: Disable Automatically update maps
  :color: primary
  :icon: note
  :animate: fade-in
  :class-container: sd-shadow-sm

  .. gpo::    Disable Automatically update maps
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Maps -->
              Turn off Automatic Download and Update of Map Data
    :value0:  ☑, {ENABLED}
    :ref:     https://www.tenforums.com/tutorials/106248-enable-disable-automatic-updates-offline-maps-windows-10-a.html
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable Automatically update maps
    :path:     KEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Maps
    :value0:   AutoDownloadAndUpdateMapData, {DWORD}, 0
    :ref:      https://www.tenforums.com/tutorials/106248-enable-disable-automatic-updates-offline-maps-windows-10-a.html
    :update:   2021-02-19
    :generic:
    :open:
