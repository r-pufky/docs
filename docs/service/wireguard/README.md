# Wireguard
Modern state-of-the-art VPN designed to be simpler and faster that IPsec and
openVPN.

Only the server endpoint needs to be exposed publicly. Clients can globally
roam as long as they have working Internet connections and can send UDP traffic
to the given port.


## Key Generation
!!! warning
    The private key will enable anyone to impersonate that client on the VPN.

Public/Private keys need to be generated for each machine using wireguard. A
bare bones utility is provided. Generated keys are not OS specific.

??? abstract "/usr/local/bin/wggen"
    0755 root:root

    ``` bash
    #!/bin/bash
    # Generate wireguard keys.
    WG=/usr/bin/wg
    TEE=/usr/bin/tee

    if [ -z "$1" ]; then
        echo "Requires name for output files."
        exit 1
    else
        name=$1
    fi

    ${WG} genkey | ${TEE} ${1}.key | ${WG} pubkey > ${1}.pub
    chmod 0400 ${1}.{key,pub}
    ```


## Examples

### Point to Point Example
This setup enables a private network connection to the server, preventing other
clients on that network from communicating to other clients. DNS and any
network access not directly addressed to the private network will egress
through the client's standard network stack.

This creates a /24 network that all machines use, while only allowing point to
point communications from each client to the server.

#### Server

??? abstract "/etc/wireguard/server.conf"
    0600 root:root

    ``` bash
    [Interface]
    Address = 172.31.255.254/24
    SaveConfig = False
    ListenPort = 51820
    PrivateKey = {SERVER PRIVATE KEY}

    # Client #1
    [Peer]
    PublicKey = {CLIENT PUBLIC KEY}
    AllowedIPs = 172.31.255.250/32
    ```

``` bash
# Bring up the tunnel for testing.
systemctl enable wg-quick@server
```

### Clients
!!! warning
    Windows clients do **not** use the **SaveConfig** option. Remove this line
    if configuring a Windows client.

??? abstract "/etc/wireguard/client.conf"
    0600 root:root

    ``` bash
    [Interface]
    Address = 172.31.255.250/24
    PrivateKey = {CLIENT PRIVATE KEY}
    SaveConfig = False

    # Wireguard server
    [Peer]
    PublicKey = {SERVER PUBLIC KEY}
    EndPoint = {SERVER PUBLIC IP}:51820
    AllowedIPs = 172.31.255.254/32
    ```

``` bash
# Bring up the tunnel for testing.
systemctl enable wg-quick@client
```

### Testing
``` bash
# Show server network status and ping a client.
wg
ping 172.31.255.250

# Show client network status and ping server. Pinging other clients should fail.
wg
ping 172.31.255.254
ping 172.31.255.100
```


## VPN Example
Behaves like a traditional VPN network. All traffic and DNS lookups are routed
through the connection to be resolved in the VPN server location.

### Server
``` bash
# Enable IP traffic forwarding on iptables.
echo 1 > /proc/sys/net/ipv4/ip_forward
echo 1 > /proc/sys/net/ipv6/ip_forward
```

??? abstract "/etc/sysctl.conf"
    0644 root:root

    ``` bash
    net.ipv4.ip_forward = 1
    net.ipv6.conf.all.forwarding = 1
    ```

??? abstract "/etc/wireguard/server.conf"
    0600 root:root

    ``` bash
    [Interface]
    Address = 172.31.255.254/24
    SaveConfig = False
    ListenPort = 51820
    PrivateKey = {SERVER PRIVATE KEY}
    # Automatically adjust iptables rules to allow forwarded traffic when VPN up.
    PostUp = iptables -A FORWARD -i {WIREGUARD TUNNEL} -j ACCEPT; iptables -t nat -A POSTROUTING -o {INTERFACE} -j MASQUERADE; ip6tables -A FORWARD -i {WIREGUARD TUNNEL} -j ACCEPT; ip6tables -t nat -A POSTROUTING -o {INTERFACE} -j MASQUERADE
    PostDown = iptables -D FORWARD -i {WIREGUARD TUNNEL} -j ACCEPT; iptables -t nat -D POSTROUTING -o {INTERFACE} -j MASQUERADE; ip6tables -D FORWARD -i {WIREGUARD TUNNEL} -j ACCEPT; ip6tables -t nat -D POSTROUTING -o {INTERFACE} -j MASQUERADE

    # Client #1
    [Peer]
    PublicKey = {CLIENT PUBLIC KEY}
    AllowedIPs = 172.31.255.250/32
    ```

``` bash
# Bring up the tunnel for testing.
systemctl enable wg-quick@server
```

### Client
!!! tip
    Set a custom DNS server if needed. DNS is resolved at the VPN server.

??? abstract "/etc/wireguard/client.conf"
    0600 root:root

    ``` bash
    # Route all traffic through VPN connection.
    [Interface]
    Address = 172.31.255.250/24
    PrivateKey = {CLIENT PRIVATE KEY}
    DNS = 1.1.1.1,1.1.2.2
    SaveConfig = False

    # Wireguard server
    [Peer]
    PublicKey = {SERVER PUBLIC KEY}
    EndPoint = {SERVER PUBLIC IP}:51820
    AllowedIPs = 0.0.0.0/0
    ```

``` bash
# Bring up the tunnel for testing.
systemctl enable wg-quick@vpn-client
```

### [Testing][a]
From the client access the Internet and verify that your data is routed through
the VPN server.

A quick test can be verifying different IP's from https://www.whatismyip.com.


## [InitRAMFS][b]
Enable wireguard during boot process allowing for remote unlocks anywhere in
the world.

[a]: https://www.ckn.io/blog/2017/11/14/wireguard-vpn-typical-setup
[b]: https://github.com/r-pufky/wireguard-initramfs
