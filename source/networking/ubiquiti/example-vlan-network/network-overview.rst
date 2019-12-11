.. _network-overview:

Network Overview
################
See :ref:`vlan-101` for detailed VLAN concept information. The example network
:ref:`example-network-diagram` will be laid out as follows:

.. gtable:: Network Overview
  :header: Color,
           Network
  :c0:     White,
           Purple,
           Teal,
           Light Blue,
           Dark Blue,
           Orange,
           Green,
           Yellow
  :c1:     Trunk: All,
           Local Router,
           Trunk: Wired,
           Trunk: Server,
           Trunk: Wifi,
           Wired,
           Server,
           Infrastructure
  :no_key_title:
  :no_section:
  :no_caption:
  :no_launch:

.. _vlan-table:

.. gtable:: VLAN Table
  :header: Network Name,
           VLANID,
           Network,
           Router,
           DHCP Start,
           DHCP End,
           DNS,
           Usage/Notes
  :c0:     Management,
           Wired,
           IOT,
           Wifi,
           Server,
           Infrastructure
  :c1:     1,
           2,
           3,
           4,
           5,
           9
  :c2:     10.1.1.0/24,
           10.2.2.0/24,
           10.3.3.0/24,
           10.4.4.0/24,
           10.5.5.0/24,
           10.9.9.0/24
  :c3:     10.1.1.1,
           10.2.2.1,
           10.3.3.1,
           10.4.4.1,
           10.5.5.1,
           10.9.9.1
  :c4:     10.1.1.10,
           10.2.2.10,
           10.3.3.10,
           10.4.4.10,
           10.5.5.10,
           10.9.9.10
  :c5:     10.1.1.240,
           10.2.2.240,
           10.3.3.240,
           10.4.4.240,
           10.5.5.240,
           10.9.9.240
  :c6:     10.1.1.1,
           10.2.2.1,
           10.3.3.1,
           10.4.4.1,
           10.5.5.1,
           10.9.9.1
  :c7:     Untagged traffic (VLAN1). Management traffic.,
           General use network for hard-wired devices. No hosted services.,
           Internet of Shit devices. Internet only. Peer Isolation.,
           Wifi Network. Internet only. Peer Isolation.,
           Servers running general services to be used.,
           Critical always-on infastructure-only services like DNS/DHCP.
  :no_key_title:
  :no_section:
  :no_caption:
  :no_launch:

.. _swtich-port-profiles:

Switch Port Profiles are applied to switch ports to define traffic allowed
through the port:

.. gtable:: Switch Port Profiles
  :header: Name;
           PoE;
           Native Network;
           Tagged Networks;
           Voice Network
  :c0:     infrastructure;
           iot;
           server;
           wifi;
           wired;
           trunk-server;
           trunk-wired;
           trunk-wifi
  :c1:     N/A;
           N/A;
           N/A;
           N/A;
           N/A;
           Off;
           Off;
           PoE
  :c2:     infrastructure;
           iot;
           server;
           wifi;
           wired;
           LAN;
           LAN;
           LAN
  :c3:     None;
           None;
           None;
           None;
           None;
           server, infrastructure;
           wired, wifi;
           wifi
  :c4:     None;
           None;
           None;
           None;
           None;
           None;
           None;
           None
  :delim: ;
  :no_key_title:
  :no_section:
  :no_caption:
  :no_launch:

.. _ip-assignments:

Infrastructure IP assignments on management network:

.. gtable:: IP Assignments
  :header: Device,
           IP,
           Name
  :c0:     Core Switch,
           Server Switch,
           Wired Switch,
           Unifi AP 1,
           Unifi AP 2,
           Edgerouter
  :c1:     10.1.1.5,
           10.1.1.6,
           10.1.1.7,
           10.1.1.70,
           10.1.1.75,
           10.1.1.1
  :c2:     core,
           server,
           wired,
           wifi1,
           wifi2,
           edge
  :no_key_title:
  :no_section:
  :no_caption:
  :no_launch: