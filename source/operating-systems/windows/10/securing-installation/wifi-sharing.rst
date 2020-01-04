.. _windows-10-disable-wifi-sharing:

`Disable Wifi Sharing`_
#######################
Wifi Sharing (Sense) will automatically make connections to Wifi Networks via
crowdsharing and identified hotspots. Disable this.

:term:`Registry`
****************
.. wregedit:: Disable Wifi Sharing (Sense) via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WcmSvc\wifinetworkmanager\config
  :names:     AutoConnectAllowedOEM
  :types:     DWORD
  :data:      0
  :no_section:

  .. note::
    :cmdmenu:`⌘ + r --> ms-settings:network --> manage wifi settings`

      * ☐ all for sharing.

:term:`GPO`
***********
.. wgpolicy:: Disable Wifi Sharing (Sense) via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Network -->
              WLAN Service -->
              WLAN Settings -->
              Allow Windows to automatically connect to suggested open hotspots, to networks shared by contacts, and to hotspots offering paid services
  :option:    ☑
  :setting:   Disabled
  :no_section:

.. rubric:: References

#. `Wifi Sharing Settings <https://docs.microsoft.com/en-us/windows/client-management/mdm/policy-csp-wifi>`_

.. _Disable Wifi Sharing: https://www.thewindowsclub.com/disable-wi-fi-sense-windows-10-enterprise
