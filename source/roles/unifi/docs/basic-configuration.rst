.. _service-unifi-basic-configuration:

Basic Configuration
###################
Ensure DNS/hosts are setup for Unifi controller. Read
:ref:`example-vlan-network` for a in-depth walkthrough.

Router Configuration
********************
Forward traffic to Unifi Controller for AP to be managed - will be located
slightly differently for each router.

.. note::
  These are only needed if not using :term:`VLAN` separation.

.. gui::   Allow AP management to controller.
  :label:  Ubiquiti
  :path:   Firewall/NAT --> Firewall Policies -->
           WIFI_IN -->
           Actions -->
           Edit Ruleset -->
           Add New Rule
  :value0: Description, AP Management
  :value1: Source, {IP}
  :value2: Destination, {CONTROLLER}
  :value3: Destination Port, 8443 8080
  :value4: Protocol, {TCP}
  :value5: Action, {ACCEPT}

.. gui::   Allow AP STUN to controller.
  :label:  Ubiquiti
  :path:   Firewall/NAT --> Firewall Policies -->
           WIFI_IN -->
           Actions -->
           Edit Ruleset -->
           Add New Rule
  :value0: Description, AP STUN
  :value1: Source, {IP}
  :value2: Destination, {CONTROLLER}
  :value3: Destination, 3478
  :value4: Protocol, {UDP}
  :value5: Action, {ACCEPT}

Enable Unifi Controller Assignment in EdgeOS or DHCP Option 43
==============================================================
This should be enabled for subnets in which the AP will reside. This will allow
the AP to be auto-detected by the controller.

See :ref:`edgerouter-vlan-setup-dns` for setting up the ``Unifi Controller``
option for DHCP on EdgeOS.

For non-EdgeOS routers, this can be enabled in using ``option 43``.

`Reference <https://help.ui.com/hc/en-us/articles/204909754-UniFi-Device-Adoption-Methods-for-Remote-UniFi-Controllers#7>`__

.. literalinclude:: source/dhcpd.conf
  :caption: **0644 root root** ``dhcpd.conf``
