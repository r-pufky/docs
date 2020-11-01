.. _networking-edge-os:

Edge OS
#######
Setup notes for Ubiquiti Edge OS.

.. danger::
  The most recent firmware update (~2019-10) has added `telemetry`_ to ubiquity
  devices; disabled by default.

  **Block or blackhole** ``trace.svc.ui.com``.

`Disable UBNT Discovery Service`_
*********************************
The UBNT Discovery Service enables other UBNT devices the ability to discover
this device.

.. danger::
  This is exposed externally and `exploitable`_. Disable this service.

.. code-block:: bash
  :caption: EdgeOS CLI.

  configure
  set service ubnt-discover disable
  set service ubnt-discover-server disable
  commit; save

Creating Duplicate DNS / Host Entries
*************************************
Effectively cnames for IP lookups without DNS.

.. uctree::   Add Static Host
  :key_title: System --> static-host-mapping --> host-name --> Add
  :option:    host-name
  :setting:   {FQDN HOSTNAME}
  :no_section:
  :no_caption:

    .. note::
      :cmdmenu:`preview` and :cmdmenu:`Apply`. When doing the initial leaf
      creation, you will get a failure message because it is not configured with
      an alias or network address yet. This is normal.


.. uctree::   Add Static Host
  :key_title: System --> static-host-mapping --> host-name --> {FQDN HOSTNAME}
  :option:    alias,
              alias,
              inet
  :setting:   {FQDN HOSTNAME},
              {ALIAS HOSTNAME},
              {HOST NETWORK ADDRESS}
  :no_section:
  :no_caption:
  :no_launch:

    .. note::
      :cmdmenu:`preview` and :cmdmenu:`Apply`. Aliases should all resolve to the
      same IP (base host). Verify by resolving both names on your network.

    .. important::
      With later versions of debian based systems, entries in the local host
      file for the system will resolve to ``127.0.1.1``. `This is by design`_.

      * The alias will resolve to network IP.
      * The hostname will resolve to ``127.0.1.1``.

Hairpin NAT (Internal Only NAT Reflection)
******************************************
Generally split-DNS is better to use than `Hairpin NAT`_ as it allows more
control. This will enable you to redirect internal requests destined for your
external IP to another internal destination based on selected criteria. You will
need to do this for every subnet on the network.

This may be used for *faking* subdomains, assuming there is a wildcard DNS setup
on your Registrar and it resolves to your public IP.

.. ufirewall:: Hairpin NAT (Internal Only NAT Reflection)
  :key_title:  NAT --> Add Destination NAT Rule
  :option:     Inbound Interface,
               Translations Address,
               Translations Port,
               Destination Address,
               Destination Port
  :setting:    {INTERFACE},
               {INTERNAL DESTINATION IP},
               {INTERNAL DESTINATION PORT},
               {EXTERNAL IP},
               {EXTERNAL PORT}
  :no_section:
  :no_caption:

    .. note::
      Do not use WAN interface for the *Inbound Interface*. Defaults for
      everything else.

Deleted DHCP Host Still Resolves in DNS
***************************************
When deleting a DHCP host, the DNS reservation should be `removed as well`_.
However `there is a bug`_ in which these hosts are never deleted.

.. code-block:: bash
  :caption: **0644 root root** ``/etc/hosts`` EdgeOS CLI.

  #Delete hosts which are no longer used and reboot the router.

Multiple Hostnames to One IP
****************************
Simulates NAT Reflection by statically adding multiple hostnames to the hosts
file. Works with subdomains as well. This will provide a hard IP resolution for
a given DNS request.

.. code-block:: bash
  :caption: **0644 root root** ``/etc/hosts`` EdgeOS CLI.

  12.12.12.12 sub1.example.com # resolve to 12.12.12.12
  12.12.12.12 sub2.example.com # resolve to 12.12.12.12

.. code-block:: bash
  :caption: Reload hosts file (EdgeOS CLI).

  /etc/init.d/dnsmasq force-reload

