.. _vlan-101:

VLAN 101
########
Basic understanding of VLANs and how they work.

Basic Concepts
**************
.. glossary::
  :abbr:`PIF (Physical InterFace)`
    Defines the physical port of a piece of equipment.

  :abbr:`PVID (Parent Vlan IDentification)`
  :abbr:`PVLAN (Parent VLAN)`
    Defines the default VLAN for traffic leaving a specified interface. Also
    referred to as **Native Network**, **Parent VLAN**. Untagged traffic will be
    tagged with this ID leaving the port.

  :abbr:`VIF (Virtual InterFace)`
    Defines a virtual port of a piece of equipment; Commonly swapped with
    :term:`VLAN` or :term:`VID`.

  :abbr:`PVIF (Parent Virtual InterFace)`
    Defines a parent virtual port of a piece of equipment; Commonly swapped with
    :term:`PVLAN` or :term:`PVID`.

  :abbr:`VID (Vlan IDentification)`
    Defines a virtual port of a piece of equipment; must be associated with a
    :term:`PIF`. Commonly used interchangeably with :term:`VLAN`, :term:`VIF`.

  :abbr:`VLAN (Virtual Local Area Network)`
    A virtual network, creating logical separations within a switch. This allows
    for *multiple broadcast domains* on the switch.

    VLAN Attributes:

    * L2 (layer 2).
    * Independent Broadcast Domain.
    * Configured with 802.1Q.
    * VLANIDs: ``0-4095``.
    * VLANID: ``1`` is generally used as a *management VLAN* with *no VLAN
      tags*.

  :abbr:`VLANID (Virtual Local Area Network IDentification)`
    Integer number between ``0-4095`` identifying a specific VLAN.

  :abbr:`ALL (All Networks)`
    Concept used to denote *ALL* VLANS and untagged traffic. Typically used in
    defining trunks. If ALL is not used, then untagged traffic must be
    *explicitly* allowed.

  Tagged
    Network packet that has already been tagged with the *802.1Q* header,
    identifying that packet as being on a specific VLAN.

  Untagged
    Network packet that does **not** have the *802.1Q* header. This is standard
    network traffic. Also commonly referred to as the :term:`Native VLAN`.

  Management VLAN
    VLAN used for general management and adminstration; not typically for
    everyday data traffic. In common practice, the management VLAN is usually
    :term:`Untagged` traffic to allow for *unconfigured devices* the ability to
    be connected to when added to the network. Some devices (like Ubiquiti)
    treat the :term:`Management VLAN`, :term:`Untagged` traffic, and
    :term:`Native VLAN` as **VLANID 1**.

  Native VLAN
    Synonym for :term:`Untagged`. Standard network traffic to allow for
    *unconfigured devices* the ability to be connected to when added to the
    network. Some devices (like Ubiquiti) treat the :term:`Management VLAN`,
    :term:`Untagged` traffic, and :term:`Native VLAN` as **VLANID 1**.

  Trunk
    Used for upstream or downstream links between switches and routers. Accepts
    and forwards traffic on multiple VLANS, usually including :term:`Untagged`
    traffic.

Basic VLAN Switch Concepts
**************************
VLANs allow you to 'breakup' a switch to effectively act as multiple switches by
isolating the broadcast domain of traffic.

In this example, port 1 will see all traffic from all VLANS. ports 2 and 3 will
only see traffic on VLAN 2, 4-6 sees only VLAN 3, 7-8 sees only VLAN4:

.. aafig::
  :name: Basic VLAN Example.

        |         |             |
     1  |  2   3  |  4   5   6  |  7   8
  +-----+---------+-------------+---------+
  | +-+ | +-+ +-+ | +-+ +-+ +-+ | +-+ +-+ |
  | |A| | |2| |2| | |3| |3| |3| | |4| |4| |
  | +-+ | +-+ +-+ | +-+ +-+ +-+ | +-+ +-+ |
  +-----+---------+-------------+---------+
    A,2,|   2     |     3       |    4
    3,4 |         |             |

The equivalent physical configuration looks something like:

.. aafig::
  :name: Standard switch example.

                1   2   3
             +-------------+
             | +-+ +-+ +-+ |
      +------+ |2| |3| |4| +------+
      |      | +-+ +-+ +-+ |      |
      |      +------+------+      |
      |             |             |
  +---+----+ +------+------+ +----+----+
  |+-+ +-+ | | +-+ +-+ +-+ | | +-+ +-+ |
  ||2| |2| | | |3| |3| |3| | | |4| |4| |
  |+-+ +-+ | | +-+ +-+ +-+ | | +-+ +-+ |
  +--------+ +-------------+ +---------+

Basic VLAN Port Concepts
************************
Conceptualize VLANS as a way to filter traffic from either side of a port. It
may also help to think of VLANs as 'cables' between switching devices.

Clarifying Terms:

* :term:`PIF` will be used for all cases of :term:`PIF`, :term:`PVIF`,
  :term:`PVID`, Native Network and Parent VLAN.
* :term:`VIF` will be used for all cases of :term:`VIF`, :term:`VID`,
  :term:`VLAN`.
* :term:`Management VLAN` is defined as :term:`Untagged` network (e.g. PIF 1,
  VLAN 1).
* **VLANS** are **NOT SUBNETS**. A VLAN may transmit multiple subnets of traffic
  as long as those packets are tagged appropriately and are physically enforced
  at the hardware/server level. Subnets are defined farther up in the networking
  stack, typically in software. Generally you'll see one subnet per VLAN.

