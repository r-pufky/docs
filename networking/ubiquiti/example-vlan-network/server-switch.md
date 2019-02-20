Server Switch VLAN Setup
------------------------
This will setup the server switch using VLANs according to example network. See
[full example network here][so].

![
   |    Unifi US-8-60W (Server)
+---------------------------------+
| +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ |
| |A| |s| |s| |s| |i| |s| |A| |D| |
| +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ |
+---------------------------------+
](server-switch.png)

### Setup Server Switch
This switch handles trunking server connections upstream to core switch.

1. Factory reset switch.
1. Connect laptop directly to _port 7_ on new switch. Any port that is not going
   to be used for trunking or VLANs is fine.
1. Connect switch trunk _port 1_ to _port 4_ (Server Trunk) on core switch.
1. Connect to Unifi GUI @ http://localhost:8443.

#### `Devices > Switch > Adopt`
> :warning:
> The initial switch IP may appear different (e.g. the LAN network defined on
> the controller); this is expected and is the default network for any new
> Unifi device adopted. This will automatically correct during adoption. See
> [adoption troubleshooting][xc] if the device does not adopt.

#### Set Static Switch IP
* Connect to Edgerouter GUI @ http://10.1.1.1.
* Reserve a static DHCP address for the switch.

##### `Services > DHCP Server > Management > Action > Leases`
* `Map Static IP`
  * IP Address: `10.1.1.6`
  * Name: `server`

Connect to Unifi GUI @ http://localhost:8443.
* Set static IP for the switch.

##### `Devices > Switch > Properties > Config > Network`
* Configure IP: `Static`
  * IP Address: `10.1.1.6`
  * Preferred DNS: `10.1.1.1`
  * Subnet Mask: `255.255.255.0`
  * Gateway: `10.1.1.1`
  * DNS Suffix: {YOUR DOMAIN}

##### `Queue Changes > Apply`
* Wait for provisioning to finish.
* Ensure switch is pingable. `ping 10.1.1.6`.
* Apply any firmware updates if needed.

### Configure Basic Switch Management

#### `Devices > Switch > Properties > Config > General`
* Alias: `server`
* LED: `use site settings`

#### `Devices > Switch > Properties > Config > Services`
* VLAN
  * Management VLAN: `LAN`
  * Spanning Tree: `RSTP`
  * Priority: `32768`
* Security
  - [ ] Enable 802.1x control
* SNMP
  * Location: ``
  * Contact: ``

#### `Queue Changes > Apply`

### Configure VLANs on Ports

#### `Devices > Switch > Properties > Ports`
* Port 1:
  * Name: `trunk`
  * Switch Port Profile: `trunk-server`
* Port 2-4:
  * Name: `serve`
  * Switch Port Profile: `server (5)`
* Port 5:
  * Name: `infra`
  * Switch Port Profiles: `infrastructure (9)`
  * Profile Overrides
    * PoE: `Off`
* Port 6:
  * Name: `serve`
  * Switch Port Profiles: `server (5)`
  * Profile Overrides
    * PoE: `Off`
* Port 7:
  * Name: `management`
  * Switch Port Profiles: `All`
  * Profile Overrides
    * PoE: `Off`
* Port 8:
  * Name: `disable`
  * Switch Port Profiles: `Disabled`

> :warning:
> Switch will re-provision for each port modification. Wait for provisioning
> to complete before proceeding through each port.

### Confirm Server/Infrastructure Network Working
* Connect laptop to _server_ port.
* Laptop should pull a _10.5.5.0/24_ network address, with the gateway
  _10.5.5.1_. This means it is properly working on the _server VLAN_. Internet
  should work.
* Connect laptop to _infrastructure_ port.
* Laptop should pull a _10.9.9.0/24_ network address, with the gateway
  _10.9.9.1_. This means it is properly working on the _server VLAN_. Internet
  should work.

[so]: README.md
[xc]: README.md#unifi-device-troubleshooting

[refiJ]: https://community.ubnt.com/t5/UniFi-Routing-Switching/Setting-Management-VLAN-for-Switches/td-p/2279619