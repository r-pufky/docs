# Wireguard VPN
Wireguard offers a quantum-safe, secure, lightweight, option to SSH port
forwarding.

Additionally, SSH forwarding may be used over wireguard if additional security
is needed.

## VPN Server
Create a Wireguard VPN server and add new clients.

!!! example "⚙ ➔ VPN ➔ VPN Server ➔ Create New ➔ Wireguard"
    * Name: **{NAME}**
    * Server Address:
        * IP Address: **{WAN}**
        * Port: **51820**
    * Advanced:
        * Listen On: **All Interfaces**
        * IPv4 Gateway/Subnet:
            * IP Address: **172.31.250.254/24**  # Use a dedicated VPN network.
        * IPv6 Gateway/Subnet: ✘
        * Auto DNS Server: ✔
        * Maximum Transmission Unit: **Auto**
        * IPv4 Maximum Segment Size: **Auto**
        * IPv6 Maximum Segment Size: **Auto**

!!! warning "Always use a pre-shared key"
    Pre-shared keys offer an additional non-shared secret key, enabling
    post-quantum security if the public/private keys are ever compromised.
    These keys are never transmitted over the network.

!!! example "⚙ ➔ VPN ➔ Wireguard ➔ Add Client"
    * Name: **{NAME}**
    * IPv4 Address: **{IP}**
        * Port: **51820**
    * Pre-shared key: ✔  # Auto-generate key.

    Download the configuration file before saving.

## Routing/Firewall Rules
Deny by default; expose only subnets/clients via rules as needed.

!!! example "⚙ ➔ Policy Engine ➔ Zones ➔ VPN"

  Dest Zone | Action | Dest     | Dest Port | Notes
 -----------|--------|----------|-----------|-------
  Internal  | Block  | any      | any       | Blocks direct access to management devices.
  External  | Allow  | any      | any       | Allows valid traffic egress to Internet.
  Gateway   | Allow  | any      | any       | Allows traffic from VPN to Gateway for routing.
  VPN       | Block  | !Gateway | any       | Blocks VPN-VPN client traffic, allow VPN-Gateway traffic.
  Hotspot   | Block  | any      | any       | No access.
  DMZ       | Block  | any      | any       | No access.
  Custom    | Block  | any      | any       | All user-defined network default behavior.

Add policies per network to enable VPN access; define client groups (set
internal and VPN IP's for the same client). This will allow sane definitions
for routing traffic that behave the same internally as well as over VPN.

!!! tip "Allow propagation time"
    Routes will be applied but not active immediately. In most cases this is a
    few seconds but may be longer.

    Some clients may need to be rebooted and re-connected.

## Linux Clients

!!! abstract "/etc/wireguard/split-tunnel.conf"
    0600 root:root

    ``` bash
    # Setup interface to automatically route specific traffic over wireguard.
    [Interface]
    PrivateKey = {KEY}
    Address = 172.31.250.80/32
    # DNS = 172.31.250.254  # Use only if internal DNS servers are required.

    [Peer]
    PublicKey = {KEY}
    PresharedKey = {KEY}
    AllowedIPs = 10.5.5.0/24,10.2.2.80/24  # Networks and hosts client will connect to.
    Endpoint = {WAN}:51821
    # For NAT and firewall traversal persistence over public networks.
    PersistentKeepalive=25
    ```

!!! abstract "/etc/wireguard/full-tunnel.conf"
    0600 root:root

    ``` bash
    # Routes ALL traffic over VPN
    [Interface]
    PrivateKey = {KEY}
    Address = 172.31.250.81/32  # Use a different IP to set different rules for full VPN.
    # DNS = 172.31.250.254  # Use to force DNS query resolution through VPN.

    [Peer]
    PublicKey = {KEY}
    PresharedKey = {KEY}
    AllowedIPs = 0.0.0.0/0  # Route all traffic over VPN.
    Endpoint = {WAN}:51821
    # For NAT and firewall traversal persistence over public networks.
    PersistentKeepalive=25
    ```

## Troubleshooting

### Ping but cannot SSH
Check UFW and network rules to ensure VPN IP can connect to destination.

### Browsers not connecting
Browsers aggressively cache and sometimes do not resolve updated routes.

Restart browser and reboot if still unable to connect.

### No connection (VPN connected via internal network)
Routing issue potentially with NAT reflection or router setup.

Confirm working with external connection before changing router settings.

## Reference[^1][^2][^3]
[^1]: https://old.reddit.com/r/WireGuard/comments/1tnwm77/how_to_set_up_split_tunneling_on_cahyos/
[^2]: https://oilandfish.net/posts/wireguard-shadowsocks.html
[^3]: https://github.com/shadowsocks
