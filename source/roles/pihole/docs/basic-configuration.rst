.. _service-pihole-configuration:

Basic Configuration
###################
Most static ads and domains will be blocked. Dynamic content is continually
changing and therefore ad-blocking for youtube is usually hit-or-miss.

Navigate to Pi-Hole admin interface: http://pi.hole/admin or use static IP if
not using Pi-Hole DNS server yet.


This will setup ad-blocking in the following manner:

#. Router upstream DNS servers set to ``1.1.1.1``, ``8.8.8.8``.
#. Router DHCP Assigns **Pi-Hole** as primary DNS server for clients.
#. Router uses DNAT to force all DNS requests to **Pi-Hole** (optional).
#. Pi-Hole upstream DNS server set to **router**.

Pi-Hole will have static hosts set in ``/etc/hosts`` to resolve multiple
hostnames resolving to the same IP.

`Reference <https://www.smarthomebeginner.com/pi-hole-setup-guide/#Pi_Hole_Configuration_and_Customization>`__

`Reference <https://old.reddit.com/r/pihole/comments/84luw8/blocking_youtube_ads/>`__

`Reference <https://old.reddit.com/r/pihole/comments/7w4n81/having_trouble_blocking_youtube_ads_in_app_on_ios/dtyatmf/>`__

.. gui::   Manual Configuration
  :path:   Manual Configuration
  :value0: Upstream DNS Provider, {INTERNAL_DNS}
  :value1: Third Party Lists, All
  :value2: Protocols, All
  :value3: Static IP Address, Use current DHCP settings
  :value4: Web admin interface, ☑
  :value5: Web Server (required for webface if no other server), ☑
  :value6: Log Queries, ☑
  :value7: Privacy Mode, 0
  :open:

  .. note::
    The *password* will be listed on the summary page. This can be set using
    ``pihole -a -p`` and reached via http://pi.hole/admin, once DNS is set to
    Pi-Hole.

.. gui::   Blocklists
  :path:   Settings --> Blocklists

  * These can be added all at once (one per line) then mass updated.
  * Wally's list has a good list of `stricter blocking <https://firebog.net/>`_.
  * Large list of `additional blocklists
    <https://www.ubuntuboss.com:443/how-to-install-pihole-on-ubuntu-16-04/>`_.
  * Ensure **all** lists have a check after loading. If there is an ✗ then the
    list could not be obtained.
  * Check `this list
    <https://discourse.pi-hole.net/t/commonly-whitelisted-domains/212>`_ for
    common services to whitelist.

.. gui::   Setup DNS Servers
  :path:   Settings --> DNS --> Upstream DNS Servers
  :value0: Custom 1, {INTERNAL_DNS}

.. gui::   Add Interface
  :path:   Settings --> DNS --> Interface Listening Behavior
  :value0: ☑, Listen only on interface {INTERFACE}

.. gui::   Add Interface
  :path:   Settings --> DNS --> Advanced DNS Settings
  :value0: ☐, Never forward non-FQDNs
  :value1: ☐, Never forward reverse lookups for private IP ranges

.. gui::   Disable DHCP Server
  :path:   Settings --> DHCP --> DHCP Settings
  :value0: ☐, DHCP Server Enabled

.. gui::   Set DNS Resolver Privacy Settings
  :path:   Settings -->
           Privacy -->
           Privacy settings -->
           DNS resolver privacy level
  :value0: ☑, Show everything and record everything

Static Host IP Resolution
*************************
Useful for hosts with multiple hostnames per IP (e.g. docker containers); or
static hosts that the router cannot resolve (e.g. the static address is not
defined in the router itself).

.. code-block:: bash
  :caption: **0644 root root** ``/etc/hosts``

  1.2.3.4    app1.host.com app1  # docker app 1
  1.2.3.4    app2.host.com app2  # docker app 2

Restarting Pi-Hole may be required.

Disable Blocking for Specific Clients
*************************************
Disabling ad blocking for specific clients. Disables can be all lists or
specific lists.

.. gui::   Add Disable Group
  :path:   Group Managements --> Groups --> Add a new group
  :value0: Name, {DISABLE}
  :value1: Description, Disables PiHole domain blocking

.. gui::   Enable the Disable Group
  :path:   Group Managements --> Groups --> List of configured groups
  :value0: Name, {DISABLE}
  :value1: Status, {ENABLE}
  :value2: Description, Disables PiHole domain blocking

.. gui::   Add Clients to Manage
  :path:   Group Managements --> Clients --> Add a new client
  :value0: Known clients, {IP}
  :value1: Comment, {DESCRIPTION}

.. gui::   Add Clients to Disable group
  :path:   Group Managements --> Clients --> List of configured clients
  :value0: IP address, {IP}
  :value1: Comment, {DESCRIPTION}
  :value2: Group assignment, ☑ Disable
  :value3: ›, ☐ Default

Router Configuration
********************
Generic Configuration - will be located slightly differently for each router.

.. gui::   Add Upstream DNS Servers
  :path:   System --> DNS Servers
  :value0: 1.1.1.1, cloudflare DNS resolver
  :value1: 8.8.8.8, google DNS resolver

.. gui::   Add Pi-Hole as DNS Server for DHCP
  :label:  Ubiquiti
  :path:   config tree -->
           service -->
           dhcp-server -->
           shared-network-name -->
           {NETWORK} -->
           subnet -->
           {IP_RANGE}
  :value0: DNS server assigned for DHCP clients, {IP}

.. gui::   Allow TCP/UDP traffic on port 53 to Pi-Hole
  :label:  Ubiquiti
  :path:   Firewall Policies -->
           WIFI_IN -->
           Actions -->
           Interfaces
  :value0: Source, *
  :value1: Destination, Pi-Hole:53
  :value2: Protocol, {TCP/UDP}
  :value3: Action, {ACCEPT}

Clients Ensure clients flush the DNS cache and new DNS server is set to start
resolution via Pi-Hole.

See :ref:`networking-dnat-for-captive-dns` to finish captive DNS setup.
