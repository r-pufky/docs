.. _unifi-ap-setup:

Unifi AP Setup
##############
This will be used to setup the Unifi APs. See :ref:`example-network-diagram`.

.. important::
  Use a unique IP and hostname for each AP device.
  :ref:`example-network-diagram`.

#. Factory reset Unifi AP.
#. Connect AP to a `trunk-wifi` port (*core:8*, *wired:5*).
#. Connect laptop to a *management* port.

Set Static AP IP
****************
* Connect to Edgerouter GUI @ http://10.1.1.1.
* Reserve a static DHCP address for the switch.

.. uctree:: Add Static Reservation for Switch Management
  :key:   Services --> DHCP Server --> Management --> Action --> Leases
  :names: Map Static IP,
          › IP Address,
          › Name
  :data:  ,
          {AP IP},
          {AP NAME}
  :no_section:
  :hide_gui:

Configure Unifi AP
******************
* Connect to Unifi Controller @ http://localhost:8443.

.. warning::
  Wait up to *5* minutes for the AP to connect controller. If the device has
  pulled a *10.1.1.0/24* address, it should eventually appear if *L2 discovery*
  is enabled on controller.

:cmdmenu:`Devices --> AP --> Adopt`

.. ucontroller:: General Switch Setup
  :key:   Devices --> Switch --> Properties --> Config --> General
  :names: Alias,
          LED
  :data:  {AP NAME},
          use site settings
  :no_section:
  :hide_gui:

.. ucontroller:: Set Static Switch IP.
  :key:   Devices --> Switch --> Properties --> Config --> Network
  :names: Configure IP,
          › IP Address,
          › Preferred DNS,
          › Subnet Mask,
          › Gateway,
          › DNS Suffix
  :data:  Static,
          {AP IP},
          10.1.1.1,
          255.255.255.0,
          10.1.1.1,
          {YOUR DOMAIN}
  :no_section:
  :hide_gui:

  .. note::
    :cmdmenu:`Queue Changes --> Apply`

    * Wait for provisioning to finish.
    * Ensure switch is pingable. ``ping {AP IP}``.
    * Apply any firmware updates if needed.

.. ucontroller:: Set WLAN Group.
  :key:   Devices --> AP --> Properties --> Config --> WLANS
  :names: WLAN Group
  :data:  wifi
  :no_section:
  :hide_gui:

.. ucontroller:: Set Management VLAN.
  :key:   Devices --> AP --> Properties --> Config --> Services --> VLAN
  :names: Management VLAN
  :data:  LAN
  :no_section:
  :hide_gui:

Confirm Wireless Network Working
********************************
* Connect laptop to wifi network.
* Laptop should pull a *10.4.4.0/24* network address, with the gateway
  *10.4.4.1*. This means it is properly working on the *wifi VLAN*. Internet
  should work.