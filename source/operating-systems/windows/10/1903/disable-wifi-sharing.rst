.. _w10-1903-disable-wifi-sharing:

`Disable Wifi Sharing`_
#######################
Wifi Sharing (Sense) will automatically make connections to Wifi Networks via
crowdsharing and identified hotspots. Disable this.

.. dropdown:: Disable Wifi sharing (sense)
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in
  :open:

  .. dropdown:: GUI
    :title: font-weight-bold
    :animate: fade-in
    :open:

    :cmdmenu:`⌘ + r --> ms-settings:network --> manage wifi settings`

      * ☐ all for sharing.

  .. gpo::    Disable Wifi Sharing (Sense) via machine GPO
    :path:    Computer Configuration -->
              Administrative Templates -->
              Network -->
              WLAN Service -->
              WLAN Settings -->
              Allow Windows to automatically connect to suggested open hotspots, to networks shared by contacts, and to hotspots offering paid services
    :value0:  ☑, {DISABLED}
    :ref:     https://docs.microsoft.com/en-us/windows/client-management/mdm/policy-csp-wifi,
              https://www.thewindowsclub.com/disable-wi-fi-sense-windows-10-enterprise
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable Wifi Sharing (Sense) via Registry
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WcmSvc\wifinetworkmanager\config
    :value0:   AutoConnectAllowedOEM, {DWORD}, 0
    :ref:      https://docs.microsoft.com/en-us/windows/client-management/mdm/policy-csp-wifi,
               https://www.thewindowsclub.com/disable-wi-fi-sense-windows-10-enterprise
    :update:   2021-02-19
    :generic:
    :open:
