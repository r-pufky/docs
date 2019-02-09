VLAN 101
========
Basic understanding of VLANs and how they work.

Basic Concepts
--------------
**PIF**: **P**hysical **I**nter**f**ace.
> Defines the physical port of a piece of equipment. Also referred to as
> **Native Network**, **Parent VLAN**. Untagged traffic will be tagged with this
> ID leaving the port.

**PVID**: **P**arent **V**LAN **ID**entification.
> Defines the physical port of a piece of equipment. Also referred to as
> **Native Network**, **Parent VLAN**. Untagged traffic will be tagged with this
> ID leaving the port.

**VIF**: **V**irtual **I**nter**f**ace.
> Defines a virtual port of a piece of equipment; Commonly swapped with
> **VLAN** or **VID**.

**VID**: **V**LAN **ID**entification.
> Defines a virtual port of a piece of equipment; must be associated with a
> **PIF**. Commonly swapped with **VLAN**, **VIF**.

**VLAN**: **V**irtual **L**ocal **A**rea **N**etwork.
> A virtual network, creating logical separations within a switch. This allows
> for _multiple broadcast domains_ on the switch.
>
> VLAN Attributes:
> * L2 (layer 2)
> * Independent Broadcast Domain
> * Configured with 802.1Q
> * VLANIDs: 0-4095
> * VLANID: 1 is generally used as a _management vlan_ with _no vlan tags_.

**VLANID**: **V**irtual **L**ocal **A**rea **N**etwork **ID**entification.
> Integer number between _0-4095_ identifying a specific VLAN.

**ALL**: All networks
> Concept used to denote _ALL_ VLANS and untagged traffic. Typically used in
> defining trunks. If ALL is not used, then untagged traffic must be
> _explicitly_ allowed.

**Tagged**
> Network packet that has already been tagged with the _802.1Q_ header,
> identifying that packet as being on a specific VLAN.

**Untagged**
> Network packet that does _not have_ the _802.1Q_ header. This is standard
> network traffic. Also commonly referred to as the **Native VLAN**.

**Management VLAN**
> VLAN used for general management and adminstration; not typically for everyday
> data traffic. In common practice, the management VLAN is usually **untagged**
> traffic to allow for _unconfigured devices_ the ability to be connected to
> when added to the network. Some devices (like Ubiquiti) treat **VLANID 1** as
> the _management VLAN_, _untagged traffic_, and _native VLAN_.

**Native VLAN**
> Synonym for **untagged**. Standard network traffic to allow for _unconfigured
> devices_ the ability to be connected to when added to the network. Some
> devices (like Ubiquiti) treat **VLANID 1** as the _management VLAN_, _untagged
> traffic_, and _native VLAN_.

**Trunk**
> Used for upstream or downstream links between switches and routers. Accepts
> and forwards traffic on multiple VLANS, usually including **untagged**
> traffic.

Basic VLAN Switch Concepts
--------------------------
VLANs allow you to 'breakup' a switch to effectively act as multiple switches by
isolating the broadcast domain of traffic.

In this example, port 1 will see all traffic from all VLANS. ports 2 and 3 will
only see traffic on VLAN 2, 4-6 sees only VLAN 3, 7-8 sees only VLAN4:
```
     +        +             +
   1 | 2   3  |  4   5   6  |  7   8
+-------------------------------------+
| +-+|+-+ +-+ | +-+ +-+ +-+ | +-+ +-+ |
| |A|||2| |2| | |3| |3| |3| | |4| |4| |
| +-+|+-+ +-+ | +-+ +-+ +-+ | +-+ +-+ |
+-------------------------------------+
 A,2,|   2    |     3       |    4
 3,4 +        +             +
```

The equivalent physicl configuration looks something like:
```
              1   2   3
           +-------------+
           | +-+ +-+ +-+ |
   +------ | |2| |3| |4| | -----+
   |       | +-+ +-+ +-+ |      |
   |       +-------------+      |
   |              |             |
+--------+ +-------------+ +---------+
|+-+ +-+ | | +-+ +-+ +-+ | | +-+ +-+ |
||2| |2| | | |3| |3| |3| | | |4| |4| |
|+-+ +-+ | | +-+ +-+ +-+ | | +-+ +-+ |
+--------+ +-------------+ +---------+
```

Basic VLAN Port Concepts
------------------------
Conceptualize VLANS as a way to filter traffic from either side of a port. It
may also help to think of VLANs as 'cables' between switching devices.

### Clarifying Terms
* _PIF_ will be used for all cases of PIF, PVID, Native Network and Parent VLAN.
* _VIF_ will be used for all cases of VIF, VID, VLAN.
* _management VLAN_ is defined as _untagged_ network (e.g. PIF 1, VLAN 1).
* **VLANS** are **NOT SUBNETS**. A VLAN may transmit multiple subnets of traffic
  as long as those packets are tagged appropriately and are physically enforced
  at the hardware/server level. Subnets are usually defined in
  software/clientside. Generally you'll see one subnet per VLAN.

