.. _w10-21h2-settings-network-and-internet-wi-fi:

Wi-Fi
#####
Hotspot 2.0 networks
********************
.. regedit:: Disable let me use online sign-up to get connected
  :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WlanSvc\AnqpCache
  :value0:   OsuRegistrationStatus, {DWORD}, 0
  :ref:      https://www.tips-howto.com/tips-how-to-activate-hotspot-2-0-wi-fi-networks-in-windows-10/
  :update:   2021-02-19
  :open:

  Don't show a list of providers for hotspot connections.

.. gpo::    Disable Wi-Fi Sense
  :path:    Computer Configuration -->
            Administrative Templates -->
            Network -->
            WLAN Service -->
            WLAN Settings -->
            Allow Windows to automatically connect to suggested open hotspots, to networks shared by contacts, and to hotspots offering paid services
  :value0:  ☑, {DISABLED}
  :ref:     https://docs.microsoft.com/en-us/windows/configuration/manage-wifi-sense-in-enterprise
  :update:  2022-01-20
  :generic:
  :open:
