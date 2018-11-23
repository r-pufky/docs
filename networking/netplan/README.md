Netplan
-------
Replacement for ifconfig scripts to abstract network configuration to yaml
files.

General Usage
-------------
Usage is typically done by generating a plan and applying it. The old moniker of
ifup/ifdown no longer applies. [bridge-utils][3] should not be used
independently with netplan. Netplan should take care of *all* network
configuration.

Make changes in `/etc/netplan/01-netcfg.yaml` by default. See __[reference][1]__
for configuration options.

Generate new configurations from the plan
```bash
netplan generate --debug
```

Apply the network plan to the system
```bash
netplan --debug apply
```

Check the status of generated devices
```bash
networkctl list
```

Show all interfaces
```bash
ip a
```

Bridging
--------
This is useful for providing a network interface to be used for VM's / Docker
containers. The bridged network can be assigned an IP address directly and used
as well; however there seems to be an issue with using a bridge network with KVM
 as well as the host network. See [reference][1] and [general bridging help.][6]

In most cases for advanced configuration the base adapter *shouldn't* be
configured for an IP address, the resulting bonded or bridged device should.

[Example](01-netcfg-bridged-networks.yaml): Two nics bridged together, using
  dhcp, ipv4, a specific MAC address with spanning tree and forward delay
  disabled. [Original Reference.][5]

[Example](01-netcfg-bonded-bridged-networks.yaml): Two nics bonded together in
  the default configuration, with a bridge created on top of the bonded
  interface. [Original Reference.][4]

[Example](01-netcfg-bonded-with-bridge.yaml): Three nics, two bonded together
  with a custom mode and primary set. The bridged network is a single card with
  spanning tree and forward delay disabled.

Default Route Issues
--------------------
Netplan does not [currently allow route or metric configuration][10] for DHCP
enabled device. This creates issues when there are multiple adapters all
connected at the same time -- the default route is last brought up. This works
around the issue by [manually setting networkd][11] **after** netplan is run.

### Configure netplan as normal
Setup however you like. Remember your interface designation. Apply your config.

### Copy desired default route adapter setting to /etc

```bash
cp /run/systemd/network/10-netplan-<ADAPTER>.network /etc/systemd/network
```

vi /etc/systemd/network/10-netplan-<ADAPTER>.network
```yaml
[DHCP]
RouteMetric=101
```
 * Add `RouteMetric`, higher number is lower priority. Default is 100.
 * Whenever you **apply a new netplan configuration** you will need to ensure
   this is still correct.

KVM Specific Issues
-------------------
There seems to be an issue with Netplan bridging, KVM, and using the same
bridged for host networking traffic as well as VM traffic. The workaround is to
have a separate bridged adapter. Thi is a [longstanding bug][8] with KVM and can
be fixed by modifying [sysctl settings][9]

### Docker adds -P FORWARD DROP rule to iptables
By default Docker will add `-P FORWARD DROP` rule to iptables to prevent
specific exploitation vectors for containers. Unfortunately, this is applied to
**all** interfaces, regardless of whatever interface docker uses; this rule is
re-applied everytime the service is started. [Iptables by default filters
bridged interfaces][7]

This will result in KVM virtual machines on a system with Docker to not be able
to use a Bridge for network communication. As a bridge is a layer 2 device, it
really shouldn't be filtering IP packets anyways. You can just disable bridged
 adapters from applying the iptables. If you still use the bridge adapter for
 system traffic, consider munging the filter instead.

Disable IP filtering on bridged interfaces:
```bash
echo "0" /proc/sys/net/bridge/bridge-nf-call-iptables
echo "0" /proc/sys/net/bridge/bridge-nf-call-ip6tables
echo "0" /proc/sys/net/bridge/bridge-nf-call-arptables
```
 * This will not persist across reboots, but to validate bridging is fixed

Update settings for sysctl as well as [UFW sysctl][9].

/etc/sysctl.conf
```bash
net.bridge.bridge-nf-call-ip6tables = 0
net.bridge.bridge-nf-call-iptables = 0
net.bridge.bridge-nf-call-arptables = 0
```

/etc/ufw/sysctl.conf
```bash
net.bridge.bridge-nf-call-ip6tables = 0
net.bridge.bridge-nf-call-iptables = 0
net.bridge.bridge-nf-call-arptables = 0
```

There is a [longstanding bug][8] bug with sysctl in debian/ubuntu not applying
sysctl.conf properly with network settings. This can be resolved using a root
cronjob

sudo crontab -e
```bash
@reboot sleep 15; /sbin/sysctl -p
```

Ensure settings are applied by rebooting and checking settings are set.
```bash
reboot
sysctl -a | grep bridge
```


[1]: https://netplan.io/reference
[2]: https://webby.land/2018/04/27/bridging-under-ubuntu-18-04/
[3]: https://ubuntuforums.org/showthread.php?t=2391884
[4]: https://serverfault.com/questions/910955/problems-with-setting-up-bonding-on-netplan-ubuntu-server-18-04
[5]: https://www.tomechangosubanana.com/2018/kvm-bridged-to-the-lan-with-dhcp/
[6]: https://askubuntu.com/questions/971126/17-10-netplan-config-with-bridge
[7]: https://serverfault.com/questions/162366/iptables-bridge-and-forward-chain
[8]: https://bugs.launchpad.net/ubuntu/+source/procps/+bug/50093
[9]: https://serverfault.com/questions/431590/how-to-make-sysctl-network-bridge-settings-persist-after-a-reboot
[10]: https://bugs.launchpad.net/netplan/+bug/1781652
[11]: https://askubuntu.com/questions/1042582/how-to-set-default-route-with-netplan-ubuntu-18-04-server-2-nic