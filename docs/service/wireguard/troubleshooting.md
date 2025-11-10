# Troubleshooting

## Debugging
Issues with wireguard connections can be debugged by enabling dynamic debug in
the kernel.

``` bash
# Enable.
echo 'module wireguard +p' | sudo tee /sys/kernel/debug/dynamic_debug/control
dmesg -wH

# Disable.
echo 'module wireguard -p' | sudo tee /sys/kernel/debug/dynamic_debug/control
```

## SSH not working, UFW allowing SSH, No NAT
Expresses as pings between clients through the wireguard server work correctly,
but SSH'ing fails. UFW on the wireguard server is enabled and allowing SSH
traffic. Disabling UFW allows SSH connections to happen.

Traffic needs to be tagged in IP tables to allow wireguard to wireguard traffic
to be forwarded; otherwise this is not tagged as inbound traffic to the
wireguard server in UFW and subsequently blocked.

**/etc/wireguard/server.conf** (1)
{ .annotate }

1. 0600 root:root
``` bash
iptables -A FORWARD -i {INTERFACE} -o {INTERFACE} -m conntrack --ctstate NEW -j ACCEPT
```

Reference

* https://serverfault.com/questions/985482/wireguard-access-between-clients-ufw-block
