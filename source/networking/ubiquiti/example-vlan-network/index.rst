.. _example-vlan-network:

Edgerouter Docker Unifi Controller VLAN Setup
#############################################
Example walkthorugh of creating a VLAN based network using an edgerouter as a
router/firewall with a Docker Unifi Controller managing Unifi Switch/APs.

.. _example-vlan-overview:

Network Overview
****************
See :ref:`vlan-101` for detailed VLAN concept information. The example network
:ref:`example-network-diagram` will be laid out as follows:

+------------+----------------+
| Color      | Network        |
+============+================+
| White      | Trunk: All     |
+------------+----------------+
| Purple     | Local Router   |
+------------+----------------+
| Teal       | Trunk: Wired   |
+------------+----------------+
| Light Blue | Trunk: Server  |
+------------+----------------+
| Dark Blue  | Trunk: Wifi    |
+------------+----------------+
| Orange     | Wired          |
+------------+----------------+
| Green      | Server         |
+------------+----------------+
| Yellow     | Infrastructure |
+------------+----------------+

.. _vlan-table:

+----------------+--------+-------------+----------+------------+------------+----------+-----------------------------------------------------------------+
| Network Name   | VLANID | Network     | Router   | DHCP Start | DHCP End   | DNS      |  Usage/Notes                                                    |
+================+========+=============+==========+============+============+==========+=================================================================+
| Management     | 1      | 10.1.1.0/24 | 10.1.1.1 | 10.1.1.10  | 10.1.1.240 | 10.1.1.1 | Untagged traffic (VLAN1). Management traffic.                   |
+----------------+--------+-------------+----------+------------+------------+----------+-----------------------------------------------------------------+
| Wired          | 2      | 10.2.2.0/24 | 10.2.2.1 | 10.2.2.10  | 10.2.2.240 | 10.2.2.1 | General use network for hard-wired devices. No hosted services. |
+----------------+--------+-------------+----------+------------+------------+----------+-----------------------------------------------------------------+
| IOT            | 3      | 10.3.3.0/24 | 10.3.3.1 | 10.3.3.10  | 10.3.3.240 | 10.3.3.1 | Internet of Shit devices. Internet only. Peer Isolation.        |
+----------------+--------+-------------+----------+------------+------------+----------+-----------------------------------------------------------------+
| Wifi           | 4      | 10.4.4.0/24 | 10.4.4.1 | 10.4.4.10  | 10.4.4.240 | 10.4.4.1 | Wifi Network. Internet only. Peer Isolation.                    |
+----------------+--------+-------------+----------+------------+------------+----------+-----------------------------------------------------------------+
| Server         | 5      | 10.5.5.0/24 | 10.5.5.1 | 10.5.5.10  | 10.5.5.240 | 10.5.5.1 | Servers running general services to be used.                    |
+----------------+--------+-------------+----------+------------+------------+----------+-----------------------------------------------------------------+
| Infrastructure | 9      | 10.9.9.0/24 | 10.9.9.1 | 10.9.9.10  | 10.9.9.240 | 10.9.9.1 | Critical always-on infastructure-only services like DNS, DHCP.  |
+----------------+--------+-------------+----------+------------+------------+----------+-----------------------------------------------------------------+

Switch Port Profiles are applied to switch ports to define traffic allowed
through the port:

+----------------+-----+----------------+------------------------+---------------+
| Name           | PoE | Native Network | Tagged Networks        | Voice Network |
+================+=====+================+========================+===============+
| infrastructure | N/A | infrastructure | None                   | None          |
+----------------+-----+----------------+------------------------+---------------+
| iot            | N/A | iot            | None                   | None          |
+----------------+-----+----------------+------------------------+---------------+
| server         | N/A | server         | None                   | None          |
+----------------+-----+----------------+------------------------+---------------+
| wifi           | N/A | wifi           | None                   | None          |
+----------------+-----+----------------+------------------------+---------------+
| wired          | N/A | wired          | None                   | None          |
+----------------+-----+----------------+------------------------+---------------+
| trunk-server   | Off | LAN            | server, infrastructure | None          |
+----------------+-----+----------------+------------------------+---------------+
| trunk-wired    | Off | LAN            | wired, wifi            | None          |
+----------------+-----+----------------+------------------------+---------------+
| trunk-wifi     | PoE | LAN            | wifi                   | None          |
+----------------+-----+----------------+------------------------+---------------+

Infrastructure IP assignments on management network:

+---------------+-----------+--------+
| Device        | IP        | Name   |
+===============+===========+========+
| Core Switch   | 10.1.1.5  | core   |
+---------------+-----------+--------+
| Server Switch | 10.1.1.6  | server |
+---------------+-----------+--------+
| Wired Switch  | 10.1.1.7  | wired  |
+---------------+-----------+--------+
| Unifi AP 1    | 10.1.1.70 | wifi1  |
+---------------+-----------+--------+
| Unifi AP 2    | 10.1.1.75 | wifi2  |
+---------------+-----------+--------+
| Edgerouter    | 10.1.1.1  | edge   |
+---------------+-----------+--------+

Before You Begin
****************
Note and prep these things before starting:

* Always set an spare port on your router with a static management address
  without VLANS so you can get in if something breaks.
* Set a spare port on switches for :term:`Management VLAN` or :term:`ALL` access
  so you can locally manage devices if something goes wrong.
* Make *backups of existing Edgerouter & Unifi Controller configs*. Export all
  data.
* Install Unifi controller on a laptop.
* Set static IP for laptop, on the :ref:`Management Network <vlan-table>`.
* Always **factory-reset** equipment before configuring. This garantees fresh
  state.
* Always physically label your switch ports so you can easily remember them when
  you come back in a year.
* Switches/APs/Routers should always have static IP information set, so they are
  at a known address if they ever get mis-configured. Plan and document static
  IPs for these devices before implementation.

.. rubric:: References

#. `Create schedule task with event log trigger <https://stackoverflow.com/questions/42801733/creating-a-scheduled-task-which-uses-a-specific-event-log-entry-as-a-trigger>`_
#. `Unifi Controller V5 Manual <https://dl.ubnt.com/guides/UniFi/UniFi_Controller_V5_UG.pdf>`_
#. `VLANs with Unifi and PFSense <https://www.youtube.com/watch?v=b2w1Ywt081o>`_
#. `Complete UniFi Setup Start to Finish <https://www.youtube.com/watch?v=HcfIpTso_Ys>`_
#. `UAP with Guest WLAN & VLAN Trunks VIF <https://www.youtube.com/watch?v=SKeFqFhBwJY&t=>`_
#. `Unifi Enterprise Networking <https://www.youtube.com/watch?v=L9gZQh1rAMc>`_
#. `Ubiquiti EdgeRouter Lite SOHO Network Design <https://www.handymanhowto.com/ubiquiti-edgerouter-lite-soho-network-design/>`_
#. `This is software-defined networking, apparently <https://arstechnica.com/information-technology/2018/07/enterprise-wi-fi-at-home-part-two-reflecting-on-almost-three-years-with-pro-gear/5/>`_

.. toctree::
   :hidden:
   :maxdepth: -1

   Initial Edgerouter Configuration <edgerouter-vlan>
   Unifi Controller Setup <unifi-controller-vlan>
   Core Switch Setup <core-swtich>
   Server Switch Setup <server-switch>
   Wired Switch Setup <wired-switch>
   Unifi Controller Wifi Setup <unifi-controller-wifi>
   Unifi APs Setup <unifi-ap>
   <example-network-diagram>