Standard device on a port
=========================
Devices which do not support VLANs will send data :term:`Untagged` onto the
network. This untagged traffic will be tagged with the :term:`PIF` ID exiting
the port.

Egress Traffic
**************
Untagged traffic from a device will be untagged exiting the port if :term:`ALL`
networks are allowed:

.. aafig::
  :name: Untagged traffic with a trunk.

   Device                Port
  +------+           +----------+
  |CCCCCC+---------->| 'PIF ALL'+---------->
  |CCCCCC| untagged  | 'VIF 20' | untagged
  |CCCCCC|           |          |
  +------+           +----------+

Untagged traffic from a device will be tagged with the :term:`PIF` VLAN if it is
explicitly defined:

.. aafig::
  :name: Tagged untagged traffic with PIF.
  :proportional:

   Device               Port
  +------+           +----------+
  |CCCCCC+---------->| 'PIF 1'  +---------->
  |CCCCCC| untagged  | 'VIF 20' |    1
  |CCCCCC|           |          |
  +------+           +----------+

Tagged and Untagged traffic will be filtered at the port based on :term:`PIF`
and :term:`VIF`:

.. aafig::
  :name: Blocking VLAN traffic at the port.

   Device               Port
  +------+           +----------+
  |CCCCCC+---------->| 'PIF 1'  +---------->
  |CCCCCC|   20      | 'VIF 20' |    20
  |CCCCCC|   30      |          |
  +------+           +----------+

Ingress Traffic
***************
Untagged traffic will be allow through the port to the device if :term:`ALL`
networks are allowed:

.. aafig::
  :name: Port allowing untagged traffic in via ALL.

   Device               Port
  +------+           +----------+
  |CCCCCC|<----------+ 'PIF ALL'|<----------
  |CCCCCC|  untagged | 'VIF 20' |  untagged
  |CCCCCC|           |          |
  +------+           +----------+

Traffic must be tagged with the :term:`PIF` VLAN for it to reach the device:

.. aafig::
  :name: PIF will untag traffic sent to it.

   Device               Port
  +------+           +----------+
  |CCCCCC|<----------+ 'PIF 1'  |<----------
  |CCCCCC|  untagged | 'VIF 20' |     1
  |CCCCCC|           |          |
  +------+           +----------+

   Device                Port
  +------+           +----------+
  |CCCCCC|     X     | 'PIF 3'  |<----------
  |CCCCCC|           | 'VIF 20' |  untagged
  |CCCCCC|           |          |
  +------+           +----------+

Tagged and Untagged traffic will be filtered at the port based on :term:`PIF`
and :term:`VIF`.

.. aafig::
  :name: Filter Tagged and Untagged Traffic.

   Device                Port
  +------+           +----------+
  |CCCCCC|<----------+ `PIF 1`  |<----------
  |CCCCCC|     20    | `VIF 20` |     20
  |CCCCCC|           |          |     40
  +------+           +----------+

Unifi APs
*********
Unifi APs transmit both *tagged* and *untagged* data at the same time.

* :term:`Tagged`: **AP data**. If configured, AP data is explicitly tagged with
  a VLAN before leaving the device.
* :term:`Untagged`: **AP Management Interface**. By default the management
  interface is exposed with untagged traffic (:term:`Management VLAN`, ``VLAN
  1``); to make adoption easier. In newer versions you can configure the
  management VLAN to a custom VLAN.
* The ``LAN`` network defined in *Networks* on the Unifi controller describes
  the properties of the :term:`Management VLAN`. This is the network that
  :term:`Untagged` traffic will be sent on.

Implementation Concepts
***********************
Fundamental concepts about VLANS need to be clarified before proceeding. VLANS
allow the separation of networks on the phyiscal switch level (L2/L3); which can
be thought of as applying switch-level filters to prevent specific traffic from
ever hitting network ports.

Important things to note:

* :term:`Untagged` traffic is traffic without any VLAN tags. `Within VLAN
  aware`_ devices this is tagged as ``1`` or ``VLAN1``. :term:`All` also
  includes this traffic.
* Ports will have a *default* or :term:`PVIF`. This is the default VLAN traffic
  will be tagged with, *if no tags are present*. If you connect a bunch of
  computers to a switch, and plug that switch into this port, they will all
  behave as though they are on the *default* or :term:`PVIF` network.
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
* Set a spare port on switches for :term:`Management VLAN` access so you can
  locally manage devices if something goes wrong.
* You need to understand your current network and layout a plan for how the
  traffic should work on VLANS. Generally VLANs segregate traffic based on type;
  e.g. wifi, iot, servers, desktops, etc.

.. rubric:: References

#. `Intro to Virtual LANs and VLANs <https://help.ui.com/hc/en-us/articles/222183968-Intro-to-Networking-Introduction-to-Virtual-LANs-VLANs-and-Tagging#3>`_
#. `Tagged VLAN1 Wireless Traffic <https://community.ui.com/questions/62e527e3-aa03-4de9-84fc-a5e42a44cfb9>`_
#. `VLANs with UniFi Products <https://help.ui.com/hc/en-us/articles/219654087>`_
#. `Guide to VLAN and Trunks <https://community.ui.com/questions/7462245c-95a7-455e-a711-209f44e194cb>`_

.. _Within VLAN aware: https://community.ui.com/questions/6205cb0e-20d5-47ac-b5f9-60c0539a8634s
