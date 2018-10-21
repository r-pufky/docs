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

KVM Specific Issues
-------------------
There seems to be an issue with Netplan bridging, KVM, and using the same
bridged for host networking traffic as well as VM traffic. The workaround is to
have a separate bridged adapter.

[1]: https://netplan.io/reference
[2]: https://webby.land/2018/04/27/bridging-under-ubuntu-18-04/
[3]: https://ubuntuforums.org/showthread.php?t=2391884
[4]: https://serverfault.com/questions/910955/problems-with-setting-up-bonding-on-netplan-ubuntu-server-18-04
[5]: https://www.tomechangosubanana.com/2018/kvm-bridged-to-the-lan-with-dhcp/
[6]: https://askubuntu.com/questions/971126/17-10-netplan-config-with-bridge
