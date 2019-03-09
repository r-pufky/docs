Ubiquiti Edge OS
================
Setup notes for Edge OS.

[Disable UBNT Discovery Service][x8]
------------------------------------
Helper service to enable other ubnt device discovery. Externally exposed and
[exploitable][ne].

CLI on EdgeOS (or SSH)
```bash
configure
set service ubnt-discover disable
set service ubnt-discover-server disable
commit; save
```
* Delete hosts which are no longer used.

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
  `127.0.1.1`. [This is by design][27].
   * The alias will resolve to network IP.
   * The hostname will resolve to 127.0.1.1.

Internal Only NAT Reflection (Hairpin NAT)
------------------------------------------
Generally split-DNS is better to use than [Hairpin NAT][UV] as it allows more
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

Deleted DHCP host still resolve in DNS
--------------------------------------
When deleting a DHCP host, the DNS reservation should be [removed as well][em].
However [there is a bug][En] in which these hosts are never deleted.

CLI on EdgeOS (or SSH)
```bash
sudo su
vi /etc/hosts
```
* Delete hosts which are no longer used.

Then reboot the router.

Multiple Hostnames to One IP
----------------------------
Simulates NAT Reflection by statically adding multiple hostnames to the hosts
file. Works with subdomains as well. This will provide a hard IP resolution for
a given DNS request.

CLI on EdgeOS (or SSH)
```bash
sudo su
vi /etc/hosts
```

```hosts
12.12.12.12 sub1.domain.com # Hard IP Resolution
12.12.12.12 sub2.domain.com # Hard IP Resolution
```

Reload hosts file
```bash
/etc/init.d/dnsmasq force-reload
```

DNS Hostnames not Resolving
---------------------------
DHCP server on the edgerouter needs to update the hosts file when new IP's are
issued.

`Config Tree > service > dhcp-server > dynamic-dns-update > enable` = `true`

Allow Subnet (Wifi) Traffic [Only Internet Access][7y]
------------------------------------------------------
May be applied to any subnet that should only have Internet access.

### Create network group that contains all private IPv4 addresses.

#### `Firewall/NAT > Firewall/NAT Groups > Add Group`
* Name: `RFC1918`
* Description: `Private IPv4 address space`
* Type: `Network Group`

#### `RFC1918 > Actions > Config`
* Network: `192.168.0.0/16`, `172.16.0.0/12`, `10.0.0.0/8`

### Prevent Wifi traffic from reaching internal networks:

#### `Firewall/NAT > Firewall Policies > Add Ruleset`
* Name: `WIFI_IN`
* Description: `Wifi to LAN`
* Default action: `Accept`
* Default Log: ``

#### `WIFI_IN > Actions > Edit Ruleset > Add New Rule`
* `Basic`
  * Description: `Drop Wifi to LAN`
  * Action: `Drop`
  * Protocol: `All protocols`
* `Destination`
  * Network Group: `Private IPv4 address space`

#### `WIFI_IN > Interfaces`
* Interface: `eth0.4`
* Direction: `in`

> :warning:
> Ensure Interface is set to the appropriate interface or VLAN.

### Allow DNS traffic for subnet clients

#### `Firewall/NAT > Firewall Policies > Add Ruleset`
* Name: `WIFI_LOCAL`
* Description: `Wifi to Router`
* Default action: `Drop`
* Default Log: ``

#### `WIFI_IN > Actions > Edit Ruleset > Add New Rule`
* `Basic`
  * Description: `Allow DNS`
  * Action: `Accept`
  * Protocol: `Both TCP and UDP`
* `Destination`
  * Port: `53`

#### `WIFI_IN > Interfaces`
* Interface: `eth0.4`
* Direction: `local`

> :warning:
> Ensure Interface is set to the appropriate Wifi VLAN.

DNAT for [Captive DNS][cp]
--------------------------
Force [all DNS][fg] queries regardless of destination server to a specific DNS
server.

Do _not_ enable this for the custom DNS server!

### Add Destination NAT [Rule][lx] Per Interface
Interface is the interface the Network is served on.