DNS Hostnames not Resolving
***************************
DHCP server on the edgerouter needs to update the hosts file when new IP's are
issued.

.. uctree::   Enable Dynamic DNS
  :key_title: Service --> dhcp-server --> dynamic-dns-update
  :option:    Enable
  :setting:   true
  :no_section:
  :no_caption:

Allow Subnet (Wifi) Traffic `Internet Only Access`_
***************************************************
May be applied to any subnet that should only have Internet access.

Create network group that contains all private IPv4 addresses.

.. ufirewall:: Define RFC1918 Private Address Group
  :key_title:  Firewall/NAT Groups --> Add Group
  :option:     Name,
               Description,
               Group Type
  :setting:    RFC1918,
               Private IPv4 address space,
               ☑ Network Group
  :no_section:
  :no_caption:

.. ufirewall:: Define Networks within RFC 1918
  :key_title:  Firewall/NAT Groups --> RFC1918 --> Actions --> Config
  :option:     Network,
               Network,
               Network
  :setting:    192.168.0.0/16,
               172.16.0.0/12,
               10.0.0.0/8
  :no_section:
  :no_caption:
  :no_launch:

    .. note::
      Use :cmdmenu:`add new` to add each individual network. Be sure to
      :cmdmenu:`save`.

Prevent Wifi Traffic from Reaching Internal Networks
====================================================
.. ufirewall:: WIFI_IN Creation
  :key_title:  Firewall Policies --> Add Ruleset
  :option:     Name,
               Description,
               Default action,
               Default Log
  :setting:    WIFI_IN,
               Wifi to LAN,
               ☑ Accept,
               ☐
  :no_section:
  :no_caption:

.. ufirewall:: Drop Wifi to LAN Basic
  :key_title:  Firewall Policies -->
               WIFI_IN -->
               Actions -->
               Edit Ruleset -->
               Add New Rule -->
               Basic
  :option:     Description,
               Action,
               Protocol
  :setting:    Drop Wifi to LAN,
               ☑ Drop,
               ☑ All protocols
  :no_section:
  :no_caption:
  :no_launch:

.. ufirewall:: Drop Wifi to LAN Destination
  :key_title:  Firewall Policies -->
               WIFI_IN -->
               Actions -->
               Edit Ruleset -->
               Drop Wifi to LAN -->
               Actions -->
               Destination
  :option:     Network Group
  :setting:    Private IPv4 address space
  :no_section:
  :no_launch:

    .. note::
      This can be done in the previous step by switching tabs.

.. ufirewall:: Drop Wifi to LAN Interface
  :key_title:  Firewall Policies -->
               WIFI_IN -->
               Actions -->
               Interfaces
  :option:     Interface,
               Direction
  :setting:    {WIFI INTERFACE},
               in
  :no_section:
  :no_caption:
  :no_launch:

  .. warning::
    Ensure Interface is set to the appropriate Wifi interface or VLAN.

Allow DNS Traffic to Router
===========================
.. ufirewall:: Allow only DNS Traffic to Router
  :key_title:  Firewall Policies --> Add Ruleset
  :option:     Name,
               Description,
               Default action,
               Default Log
  :setting:    WIFI_LOCAL,
               Wifi to Router,
               ☑ Drop,
               ☐
  :no_section:
  :no_caption:

.. ufirewall:: Drop Wifi to LAN Basic
  :key_title:  Firewall Policies -->
               WIFI_LOCAL -->
               Actions -->
               Edit Ruleset -->
               Add New Rule -->
               Basic
  :option:     Description,
               Action,
               Protocol
  :setting:    Allow DNS,
               ☑ Accept,
               ☑ Both TCP and UDP
  :no_section:
  :no_caption:
  :no_launch:

.. ufirewall:: Drop Wifi to LAN Destination
  :key_title:  Firewall Policies -->
               WIFI_LOCAL -->
               Actions -->
               Edit Ruleset -->
               Drop Wifi to LAN -->
               Actions -->
               Destination
  :option:     Destination
  :setting:    53
  :no_section:
  :no_caption:
  :no_launch:

    .. note::
      This can be done in the previous step by switching tabs.

.. ufirewall:: Drop Wifi to LAN Interface
  :key_title:  Firewall Policies -->
               WIFI_LOCAL -->
               Actions -->
               Interfaces
  :option:     Interface,
               Direction
  :setting:    {WIFI INTERFACE},
               local
  :no_section:
  :no_caption:
  :no_launch:

    .. warning::
      Ensure Interface is set to the appropriate Wifi interface or VLAN.

.. _networking-dnat-for-captive-dns:

DNAT for `Captive DNS`_
***********************
Force `all DNS`_ queries regardless of destination server to a specific DNS
server.

.. danger::
  Do **not** enable this for the custom DNS server!

.. _networking-destination-nat:

Add a `Destination NAT Rule`_ for each interface serving internal networks:

.. ufirewall:: Captive DNS Destination Setup
  :key_title:  NAT --> Add Destination NAT Rule
  :option:     Description,
               Enable,
               Inbound Interface,
               Translations Address,
               Translations Port,
               Exclude from NAT,
               Enable Logging,
               Protocol,
               Source Address,
               Destination Address,
               Destination Port
  :setting:    {NETWORK} Destination Captive DNS,
               ☑,
               {INTERFACE},
               {CUSTOM DNS SERVER IP},
               53,
               ☐,
               ☐,
               ☑ Both TCP and UDP,
               {CIDR NETWORK RANGE},
               !{CUSTOM DNS SERVER IP},
               53
  :no_section:
  :no_caption:

    .. note::
      Note the **!** to negate matching for destination address.

Add `Masquerade NAT Rule`_ for each interface serving internal networks. This
enables appropriate transparent DNS lookups (Clients will think that they are
resolving from the DNS they requested, not the actual DNS server serving
responses):

:download:`local image <source/IFYUX2T.png>`.

.. ufirewall:: Captive DNS Masquerade Setup
  :key_title:  NAT --> Add Source NAT Rule
  :option:     Description,
               Enable,
               Outbound Interface,
               Translation,
               Exclude from NAT,
               Enable Logging,
               Protocol,
               Source Address,
               Destination Address,
               Destination Port
  :setting:    {NETWORK} Masquerade Captive DNS,
               ☑,
               {INTERFACE},
               ☑ Use Masquerade,
               ☐,
               ☐,
               ☑ Both TCP and UDP,
               {CIDR NETWORK RANGE},
               {CUSTOM DNS SERVER IP},
               53
  :no_section:
  :no_caption:

Captive DNS Exceptions
======================
Allow for specific client exceptions to DNAT rules. These should be an
*exception* and not the rule. Keep this list small.

Create a *Source Address Group* to manage all clients for the exception:

.. ufirewall:: Create Captive DNS Exceptions Group
  :key_title:  Firewall/NAT Groups --> Add Group
  :option:     Name,
               Description,
               Group Type
  :setting:    {NETWORK}-dnat-exception-group,
               Disable DNAT / Captive DNS for exceptions,
               ☑ Address Group
  :no_section:
  :no_caption:

.. ufirewall:: Add Clients to Exceptions Group
  :key_title:  Firewall/NAT Groups -->
               {NETWORK}-dnat-exception-group -->
               Actions -->
               Edit
  :option:     Address
  :setting:    {CLIENT IP}
  :no_section:
  :no_caption:
  :no_launch:

Add an additional `Destination NAT Rule`_ for each interface serving internal
networks:

