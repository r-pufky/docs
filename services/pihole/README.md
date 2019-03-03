[Pi-Hole][gh]
=============
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
1. [Docker Capabilities](#docker-capabilities)
1. [Important File Locations](#important-file-locations)
1. [Docker Creation](#docker-creation)
1. [Reverse Proxy Setup](#reverse-proxy-setup)
1. [Configuration](#configuration)
1. [Ubuntu 18.04 Systemd](#ubuntu-1804-systemd)
1. [Slow Boot Times](#slow-boot-times)
1. [Clear DNS Cache](#clear-dns-cache)

Ports
-----
Docker reverse-proxy.

| Port | Protocol | Exposed/Public | Purpose      |
|------|----------|----------------|--------------|
| 53   | TCP/UDP  | Public         | DNS Service. |

Docker Capabilities
-------------------

| Capability | Action |
|------------|--------|
| NET_ADMIN  | ADD    |

Important File Locations
------------------------
Relative to docker container.

| File           | Purpose             |
|----------------|---------------------|
| /etc/pihole    | Service Data.       |
| /etc/dnsmasq.d | Configuration Data. |

Docker Creation
---------------
If first-run, just launch the docker container to generate the correct
configuration directory structure, afterwards you can re-create with a mapped
directories.

* `NET_ADMIN` is required with FTLDNS now.
* Docker container DNS is setup to resolve using pihole first, then `1.1.1.1`.
* Pihole upstream DNS servers set to `1.1.1.1`,`8.8.8.8`.

Docker Compose:
```yaml
pihole:
  image: pihole/pihole:latest
  restart: unless-stopped
  ports:
    - '53:53'
    - '53:53/udp'
  cap_add:
    - NET_ADMIN
  dns:
    - 127.0.0.1
    - 1.1.1.1
  environment:
    - ServerIP={HOST IP}
    - VIRTUAL_HOST={HOST DNS NAME}
    - DNS1=1.1.1.1
    - DNS2=8.8.8.8
    - TZ=America/Los_Angeles
  volumes:
    - /data/services/pihole:/etc/pihole
    - /data/services/pihole/dnsmasq.d:/etc/dnsmasq.d
    - /etc/localtime:/etc/localtime:ro
```

Reverse Proxy Setup
-------------------
Allows you to isolate your containers as well as wrap connections in SSL. See
[nginx][refkk] for more details.

### Using Subdomains
[nginx/conf.d/reverse-proxy.conf][4t] `root:root 0644`
```nginx
server {
  listen 443 ssl http2;
  server_name pihole.{DOMAIN} pihole;

  location / {
    proxy_pass http://pihole/admin/;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header X-Forwarded-Host $http_host;
  }
}
```
* [proxy-control.conf][refju] contains default proxy settings. Reload nginx.

### Using Subpaths
nginx/conf.d/reverse-proxy.conf `root:root 0644`
```nginx
server {
  location /pihole/ {
    proxy_pass http://pihole/admin/;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header X-Forwarded-Host $http_host;
  }
}
```
* [proxy-control.conf][refju] contains default proxy settings. Reload nginx.

Configuration
-------------
Most static [Ads and domains][ao] will be blocked. Dynamic content is
continually changing and therefore ad-blocking for [youtube][af] is usually
[hit-or-miss][ab].

### Password
The password is set randomly on container start. This can be found by searching
the container logs and finding the latest password.

```bash
docker logs pihole | grep pass
```

Alternatively, a password may be statically set from within the container.
```bash
docker exec pihole pihole -a -p {PASSWORD}
```
* `WEBPASSWORD` environment variable will set as well but exposes password.

### Pi-Hole Configuration
`Settings > Blocklists`
```
https://v.firebog.net/hosts/lists.php?type=tick

https://raw.githubusercontent.com/HenningVanRaumle/pihole-ytadblock/master/ytadblock.txt

https://hosts-file.net/grm.txt
https://reddestdream.github.io/Projects/MinimalHosts/etc/MinimalHostsBlocker/minimalhosts
https://raw.githubusercontent.com/StevenBlack/hosts/master/data/KADhosts/hosts
https://raw.githubusercontent.com/StevenBlack/hosts/master/data/add.Spam/hosts
https://v.firebog.net/hosts/static/w3kbl.txt

https://adaway.org/hosts.txt
https://v.firebog.net/hosts/AdguardDNS.txt
https://s3.amazonaws.com/lists.disconnect.me/simple_ad.txt
https://hosts-file.net/ad_servers.txt
https://v.firebog.net/hosts/Easylist.txt
https://raw.githubusercontent.com/StevenBlack/hosts/master/data/SpotifyAds/hosts
https://raw.githubusercontent.com/StevenBlack/hosts/master/data/UncheckyAds/hosts

https://v.firebog.net/hosts/Airelle-trc.txt
https://v.firebog.net/hosts/Easyprivacy.txt
https://v.firebog.net/hosts/Prigent-Ads.txt
https://raw.githubusercontent.com/quidsup/notrack/master/trackers.txt
https://raw.githubusercontent.com/StevenBlack/hosts/master/data/add.2o7Net/hosts
https://raw.githubusercontent.com/StevenBlack/hosts/master/data/tyzbit/hosts

https://v.firebog.net/hosts/Airelle-hrsk.txt
https://s3.amazonaws.com/lists.disconnect.me/simple_malvertising.txt
https://mirror1.malwaredomains.com/files/justdomains
https://hosts-file.net/exp.txt
https://hosts-file.net/emd.txt
https://hosts-file.net/psh.txt
https://mirror.cedia.org.ec/malwaredomains/immortal_domains.txt
https://www.malwaredomainlist.com/hostslist/hosts.txt
https://bitbucket.org/ethanr/dns-blacklists/raw/8575c9f96e5b4a1308f2f12394abd86d0927a4a0/bad_lists/Mandiant_APT1_Report_Appendix_D.txt
https://v.firebog.net/hosts/Prigent-Malware.txt
https://v.firebog.net/hosts/Prigent-Phishing.txt
https://raw.githubusercontent.com/quidsup/notrack/master/malicious-sites.txt
https://ransomwaretracker.abuse.ch/downloads/RW_DOMBL.txt
https://v.firebog.net/hosts/Shalla-mal.txt
https://raw.githubusercontent.com/StevenBlack/hosts/master/data/add.Risk/hosts
https://zeustracker.abuse.ch/blocklist.php?download=domainblocklist

https://raw.githubusercontent.com/ZeroDot1/CoinBlockerLists/master/hosts
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

Ubuntu 18.04 Systemd
--------------------
Systemd DNS STUB Resolver has a [bug where disabling the STUB resolver does not
re-link the appropriate resolve.conf file][4t].

There are two ways to fix this. You can either [disable systemd resolver][8i] or
manually set the [appropriate resolv.conf file][vj].

The preferred fix is re-linking resolv.conf to keep the system as close to
vanilla as possible; choose **only one** based on needs.

### Re-link correct resolv.conf file (preferred)
This method will disable the STUB DNS server and link the correct resolv.conf
file.

/etc/systemd/resolved.conf `root:root 0644`
```bash
[Resolve]
...
DNSStubListener=no
```

```bash
rm /etc/resolv.conf`
ln -s /run/systemd/resolve/resolv.conf /etc/resolv.conf
```
* Originally, `resolv.conf` links to systemd stub resolver
  `/run/systemd/resolve/stub-resolv.conf`.

/etc/resolv.conf `root:root 0644`
```bash
nameserver x.x.x.x
search <your domain>
```
* `nameserver` should use router DNS IP.

```bash
service systemd-resolved restart
```

### Disable systemd-resolved entirely (not-preferred)
This will disble the systemd resolver entirely and create a static resolv.conf
file.

```bash
systemctl disable systemd-resolved.service
service systemd-resolved stop
rm /etc/resolv.conf
touch /etc/resolv.conf
chmod 0644 /etc/resolv.conf
chmod root:root /etc/resolve.conf
```

/etc/resolv.conf `root:root 0644`
```bash
nameserver x.x.x.x
search <your domain>
```
* `nameserver` should use router DNS IP.

Slow Boot Times
---------------
Any computer on the network using the pihole server (including the docker host),
will appear to 'slow down' when the pihole server is unreachable, or the docker
host is booting. This is due to the DNS request timing out and being forwarded
to the next DNS server for resolution. This will appear to slow down boot times
for systems with heavy DNS reoslution use and may result in some resolution
failures (depending on how the application handles initial DNS failures) until
the pihole server is back online.

Resolving in a degraded state is intended behavior for this setup. See start of
document.

Clear DNS Cache
---------------
Cache is automatically cleared by restarting the FTLDNS service.

`Settings`
* `Restart DNS resolver`

[docker-service-template.md|14f2197][XX]

[gh]: https://hub.docker.com/r/pihole/pihole/
[4t]: https://bugs.launchpad.net/ubuntu/+source/systemd/+bug/1624320/comments/8
[8i]: https://discourse.pi-hole.net/t/docker-reply-from-unexpected-source/5729/4
[vj]: https://old.reddit.com/r/pihole/comments/8sgro3/server_name_resolution_messed_up_when_running
[ao]: https://www.smarthomebeginner.com/pi-hole-tutorial-whole-home-ad-blocking/#Pi_Hole_Configuration_and_Customization
[af]: https://old.reddit.com/r/pihole/comments/84luw8/blocking_youtube_ads/
[ab]: https://old.reddit.com/r/pihole/comments/7w4n81/having_trouble_blocking_youtube_ads_in_app_on_ios/dtyatmf/
[a7]: https://v.firebog.net/hosts/lists.php
[an]: http://www.ubuntuboss.com/how-to-install-pihole-on-ubuntu-16-04/
[XX]: https://github.com/r-pufky/docs/blob/14f219752a17cf0017eccef6157c7957c16a9f78/services/docker-service-template.md

[refju]: ../nginx/proxy-control.conf
[refkk]: ../nginx/README.md