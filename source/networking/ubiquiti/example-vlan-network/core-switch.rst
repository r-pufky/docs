.. _core-switch-vlan-setup:

Core Switch VLAN Setup
######################
This will setup the core switch using VLANs according to example network. See
:ref:`example-network-diagram`.

.. aafig::
  :name: Unifi US-8-60W (Core).

     |    'Unifi US-8-60W (Core)'
  +--+------------------------------+
  | +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ |
  | |A| |D| |W| |S| |D| |D| |A| |I| |
  | +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ |
  +----------+---+---------------+--+
             |   |               |
             |   |           'Unifi AP 1 (8)'

Setup Core Switch
*****************
This switch handles trunking to the router upstream and connections downstream
to switches/APs.

#. Factory reset switch.
#. Connect laptop directly to *port 7* on new switch. Any port that is not going
   to be used for trunking or VLANs is fine.
#. Connect switch trunk *port 1* to *eth0* on edgerouter.
#. Connect to Unifi Controller @ http://localhost:8443.

Adopt Core Switch
=================
:cmdmenu:`Devices --> Switch --> Adopt`

.. warning::
  The initial switch IP may appear different (e.g. the LAN network defined on
  the controller); this is expected and is the default network for any new
  Unifi device adopted. This will automatically correct during adoption. See
  [adoption troubleshooting][xc] if the device does not adopt.

Set Static Switch IP
====================
#. Connect to Edgerouter GUI @ http://192.168.1.1.
#. Reserve a static DHCP address for the switch.

.. uctree:: Add Static Reservation for Switch Management
  :key:   Services --> DHCP Server --> Management --> Action --> Leases
  :names: Map Static IP,
          › IP Address,
          › Name
  :data:  ,
          10.1.1.5,
          core
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
          10.1.1.5,
          10.1.1.1,
          255.255.255.0,
          10.1.1.1,
          {YOUR DOMAIN}
  :no_section:
  :hide_gui:

  .. note::
    :cmdmenu:`Queue Changes --> Apply`

    * Wait for provisioning to finish.
    * Ensure switch is pingable. ``ping 10.1.1.5``.
    * Apply any firmware updates if needed.

Configure Basic Switch Management
*********************************
.. ucontroller:: General Switch Setup
  :key:   Devices --> Switch --> Properties --> Config --> General
  :names: Alias,
          LED
  :data:  core,
          use site settings
  :no_section:
  :hide_gui:

.. ucontroller:: Switch Services Setup
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
          {REPLACE WITH UNICODE BLANK SPACE CHARACTER}
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
          Port 2,
          › Name,
          › Switch Port Profile,
          Port 3,
          › Name,
          › Switch Port Profile,
          Port 4,
          › Name,
          › Switch Port Profile,
          Port 5-6,
          › Name,
          › Switch Port Profile,
          Port 7,
          › Name,
          › Switch Port Profile,
          › › Profile Overrides,
          › › › PoE,
          Port 8,
          › Name,
          › Switch Port Profile,
  :data:  ,
          trunk,
          All,
          ,
          disable,
          Disabled,
          ,
          wired,
          trunk-wired,
          ,
          server,
          trunk-server,
          ,
          disable,
          Disabled,
          ,
          management,
          All,
          ,
          Off,
          ,
          wifi,
          trunk-wifi
  :no_section:
  :hide_gui:

* Port 1:
  * Name: `trunk`
  * Switch Port Profile: `All`
* Port 2:
  * Name: `disable`
  * Switch Port Profile: `Disabled`
* Port 3:
  * Name: `wired`
  * Switch Port Profiles: `trunk-wired`
* Port 4:
  * Name: `server`
  * Switch Port Profiles: `trunk-server`
* Port 5-6:
  * Name: `disable`
  * Switch Port Profiles: `Disabled`
* Port 7:
  * Name: `management`
  * Switch Port Profiles: `All`
  * Profile Overrides
    * PoE: `Off`
* Port 8:
  * Name: `wifi`
  * Switch Port Profiles: `trunk-wifi`

> :warning:
> Switch will re-provision for each port modification. Wait for provisioning
> to complete before proceeding through each port.

.. rubric:: References

#. `Setting Management VLAN for Switches <https://community.ubnt.com/t5/UniFi-Routing-Switching/Setting-Management-VLAN-for-Switches/td-p/2279619>`_

[xc]: README.md#unifi-device-troubleshooting