.. _unifi-conftroller-wifi-setup:

Unifi Controller Wifi Setup
###########################
This will be used to setup the Unifi managed switches and APs. See
:ref:`example-network-diagram`.

Connect to Unifi Controller @ http://localhost:8443.

.. ubiquiti:: Create Wifi User Group
  :path:      Settings --> User Groups --> Create New User Group
  :value0:       Name, throttled-wifi
  :value1:       ☑, Limit download bandwidth 10 Mbps
  :value2:       ☑, Limit upload bandwidth 10 Mbps

.. ubiquiti:: Set Default Wireless Group
  :path:      Settings --> Wireless Networks --> WLAN Group Default
  :value0:    Edit, wifi

  .. hint::
    This is located in the upper right, above the wireless network list.

.. ubiquiti:: Create Wireless Network
  :path:      Settings --> Wireless Networks --> Create New Wireless Network
  :value0:    Name/SSID, {SSID}
  :value1:    ☑, Enable this wireless network
  :value2:    ☑, WPA Personal
  :value3:    Security Key, {PASS}
  :value4:    ☐, Apply guest policies
  :value5:    Advanced Options,
  :value6:    › ☐, Block LAN to WLAN Multicast and Broadcast Data
  :value7:    › ☑, Use VLAN 4
  :value8:    › ☐, Enable fast roaming
  :value9:    › ☐, Prevent this SSID from being broadcast
  :value10:   › WPA Mode, WPA2 Only
  :value11:   › Encryption, AES/CCMP Only
  :value12:   › › ☑, Enable GTK rekeying every 3600 seconds
  :value13:   › User Group, throttled-wifi
  :value14:   › ☐, Enable Unscheduled Automatic Power Save Delivery
  :value15:   › ☐, Enable WLAN schedule
  :value16:   › ☐, Enable multicast enhancement (IGMPv3)
