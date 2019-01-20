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
requests.

The router will be able to forward DNS requests upstream if the Pi-hole server
is unreachable.

[Docker repository][1]

1. [Docker Ports Exposed](#docker-ports-exposed)
1. [Important File Locations](#important-file-locations)
1. [Docker Creation](#docker-creation)
1. [Reverse Proxy Setup](#reverse-proxy-setup)
1. [Configuration](#configuration)
1. [Ubuntu 18.04 Systemd](#ubuntu-1804-systemd)
1. [Reset Password](#reset-password)

Docker Ports Exposed
--------------------

| Port | Protocol | Purpose      |
|------|----------|--------------|
| 53   | TCP/UDP  | DNS Service. |

Important File Locations
------------------------
Relative to docker container

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

### Independent Container
```bash
docker run -t -d \
  --name=pihole \
  --restart=unless-stopped \
  --cap_add=NET_ADMIN \
  --dns=127.0.0.1,1.1.1.1 \
  -p 53:53 \
  -p 53:53/udp \
  -e ServerIP=<HOST IP> \
  -e VIRTUAL_HOST=<HOST DNS NAME> \
  -e DNS1=1.1.1.1 \
  -e DNS2=8.8.8.8 \
  -e TZ=America/Los_Angeles \
  -v /data/services/pihole:/etc/pihole \
  -v /data/services/pihole/dnsmasq.d:/etc/dnsmasq.d \
  -v /etc/localtime:/etc/localtime:ro \
  pihole/pihole:latest
```
* Use `-t -d` is needed to keep the container in interactive mode otherwise as
  soon as the container is idle it will sleep, which will stop background
  running services.

### Docker Compose
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
    - ServerIP=<HOST IP>
    - VIRTUAL_HOST=<HOST DNS NAME>
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
[nginx][ref2] for more details. Recommended.

nginx/conf.d/reverse-proxy.conf
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
* [proxy-control.conf][ref1] contains default proxy settings. Reload nginx.

Configuration
-------------
Most static [Ads and domains][ads1] will be blocked. Dynamic content is
continually changing and therefore ad-blocking for [youtube][ads2] is usually
[hit-or-miss][ads3].

### Password
The password is set randomly on container start. This can be found by searching
the container logs and finding the latest password.

```bash
docker logs pihole | grep pass
```

Alternatively, a password may be statically set from within the container.
```bash
docker exec pihole pihole -a -p <PASSWORD>
```
* `WEBPASSWORD` environment variable will set as well but exposes password.

### Pi-Hole Configuration
`Settings > Blocklists`
* Add `https://v.firebog.net/hosts/lists.php?type=tick`
  * This will block widely-accepted Ads sites. See [Wally's Lists][ads4] for
    stricter lists.
* Add `https://raw.githubusercontent.com/HenningVanRaumle/pihole-ytadblock/master/ytadblock.txt`

`Settings > DNS`
1. Upstream DNS Servers
  * Custom 1: `1.1.1.1`
  * Custom 2: `8.8.8.8`
1. Interface Listening Behavior
  * Check `Listen only on interface XXX`
1. Advanced DNS Settings
  * Check `Never forward non-FQDNs`
  * Check `Never forward reverse lookups for private IP ranges`

`Settings > DHCP`
1. DHCP Settings
  * Uncheck `DHCP Server Enabled`

`Settings > Privacy`
1. DNS resolver privacy level
  * `Show everything and record everything`

### Router Configuration
Generic Configuration - will be located slightly differently for each server.

1. `System > DNS Servers` (Upstream DNS servers for router)
  1. `x.x.x.x` (Pihole IP)
  1. `1.1.1.1` (cloudflare DNS resolver)
  1. `8.8.8.8` (google DNS resolver)
1. `Config Tree > Service > dhcp-server > shared-network-name > <NETWORK> > subnet > <IP Range>` (DNS server assigned for DHCP clients)
  1. `x.x.x.x` (Router IP for given subnet)
1. `Firewall Policies` (Enable DNS traffic to Pi-Hole server)
  1. `x.x.x.x 53 udp/tcp` (Allow TCP/UDP traffic on port 53 to Pihole)

Ubuntu 18.04 Systemd
--------------------
Systemd's stub DNS resolver [needs to be disabled][3] for pihole to work.
However there is a [bug in systemd][2] which needs to be fixed by linking to the
right resolv.conf file.

```bash
systemctl disable systemd-resolved.service
service systemd-resolved stop
rm /etc/resolv.conf
ln -s /run/systemd/resolve/resolv.conf /etc/resolv.conf
```
* Originally, `resolv.conf` links to systemd stub resolver
  `/run/systemd/resolve/stub-resolv.conf`

/etc/resolv.conf
```bash
nameserver x.x.x.x
search <your domain>
```
* `nameserver` should use router DNS IP.

[1]: https://hub.docker.com/r/pihole/pihole/
[2]: https://bugs.launchpad.net/ubuntu/+source/systemd/+bug/1624320/comments/8
[3]: https://discourse.pi-hole.net/t/docker-reply-from-unexpected-source/5729/4
[ads1]: https://www.smarthomebeginner.com/pi-hole-tutorial-whole-home-ad-blocking/#Pi_Hole_Configuration_and_Customization
[ads2]: https://old.reddit.com/r/pihole/comments/84luw8/blocking_youtube_ads/
[ads3]: https://old.reddit.com/r/pihole/comments/7w4n81/having_trouble_blocking_youtube_ads_in_app_on_ios/dtyatmf/
[ads4]: https://v.firebog.net/hosts/lists.php

[ref1]: ../nginx/proxy-control.conf
[ref2]: ../nginx/README.md