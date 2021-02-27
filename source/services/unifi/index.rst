.. _service-unifi-controller:

Unifi Controller
################
Manage Ubiquity Unifi APs & Switches.

See `Unifi Docker and Documentation`_.

Read :ref:`example-vlan-network` for detailed configuration instructions on
an example network.

Ports
*****
.. ports:: Unifi Controller Ports
  :value0:      3478, {UDP},  {PUBLIC}, STUN
  :value1:      8080, {TCP},  {PUBLIC}, Device and controller communication
  :value2:      8443, {TCP},  {PUBLIC}, Controller GUI/API webface
  :value3:      8880, {TCP},  {PUBLIC}, HTTP portal redirection
  :value4:      8843, {TCP},  {PUBLIC}, HTTPS portal redirection
  :value5:      6789, {TCP}, {DISABLE}, UniFi mobile speed test
  :value6:     27117, {TCP}, {DISABLE}, local-bound database communication
  :value7: 5656-5699, {UDP}, {DISABLE}, AP-EDU broadcasting
  :value8:     10001, {UDP}, {DISABLE}, AP discovery
  :value9:      1900, {UDP}, {DISABLE}, "Make controller discoverable on L2
                                        network" in controller setting
  :open:

Files
*****
.. files:: Unifi Controller Files
  :value0: /config, Unifi main service directory
  :open:

Docker Creation
***************
You can copy your existing configuration to docker ``/config`` directory
adjusting for paths.

* ``unstable`` is the current release branch. ``latest`` is ``5.6.x`` branch.

.. code-block:: yaml
  :caption: Docker Compose

  unifi:
    image: linuxserver/unifi:unstable
    restart: unless-stopped
    ports:
      - '3478:3478/udp'
      - '8080:8080'
      - '8443:8443'
      - '8880:8880'
      - '8843:8843'
    environment:
      - PGID=1001
      - PUID=1001
      - TZ=America/Los_Angeles
    volumes:
      - /data/services/unifi:/config
      - /etc/localtime:/etc/localtime:ro

Reverse Proxy Setup
*******************
Allows you to isolate your containers as well as wrap connections in SSL. See
:ref:`service-nginx` for more details. See
:ref:`service-nginx-base-proxy-control` for basic proxy configuration.

Using Subdomains
================
.. literalinclude:: source/subdomain.conf
  :caption: **0644 root root** ``nginx/conf.d/reverse-proxy.conf``

Using Subpaths
==============
.. literalinclude:: source/subpath.conf
  :caption: **0644 root root** ``nginx/conf.d/reverse-proxy.conf``

Configuration
*************
Ensure DNS/hosts are setup for Unifi controller.

Read :ref:`example-vlan-network` for a in-depth walkthrough.

Router Configuration
====================
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

.. literalinclude:: source/dhcpd.conf
  :caption: **0644 root root** ``dhcpd.conf``

.. rubric:: References

#. `Unifi Ports <https://help.ui.com/hc/en-us/articles/218506997-UniFi-Ports-Used>`_
#. `Unifi controller DHCP option 43 <https://help.ui.com/hc/en-us/articles/204909754-UniFi-Device-Adoption-Methods-for-Remote-UniFi-Controllers#7>`_

.. _Unifi Docker and Documentation: https://hub.docker.com/r/linuxserver/unifi/
