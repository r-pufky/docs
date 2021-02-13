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

.. ucontroller:: Set Static Switch IP
  :key_title:    Devices --> Switch --> Properties --> Config --> Network
  :option:       Configure IP,
                 › IP Address,
                 › Preferred DNS,
                 › Subnet Mask,
                 › Gateway,
                 › DNS Suffix
  :setting:      Static,
                 10.1.1.7,
                 10.1.1.1,
                 255.255.255.0,
                 10.1.1.1,
                 {YOUR DOMAIN}
  :no_section:
  :no_caption:
  :no_launch:

    .. note::
      :cmdmenu:`Queue Changes --> Apply`

      * Wait for provisioning to finish.
      * Ensure switch is pingable. ``ping 10.1.1.7``.
      * Apply any firmware updates if needed.

Configure Wired Switch Management
*********************************
.. ucontroller:: General Wired Switch Setup
  :key_title:    Devices --> Switch --> Properties --> Config --> General
  :option:       Alias,
                 LED
  :setting:      wired,
                 use site settings
  :no_section:
  :no_caption:
  :no_launch:

.. ucontroller:: Wired Switch Services Setup
  :key_title:    Devices --> Switch --> Properties --> Config --> Services
  :option:       VLAN,
                 › Management VLAN,
                 › Spanning Tree,
                 › Priority,
                 Security,
                 › ☐,
                 SNMP,
                 › Location,
                 › Contact
  :setting:      ,
                 LAN,
                 RSTP,
                 32768,
                 ,
                 Enable 802.1x control,
                 ,
                 ,
                 ​ 
  :no_section:
  :no_caption:
  :no_launch:

:cmdmenu:`Queue Changes --> Apply`

Configure VLANs on Ports
************************
.. ucontroller:: Configure Switch VLANs
  :key_title:    Devices --> Switch --> Properties --> Ports
  :option:       Port 1,
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
  :setting:      ,
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
  :no_caption:
  :no_launch:

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
