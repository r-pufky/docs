Edgerouter VLAN Setup
---------------------
This will setup the edgerouter in a [router-on-a-stick][34] configuration using
VLANs, with no subnet restrictions (these will be applied after setup). See
[full example network here][so].

![
Edgerouter ER-4
+-----------------------------+
| +----+ +----+ +----+ +----+ |
| |eth0| |eth1| |eth2| |eth3| |------- Internet (eth3)
| +----+ +----+ +----+ +----+ |
+-----------------------------+
    |
](edgerouter.png)

### Reset & Login to Router
1. Factory reset edgerouter.
1. Connect _eth1_, set laptop static `192.168.1.5`, gateway: `192.168.1.1`.
1. Connect to Edgerouter GUI @ http://192.168.1.1.
   * Default credentials: `ubnt`/`ubnt`.

### `Basic Setup Wizard`
Basic Setup (Basic Setup is the same as _WAN+2LAN2_).

* Internet (`eth3/SFP`)
    - [x] Static IP
        * Address: {YOUR PUBLIC IP} / {PUBLIC IP NETMASK}
        * Gateware: {YOUR ISP GATEWAY}
        * DNS: `1.1.1.1`
    - [ ] Internet connection is on VLAN
    - [x] Enable the default firewall
    - [ ] Enable DHCPv6 Prefix Delegation
    - [ ] Bridge LAN interfaces into a single network
* LAN Ports (`eth2`)
  * Address: `192.168.2.1` / `255.255.255.0`
    * This will become static management port for the router, in case anything
      happens.
* User Setup
    - [x] Create new admin user
        * Username: {USER}
        * Password: {PW}
* Apply and reboot router

> :thought_balloon:
> The reason to use the SFP connection for Internet is to make it physically
> distinguishable from the rest of the ports on the router.

### Setup VLANs on eth0
1. Set laptop DHCP. Connect to _eth2_.
1. Connect to Edgerouter GUI @ http://192.168.1.1.

#### `System`
* Host Name: {ROUTER HOSTNAME}
* Domain Name: {YOUR DOMAIN}
* `Management Settings > SSH Server`
  - [x] Enable
    * Port: `2222`
  - [ ] Ubnt Discovery

#### `Dashboard > eth0 > Actions > Config`
* Address: `Manually define IP address`
    * `10.1.1.1/24`

> :warning:
> This handles untagged traffic coming into the router; this is the
> _management VLAN_ (VLAN1) network.

#### `Dashboard > Add Interface > Add VLAN`
  * VLANID: `2`
  * Interface: `eth0`
  * Description: {VLAN description}
  * Address: `Manually define IP address`
    * `10.2.2.1/24`

> :warning:
> Add all VLANS using [VLAN table in example network][Xv] to _eth0_. _Management
> VLAN_ is not explicitly defined as a VLAN -- untagged traffic coming into
> _eth0_ IS management traffic.

### Setup DHCP & DNS for VLANs

#### `Services > DHCP Server > Add DHCP Server`
* DHCP Name: `Wired`
* Subnet: `10.2.2.0/24`
* Range Start: `10.2.2.10`
* Range End: `10.2.2.240`
* Router: `10.2.2.1`
* DNS 1: `10.2.2.1`
* Domain: {YOUR DOMAIN}
- [x] Enable

> :warning:
> Add DHCP for all VLANS. For the _management_ DHCP server, set the _Unifi
> Controller_ field to the IP for the permenant Unifi Controller and not your
> laptop.

#### `Services > DNS > Interface > Add Listen Interface`
* Add for all networks and VLANS. VLANS will appear as _eth0.vlanid_.

### Confirm Management Network Working
* Connect laptop to _eth0_.
* Laptop should pull a _management VLAN_ network address, with the gateway
  _10.1.1.1_. This means untagged traffic is being properly assigned to the
  management network.

[so]: README.md
[Xv]: README.md#vlan-table
[34]: https://help.ubnt.com/hc/en-us/articles/204959444-EdgeRouter-Router-on-a-Stick
