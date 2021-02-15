.. _service-pihole-troubleshooting:

Troubleshooting
###############

Clear DNS Cache
***************
Cache is automatically cleared by restarting the ``FTLDNS`` service.

:cmdmenu:`Settings --> Restart DNS resolver`

Failed Upgrade
**************
This may happen with major changes between pi-hole versions, especially with
``FTLDNS``; which may leave the system with a permenant *DNS server not started*
error.

Backup all files in :ref:`service-pihole-file-locations`.

Reinstall the Pi-Hole server and setup vanilla. Then copy the following files to
do a manual **teleporter** install. ``5.x`` `may be exported to 4.x flat
files`_ if needed. A teleporter install in ``5.x`` will not carry over all
settings.

.. files:: Teleporter Install
  :value0: /etc/hosts, Hostname resolutions
  :value1: /etc/pihole/gravity.db, PiHole list/group/client settings
  :value2: /etc/pihole/dhcp.leases, Current DHCP leases (optional)
  :value3: /etc/pihole/pihole-FTL.db, SQLite DNS resolution log (optional)
  :open:

.. warning::
  ``setupVars.conf``, ``pihole-FTL.conf`` and anything in ``dnsmasq.d`` are
  probably different if the upgrade failed. Diff these and make a determination
  to copy.

.. _may be exported to 4.x flat files: https://old.reddit.com/r/pihole/comments/gnhesb/v50python_pyphdb_export_your_adlists_whitelists/

Restart Pi-Hole.
