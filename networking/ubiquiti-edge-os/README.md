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

Deleted DHCP host still resolve in DNS
--------------------------------------
When deleting a DHCP host, the DNS reservation should be [removed as well][4].
However [there is a bug][5] in which these hosts are never deleted.

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

Let's [Encrypt SSL][6] for Webface
----------------------------------
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

[1]: https://community.ubnt.com/t5/EdgeRouter/Create-DNS-enteries/td-p/468375
[2]: https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=316099
[3]: https://help.ubnt.com/hc/en-us/articles/204952134-EdgeRouter-Hairpin-NAT
[4]: https://community.ubnt.com/t5/EdgeRouter/DNS-resolution-of-local-hosts/m-p/1386378/highlight/true#M83801
[5]: https://community.ubnt.com/t5/EdgeRouter/hostfile-update-enable-doesn-t-clear-expired-leases/td-p/969389
[6]: https://www.stevejenkins.com/blog/2015/10/install-an-ssl-certificate-on-a-ubiquiti-edgemax-edgerouter/