Ubiquiti Edge OS
----------------
Setup notes for Edge OS.

Creating Duplicate DNS / Host Entries
-------------------------------------
Effectively cnames for IP lookups.

1. Expand Config Tree > System > Static Host Mapping > host-name
1. Add existing host-name for static mapping
1. click `preview`
1. Expand newly created __host-name__ leaf
1. Add both existin host-name and and aliases to `alias`
1. Add network address to `inet`
1. click `preview` and `Apply`

 * When doing the initial leaf creation, you will get a failure message because
   it is not configured with an alias or network address yet. This is normal.
 * Aliases should all resolve to the same IP (off aliased host)
 * Verify by resolving both names on your network. With later versions of debian
   based systems, entries in the local host file for the system will resolve to
   `127.0.1.1`. [This is by design][2].
    * The alias will resolve to network IP.
    * The hostname will resolve to 127.0.1.1.

[1]: https://community.ubnt.com/t5/EdgeRouter/Create-DNS-enteries/td-p/468375
[2]: https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=316099