.. _service-unifi-controller:

Unifi Controller
################
Manage Ubiquity Unifi APs & Switches.

See `Unifi Docker and Documentation`_.

Read :ref:`example-vlan-network` for detailed configuration instructions on
an example network.

.. gport:: Ports (Unifi Controller)
  :port:     3478,
             8080,
             8443,
             8880,
             8843,
             6789,
             27117,
             5656-5699,
             10001,
             1900
  :protocol: UDP,
             TCP,
             TCP,
             TCP,
             TCP,
             TCP,
             TCP,
             UDP,
             UDP,
             UDP
  :type:     Public,
             Public,
             Public,
             Public,
             Public,
             Disabled,
             Disabled,
             Disabled,
             Disabled,
             Disabled
  :purpose:  Port used for STUN.,
             Port used for device and controller communication.,
             Port used for controller GUI/API as seen in a web browser.,
             Port used for HTTP portal redirection.,
             Port used for HTTPS portal redirection.,
             Port used for UniFi mobile speed test.,
             Port used for local-bound database communication.,
             Ports used by AP-EDU broadcasting.,
             Port used for AP discovery.,
             Port used for "Make controller discoverable on L2 network" in controller settings.
  :no_key_title:
  :no_caption:
  :no_launch:

.. gflocation:: Important File Locations (Unifi Controller)
  :file:    /config
  :purpose: Unifi main service directory.
  :no_key_title:
  :no_caption:
  :no_launch:

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

.. ufirewall:: Allow AP management to controller.
  :key_title:  Firewall Policies -->
               WIFI_IN -->
               Actions -->
               Interfaces
  :option:     Description,
               Source,
               Destination,
               Protocol,
               Action
  :setting:    AP Management,
               {AP IP},
               {Unifi Controller IP} 8443 8080,
               TCP,
               Accept
  :no_section:
  :no_caption:
  :no_launch:

.. ufirewall:: Allow AP STUN to controller.
  :key_title:  Firewall Policies -->
               WIFI_IN -->
               Actions -->
               Interfaces
  :option:     Description,
               Source,
               Destination,
               Protocol,
               Action
  :setting:    AP STUN,
               {AP IP},
               {Unifi Controller IP} 3478,
               UDP,
               Accept
  :no_section:
  :no_caption:
  :no_launch:

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
