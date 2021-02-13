.. _server-switch-vlan-setup:

Server Switch VLAN Setup
########################
This will setup the server switch using VLANs according to example network. See
:ref:`example-network-diagram`.

.. aafig::
  :name: Unifi US-8-60W (Server)

     |   'Unifi US-8-60W (Server)
  +--+------------------------------+
  | +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ |
  | |A| |s| |s| |s| |i| |s| |A| |D| |
  | +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ |
  +---------------------------------+

.. figure:: source/server-switch.png
  :width: 90%

Setup Server Switch
*******************
This switch handles trunking server connections upstream to core switch.

#. Factory reset switch.
#. Connect laptop directly to *port 7* on new switch. Any port that is not going
   to be used for trunking or VLANs is fine.
#. Connect switch trunk *port 1* to *port 4* (Server Trunk) on core switch.
#. Connect to Unifi Controller @ http://localhost:8443.

Adopt Server Switch
===================
:cmdmenu:`Devices --> Switch --> Adopt`

.. warning::
  The initial switch IP may appear different (e.g. the LAN network defined on
  the controller); this is expected and is the default network for any new
  Unifi device adopted. This will automatically correct during adoption. See
  :ref:`unifi-adoption-failure` if the device does not adopt.

Set Static Switch IP
====================
#. Connect to Edgerouter GUI @ http://10.1.1.1.
#. Reserve a static DHCP address for the switch.

.. ubiquiti:: Add Static Reservation for Switch Management
  :path:      Services --> DHCP Server --> Management --> Action --> Leases
  :value0:    Map Static IP,
  :value1:    › IP Address, 10.1.1.6
  :value2:    › Name, server

Connect to Unifi Controller @ http://localhost:8443.

.. ubiquiti:: Set Static Switch IP
  :path:      Devices --> Switch --> Properties --> Config --> Network
  :value0:    Configure IP, {STATIC}
  :value1:    › IP Address, 10.1.1.6
  :value2:    › Preferred DNS, 10.1.1.1
  :value3:    › Subnet Mask, 255.255.255.0
  :value4:    › Gateway, 10.1.1.1
  :value5:    › DNS Suffix, {DOMAIN}

  .. note::
    :cmdmenu:`Queue Changes --> Apply`

    * Wait for provisioning to finish.
    * Ensure switch is pingable. ``ping 10.1.1.6``.
    * Apply any firmware updates if needed.

Configure Server Switch Management
**********************************
.. ubiquiti:: General Server Switch Setup
  :path:      Devices --> Switch --> Properties --> Config --> General
  :value0:    Alias, server
  :value1:    LED, use site settings

.. ubiquiti:: Server Switch Services Setup
  :path:      Devices --> Switch --> Properties --> Config --> Services
  :value0:    VLAN,
  :value1:    › Management VLAN, LAN
  :value2:    › Spanning Tree, RSTP
  :value3:    › Priority, 32768
  :value4:    Security,
  :value5:    › ☐, Enable 802.1x control
  :value6:    SNMP,
  :value7:    › Location, {NONE}
  :value8:    › Contact, {NONE}

:cmdmenu:`Queue Changes --> Apply`

Configure VLANs on Ports
************************
.. ubiquiti:: Configure Switch VLANs
  :path:    Devices --> Switch --> Properties --> Ports
  :value0:  Port 1,
  :value1:  › Name, trunk
  :value2:  › Switch Port Profile, trunk-server
  :value3:  Port 2-4,
  :value4:  › Name, serve
  :value5:  › Switch Port Profile, server (5)
  :value6:  Port 5,
  :value7:  › Name, infra
  :value8:  › Switch Port Profile, infrastructure (9)
  :value9:  › › Profile Overrides,
  :value10:  › › › PoE, {OFF}
  :value11:  Port 6,
  :value12:  › Name, serve
  :value13:  › Switch Port Profile, server (5)
  :value14:  › › Profile Overrides,
  :value15:  › › › PoE, {OFF}
  :value16:  Port 7,
  :value17:  › Name, management
  :value18:  › Switch Port Profile, All
  :value19:  › › Profile Overrides,
  :value20:  › › › PoE, {OFF}
  :value21:  Port 8,
  :value22:  › Name, {DISABLE}
  :value23:  › Switch Port Profile, {DISABLED}

  .. warning::
    Switch will re-provision for each port modification. Wait for provisioning
    to complete before proceeding through each port.

Confirm Server/Infrastructure Network Working
*********************************************
* Connect laptop to *server* port.
* Laptop should pull a *10.5.5.0/24* network address, with the gateway
  *10.5.5.1*. This means it is properly working on the *server VLAN*.
  Internet should work.
* Connect laptop to *infrastructure* port.
* Laptop should pull a *10.9.9.0/24* network address, with the gateway
  *10.9.9.1*. This means it is properly working on the *infrastructure VLAN*.
  Internet should work.

.. rubric:: References

#. `Setting Management VLAN for Switches <https://community.ui.com/questions/5e765ef4-c734-413b-97fe-c38e5b33916e>`_
