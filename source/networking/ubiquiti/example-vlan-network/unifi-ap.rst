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

.. ubiquiti:: Add Static Reservation for Switch Management
  :path:      Services --> DHCP Server --> Management --> Action --> Leases
  :value0:    Map Static IP,
  :value1:    › IP Address, {IP}
  :value2:    › Name, {HOST}

Configure Unifi AP
******************
* Connect to Unifi Controller @ http://localhost:8443.

.. warning::
  Wait up to *5* minutes for the AP to connect controller. If the device has
  pulled a *10.1.1.0/24* address, it should eventually appear if *L2 discovery*
  is enabled on controller.

:cmdmenu:`Devices --> AP --> Adopt`

.. ubiquiti:: General Switch Setup
  :path:      Devices --> Switch --> Properties --> Config --> General
  :value0:    Alias, {HOST}
  :value1:    LED, use site settings

.. ubiquiti:: Set Static Switch IP
  :path:      Devices --> Switch --> Properties --> Config --> Network
  :value0:    Configure IP, {STATIC}
  :value1:    › IP Address, {IP}
  :value2:    › Preferred DNS, 10.1.1.1
  :value3:    › Subnet Mask, 255.255.255.0
  :value4:    › Gateway, 10.1.1.1
  :value5:    › DNS Suffix, {DOMAIN}

  .. note::
    :cmdmenu:`Queue Changes --> Apply`

    * Wait for provisioning to finish.
    * HOST/IP is AP. Ensure switch is pingable. ``ping {AP IP}``.
    * Apply any firmware updates if needed.

.. ubiquiti:: Set WLAN Group
  :path:      Devices --> AP --> Properties --> Config --> WLANS
  :value0:    WLAN Group, wifi

.. ubiquiti:: Set Management VLAN
  :path:      Devices --> AP --> Properties --> Config --> Services --> VLAN
  :value0:    Management VLAN, LAN

Confirm Wireless Network Working
********************************
* Connect laptop to wifi network.
* Laptop should pull a *10.4.4.0/24* network address, with the gateway
  *10.4.4.1*. This means it is properly working on the *wifi VLAN*. Internet
  should work.