.. ufirewall:: Captive DNS Destination Exceptions Setup
  :key_title:  NAT --> Add Destination NAT Rule
  :option:     Description,
               Enable,
               Inbound Interface,
               Translations Address,
               Translations Port,
               Exclude from NAT,
               Enable Logging,
               Protocol,
               Source Address,
               Destination Port
  :setting:    {NETWORK} Destination Captive DNS Exceptions,
               ☑,
               {INTERFACE},
               {ROUTER DNS SERVER IP},
               53,
               ☐,
               ☐,
               ☑ Both TCP and UDP,
               {NETWORK}-dnat-exception-group,
               53
  :no_section:
  :no_caption:

    .. warning::
      Set rule above the captive DNS rule for the specific network for the
      exception to apply.

Custom `SSL`_ Certifcate for Webface
************************************
A custom SSL certifcate may be used to serve HTTPS router traffic. Turn on
EdgeOS SSH.

.. code-block:: bash
  :caption: Combine private key and certifcate into one file, copy to EdgeOS.

  cat privkey.pem cert.pem > server.pem

.. code-block:: bash
  :caption: Backup existing cert and restart webface (EdgeOS CLI).

  cp /etc/lighttpd/server.pem /etc/lighttpd/server.pem.Backup
  mv /tmp/server.pem /etc/lighttpd/server.pem
  kill -SIGINT $(cat /var/run/lighttpd.pid)
  /usr/sbin/lighttpd -f /etc/lighttpd/lighttpd.conf

`Dump Configuration`_ via CLI Command Export
********************************************
Export the list of CLI commands to manually re-create the current configuration
of the router.

.. code-block:: bash
  :caption: EdgeOS CLI.

  show configuration commands

`Dump Configuration`_ to JSON-like file
***************************************
Show a JSON-like representation of the current router configuration.

.. code-block:: bash
  :caption: EdgeOS CLI.

  show configuration all


.. rubric:: References

#. `Creating DNS Entries <https://community.ui.com/questions/ab712740-d579-4c89-824a-cda582a6bdd4>`_
#. `How to Create a Guest\LAN Firewall Rule <https://help.ui.com/hc/en-us/articles/218889067-EdgeMAX-How-to-Protect-a-Guest-Network-on-EdgeRouter>`_

.. _This is by design: https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=316099
.. _Hairpin NAT: https://help.ui.com/hc/en-us/articles/204952134-EdgeRouter-Hairpin-NAT
.. _removed as well: https://community.ui.com/questions/DNS-resolution-of-local-hosts/3b0a70d6-aefb-44a2-872e-e3703e757cd2
.. _there is a bug: https://community.ui.com/questions/12901fe9-f520-49cc-99f7-12cbbc8d6aed
.. _SSL: https://www.stevejenkins.com/blog/2015/10/install-an-ssl-certificate-on-a-ubiquiti-edgemax-edgerouter/
.. _Internet Only Access: https://help.ui.com/hc/en-us/articles/218889067-EdgeRouter-How-to-Create-a-Guest-LAN-Firewall-Rule
.. _exploitable: https://www.zdnet.com/google-amp/article/over-485000-ubiquiti-devices-vulnerable-to-new-attack/
.. _Disable UBNT Discovery Service: https://help.ui.com/hc/en-us/articles/204976244-EdgeRouter-UBNT-Device-Discovery
.. _Dump Configuration: https://community.ui.com/questions/66768622-c0a9-4c79-9dfa-331bd0a90e90
.. _Captive DNS: https://old.reddit.com/r/pihole/comments/ahmg14/finally_set_up_a_dnat_for_hardcoded_dns/eeg114d/
.. _Masquerade NAT Rule: https://i.imgur.com/IFYUX2T.png
.. _all DNS: https://community.ui.com/questions/cd0a248d-ca54-4d16-84c6-a5ade3dc3272
.. _Destination NAT Rule: https://old.reddit.com/r/Ubiquiti/comments/6lndq4/question_redirect_port_53_to_internal_dns_server/
.. _telemetry: https://community.ui.com/questions/Update-UniFi-Phone-Home-Performance-Data-Collection/f84a71c9-0b81-4d69-a3b3-45640aba1c8b
