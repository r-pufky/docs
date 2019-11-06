.. _wired-switch-vlan-setup:

Wired Switch VLAN Setup
#######################
This will setup the wired switch using VLANs according to example network. See
:ref:`example-network-diagram`.

.. aafig::
  :name: Unifi US-8-60W (Wired)

     |   'Unifi US-8-60W (Wired)''
  +--+------------------------------+
  | +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ |
  | |A| |w| |w| |w| |I| |w| |A| |w| |
  | +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ |
  +---------------------------------+

Setup Wired Switch
******************
This switch handles trunking wired and wifi connections upstream to the core
switch.

#. Factory reset switch.
#. Connect laptop directly to *port 7* on new switch. Any port that is not going
   to be used for trunking or VLANs is fine.
#. Connect switch trunk *port 1* to *port 3* (Wired Trunk) on core switch.
#. Connect to Unifi Controller @ http://localhost:8443.

Adopt Wired Switch
==================
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
          10.1.1.7,
          wired
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
          10.1.1.7,
          10.1.1.1,
          255.255.255.0,
          10.1.1.1,
          {YOUR DOMAIN}
  :no_section:
  :hide_gui:

  .. note::
    :cmdmenu:`Queue Changes --> Apply`

    * Wait for provisioning to finish.
    * Ensure switch is pingable. ``ping 10.1.1.7``.
    * Apply any firmware updates if needed.

Configure Wired Switch Management
*********************************
.. ucontroller:: General Wired Switch Setup
  :key:   Devices --> Switch --> Properties --> Config --> General
  :names: Alias,
          LED
  :data:  wired,
          use site settings
  :no_section:
  :hide_gui:

.. ucontroller:: Wired Switch Services Setup
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
          › Switch Port Profile,
          › › Profile Overrides,
          › › › PoE
  :data:  ,
          trunk,
          trunk-wired,
          ,
          wire,
          wired (2),
          ,
          wifi,
          trunk-wifi,
          ,
          wire,
          wired (2),
          ,
          Off,
          ,
          management,
          All,
          ,
          Off,
          ,
          wire,
          wired (2),
          ,
          Off
  :no_section:
  :hide_gui:

  .. warning::
    Switch will re-provision for each port modification. Wait for provisioning
    to complete before proceeding through each port.

Confirm Wired Network Working
*****************************
* Connect laptop to *wired* port.
* Laptop should pull a *10.2.2.0/24* network address, with the gateway
  *10.2.2.1*. This means it is properly working on the *wired VLAN*. Internet
  should work.

.. rubric:: References

#. `Setting Management VLAN for Switches <https://community.ubnt.com/t5/UniFi-Routing-Switching/Setting-Management-VLAN-for-Switches/td-p/2279619>`_