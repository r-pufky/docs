Unifi Controller VLAN Setup
---------------------------
This will be used to setup the Unifi managed switches and APs. See [full example
network here][so]. Download and install the [Unifi Controller][8l] onto the
setup laptop.

### Setup Wizard
Connect to Unifi GUI @ http://localhost:8443.

* Select your Country: {COUNTRY}
* Select your Timezone: {LOCAL TIMEZONE}
- [x] Enable Auto Backup
* Skip _device_ configuration.
* Skip _wifi_ configuration.
* Controller Access:
  * Admin Name: {ADMIN USER}
  * Admin Email: {EMAIL}
  * Admin Password: {ADMIN PW}
  * Device Authentication: {DEVICE USER}
  * Device Password: {DEVICE PW}
* Skip _cloud login_ credentials

> :warning:
> The _admin name_ account is the **super admin** for [the controller][0F],
> meaning that account can manage multiple sites as well as devices. The
> _device authentication_ account is used to manage physical devices via the UI
> or SSH on that device.

### Base Unifi Controller Setup

#### `Settings > Controller`
* Controller Settings:
  * Controller Name: {CONTROLLER DNS NAME}
  * Controller Hostname/IP: {CONTROLLER IP}
  - [ ] Override inform host with controller hostname/IP
  - [x] Make controller discoverable on L2 network
  * Store: `Disable store for all users`
  * Support Messaging: `Disable live support for all users`
  * Real-time Updates in Web Browser: `Automatically adapt rates of real-time
    updates`
  - [ ] Enable mail server

> :warning:
> L2 device discovery will help to adopt controllers which are not receiving
> a [unifi controller DHCP option][pD]. These settings are only for initial
> setup with the laptop and may be changed or disabled after initial
> configuration to rely on DHCP or set inform.

#### `Settings > Site`
* Site Configuration
  * Site Name: {YOUR SITE NAME}
  * Country: {COUNTRY}
  * Timezone: {LOCAL TIMEZONE}
* Services
  - [ ] Advanced Features
  - [x] Automatically upgrade AP firmware
  - [ ] Enable status LED
  - [ ] Enable alert emails
  - [ ] Enable periodic speed test every
  - [x] Enable connectivity monitor and wireless uplink
  - [x] Default gateway
  - [ ] Enable remote Syslog server
  - [ ] Enable Netconsole logging server
* Provider Capabilities
  * Download: `1` `Gbps`
  * Upload: `1` `Gbps`
* Device Authentication
  - [x] Enable SSH authentication
      * Username: {DEVICE USER}
      * Password: {DEVICE PW}
* Apply changes.

> :warning:
> Alerts and advanced logging disabled for initial setup, change these after
> finishing configuration. Upload/Download settings should be reflective of
> your Internet connection for proper scaling of graphing data. It is _not_ a
> throttle.

### VLAN Configuration
Add all VLANS using [VLAN table in example network][Xv].

#### `Settings > Networks > LAN`
- [x] Corporate
- [x] LAN
* Gateway/Subnet: `10.1.1.1/24`
* Domain Name: {YOUR DOMAIN}
- [ ] Enable IGMP Snooping
* DHCP Server: `None`
- [ ] Enable DHCP gaurding
- [ ] Enable UPnP LAN
* IPv6 Interface Type: `None`

> :warning:
> This will be the default network when new devices are discovered before they
> are adopted. This is also the untagged _management VLAN_ network. Configure
> with _management VLAN_ settings.

#### `Settings > Networks > Create New Network`
* Name: `Wired`
- [x] VLAN Only
* VLAN: `2`

> :warning:
> Add all VLANS using [VLAN table in example network][Xv]. _Management
> VLAN_ is not explicitly defined as a VLAN -- untagged traffic coming into
> _eth0_ IS management traffic.

#### `Settings > Profiles > Switch Ports > Add New Port Profile`
* Unifi AP Wireless Trunk
  * Create New Switch Port Profile
    * Profile Name: `trunk-wifi`
      * PoE: `PoE/PoE+`
  * Networks/VLANs
    * Native Network: `LAN`
    * Tagged Networks: `wifi`
    * Voice Network: `None`
* Wired Trunk
  * Create New Switch Port Profile
    * Profile Name: `trunk-wired`
      * PoE: `Off`
  * Networks/VLANs
    * Native Network: `LAN`
    * Tagged Networks: `wifi`, `wired`
    * Voice Network: `None`
* Server Trunk
  * Create New Switch Port Profile
    * Profile Name: `trunk-server`
      * PoE: `Off`
  * Networks/VLANs
    * Native Network: `LAN`
    * Tagged Networks: `server`, `infrastructure`
    * Voice Network: `None`

[so]: README.md
[Xv]: README.md#vlan-table
[8l]: https://www.ui.com/download/?q=controller
[0F]: https://help.ubnt.com/hc/en-us/articles/204909374-UniFi-Accounts-and-Passwords-for-Controller-Cloud-Key-and-Other-Devices
[pD]: https://help.ubnt.com/hc/en-us/articles/204909754-UniFi-Device-Adoption-Methods-for-Remote-UniFi-Controllers#7

[ref8d]: https://help.ubnt.com/hc/en-us/articles/219654087-UniFi-Using-VLANs-with-UniFi-Wireless-Routing-Switching-Hardware#UAP
[refv2]: https://help.ubnt.com/hc/en-us/articles/204962144#1
[refs0]: https://www.douglasisaksson.com/lessons-learned-from-deploying-a-unifi-network-at-home/
[refRU]: https://www.youtube.com/watch?v=JblnjsnJNJU