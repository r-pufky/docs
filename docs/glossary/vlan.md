# VLAN

## VLAN
Virtual Local Area Network.

## PIF (Physical InterFace)
Defines the physical port of a piece of equipment.

## PVID (Parent Vlan IDentification) / PVLAN (Parent VLAN)
Defines the default VLAN for traffic leaving a specified interface. Also
referred to as **Native Network**, **Parent VLAN**. [Untagged](#untagged)
traffic will be tagged with this ID leaving the port.

## VIF (Virtual InterFace)
Defines a virtual port of a piece of equipment; Commonly swapped with
[VLAN](#vlan-virtual-local-area-network) or [VID](#vid-vlan-identification).

## PVIF (Parent Virtual InterFace)
Defines a parent virtual port of a piece of equipment; Commonly swapped with
[PVLAN or PVID](#pvid-parent-vlan-identification-pvlan-parent-vlan).

## VID (Vlan IDentification)
Defines a virtual port of a piece of equipment; must be associated with a
[PIF](#pif-physical-interface). Commonly used interchangeably with
[VLAN](#vlan-virtual-local-area-network), [VIF](#vif-virtual-interface).

## VLAN (Virtual Local Area Network)
A virtual network, creating logical separations within a switch. This allows
for **multiple broadcast domains** on the switch.

VLAN Attributes:

* L2 (layer 2).
* Independent Broadcast Domain.
* Configured with 802.1Q.
* VLANIDs: **0-4095**.
* VLANID: **1** is generally used as a **management VLAN** with **no VLAN
  tags**.

## VLANID (Virtual Local Area Network IDentification)
Integer number between **0-4095** identifying a specific VLAN.

## ALL (All Networks)
Concept used to denote **ALL** VLANS and untagged traffic. Typically used in
defining [Trunks](#trunk). If ALL is not used, then untagged traffic must be
**explicitly** allowed.

## Tagged
Network packet that has already been tagged with the *802.1Q* header,
identifying that packet as being on a specific VLAN.

## Untagged
Network packet that does **not** have the **802.1Q** header. This is standard
network traffic. Also commonly referred to as the
[Native VLAN](#native-vlan-native-network).

## Management VLAN (Default)
VLAN used for general management and administration; not typically for everyday
data traffic. In common practice, the management VLAN is usually
[Untagged](#untagged) traffic to allow for **un-configured devices** the ability
to be connected to when added to the network. Some devices (like Ubiquiti)
treat the [Management VLAN](#management-vlan-default), [Untagged](#untagged)
traffic, and [Native VLAN](#native-vlan-native-network) as **VLANID 1**. May be
referred to as **Default** network.

## Native VLAN (Native Network)
Synonym for [Untagged](#untagged). Standard network traffic to allow for
**un-configured devices** the ability to be connected to when added to the
network. Some devices (like Ubiquiti) treat the
[Management VLAN](#management-vlan-default), [Untagged](#untagged) traffic, and
[Native VLAN](#native-vlan-native-network) as **VLANID 1**.

## Trunk
Used for upstream or downstream links between switches and routers. Accepts and
forwards traffic on multiple VLANS, usually including [Untagged](#untagged)
traffic.
