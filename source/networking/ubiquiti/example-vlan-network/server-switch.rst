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

.. uctree:: Add Static Reservation for Switch Management
  :key:   Services --> DHCP Server --> Management --> Action --> Leases
  :names: Map Static IP,
          › IP Address,
          › Name
  :data:  ,
          10.1.1.6,
          server
  :no_section:
  :hide_gui:

Connect to Unifi Controller @ http://localhost:8443.

.. ucontroller:: Set Static Switch IP.
  :key:   Devices --> Switch --> Properties --> Config --> Network
  :names: Configure IP,
          › IP Address,
          › Preferred DNS,
          › Subnet Mask,
          › Gateway,
          › DNS Suffix
  :data:  Static,
          10.1.1.6,
          10.1.1.1,
          255.255.255.0,
          10.1.1.1,
          {YOUR DOMAIN}
  :no_section:
  :hide_gui:

  .. note::
    :cmdmenu:`Queue Changes --> Apply`

    * Wait for provisioning to finish.
    * Ensure switch is pingable. ``ping 10.1.1.6``.
    * Apply any firmware updates if needed.

Configure Server Switch Management
**********************************
.. ucontroller:: General Server Switch Setup
  :key:   Devices --> Switch --> Properties --> Config --> General
  :names: Alias,
          LED
  :data:  server,
          use site settings
  :no_section:
  :hide_gui:

.. ucontroller::  Server Switch Services Setup
  :key:   Devices --> Switch --> Properties --> Config --> Services
  :names: VLAN,
          › Management VLAN,
          › Spanning Tree,
          › Priority,
          Security,
          › ☐,
          SNMP,
          › Location,
          › Contact
  :data:  ,
          LAN,
          RSTP,
          32768,
          ,
          Enable 802.1x control,
          ,
          ,
          ​ 
  :no_section:
  :hide_gui:

:cmdmenu:`Queue Changes --> Apply`

Configure VLANs on Ports
************************
.. ucontroller:: Configure Switch VLANs
  :key:   Devices --> Switch --> Properties --> Ports
  :names: Port 1,
          › Name,
          › Switch Port Profile,
          Port 2-4,
          › Name,
          › Switch Port Profile,
          Port 5,
          › Name,
          › Switch Port Profile,
          › › Profile Overrides,
          › › › PoE,
          Port 6,
          › Name,
          › Switch Port Profile,
          › › Profile Overrides,
          › › › PoE,
          Port 7,
          › Name,
          › Switch Port Profile,
          › › Profile Overrides,
          › › › PoE,
          Port 8,
          › Name,
          › Switch Port Profile
  :data:  ,
          trunk,
          trunk-server,
          ,
          serve,
          server (5),
          ,
          infra,
          infrastructure (9),
          ,
          Off,
          ,
          serve,
          server (5),
          ,
          Off,
          ,
          management,
          All,
          ,
          Off,
          ,
          disable,
          Disabled
  :no_section:
  :hide_gui:

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

#. `Setting Management VLAN for Switches <https://community.ubnt.com/t5/UniFi-Routing-Switching/Setting-Management-VLAN-for-Switches/td-p/2279619>`_
