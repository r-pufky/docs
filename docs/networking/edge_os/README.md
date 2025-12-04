# Edge OS
Advanced routing, high performance, and long support lifetime Ubiquiti devices.


## Security

### [Telemetry][a]
Options exists but are disable by default. Block or black hole
**trace.svc.ui.com**.

### [Disable UBNT Discovery Service][b]
UBNT Discovery Service enables other UBNT devices the ability to discover this
device.

!!! danger
    This is exposed externally and [exploitable][c].
    Disable this service.

    ``` bash
    configure
    set service ubnt-discover disable
    set service ubnt-discover-server disable
    commit
    save
    ```

### Default Login
Common default username and password is **ubnt**.


## CLI

### Create [Static DHCP Mapping][d]
Maps computer to 10.0.0.2 on Test DHCP server using MAC address
AA:BB:CC:11:22:33.

``` bash
configure
set service dhcp-server shared-network-name Test subnet 10.0.0.0/24 static-mapping computer ip-address 10.0.0.2
set service dhcp-server shared-network-name Test subnet 10.0.0.0/24 static-mapping computer mac-address AA:BB:CC:11:22:33
commit
save
```

### Create [Static Host Mapping][e]
CNAME for IP lookups without DNS - static **/etc/hosts** mapping.

Simulates NAT Reflection by statically adding multiple host names to hosts
file. Works with subdomains as well. This will provide an internal or custom IP
for a given DNS request.

!!! important
    Modifications should only be done via the GUI or CLI. Do **not** modify
    **/etc/hosts** manually as these are not recognized or kept by system
    across upgrades and restores.

    With later versions of debian based systems, entries in the local host file
    for the system will resolve to **127.0.1.1**. [This is by design][f].

    * The alias will resolve to network IP.
    * The hostname will resolve to **127.0.1.1**.

Map computer and computer.example.com to 10.0.0.2. Appear in **/etc/hosts** as:
``` conf
10.0.0.2  computer.example.com computer
```

#### CLI
!!! abstract "create_host"
    0755 root:root

    ``` bash
    #!/bin/vbash
    #
    # create_host {HOST} {IP}
    #
    source /opt/vyatta/etc/functions/script-template

    configure
    set system static-host-mapping host-name ${1}.example.com inet ${2}
    set system static-host-mapping host-name ${1}.example.com alias ${1}
    commit
    save
    exit
    ```

``` bash
configure
set system static-host-mapping host-name computer.example.com inet 10.0.0.2
set system static-host-mapping host-name computer.exmaple.com alias computer
commit
save
```

#### WebUI
!!! example "Config Tree ➔ system ➔ static-host-mapping ➔ host-name"
    * Add ➔ host-name: **{FQDN}**

        **Preview** then **Apply**.

        When doing the initial leaf creation a failure message appears because
        it is not configured with an alias or network address yet. This is
        **normal**.
    * {FQDN}:
        * alias: **{FQDN}**
        * alias: **{ALIAS}**
        * inet: **{IP}**

        **Preview** then **Apply**.

        Aliases should all resolve to the same IP (base host). Verify by
        resolving both names on your network.


## Hairpin NAT
Internal Only NAT Reflection. This may be used for **faking** subdomains,
assuming there is a wildcard DNS setup on your Registrar and it resolves to
your public IP.

!!! info
    Split DNS is better to use than [Hairpin NAT][g]
    as it allows more control. This will enable you to redirect internal
    requests destined for your external IP to another internal destination
    based on selected criteria. You will need to do this for every subnet on
    the network.

!!! example "Firewall/NAT ➔ Port Forwarding"
    * WAN Interface: **{WAN}**
    * Hairpin NAT: ✔ Enable hairpin NAT (also known as 'NAT loopback' or 'NAT reflection')
    * LAN Interface: **{ALL LAN INTERFACES}**


## Restrict Subnet Traffic to [Internet Only Access][h]

### Define RFC1918 Private Address Group
!!! example "Firewall/NAT ➔ Firewall/NAT Groups ➔ Add Group"
    * Name: **RFC1918**
    * Description: **Private IPv4 address space**
    * Group Type: **Network Group**

### Define Networks within RFC 1918
!!! example "Firewall/NAT ➔ Firewall/NAT Groups ➔ RFC1918 ➔ Actions ➔ Config"
    * Network: **192.168.0.0/16**
    * Network: **172.16.0.0/12**
    * Network: **10.0.0.0/8**


## Restrict Subnet Traffic from Reaching Internal Networks

