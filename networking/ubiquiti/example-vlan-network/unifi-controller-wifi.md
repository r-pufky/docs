Unifi Controller VLAN Setup
---------------------------
This will be used to setup the Unifi managed switches and APs. See [full example
network here][so].

Connect to Unifi GUI @ http://localhost:8443.

#### `Settings > User Groups > Create New User Group`
* Name: `throttled-wifi`
- [x] Limit download bandwidth `10` `Mbps`
- [x] Limit upload bandwidth `10` `Mbps`

#### `Settings > Wireless Networks`
* WLAN Group `Default`: `Click Edit`
  * Name: `wifi`

> :warning:
> This is located in the upper right, above the wireless network list.

#### `Settings > Wireless Networks > Create New Wireless Network`
* Name/SSID: {YOUR SSID}
- [x] Enable this wireless network
- [x] WPA Personal
* Security Key: {YOUR SSID PASSWORD}
- [ ] Apply guest policies

* Advanced Options
  - [ ] Block LAN to WLAN Multicast and Broadcast Data
  - [x] Use VLAN `4`
  - [ ] Enable fast roaming
  - [ ] Prevent this SSID from being broadcast
  * WPA Mode: `WPA2 Only` Encryption: `AES/CCMP Only`
  - [x] Enable GTK rekeying every `3600` seconds
  * User Group: `throttled-wifi`
  - [ ] Enable Unscheduled Automatic Power Save Delivery
  - [ ] Enable WLAN schedule
  - [ ] Enable multicast enhancement (IGMPv3)

[so]: README.md