### Standard device on a port
Devices which do not support VLANs will send data _untagged_ onto the network.
This untagged traffic will be tagged with the _PIF_ ID exiting the port.

#### Egress Traffic
Untagged traffic from a device will be untagged exiting the port if _ALL_
networks are allowed:
```
---- Direction of traffic ------->
 Device                Port
+------+            +--------+
|      | +--------> |PIF ALL +---------->
|      |  untagged  |VIF 20  | untagged
+------+            +--------+
```

Untagged traffic from a device will be tagged with the _PIF_ VLAN if it is
explicitly defined:
```
---- Direction of traffic ------->
 Device                Port
+------+            +--------+
|      | +--------> |PIF 1   +---------->
|      |  untagged  |VIF 20  |    1
+------+            +--------+
```

Tagged and Untagged traffic will be filtered at the port based on _PIF_ and
_VIF_.
```
---- Direction of traffic ------->
 Device                Port
+------+            +--------+
|      | +--------> |PIF 1   +---------->
|      |     20     |VIF 20  |    20
|      |     30     |        |
+------+            +--------+

```

#### Ingress Traffic
Untagged traffic will be allow through the port to the device if _ALL_ networks
are allowed:
```
<---- Direction of traffic -------
 Device                Port
+------+            +--------+
|      | <--------+ |PIF ALL + <--------+
|      |  untagged  |VIF 20  |  untagged
+------+            +--------+
```

Traffic must be tagged with the _PIF_ VLAN for it to reach the device:
```
<---- Direction of traffic -------
 Device                Port
+------+            +--------+
|      | <--------+ |PIF 1   + <--------+
|      |  untagged  |VIF 20  |     1
+------+            +--------+

<---- Direction of traffic -------
 Device                Port
+------+            +--------+
|      |     X      |PIF 3   + <--------+
|      |            |VIF 20  |  untagged
+------+            +--------+
```

Tagged and Untagged traffic will be filtered at the port based on _PIF_ and
_VIF_.
```
<---- Direction of traffic -------
 Device                Port
+------+            +--------+
|      | <--------+ |PIF 1   + <--------+
|      |     20     |VIF 20  |     20
|      |            |        |     40
+------+            +--------+

```

Unifi AP
--------
Unifi APs transmit both _tagged_ and _untagged_ data at the same time.

* Tagged: AP data. If configured, AP data is explicitly tagged with a VLAN
  before leaving the device.
* Untagged: AP Management Interface. By default the management interface is
  exposed with untagged traffic (_management VLAN_, VLAN 1); to make adoption
  easier. In newer versions you can configure the management VLAN to a custom
  VLAN.
* The 'LAN' network defined in _Networks_ in the Unifi controller describes the
  properties of the _management VLAN_. This is the network that untagged traffic
  will be sent on.

Implementation Concepts
-----------------------
Fundamental concepts about VLANS need to be clarified before proceeding. VLANS
allow the separation of networks on the phyiscal switch level (L2/L3); which can
be thought of as applying switch-level filters to prevent specific traffic from
ever hitting network ports.

Important things to note:
* Untagged traffic is traffic without any VLAN tags. Within VLAN aware devices
  this is tagged as [**1** or **VLAN1**][Id]. **All** also includes this
  traffic.
* Ports will have a _default_ or _Parent VLAN (PVIF)_. This is the default VLAN
  traffic will be tagged with, _if no tags are present_. If you connect a bunch
  of computers to a switch, and plug that switch into this port; they will all
  behave as though they are on the _default_ or _Parent VLAN (PVIF)_ network.
* Ports will typically have an additional set of VLANS that are allowed. Traffic
  using these VLANS needs to be pre-tagged with VLAN IDs to be allowed through.
  Untagged traffic will be tagged with the default VLAN.
* Trunks aggregate traffic together, used to push traffic upstream to another
  device. Trunk configurations should be the same set of VLANS on both ends in
  most cases. Trunks connecting directly to the router should generally contain
  all VLANS, while Trunks downstream should only specify VLANS that are actually
  used or needed on those devices. It my be helpful to look at the leaf nodes
  first and work your way back to prevent VLANS inadvertently being dropped on
  the way to the router.
* Set a spare port on switches for _management_ access so you can locally manage
  devices if something goes wrong.
* You need to understand your current network and layout a plan for how the
  traffic should work on VLANS. Generally VLANs segregate traffic based on type;
  e.g. wifi, iot, servers, desktops, etc.

[ref9d]: https://help.ubnt.com/hc/en-us/articles/222183968-Intro-to-Networking-Introduction-to-Virtual-LANs-VLANs-and-Tagging#3
[refk3]: https://community.ubnt.com/t5/UniFi-Wireless/Is-it-not-possible-to-have-a-tagged-VLAN-1-wireless-network/td-p/2477872
[ref0d]: https://help.ubnt.com/hc/en-us/articles/219654087