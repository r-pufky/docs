Core Switch VLAN Setup
----------------------
This will setup the core switch using VLANs according to example network. See
[full example network here][so].

![
   |    Unifi US-8-60W (Core)
+---------------------------------+
| +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ |
| |A| |D| |W| |S| |D| |D| |A| |I| |
| +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ |
+---------------------------------+
           |   |
](core-switch.png)

### Setup Core Switch
This switch handles trunking to the router upstream and connections downstream
to switches/APs.

1. Factory reset switch.
1. Connect laptop directly to _port 7_ on new switch. Any port that is not going
   to be used for trunking or VLANs is fine.
1. Connect switch trunk _port 1_ to _eth0_ on edgerouter.
1. Connect to Unifi GUI @ http://localhost:8443.

#### `Devices > Switch > Adopt`
> :warning:
> The initial switch IP may appear different (e.g. the LAN network defined on
> the controller); this is expected and is the default network for any new
> Unifi device adopted. This will automatically correct during adoption. See
> [adoption troubleshooting][xc] if the device does not adopt.

#### Set Static Switch IP
* Connect to Edgerouter GUI @ http://192.168.1.1.
* Reserve a static DHCP address for the switch.

##### `Services > DHCP Server > Management > Action > Leases`
* `Map Static IP`
  * IP Address: `10.1.1.5`
  * Name: `core`

Connect to Unifi GUI @ http://localhost:8443.
* Set static IP for the switch.

##### `Devices > Switch > Properties > Config > Network`
* Configure IP: `Static`
  * IP Address: `10.1.1.5`
  * Preferred DNS: `10.1.1.1`
  * Subnet Mask: `255.255.255.0`
  * Gateway: `10.1.1.1`
  * DNS Suffix: {YOUR DOMAIN}

##### `Queue Changes > Apply`
* Wait for provisioning to finish.
* Ensure switch is pingable. `ping 10.1.1.5`.
* Apply any firmware updates if needed.

### Configure Basic Switch Management

#### `Devices > Switch > Properties > Config > General`
* Alias: `core`
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
  * Switch Port Profile: `All`
* Port 2:
  * Name: `disable`
  * Switch Port Profile: `Disabled`
* Port 3:
  * Name: `wired`
  * Switch Port Profiles: `trunk-wired`
* Port 4:
  * Name: `server`
  * Switch Port Profiles: `trunk-server`
* Port 5-6:
  * Name: `disable`
  * Switch Port Profiles: `Disabled`
* Port 7:
  * Name: `management`
  * Switch Port Profiles: `All`
  * Profile Overrides
    * PoE: `Off`
* Port 8:
  * Name: `wifi`
  * Switch Port Profiles: `trunk-wifi`

> :warning:
> Switch will re-provision for each port modification. Wait for provisioning
> to complete before proceeding through each port.

[so]: README.md
[xc]: README.md#unifi-device-troubleshooting