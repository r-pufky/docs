.. _edgerouter-vlan-setup:

Edgerouter VLAN Setup
#####################
This will setup the edgerouter in a `router on a stick`_ configuration using
VLANs, with no subnet restrictions (these will be applied after setup).
:ref:`example-network-diagram`.

.. aafig::
  :name: Example VLAN Networking Using ER-4.

         'Edgerouter ER-4'
  +-----------------------------+
  | +----+ +----+ +----+ +----+ |
  | |eth0| |eth1| |eth2| |eth3| +
  | +----+ +----+ +----+ +----+ |
  +---+--------------------+----+
      |                    |
     ++                'Internet (eth3)'

.. figure:: source/edgerouter.png
  :width: 90%

Reset & Login to Router
***********************
#. Factory reset edgerouter.
#. Connect *eth1*, set laptop static ``192.168.1.5``, gateway: ``192.168.1.1``.
#. Connect to Edgerouter GUI @ http://192.168.1.1.

   * Default credentials: ``ubnt``/``ubnt``.

Basic Setup Wizard
******************
Basic Setup (Basic Setup is the same as *WAN+2LAN2*).

.. uctree:: Configure WAN / Internet port.
  :key:    Internet (eth3/SFP)
  :names:  ☑,
           › Address,
           › Gateway,
           › DNS,
           ☐,
           ☑,
           ☐,
           ☐
  :data:   Static IP,
           {YOUR PUBLIC IP} / {PUBLIC IP NETMASK},
           {YOUR ISP GATEWAY},
           1.1.1.1,
           Internet connection is on VLAN,
           Enable the default firewall,
           Enable DHCPv6 Prefix Delegation,
           Bridge LAN interfaces into a single network
  :no_section:
  :hide_gui:

.. uctree:: Configure LAN Management Ports.
  :key:    LAN Ports (eth2)
  :names:  Address
  :data:   192.168.2.1 / 255.255.255.0
  :no_section:
  :hide_gui:

  .. note::
    This will become static management port for the router, in case anything
    happens.

.. uctree:: Configure New Admin User.
  :key:   User Setup
  :names: Username,
          Password
  :data:  {USERNAME},
          {PASSWORD}
  :no_section:
  :hide_gui:

Apply and reboot router.

.. hint::
  The reason to use the SFP connection for Internet is to make it physically
  distinguishable from the rest of the ports on the router, even if it just
  converted immediately to ethernet.

Setup VLANs on eth0
*******************
#. Set laptop DHCP. Connect to *eth2*.
#. Connect to Edgerouter GUI @ http://192.168.1.1.

.. uctree:: Configure Host and Domain.
  :key:   Management Settings --> System
  :names: Host Name,
          Domain Name,
          ☐
  :data:  {ROUTER HOSTNAME},
          {YOUR DOMAIN},
          Ubntu Discovery
  :no_section:
  :hide_gui:

.. uctree:: Configure SSH Server.
  :key:   Management Settings --> SSH Server
  :names: ☑,
          Port
  :data:  Enable,
          {SSH PORT}
  :no_section:
  :hide_gui:

.. uctree:: Define Management Network on Interfaces.
  :key:   Dashboard --> eth0 --> Actions --> Config
  :names: Address,
          Address
  :data:  Manually define IP address,
          10.1.1.1/24
  :no_section:
  :hide_gui:

.. important::
  This handles untagged traffic coming into the router; this is the
  :term:`Management VLAN` network.

.. uctree:: Add Wired Network VLAN.
  :key:   Dashboard --> Add Interface --> Add VLAN
  :names: VLANID,
          Interface,
          Description,
          Address,
          Address
  :data:  2,
          eth0,
          {VLAN DESCRIPTION},
          Manually define IP address,
          10.2.2.1/24
  :no_section:
  :hide_gui:

.. warning::
  Add all VLANS using the :ref:`VLAN Table <vlan-table>` to *eth0*.
  :term:`Management VLAN` is not explicitly defined as a VLAN -- untagged
  traffic coming into *eth0* **IS** management traffic.

Setup DHCP & DNS for VLANs
**************************

.. uctree:: Add DHCP Server for Each Network.
  :key:   Services --> DHCP Server --> Add DHCP Server
  :names: DHCP Name,
          Subnet,
          Range Start,
          Range End,
          Router,
          DNS 1,
          Domain,
          Domain
  :data:  Wired,
          10.2.2.0/24,
          10.2.2.10,
          10.2.2.240,
          10.2.2.1,
          10.2.2.1,
          {YOUR DOMAIN},
          ☑ Enable
  :no_section:
  :hide_gui:

.. warning::
  Add DHCP for all VLANS. For the *management* DHCP server, set the *Unifi
  Controller* field to the IP for the permenant Unifi Controller and not your
  laptop.

:cmdmenu:`Services > DNS > Interface > Add Listen Interface`

.. note::
  Add for all networks and VLANS. VLANS will appear as *eth0.vlanid*.

Confirm Management Network Working
**********************************
* Connect laptop to *eth0*.
* Laptop should pull a :term:`management VLAN` network address, with the gateway
  *10.1.1.1*. This means untagged traffic is being properly assigned to the
  management network.

.. _router on a stick: https://help.ubnt.com/hc/en-us/articles/204959444-EdgeRouter-Router-on-a-Stick
