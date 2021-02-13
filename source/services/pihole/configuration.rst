.. _service-pihole-configuration:

Pi-Hole Configuration
#####################
Most static `Ads and domains`_ will be blocked. Dynamic content is continually
changing and therefore ad-blocking for `youtube`_ is usually `hit-or-miss`_.

Navigate to Pi-Hole admin interface: http://pi.hole/admin or use static IP if
not using Pi-Hole DNS server yet.

.. literalinclude:: source/blocklist
  :caption: :cmdmenu:`Settings --> Blocklists`

* These can be added all at once (one per line) then mass updated.
* Wally's list has a good list of `stricter blocking`_.
* Large list of `additional blocklists`_.
* Ensure **all** lists have a check after loading. If there is an ✗ then the
  list could not be obtained.
* Check `this list`_ for common services to whitelist.

.. ggui:: Setup DNS Servers
  :key_title: Settings --> DNS --> Upstream DNS Servers
  :option:  Custom 1
  :setting: {ROUTER DNS IP}
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: Add Interface
  :key_title: Settings --> DNS --> Interface Listening Behavior
  :option:  ☑
  :setting: Listen only on interface {INTERFACE}
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: Add Interface
  :key_title: Settings --> DNS --> Advanced DNS Settings
  :option:  ☐,
            ☐
  :setting: Never forward non-FQDNs,
            Never forward reverse lookups for private IP ranges
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: Disable DHCP
  :key_title: Settings --> DHCP --> DHCP Settings
  :option:  ☐
  :setting: DHCP Server Enabled
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: Disable DHCP
  :key_title: Settings -->
              Privacy -->
              Privacy settings -->
              DNS resolver privacy level
  :option:  ☑
  :setting: Show everything and record everything
  :no_section:
  :no_caption:
  :no_launch:

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

.. ggui:: Add Disable Group
  :key_title: Group Managements --> Groups --> Add a new group
  :option:  Name,
            Description
  :setting: Disable,
            Disables PiHole domain blocking.
  :no_section:

.. ggui:: Enable Disable Group
  :key_title: Group Managements --> Groups --> List of configured groups
  :option:  Name,
	          Status,
            Description
  :setting: Disable,
	          Enabled,
            Disables PiHole domain blocking.
  :no_section:

.. ggui:: Add Clients to Manage
  :key_title: Group Managements --> Clients --> Add a new client
  :option:  Known clients,
            Comment
  :setting: {HOST IP},
            {HOST COMMENT}
  :no_section:
 
.. ggui:: Add Clients to Disable group
  :key_title: Group Managements --> Clients --> List of configured clients
  :option:  IP address,
            Comment,
						Group assignment,
            ›
  :setting: {HOST IP},
            {HOST COMMENT},
						☑ Disable,
						☐ Default
  :no_section:

Router Configuration
********************
Generic Configuration - will be located slightly differently for each router.

.. ggui:: Add Upstream DNS Servers
  :key_title: System --> DNS Servers
  :option:  1.1.1.1,
            8.8.8.8
  :setting: cloudflare DNS resolver,
            google DNS resolver
  :no_section:
  :no_caption:
  :no_launch:

.. ubiquiti:: Add Pi-Hole as DNS Server for DHCP
  :path:      config tree -->
              service -->
              dhcp-server -->
              shared-network-name -->
              {NETWORK} -->
              subnet -->
              {IP_RANGE}
  :value0:    DNS server assigned for DHCP clients, {IP}

.. ubiquiti:: Allow TCP/UDP traffic on port 53 to Pi-Hole
  :path:      Firewall Policies -->
              WIFI_IN -->
              Actions -->
              Interfaces
  :value0:    Source, *
  :value1:    Destination, Pi-Hole:53
  :value2:    Protocol, {TCP/UDP}
  :value3:    Action, {ACCEPT}

Clients Ensure clients flush the DNS cache and new DNS server is set to start
resolution via Pi-Hole.

See :ref:`networking-dnat-for-captive-dns` to finish captive DNS setup.

.. _stricter blocking: https://firebog.net/
.. _additional blocklists: https://www.ubuntuboss.com:443/how-to-install-pihole-on-ubuntu-16-04/
.. _Ads and domains: https://www.smarthomebeginner.com/pi-hole-setup-guide/#Pi_Hole_Configuration_and_Customization
.. _youtube: https://old.reddit.com/r/pihole/comments/84luw8/blocking_youtube_ads/
.. _hit-or-miss: https://old.reddit.com/r/pihole/comments/7w4n81/having_trouble_blocking_youtube_ads_in_app_on_ios/dtyatmf/
.. _this list: https://discourse.pi-hole.net/t/commonly-whitelisted-domains/212
