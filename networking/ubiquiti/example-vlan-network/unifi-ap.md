Unifi AP Setup
--------------
This will be used to setup the Unifi APs. See [full example network here][so].

> :exclamation:
> Use a unique IP and hostname for each AP device [using example network][so].

1. Factory reset Unifi AP.
1. Connect AP to a `trunk-wifi` port (_core:8_, _wired:5_).
1. Connect laptop to a _management_ port.

### Set Static AP IP
* Connect to Edgerouter GUI @ http://10.1.1.1.
* Reserve a static DHCP address for the switch.

#### `Services > DHCP Server > Management > Action > Leases`
* `Map Static IP`
  * IP Address: {STATIC AP IP}
  * Name: {STATIC AP NAME}

### Configure Unifi AP
* Connect to Unifi GUI @ http://localhost:8443.

> :warning:
> Wait up to _5_ minutes for the AP to connect controller. If the device has
> pulled a _10.1.1.0/24_ address, it should eventually appear if _L2 discovery_
> is enabled on controller.

#### `Devices > AP > Adopt`

#### `Devices > AP > Properties > Config > General`
* Alias: {STATIC AP NAME}
- [x] Use site settings

#### `Devices > AP > Properties > Config > Network`
* Configure IP: `Static`
  * IP Address: {STATIC AP IP}
  * Preferred DNS: `10.1.1.1`
  * Subnet Mask: `255.255.255.0`
  * Gateway: `10.1.1.1`
  * DNS Suffix: {YOUR DOMAIN}

#### `Queue Changes > Apply`
* Wait for provisioning to finish.
* Ensure AP is pingable. `ping {STATIC AP IP}`.
* Apply any firmware updates if needed.

#### `Devices > AP > Properties > Config > WLANS`
* WLAN Group: `wifi`

#### `Devices > AP > Properties > Config > Services > VLAN`
* Management VLAN: `LAN`

### Confirm Wireless Network Working
* Connect laptop to wifi network.
* Laptop should pull a _10.4.4.0/24_ network address, with the gateway
  _10.4.4.1_. This means it is properly working on the _wifi VLAN_. Internet
  should work.

[so]: README.md
