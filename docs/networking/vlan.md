# VLANs
Basic understanding of [VLANs](../glossary/vlan.md#vlan) and how they work.

[Edge OS VLAN Setup](edge_os/README.md#vlan-setup).


## VLANS are Not Subnets
A VLAN may transmit multiple subnets of traffic as long as those packets are
tagged appropriately and are physically enforced at the hardware/server level.
Subnets are defined farther up in the networking stack, typically in software.

Generally you'll see one subnet per VLAN.

## Implementation Concepts
Fundamental concepts about VLANS need to be clarified before proceeding. VLANS
allow the separation of networks on the physical switch level (L2/L3); which can
be thought of as applying switch-level filters to prevent specific traffic from
ever hitting network ports.

Important things to note:

* [Untagged](../glossary/vlan.md#untagged) traffic is traffic without any VLAN
  tags. Within [VLAN aware](https://community.ui.com/questions/6205cb0e-20d5-47ac-b5f9-60c0539a8634s)
  devices this is tagged as **1** or **VLAN1**.
  [ALL](../glossary/vlan.md#all-all-networks) also includes this traffic.
* Ports will have a **default** or
  [PVIF](../glossary/vlan.md#pvif-parent-virtual-interface). This is the
  default VLAN traffic will be tagged with, **if no tags are present**. If you
  connect a bunch of computers to a switch, and plug that switch into this
  port, they will all behave as though they are on the **default** or
  [PVIF](../glossary/vlan.md#pvif-parent-virtual-interface) network.
* Ports will typically have an additional set of VLANS that are allowed.
  Traffic using these VLANS needs to be pre-tagged with VLAN IDs to be allowed
  through. Untagged traffic will be tagged with the default VLAN.
* Trunks aggregate traffic together, used to push traffic upstream to another
  device. Trunk configurations should be the same set of VLANS on both ends in
  most cases. Trunks connecting directly to the router should generally contain
  all VLANS, while Trunks downstream should only specify VLANS that are
  actually used or needed on those devices. It my be helpful to look at the
  leaf nodes first and work your way back to prevent VLANS inadvertently being
  dropped on the way to the router.
* Set a spare port on switches for
  [Management VLAN](../glossary/vlan.md#management-vlan-default) access so you
  can locally manage devices if something goes wrong.
* Design and understand your network layout and plan for how the traffic should
   work on VLANS. Generally VLANs segregate traffic based on type; e.g. wifi,
   iot, servers, desktops, etc.

## Switch Concepts
VLANs allow you to breakup a switch to effectively act as multiple switches by
isolating the broadcast domain of traffic.

In this example

* Port 1 will see all traffic from all VLANS.
* Ports 2 and 3 will only see traffic on VLAN 2.
* Ports 4-6 sees only VLAN 3.
* Ports 7-8 sees only VLAN4.

``` ascii
VLAN       A  │  2   2  │  3   3   3  │  4   4
        ╭-────┼─────────┼─────────────┼─────────╮
        │ ╭-╮ │ ╭-╮ ╭-╮ │ ╭-╮ ╭-╮ ╭-╮ │ ╭-╮ ╭-╮ │
Port    │ │1│ │ │2│ │3│ │ │4│ │5│ │6│ │ │7│ │8│ │
        │ ╰-╯ │ ╰-╯ ╰-╯ │ ╰-╯ ╰-╯ ╰-╯ │ ╰-╯ ╰-╯ │
        ╰─────┼─────────┼─────────────┼─────────╯
Traffic   A,2,│   2     │     3       │    4
          3,4 │         │             │
```

The equivalent physical configuration looks something like:

``` ascii
Switch        2   3   4
           ╭────────────-╮
           │ ╭─╮ ╭─╮ ╭─╮ │
    ╭──────┤ │1│ │2│ │3│ ├──────╮
    │      │ ╰─╯ ╰─╯ ╰─╯ │      │
    │      ╰──────┬──────╯      │
  2 │ 2       3   │3  3       4 │ 4
╭──-┴────╮ ╭──────┴──────╮ ╭────┴────╮
│╭─╮ ╭─╮ │ │ ╭─╮ ╭─╮ ╭─╮ │ │ ╭─╮ ╭─╮ │
││1│ │2│ │ │ │1│ │2│ │3│ │ │ │1│ │2│ │
│╰─╯ ╰─╯ │ │ ╰─╯ ╰─╯ ╰─╯ │ │ ╰─╯ ╰─╯ │
╰────────╯ ╰────────────-╯ ╰────────-╯
```

## Basic VLAN Port Concepts
Conceptualize VLANS as a way to filter traffic from either side of a port. It
may also help to think of VLANs as 'cables' between switching devices.

### Clarifying Terms

* [PIF](../glossary/vlan.md#pif-physical-interface) will be used for all cases
  of [PIF](../glossary/vlan.md#pif-physical-interface), [PVIF](../glossary/vlan.md#pvif-parent-virtual-interface),
  [PVID](../glossary/vlan.md#pvid-parent-vlan-identification-pvlan-parent-vlan),
  [Native VLAN](../glossary/vlan.md#native-vlan-native-network) and
  [Parent VLAN](../glossary/vlan.md#pvid-parent-vlan-identification-pvlan-parent-vlan).
* [VIF](../glossary/vlan.md#vif-virtual-interface) will be used for all cases
  of [VIF](../glossary/vlan.md#vif-virtual-interface),
  [VID](../glossary/vlan.md#vid-vlan-identification),
  [VLAN](../glossary/vlan.md#vlan-virtual-local-area-network).
* [Management VLAN](../glossary/vlan.md#management-vlan-default) is defined as
  [Untagged](../glossary/vlan.md#untagged) network (e.g. PIF 1, VLAN 1).


### Standard device on a port
Devices which do not support VLANs will send data
[Untagged](../glossary/vlan.md#untagged) onto the network. This untagged
traffic will be tagged with the
[PIF](../glossary/vlan.md#pif-physical-interface) ID exiting the port.

### Egress Traffic

#### Untagged traffic with a trunk
Untagged traffic from a device will be untagged exiting the port if
[ALL](../glossary/vlan.md#all-all-networks) networks are allowed:

``` ascii
 Device               Port
╭──────╮           ╭─────────╮
│      │ untagged  │ PIF ALL │ untagged
│      ├──────────>│ VIF 20  ├──────────>
╰──────╯           ╰─────────╯
```

#### Tagged untagged traffic with PIF
Untagged traffic from a device will be tagged with the
[PIF](../glossary/vlan.md#pif-physical-interface) VLAN if it is explicitly
defined.

``` ascii
 Device               Port
╭──────╮           ╭────────╮
│      │ untagged  │ PIF 1  │    1
│      ├──────────>│ VIF 20 ├──────────>
╰──────╯           ╰────────╯
```

#### Blocking VLAN traffic at the port
Tagged and Untagged traffic will be filtered at the port based on
[PIF](../glossary/vlan.md#pif-physical-interface) and
[VIF](../glossary/vlan.md#vif-virtual-interface):

``` ascii
 Device               Port
╭──────╮           ╭─────────╮
│      │   20      │  PIF 1  │
│      │   30      │  VIF 20 │   20
│      ├──────────>│         ├──────────>
╰──────╯           ╰─────────╯
```

### Ingress Traffic

#### Port allowing untagged traffic in via ALL
Untagged traffic will be allow through the port to the device if
[ALL](../glossary/vlan.md#all-all-networks) networks are allowed:

``` ascii
 Device               Port
╭──────╮           ╭─────────╮
│      │  untagged │ PIF ALL │  untagged
│      │<──────────┤ VIF 20  │<──────────
╰──────╯           ╰─────────╯
```

#### PIF will untag traffic sent to it
Traffic must be tagged with the
[PIF](../glossary/vlan.md#pif-physical-interface) VLAN for it to reach the
device:

``` ascii
 Device               Port
╭──────╮           ╭────────╮
│      │  untagged │ PIF 1  │     1
│      │<──────────┤ VIF 20 │<──────────
╰──────╯           ╰────────╯

 Device                Port
╭──────╮           ╭────────╮
│      │     X     │ PIF 3  │  untagged
│      │           │ VIF 20 │<──────────
╰──────╯           ╰────────╯
```

#### Filter Tagged and Untagged Traffic
Tagged and Untagged traffic will be filtered at the port based on
[PIF](../glossary/vlan.md#pif-physical-interface) and
[VIF](../glossary/vlan.md#vif-virtual-interface).

``` ascii
 Device                Port
╭──────╮           ╭────────╮
│      │     20    │ PIF 1  │     20
│      │<──────────┤ VIF 20 │<──────────
╰──────╯           ╰────────╯
```

## UniFi APs
UniFi APs transmit both **tagged** and **untagged** data at the same time.

* [Tagged](../glossary/vlan.md#tagged): **AP data**. If configured, AP data is
  explicitly tagged with a VLAN before leaving the device.
* [Untagged](../glossary/vlan.md#untagged): **AP Management Interface**. By
  default the management interface is exposed with untagged traffic
  [Management VLAN](../glossary/vlan.md#management-vlan-default) - **VLAN1**; to make
  adoption easier. In newer versions you can configure the management VLAN to a
  custom VLAN.
* The **LAN** network defined in **Networks** on the UniFi controller describes
  the properties of the
  [Management VLAN](../glossary/vlan.md#management-vlan-default).
  This is the network that [Untagged](../glossary/vlan.md#untagged) traffic
  will be sent on.

## References

* https://help.ui.com/hc/en-us/articles/222183968-Intro-to-Networking-Introduction-to-Virtual-LANs-VLANs-and-Tagging#3
* https://community.ui.com/questions/62e527e3-aa03-4de9-84fc-a5e42a44cfb9
* https://help.ui.com/hc/en-us/articles/219654087
* https://community.ui.com/questions/7462245c-95a7-455e-a711-209f44e194cb