`Firewall/NAT > NAT > Add Destination Rule`
* Description: {NETWORK} `Captive DNS`
- [x] Enable
* Inbound Interface: `ethX`
* Translations:
  * Address: {PI-HOLE DNS SERVER}
  * Port: 53
- [ ] Exclude from NAT
- [ ] Enable logging
- [x] Both TCP and UDP
* Src Address: {NETWORK RANGE CIDR}
* Dest Address: `!`{PI-HOLE DNS SERVER}
* Dest Port: `53`

> :warning:
> Note the _!_ to negate matching for destination address.

### Add Masquerade NAT [Rule][pv]
Enables appropriate transparent DNS lookups (e.g. the clients will think that
they are resolving from the requested DNS server, not the actual one).

Interface is the interface the Network is served on.

`Firewall/NAT > NAT > Add Source NAT Rule`
* Description: {NETWORK} `Masquerade Captive DNS`
- [x] Enable
* Inbound Interface: `ethX`
- [x] Use Masquerade
- [ ] Exclude from NAT
- [ ] Enable logging
- [x] Both TCP and UDP
* Src Address: {NETWORK RANGE CIDR}
* Dest Address: {PI-HOLE DNS SERVER}
* Dest Port: `53`

Let's [Encrypt SSL][0c] for Webface
-----------------------------------
A let's encrypt certifcate may be used to serve https router traffic. Turn on
EdgeOS SSH.

Combine private key and certifcate into one file, copy to server.
```bash
cat privkey.pem cert.pem > server.pem
```

Backup existing cert and restart webface.
```bash
cd /etc/lighttpd
cp server.pem server.pem.Backup
kill -SIGINT $(cat /var/run/lighttpd.pid)
/usr/sbin/lighttpd -f /etc/lighttpd/lighttpd.conf
```

Dump List of [Commands for Current Config][7b]
----------------------------------------------
Export the list of CLI commands to manually re-create the current configuration
of the router.

CLI on EdgeOS (or SSH)
```bash
show configuration commands
```

Dump Router [Configuration][7b]
-------------------------------
Show a JSON-like representation of the current router configuration.

CLI on EdgeOS (or SSH)
```bash
show configuration all
```

[js]: https://community.ubnt.com/t5/EdgeRouter/Create-DNS-enteries/td-p/468375
[27]: https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=316099
[UV]: https://help.ubnt.com/hc/en-us/articles/204952134-EdgeRouter-Hairpin-NAT
[em]: https://community.ubnt.com/t5/EdgeRouter/DNS-resolution-of-local-hosts/m-p/1386378/highlight/true#M83801
[En]: https://community.ubnt.com/t5/EdgeRouter/hostfile-update-enable-doesn-t-clear-expired-leases/td-p/969389
[0c]: https://www.stevejenkins.com/blog/2015/10/install-an-ssl-certificate-on-a-ubiquiti-edgemax-edgerouter/
[7y]: https://help.ubnt.com/hc/en-us/articles/218889067-EdgeRouter-How-to-Create-a-Guest-LAN-Firewall-Rule
[ne]: https://www.zdnet.com/google-amp/article/over-485000-ubiquiti-devices-vulnerable-to-new-attack/
[x8]: https://help.ubnt.com/hc/en-us/articles/204976244-EdgeRouter-UBNT-Device-Discovery
[7b]: https://community.ubnt.com/t5/EdgeRouter/Importing-and-exporting-configurations/td-p/1513041
[cp]: https://old.reddit.com/r/pihole/comments/ahmg14/finally_set_up_a_dnat_for_hardcoded_dns/eeg114d/
[pv]: https://i.imgur.com/IFYUX2T.png
[fg]: https://community.ubnt.com/t5/EdgeRouter/Intercepting-and-Re-Directing-DNS-Queries/td-p/1554378
[lx]: https://old.reddit.com/r/Ubiquiti/comments/6lndq4/question_redirect_port_53_to_internal_dns_server/

[ref7y]: https://help.ubnt.com/hc/en-us/articles/218889067-EdgeMAX-How-to-Protect-a-Guest-Network-on-EdgeRouter