### {NET}_IN Creation
!!! example "Firewall/NAT ➔ Firewall Policies ➔ Add Ruleset"
    * Name: **{NET}_IN**
    * Description: **{NET} to LAN**
    * Default action: **Accept**
    * Default Log: ✘

### Drop {NET} to LAN Basic
!!! example "Firewall/NAT ➔ Firewall Policies ➔ {NET}_IN ➔ Actions ➔ Edit Ruleset ➔ Add New Rule ➔ Basic"
    * Description: **Drop {NET} to LAN**
    * Action: **Drop**
    * Protocol: **All protocols**
    * Actions ➔ Destination
        * Network Group: **Private IPv4 address space**

### Drop {NET} to LAN Interface
!!! example "Firewall/NAT ➔ Firewall Policies ➔ {NET}_IN ➔ Actions ➔ Interfaces"
    * Interface: **{NET}**
    * Direction: **{IN}**


## Only Allow DNS Traffic to Router

!!! example "Firewall/NAT ➔ Firewall Policies ➔ Add Ruleset"
    * Name: **{NET_LOCAL}**
    * Description: **{NET} to Router**
    * Default action: **Drop**
    * Default Log: ✘
    * Actions ➔ Edit Ruleset ➔ Add New Rule ➔ Basic
        * Description: **Allow DNS**
        * Action: **Accept**
        * Protocol: **Both TCP and UDP**
    * Actions ➔ Edit Ruleset ➔ Drop {NET} to LAN ➔ Actions ➔ Destination
        * Destination: **53**
    * Actions ➔ Interfaces
        * Interface: **{NET}**
        * Direction: **{LOCAL}**


## Destination NAT (DNAT) for [Captive DNS][i]
Force [all unencrypted DNS][j] queries regardless of destination server to a
specific DNS server.

!!! danger
    Do **not** enable this for internal DNS servers!

### [Add a Destination NAT Rule][k]
For each interface serving internal networks.

!!! example "Firewall/NAT ➔ NAT ➔ Add Destination NAT Rule"
    * Description:  **{CAPTIVE_DNS_NAME}**
    * Enable: ✔
    * Inbound Interface: **{INTERFACE}**
    * Translations Address: **{DNS_IP}**
    * Translations Port: **53**
    * Exclude from NAT:✘
    * Enable Logging: ✘
    * Protocol: **Both TCP and UDP**
    * Source Address: **{IP_NET_CIDR}**
    * Destination Address: **!{DNS_IP}**
    * Destination Port: **53**

    **!** negates matching for address.

### Add [Masquerade NAT Rule][l]
For each interface serving internal networks.

!!! note
    Enables appropriate transparent DNS lookups (Clients will think that they
    are resolving from the DNS server they made request to, not the actual DNS
    server responding).

!!! example "Firewall/NAT ➔ NAT ➔ Add Source NAT Rule"
    * Description: **{CAPTIVE_DNS_NAME}**
    * Enable: ✔
    * Outbound Interface: **{INTERFACE}**
    * Translation: **Use Masquerade**
    * Exclude from NAT: ✘
    * Enable Logging: ✘
    * Protocol: **Both TCP and UDP**
    * Source Address: **{IP_NET_CIDR}**
    * Destination Address: **{DNS_IP}**
    * Destination Port: **53**

### Captive DNS Exceptions
Allow for specific client exceptions to DNAT rules.

Create a **Source Address Group** to manage all clients for the exception
!!! example "Firewall/NAT ➔ Firewall/NAT Groups ➔ Add Group"
    * Name: **{DNAT_EXCEPTION_NAME}**
    * Description: **Disable DNAT / Captive DNS for exceptions**
    * Group Type: **Address Group**
    * Actions ➔ Edit
        * Address: **{IP}**

Add additional Destination NAT Rule for each interface on internal networks
!!! example "Firewall/NAT ➔ NAT ➔ Add Destination NAT Rule"
    * Description: **{CAPTIVE_DNS_EXCEPTIONS}**
    * Enable: ✔
    * Inbound Interface: **{INTERFACE}**
    * Translations Address: **{DNS_IP}**
    * Translations Port: **53**
    * Exclude from NAT: ✘
    * Enable Logging: ✘
    * Protocol: **Both TCP and UDP**
    * Source Address: **{DNAT_EXCEPTION_NAME}**
    * Destination Port: **53**

    Set rule above the captive DNS rule for the specific network for the
    exception to apply. IP is router.


