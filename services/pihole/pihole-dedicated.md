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

1. [Ports Exposed](#ports-exposed)
1. [Important File Locations](#important-file-locations)
1. [Installing](#installing)
1. [Configuration](#configuration)

Port Exposed
------------
| Port | Protocol | Purpose                       |
|------|----------|-------------------------------|
| 443  | TCP      | HTTPS administration webface. |
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
[website][1], but you should never blindly execute scripts from the Internet.

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
Most static [Ads and domains][ads1] will be blocked. Dynamic content is
continually changing and therefore ad-blocking for [youtube][ads2] is usually
[hit-or-miss][ads3].

### Force HTTPS for Pi-Hole Adminstration Page
HTTPS should only be enabled for the FQDN of the pihole server; as the server is
redirecting [traffic, you may get a bunch of cert wonkiness when DNS resolves
return blocked domains][2].

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

[1]: https://pi-hole.net/
[2]: https://discourse.pi-hole.net/t/enabling-https-for-your-pi-hole-web-interface/5771
[ads1]: https://www.smarthomebeginner.com/pi-hole-tutorial-whole-home-ad-blocking/#Pi_Hole_Configuration_and_Customization
[ads2]: https://old.reddit.com/r/pihole/comments/84luw8/blocking_youtube_ads/
[ads3]: https://old.reddit.com/r/pihole/comments/7w4n81/having_trouble_blocking_youtube_ads_in_app_on_ios/dtyatmf/
[ads4]: https://v.firebog.net/hosts/lists.php