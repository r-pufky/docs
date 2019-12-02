.. _unifi-conftroller-wifi-setup:

Unifi Controller Wifi Setup
###########################
This will be used to setup the Unifi managed switches and APs. See
:ref:`example-network-diagram`.

Connect to Unifi Controller @ http://localhost:8443.

.. ucontroller:: Create Wifi User Group
  :key_title:    Settings --> User Groups --> Create New User Group
  :option:       Name,
                 ☑,
                 ☑
  :setting:      throttled-wifi,
                 Limit download bandwidth 10 Mbps,
                 Limit upload bandwidth 10 Mbps
  :no_section:
  :no_caption:
  :no_launch:

.. ucontroller:: Set Default Wireless Group
  :key_title:    Settings --> Wireless Networks --> WLAN Group Default
  :option:       Edit
  :setting:      wifi
  :no_section:
  :no_caption:
  :no_launch:

    .. hint::
      This is located in the upper right, above the wireless network list.

.. ucontroller:: Create Wireless Network
  :key_title:    Settings --> Wireless Networks --> Create New Wireless Network
  :option:       Name/SSID,
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
  :setting:      {YOUR SSID},
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
  :no_caption:
  :no_launch: