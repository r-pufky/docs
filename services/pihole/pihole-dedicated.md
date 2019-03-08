Pi-Hole
-------
Block nefarious websites & Ads.

This will setup ad-blocking in the following manner:

1. Router upstream DNS servers set to: `pihole`, `1.1.1.1`, `8.8.8.8`.
1. Router DHCP Assigns Router as primary DNS server for clients.
1. Pihole upstream DNS servers set to: `1.1.1.1`, `8.8.8.8`.

Clients can now be dynamically assigned DNS hostnames on multiple subnets, these
clients will be able to locally resolve internal hosts on all subnets; and then
send unknown DNS requets to pihole. Pihole will either block or foward those
requests. The router will be able to forward DNS requests upstream if the
Pi-hole server is unreachable.

The intent of this setup is to provide 'DNS resolution at all costs'; meaning
DNS should still resolve in a degraded state (e.g. pihole server or server is
offline).

1. [Ports](#ports)
1. [Important File Locations](#important-file-locations)
1. [Installing](#installing)
1. [Configuration](#configuration)

Port
----
| Port | Protocol | Purpose                       |
|------|----------|-------------------------------|
| 443  | TCP      | HTTPS administration webface. |
| 80   | TCP      | HTTP administration webface.  |
| 53   | TCP/UDP  | DNS Service.                  |

Important File Locations
------------------------
| File                          | Purpose                           |
|-------------------------------|-----------------------------------|
| /etc/pihole                   | Configuration Data.               |
| /etc/pihole/SetupVars.conf    | Startup Configuration Settings.   |
| /etc/lighthttpd/external.conf | Pi-Hole web server configuration. |

Installing
----------
Assume a working Debian installation. Pihole has an installer script on the
[website][3m], but you should never blindly execute scripts from the Internet.

Instead, download the GIT repository and run installer.
```bash
sudo apt install curl git
git clone --depth 1 https://github.com/pi-hole/pi-hole
cd 'pi-hole/automated install/'
sudo bash basic-install.sh
```
1. Upstream DNS Provider: `1.1.1.1,8.8.8.8`.
1. Third Party Lists: All.
1. Protocols: All.
1. Static IP Address: Use current DHCP settings.
1. Web admin interface: Yes.
1. Web Server (required for webface if no other server): Yes.
1. Log Queries: Yes.
1. Privacy Mode: `0`.

The _password_ will be listed on the summary page. This can be set using
`pihole -a -p`.

Configuration
-------------
Most static [Ads and domains][6d] will be blocked. Dynamic content is
continually changing and therefore ad-blocking for [youtube][cu] is usually
[hit-or-miss][c8].

### Force HTTPS for Pi-Hole Adminstration Page
HTTPS should only be enabled for the FQDN of the pihole server; as the server is
redirecting [traffic, you may get a bunch of cert wonkiness when DNS resolves
return blocked domains][do].

Create a combined certificate
```bash
sudo cat privkey.pem cert.pem | sudo tee combined.pem
sudo chmod www-data -R combined.pem
```
* This contains private information and should not be placed in a web directory.

/etc/lighthttpd/external.conf
```
$HTTP['host'] == 'pihole.example.com' {
  # Ensure the Pi-hole Block Page knows that this is not a blocked domain
  setenv.add-environment = ('fqdn' => 'true')

  # Enable the SSL engine with a LE cert, only for this specific host
  $SERVER['socket'] == ':443' {
    ssl.engine = 'enable'
    ssl.pemfile = 'combined.pem'
    ssl.ca-file =  'fullchain.pem'
    ssl.honor-cipher-order = 'enable'
    ssl.cipher-list = 'EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH'
    ssl.use-sslv2 = 'disable'
    ssl.use-sslv3 = 'disable'
  }

  # Redirect HTTP to HTTPS
  $HTTP['scheme'] == 'http' {
    $HTTP['host'] =~ '.*' {
      url.redirect = ('.*' => 'https://%0$0')
    }
  }
}
```

Restart services
```bash
sudo service lighthttpd restart
```

### Pi-Hole Configuration
`Settings > Blocklists`
```
https://adaway.org/hosts.txt

https://bitbucket.org/ethanr/dns-blacklists/raw/8575c9f96e5b4a1308f2f12394abd86d0927a4a0/bad_lists/Mandiant_APT1_Report_Appendix_D.txt

https://gitlab.com/quidsup/notrack-blocklists/raw/master/notrack-blocklist.txt
https://gitlab.com/quidsup/notrack-blocklists/raw/master/notrack-malware.txt

https://hosts-file.net/ad_servers.txt
https://hosts-file.net/emd.txt
https://hosts-file.net/exp.txt
https://hosts-file.net/grm.txt
https://hosts-file.net/psh.txt

https://mirror1.malwaredomains.com/files/justdomains

https://mirror.cedia.org.ec/malwaredomains/immortal_domains.txt

https://www.malwaredomainlist.com/hostslist/hosts.txt

https://ransomwaretracker.abuse.ch/downloads/RW_DOMBL.txt

https://raw.githubusercontent.com/HenningVanRaumle/pihole-ytadblock/master/ytadblock.txt
https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews-gambling-social/hosts
https://raw.githubusercontent.com/StevenBlack/hosts/master/data/adaway.org/hosts
https://raw.githubusercontent.com/StevenBlack/hosts/master/data/add.2o7Net/hosts
https://raw.githubusercontent.com/StevenBlack/hosts/master/data/add.Risk/hosts
https://raw.githubusercontent.com/StevenBlack/hosts/master/data/add.Spam/hosts
https://raw.githubusercontent.com/StevenBlack/hosts/master/data/Badd-Boyz-Hosts/hosts
https://raw.githubusercontent.com/StevenBlack/hosts/master/data/CoinBlockerList/hosts
https://raw.githubusercontent.com/StevenBlack/hosts/master/data/KADhosts/hosts
https://raw.githubusercontent.com/StevenBlack/hosts/master/data/malwaredomainlist.com/hosts
https://raw.githubusercontent.com/StevenBlack/hosts/master/data/UncheckyAds/hosts
https://raw.githubusercontent.com/StevenBlack/hosts/master/data/yoyo.org/hosts

https://reddestdream.github.io/Projects/MinimalHosts/etc/MinimalHostsBlocker/minimalhosts

https://s3.amazonaws.com/lists.disconnect.me/simple_ad.txt
https://s3.amazonaws.com/lists.disconnect.me/simple_malvertising.txt

https://v.firebog.net/hosts/AdguardDNS.txt
https://v.firebog.net/hosts/Airelle-hrsk.txt
https://v.firebog.net/hosts/Airelle-trc.txt
https://v.firebog.net/hosts/Easylist.txt
https://v.firebog.net/hosts/Easyprivacy.txt
https://v.firebog.net/hosts/lists.php?type=tick
https://v.firebog.net/hosts/Prigent-Ads.txt
https://v.firebog.net/hosts/Prigent-Malware.txt
https://v.firebog.net/hosts/Prigent-Phishing.txt
https://v.firebog.net/hosts/Shalla-mal.txt
https://v.firebog.net/hosts/static/w3kbl.txt

https://zeustracker.abuse.ch/blocklist.php?download=domainblocklist
```
* These can be added all at once (one per line) then mass updated.
* Wally's list has a good list of [stricter blocking][a7].
* Large list of [additional blocklists][an].

`Settings > DNS`
* Upstream DNS Servers
  * Custom 1: `1.1.1.1`
  * Custom 2: `8.8.8.8`
* Interface Listening Behavior
  - [x] Listen only on interface XXX
* Advanced DNS Settings
  - [x] Never forward non-FQDNs
  - [x] Never forward reverse lookups for private IP ranges

`Settings > DHCP`
* DHCP Settings
  - [ ] DHCP Server Enabled

`Settings > Privacy`
* DNS resolver privacy level
  - [x] Show everything and record everything

### Router Configuration
Generic Configuration - will be located slightly differently for each server.

* `System > DNS Servers` (Upstream DNS servers for router)
  1. `x.x.x.x` (Pihole IP)
  1. `1.1.1.1` (cloudflare DNS resolver)
  1. `8.8.8.8` (google DNS resolver)
* `Config Tree > Service > dhcp-server > shared-network-name > {NETWORK} > subnet > <IP Range>` (DNS server assigned for DHCP clients)
  1. `x.x.x.x` (Router IP for given subnet)
* `Firewall Policies` (Enable DNS traffic to Pi-Hole server)
  1. `x.x.x.x 53 udp/tcp` (Allow TCP/UDP traffic on port 53 to Pihole)

Clear DNS Cache
---------------
Cache is automatically cleared by restarting the FTLDNS service.

`Settings`
* `Restart DNS resolver`

[a7]: https://v.firebog.net/hosts/lists.php
[an]: http://www.ubuntuboss.com/how-to-install-pihole-on-ubuntu-16-04/
[3m]: https://pi-hole.net/
[do]: https://discourse.pi-hole.net/t/enabling-https-for-your-pi-hole-web-interface/5771
[6d]: https://www.smarthomebeginner.com/pi-hole-tutorial-whole-home-ad-blocking/#Pi_Hole_Configuration_and_Customization
[cu]: https://old.reddit.com/r/pihole/comments/84luw8/blocking_youtube_ads/
[c8]: https://old.reddit.com/r/pihole/comments/7w4n81/having_trouble_blocking_youtube_ads_in_app_on_ios/dtyatmf/
[si]: https://v.firebog.net/hosts/lists.php