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

.. figure:: source/wired-switch.png
  :width: 90%

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

.. ubiquiti:: Add Static Reservation for Switch Management
  :path:      Services --> DHCP Server --> Management --> Action --> Leases
  :value0:    Map Static IP,
  :value1:    › IP Address, 10.1.1.7
  :value2:    › Name, wired

Connect to Unifi Controller @ http://localhost:8443.

.. ubiquiti:: Set Static Switch IP
  :path:      Devices --> Switch --> Properties --> Config --> Network
  :value0:    Configure IP, {STATIC}
  :value1:    › IP Address, 10.1.1.7
  :value2:    › Preferred DNS, 10.1.1.1
  :value3:    › Subnet Mask, 255.255.255.0
  :value4:    › Gateway, 10.1.1.1
  :value5:    › DNS Suffix, {DOMAIN}

  .. note::
    :cmdmenu:`Queue Changes --> Apply`

    * Wait for provisioning to finish.
    * Ensure switch is pingable. ``ping 10.1.1.7``.
    * Apply any firmware updates if needed.

Configure Wired Switch Management
*********************************
.. ubiquiti:: General Wired Switch Setup
  :path:      Devices --> Switch --> Properties --> Config --> General
  :value0:    Alias, wired
  :value1:    LED, use site settings

.. ubiquiti:: Wired Switch Services Setup
  :path:    Devices --> Switch --> Properties --> Config --> Services
  :value0:  VLAN,
  :value1:  › Management VLAN, LAN
  :value2:  › Spanning Tree, RSTP
  :value3:  › Priority, 32768
  :value4:  Security,
  :value5:  › ☐, Enable 802.1x control
  :value6:  SNMP,
  :value7:  › Location, {NONE}
  :value8:  › Contact, {NONE}

:cmdmenu:`Queue Changes --> Apply`

Configure VLANs on Ports
************************
.. ubiquiti:: Configure Switch VLANs
  :path:      Devices --> Switch --> Properties --> Ports
  :value0:    Port 1,
  :value1:    › Name, trunk
  :value2:    › Switch Port Profile, trunk-wired
  :value3:    Port 2-4,
  :value4:    › Name, wire
  :value5:    › Switch Port Profile, wired (2)
  :value6:    Port 5,
  :value7:    › Name, wifi
  :value8:    › Switch Port Profile, trunk-wifi
  :value9:    Port 6,
  :value10:   › Name, wire
  :value11:   › Switch Port Profile, wired (2)
  :value12:   › › Profile Overrides,
  :value13:   › › › PoE, {OFF}
  :value14:   Port 7,
  :value15:   › Name, management
  :value16:   › Switch Port Profile, All
  :value17:   › › Profile Overrides,
  :value18:   › › › PoE, {OFF}
  :value19:   Port 8,
  :value20:   › Name, wire
  :value21:   › Switch Port Profile, wired (2)
  :value22:   › › Profile Overrides,
  :value23:   › › › PoE, {OFF}

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

#. `Setting Management VLAN for Switches <https://community.ui.com/questions/5e765ef4-c734-413b-97fe-c38e5b33916e>`_
