.. _service-pihole:

`Pi-Hole`_
##########
Block nefarious websites & Ads.

This will setup ad-blocking in the following manner:

#. Router upstream DNS servers set to ``1.1.1.1``, ``8.8.8.8``.
#. Router DHCP Assigns **Pi-Hole** as primary DNS server for clients.
#. Router uses DNAT to force all DNS requests to **Pi-Hole** (optional).
#. Pi-Hole upstream DNS server set to **router**.

Clients will send DNS requets to Pi-Hole. Pi-Hole will either block, resolve or
foward those requests to the router. The router will be able to resolve local
DNS names and forward remaining unknown queries to upstream DNS servers.

Optionally, if the router supports *destination NAT*, all DNS traffic will be
routed directly to *Pi-Hole*. This catches hard-coded DNS servers that many
phone apps, IoT devices, and applications use.

Pi-Hole will have static hosts set in ``/etc/hosts`` to resolve multiple
hostnames resolving to the same IP.

#. :ref:`service-pihole-setup`.
#. :ref:`service-pihole-configuration`.
#. :ref:`service-pihole-force-https-admin`.
#. :ref:`service-pihole-troubleshooting`.

.. _Pi-Hole: https://pi-hole.net/

.. toctree::
   :hidden:
   :maxdepth: -1

   setup
   configuration
   https-admin
   troubleshooting