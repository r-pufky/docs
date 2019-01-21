Ubiquiti Edge OS
----------------
Setup notes for Edge OS.

Creating Duplicate DNS / Host Entries
-------------------------------------
Effectively cnames for IP lookups without DNS.

1. Expand `Config Tree > System > Static Host Mapping > host-name`
1. Add existing FQDN host-name for static mapping
1. click `preview`
1. Expand newly created **host-name** leaf
1. Add both existing host-name and and aliases to `alias`
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

Internal Only NAT Reflection (Hairpin NAT)
------------------------------------------
Generally split-DNS is better to use than [Hairpin NAT][3] as it allows more
control. This will enable you to redirect internal requests destined for your
external IP to another internal destination based on selected criteria. You will
need to do this for every subnet on the network.

This may be used for 'faking' subdomains, assuming there is a wildcard DNS setup
on your Registrar and it resolves to your public IP.

1. `Firewall/Nat > NAT > Add Destination NAT Rule`
1. Inbound Interface: Interface for rule. Don't use WAN interface.
1. Translations
  * Address: Internal destination IP
  * Post: Internal destination Port
1. Destination Address: Your external IP
1. Destination Port: External Service Port

[1]: https://community.ubnt.com/t5/EdgeRouter/Create-DNS-enteries/td-p/468375
[2]: https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=316099
[3]: https://help.ubnt.com/hc/en-us/articles/204952134-EdgeRouter-Hairpin-NAT