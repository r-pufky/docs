.. _unifi-conftroller-wifi-setup:

Unifi Controller Wifi Setup
###########################
This will be used to setup the Unifi managed switches and APs. See
:ref:`example-network-diagram`.

Connect to Unifi Controller @ http://localhost:8443.

.. ucontroller:: Create Wifi User Group
  :key:   Settings --> User Groups --> Create New User Group
  :names: Name,
          ☑,
          ☑
  :data:  throttled-wifi,
          Limit download bandwidth 10 Mbps,
          Limit upload bandwidth 10 Mbps
  :no_section:
  :hide_gui:

.. ucontroller:: Set Default Wireless Group
  :key:   Settings --> Wireless Networks --> WLAN Group Default
  :names: Edit
  :data:  wifi
  :no_section:
  :hide_gui:

  .. hint::
    This is located in the upper right, above the wireless network list.

.. ucontroller:: Create Wireless Network
  :key:   Settings --> Wireless Networks --> Create New Wireless Network
  :names: Name/SSID,
          ☑,
          ☑,
          Security Key,
          ☐,
          Advanced Options,
          › ☐,
          › ☑,
          › ☐,
          › ☐,
          › WPA Mode,
          › Encryption,
          › › ☑,
          › User Group,
          › ☐,
          › ☐,
          › ☐
  :data:  {YOUR SSID},
          Enable this wireless network,
          WPA Personal,
          {YOUR SSID PASSWORD},
          Apply guest policies,
          ,
          Block LAN to WLAN Multicast and Broadcast Data,
          Use VLAN 4,
          Enable fast roaming,
          Prevent this SSID from being broadcast,
          WPA2 Only,
          AES/CCMP Only,
          Enable GTK rekeying every 3600 seconds,
          throttled-wifi,
          Enable Unscheduled Automatic Power Save Delivery,
          Enable WLAN schedule,
          Enable multicast enhancement (IGMPv3)
  :no_section:
  :hide_gui: