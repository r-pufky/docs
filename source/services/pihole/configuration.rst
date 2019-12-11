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

.. uctree::   Add Pi-Hole as DNS Server for DHCP
  :key_title: Service -->
              dhcp-server -->
              shared-network-name -->
              {NETWORK} -->
              subnet -->
              {IP Range}
  :option:    DNS server assigned for DHCP clients
  :setting:   {Pi-Hole IP}
  :no_section:
  :no_caption:
  :no_launch:

.. ufirewall:: Allow TCP/UDP traffic on port 53 to Pi-Hole
  :key_title:  Firewall Policies -->
               WIFI_IN -->
               Actions -->
               Interfaces
  :option:     Source,
               Destination,
               Protocol,
               Action
  :setting:    *,
               {Pi-Hole IP}:53,
               TCP/UDP,
               Accept
  :no_section:
  :no_caption:
  :no_launch:

Clients Ensure clients flush the DNS cacheand new DNS server is set to start
resolution via Pi-Hole.

See :ref:`networking-dnat-for-captive-dns` to finish captive DNS setup.

.. _stricter blocking: https://firebog.net/
.. _additional blocklists: http://www.ubuntuboss.com/how-to-install-pihole-on-ubuntu-16-04/
.. _Ads and domains: https://www.smarthomebeginner.com/pi-hole-setup-guide/#Pi_Hole_Configuration_and_Customization
.. _youtube: https://old.reddit.com/r/pihole/comments/84luw8/blocking_youtube_ads/
.. _hit-or-miss: https://old.reddit.com/r/pihole/comments/7w4n81/having_trouble_blocking_youtube_ads_in_app_on_ios/dtyatmf/
.. _this list: https://discourse.pi-hole.net/t/commonly-whitelisted-domains/212