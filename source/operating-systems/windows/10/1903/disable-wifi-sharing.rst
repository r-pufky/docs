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

    :cmdmenu:`⌘ + r --> ms-settings:network --> manage wifi settings`

      * ☐ all for sharing.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Disable Wifi Sharing (Sense) via Registry
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WcmSvc\wifinetworkmanager\config
      :names:     AutoConnectAllowedOEM
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

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
      :no_caption:

.. rubric:: References

#. `Wifi Sharing Settings <https://docs.microsoft.com/en-us/windows/client-management/mdm/policy-csp-wifi>`_

.. _Disable Wifi Sharing: https://www.thewindowsclub.com/disable-wi-fi-sense-windows-10-enterprise