## [Custom SSL Certificate for WebUI][m]
Use custom SSL certificates to serve HTTPS router traffic. Turn on SSH.

Combine private key and certificate into one file and copy to EdgeOS.
``` bash
cat privkey.pem cert.pem➔server.pem

# Backup existing cert and restart webface (EdgeOS CLI).
cp /etc/lighttpd/server.pem /etc/lighttpd/server.pem.Backup
mv /tmp/server.pem /etc/lighttpd/server.pem
kill -SIGINT $(cat /var/run/lighttpd.pid)
/usr/sbin/lighttpd -f /etc/lighttpd/lighttpd.conf
```


## [Export Config (CLI)][n]
Export the list of CLI commands to manually re-create the current configuration
of the router.

``` bash
show configuration commands

# Dump router configuration as JSON file.
show configuration all
```


## VLAN Setup
See [VLANs](../vlan.md) for concepts.

!!! tip
    Set an spare port on your router with a static management address without
    VLANS or use a [console cable][o].

### Add VLAN
!!! example "Dashboard ➔ Add Interface ➔ Add VLAN"
    * VLANID: **{ID}**
    * Interface: **{BASE INTERFACE}**
    * Description: **{DESCRIPTION}**
    * Address: **Static**
    * Address: **{CIDR}**

### Define Management Network on Base Interface
!!! example "Dashboard ➔ {BASE INTERFACE} ➔ Actions ➔ Config"
    * Address: **Static**
    * Address: **10.1.1.1/24**

    [Management VLAN](../../glossary/vlan.md#management-vlan-default) is not explicitly
    defined as a VLAN - untagged traffic coming into an interface **IS**
    management traffic.

### Add DHCP Server
!!! example "Services ➔ DHCP Server ➔ Add DHCP Server"
    * DHCP Name: **{NAME}**
    * Subnet: **{CIDR}**
    * Range Start: **{START}**
    * Range End: **{END}**
    * Router: **{ROUTER_IP}**
    * UniFi Network IP: **{UNIFI_CONTROLLER_IP}**
    * DNS 1: **{DNS_IP}**
    * Domain: **{DOMAIN}**
    * Domain: **Enable**

### Add DNS
!!! example "Services ➔ DNS ➔ Interface ➔ Add Listen Interface"
    Add for all networks and VLANS. VLANS will appear as **eth0.{VLAN_ID}**.


## Reference[^1][^2][^3]

[^1]: https://community.ui.com/questions/ab712740-d579-4c89-824a-cda582a6bdd4
[^2]: https://help.ui.com/hc/en-us/articles/218889067-EdgeMAX-How-to-Protect-a-Guest-Network-on-EdgeRouter
[^3]: https://help.ui.com/hc/en-us/articles/204959444-EdgeRouter-Router-on-a-Stick

[a]: https://community.ui.com/questions/Update-UniFi-Phone-Home-Performance-Data-Collection/f84a71c9-0b81-4d69-a3b3-45640aba1c8b
[b]: https://help.ui.com/hc/en-us/articles/204976244-EdgeRouter-UBNT-Device-Discovery
[c]: https://www.zdnet.com/google-amp/article/over-485000-ubiquiti-devices-vulnerable-to-new-attack
[d]: https://help.ui.com/hc/en-us/articles/360044494093-EdgeRouter-DHCP-Server-Static-Mapping
[e]: https://community.ui.com/questions/Create-DNS-enteries/ab712740-d579-4c89-824a-cda582a6bdd4
[f]: https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=316099
[g]: https://help.ui.com/hc/en-us/articles/204952134-EdgeRouter-Hairpin-NAT
[h]: https://help.ui.com/hc/en-us/articles/218889067-EdgeRouter-How-to-Create-a-Guest-LAN-Firewall-Rule
[i]: https://old.reddit.com/r/pihole/comments/ahmg14/finally_set_up_a_dnat_for_hardcoded_dns/eeg114d
[j]: https://community.ui.com/questions/cd0a248d-ca54-4d16-84c6-a5ade3dc3272
[k]: https://old.reddit.com/r/Ubiquiti/comments/6lndq4/question_redirect_port_53_to_internal_dns_server/
[l]: https://i.imgur.com/IFYUX2T.png
[m]: https://www.stevejenkins.com/blog/2015/10/install-an-ssl-certificate-on-a-ubiquiti-edgemax-edgerouter/
[n]: https://community.ui.com/questions/66768622-c0a9-4c79-9dfa-331bd0a90e90
[o]: https://www.amazon.com/dp/B078PVJ5ZQ
