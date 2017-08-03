Unifi AP Controller
-------------------
Uses [Ubuntu 16.04 base Xen template](../templates/ubuntu-server.md), and assumes post template setup scripts have been run.

1. [Ports Exposed](#ports-exposed)
2. [Service Setup](#service-setup)
3. [Simple AP Configuration](#simple-ap-configuration)
4. [Migrating existing AP's to a new controller](#migrating-existing-aps-to-a-new-controller)
3. [References](#references)


Ports Exposed
-------------

| Port | Protocol |Purpose                 |
|------|----------|------------------------|
| 8443 | TCP      | webface management     |
| 8080 | TCP      | AP management / inform |


Service Setup
-------------
### Add ubiquiti apt repository
sudo vim /etc/apt/sources.list.d/100-unifi-controller.list
```bash
deb http://www.ubnt.com/downloads/unifi/debian stable ubiquiti
```
Install the service and start
```bash
sudo chmod 0644 /etc/apt/sources.list.d/100-unifi-controller.list
sudo chown root:root /etc/apt/sources.list.d/100-unifi-controller.list
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv 06E85760C0A52C50
sudo apt update && sudo apt upgrade && sudo apt install unifi
sudo service unifi start
```

If you have an existing backup of a controller, you can import it immediately and not have to manually re-configure anything.


Simple AP Configuration
-----------------------
This is a sample configuration for a WPA2 single AP setup with basic filtering.

Settings (lower left gear)
Site
- Site Configuration
  * Site Name: [sitename]
- Services
  * Automatic Upgrades: Automaticall Upgrade Firmware
  * LED: Disable enable status LED
  * Uplink Connectivity Monitor: Enable connectivity monitor and wireless uplink
  * Uplink Connectivity Monitor: Default Gateway
  * Device Authentication: <username> <password>

Wireless Networks
- Wireless Network
  * SSID: [WIFI name]
  * Enabled: Enable this wireless network
  * Security: WPA Personal
  * Security KEy: [WIFI password]
- Advanced Options
  * Multicast and Broadcast Filtering: Block LAN to WLAN multicast and broadcast data
  * WPA Mode: WPA2 Only, AES/CCMP Only
  * User Group: Default
- 802.11 Rate and Beacon Controls
  * DTIM Mode: Use default values

Networks
- Edit Network
  * Name: WIFI
  * Purpose: Corporate
  * Parent Interface: LAN
  * Gateway/Subnet: 10.10.10.1/24
      _not just subnet, gateway ip and bitmask; this is an example IP_
  * DHCP Server: Disable DHCP
  * Domain Name: localdomain

Guest Control
- Access Control
  * Pre-Authorization Access: Remove All
      _any networks accessible without auth_
  * Post-Authorization Restrictions: Add networks you don't want accessed
      _This will block wifi clients from accessing these networks. Valid to use the gateway network (10.10.10.0/24) as well -- gateway is always accessible_

Controller
- Controller Settings
  * Controller Name: [hostname]
  * Controller Hostname/IP: [FQDN]
  * Controller Hostname/IP: Override inform host with Controller Hostname/IP
  * Network Discovery: Remove make controller discoverable on L2 network
  * Support Messaging: Disable live support for all users


Devices (upper left Circles)
- adopt if needed and upgrade firmware
- Configuration
  - Radio 2G (11N/B/G)
    * Channel Width: HT40
    * Channel: Auto
    * Transmit Power: High
  - Radio 5G (11N/A/AC)
    * Channel Width: VHT80
    * Channel: Auto
    * Transmit Power: High
  - WLANS
    * WLAN 2G (11N/B/G)
      * Group: Default
      * Name: [WIFI name]
    * WLAN 5G (11N/A/AC)
      * Group: Default
      * Name: [WIFI name]
  - Network
    * Configure IP: Using DHCP
        _This is the AP IP_


Migrating existing AP's to a new controller
-------------------------------------------
This will adopt the AP to the new controller
* ssh to AP
```bash
set-inform http://<new controller>:8080/inform
syswrapper.sh restore-default
```
The system will reset and reboot to factory settings; AP should appear in the controller device listing


References
----------
[Unifi Apt install with Ubuntu](https://help.ubnt.com/hc/en-us/articles/220066768-UniFi-How-to-Install-Update-via-APT-on-Debian-or-Ubuntu)

[Unifi Ports](https://help.ubnt.com/hc/en-us/articles/218506997-UniFi-Ports-Used)

[Migrating Unifi AP's to New Controller](https://community.ubnt.com/t5/UniFi-Wireless/Migrating-UNIFI-APs-to-new-controller/td-p/308741)
