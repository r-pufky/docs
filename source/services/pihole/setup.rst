.. _service-pihole-setup:

`Pi-Hole`_ Setup
################
Block nefarious websites & Ads.

.. gport:: Ports (Pi-Hole)
  :port:     53,
             80,
             443,
             67,
             547,
             4711-4720
  :protocol: UDP/TCP,
             TCP,
             TCP,
             UDP,
             UDP,
             TCP
  :type:     Public,
             Public,
             Public,
             Public,
             Public,
             Public
  :purpose:  DNS Service.,
             HTTP administration webface.,
             (Optional) HTTPS administration webface.,
             (Optional) DHCP Service.,
             (Optional) DHCPv6 Service.,
             (Optional) FTL API Service.
  :no_key_title:
  :no_caption:
  :no_launch:

.. note::
  FTL API should not be acessible from any other interface.

.. attention::
  See older revisions of this document for PiHole ``4.x`` and lower. ``5.x``+
	now uses a single SQLlite database for configuration.

.. _service-pihole-file-locations:

.. gflocation:: Important File Locations (Pi-Hole)
  :file:    /etc/dnsmasq.d/*,
            /etc/hosts,
            /etc/lighthttpd/external.conf,
            /etc/pihole,
            /etc/pihole/SetupVars.conf,
            /etc/pihole/gravity.db
  :purpose: DNS masqerade settings.,
            Static host/IP lookup.,
            Pi-Hole web server configuration.,
            Configuration Data.,
            Startup Configuration Settings.,
            PiHole whitelist,blacklist,group,regex settings.
  :no_key_title:
  :no_caption:
  :no_launch:

Installing
**********
Uses :ref:`debian-server-base-install`. Pi-Hole has an installer script on the
website, but you should never blindly execute scripts from the Internet.

.. code-block:: bash
  :caption: Download the GIT repository and run installer.

  sudo apt install curl git
  git clone --depth 1 https://github.com/pi-hole/pi-hole
  cd 'pi-hole/automated install/'
  sudo bash basic-install.sh

.. ggui:: Base Configuration
  :option:  Upstream DNS Provider;
            Third Party Lists;
            Protocols;
            Static IP Address;
            Web admin interface;
            Web Server (required for webface if no other server);
            Log Queries;
            Privacy Mode
  :setting: 1.1.1.1,8.8.8.8;
            All;
            All;
            Use current DHCP settings;
            ☑;
            ☑;
            ☑;
            0
  :no_key_title:
  :no_section:
  :no_caption:
  :no_launch:
  :delim: ;

.. note::
  The *password* will be listed on the summary page. This can be set using
  ``pihole -a -p`` and reached via http://pi.hole/admin, once DNS is set to
  Pi-Hole.

.. _Pi-Hole: https://pi-hole.net/
