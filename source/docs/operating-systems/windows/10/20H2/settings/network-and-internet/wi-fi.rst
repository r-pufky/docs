.. _w10-20h2-settings-network-and-internet-wi-fi:

Wi-Fi
#####
Wi-Fi `Sense removed in 20H2`_ due to privacy concerns.

Hotspot 2.0 networks
********************
.. regedit:: Disable let me use online sign-up to get connected
  :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WlanSvc\AnqpCache
  :value0:   OsuRegistrationStatus, {DWORD}, 0
  :ref:      https://www.tips-howto.com/tips-how-to-activate-hotspot-2-0-wi-fi-networks-in-windows-10/
  :update:   2021-02-19
  :open:

  Don't show a list of providers for hotspot connections.

.. _Sense removed in 20h2: https://threatpost.com/microsoft-quietly-kills-controversial-wi-fi-sense-feature/118124/
