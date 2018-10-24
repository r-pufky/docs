KVM Server Setup
----------------
Basic KVM server setup on ubuntu (18.04).
1. [Install Service](#install-service)
1. [KVM Networking](#kvm-networking)
1. [Important File Locations](#important-file-locations)
1. [Creating New VM](#creating-new-vm)
1. [Convert XenServer XVA to KVM Image](#convert-xenserver-xva-to-kvm-template)
1. [Moving KVM Images](#moving-kvm-images)
1. [Moving KVM Storage Pool](#moving-kvm-storage-pool)
1. [References](#references)

Install Service
---------------

### Ensure hardware can support virtualization
```bash
egrep -c '(vmx|svm)' /proc/cpuinfo
```
 * Anythings <= 0 means that hardware virtualization is disabled or not
   supported with hardware
 * Check BIOS, ensure `IMMOU` and `SVM` is enabled for AMD processors
 * Check BIOS, ensure `IMMOU` and `VT-d` is enabled for Intel processors

### Verify KVM accleration can be used
```bash
apt install cpu-checker
kvm-ok
```
 * This should clearly state if accleration can be used

### Install KVM packages
```bash
apt install qemu qemu-kvm qemu-efi qemu-utils libvirt-bin libvirt-clients libvirt-daemon-system virt-manager
```

### Set user group permissions
```bash
adduser <user> libvirt
adduser <user> libvirt-qemu
```
 * This is so a normal user can run virt-manager, instead of logging in as root

KVM Networking
--------------
By default KVM creates its own NAT network for VMs, howver using a bridge will
allow these VMs to directly use your physical network.

### Docker adds -P FORWARD DROP rule to iptables
By default Docker will add `-P FORWARD DROP` rule to iptables to prevent
specific exploitation vectors for containers. Unfortunately, this is applied to
**all** interfaces, regardless of whatever interface docker uses; this rule is
re-applied everytime the service is started. [iptables by default filters
bridged interfaces][14]

This will result in KVM virtual machines on a system with Docker to not be able
to use a Bridge for network communication. As a bridge is a layer 2 device, it
really shouldn't be filtering IP packets anyways. You can just disable bridged
 adapters from applying the iptables. If you still use the bridge adapter for
 system traffic, consider munging the filter instead:

Disable IP filtering on bridged interfaces
```bash
echo "0" /proc/sys/net/bridge/bridge-nf-call-iptables
echo "0" /proc/sys/net/bridge/bridge-nf-call-ip6tables
```

### Create a Network Bridge
This is so VM's can get IP's on the network, instead of using NAT.

/etc/netplan/01-netcfg.yaml
```bash
network:
  version: 2
  renderer: networkd
  ethernets:
    eno1:
      dhcp4: yes
    eno2:
      dhcp4: no

  bridges:
    br0:
      interfaces: [eno2]
      dhcp4: no
      macaddress: A0:B1:C2:D3:E4:F5
```
 * netplan seems funky in consistently applying changes. In most cases a reboot
   applies the config correctly.
 * You may lose network connectivity while applying
 * MAC is randomly generated on boot if not specified for the bridge network.
 * `ip a` to show a list of networks and state

Apply the network configuration
```bash
netplan --debug apply
networkctl status -a
```
 * `ip a` should also display corresponding information
 * `ifconfig` not as useful

### Add bridge to KVM menu drop down.
By default if you add a bridge, you will have to select `Specify Shared Device
Name` then entering your bridge (typically `br0`). This will add the bridge
directly to the dropdown menu instead.

Create an xml configuration file with your settings

/etc/libvertd/qemu/networks/br0.xml
```xml
<network>
  <name>br0</name>
  <bridge name='br0'/>
  <forward mode='bridge'/>
</network>
```
 * See [network XML file format][11]
 * See bug for creating [bridged netplan interfaces for libvirtd][13]

Import the network into KVM, start it and set to autostart
To define a network from an XML file without starting it, use:

```bash
virsh net-define /etc/libvertd/qemu/networks/br0.xml
virsh net-start br0
virsh net-autostart br0
```

Show virtual networks, persistent should read `yes` for it to autostart
```bash
virsh net-list --all
```

###Remove pre-made NAT virtual bridge
This network is un-needed if using bridging.

Identify the NAT virtual network
```bash
virsh net-list -all
```

Set network inactive, remove it and restart libvirtd
```bash
virsh net-destroy br1
virsh net-undefine br1
service libvirtd restart
```

Confirm the network no longer exists
```bash
virch net-list --all
```

Important File Locations
------------------------
Basic locations of important files for KVM

| File                            | Purpose                           |
|---------------------------------|-----------------------------------|
| /etc/libvirtd/                  | KVM and VM configuration data     |
| /var/lib/libvirt/images         | Default KVM image pool Location   |

Creating New VM
---------------
Setup a standard VM to use the network bridge.

Enabled X11 forwarding, then start Virtualization Manager
```bash
virt-manager
```
 * Select existing RAW image for disk, or createa new one
 * check: customize configuration before install
 * Network selection dropodown
   * Specify Shared Device Name > br0
   "br0" or whatever your bridge is called.
 * Hardware details
   * NIC
      * Set MAC address
      * Use virtio device
   * Add Hardware
     * Select disk image to use.
 * *** Important, be sure to click 'begin installation' for VM to be created
   * Virtual Hardware details
   * Disk - link to existing disks, or create a new disk using `RAW`

Convert XenServer XVA to KVM Image
----------------------------------
XenServer images cannot be directly imported, they must be converted first.
 * VM's should be exported 1 instance per XVA image export.

### Install Build Tools
```bash
apt install cmake gcc build-essentials libssl-dev
```

### Clone xva-img Tool & Build
```bash
git clone https://github.com/eriklax/xva-img.git
cd xva-img/
cmake .
sudo make install
```

### Extract VM from XVA Image
```bash
mkdir my_vm
tar -xvf my_vm.xva -C my_vm
chmod -R 0755 my_vm
xva-img -p disk-export my_vm/Ref\:{XXX}/ my_vm/ref-{XXX}.raw
```
 * Disks have no permissions by default.
 * There will be __one `Ref:XXX` directory per disk__. Generally, keep this
   named as the reference number for sanity, until you know what they are.
 * Note: RAW is generally better for performance and long term performance.

### (Optional): Convert Disk Image to qcow2
```bash
qemu-img convert -f raw -O qcow2 my_vm/ref-{XXX}.raw my_vm/ref-{XXX}.qcow2
```

### Grab Metadata From VM
VM metadata (such as # of CPU's, memory, MAC) are not extracted by default.
This should be extracted for correct VM import into KVM.

CPU
```bash
grep -o '.\{0,40\}CPU.\{0,40\}' my_vm/ova.xml
```

Memory
```bash
grep -o '.\{0,40\}memory.\{0,40\}' my_vm/ova.xml
```

MAC
```bash
grep -o '.\{0,40\}MAC.\{0,40\}' my_vm/ova.xml
```

Hostname
```bash
grep -o '.\{0,40\}hostname.\{0,40\}' my_vm/ova.xml
```

Moving KVM Images
-----------------
KVM images are stored in two locations, configuration and disk images.

Dump the Current VM configuration
```bash
virsh dumpxml <vm-name> > vm-name.xml
```
 * Copy the XML file and associated disks to new location

Import VM
```bash
virsh create vm-name.xml
```
 * Update disk location in XML file if location has changed

Moving KVM Storage Pool
-----------------------
The default image storage location makes sense for linux (/var), but not for
servers centralizing data to storage pools.

Dump Disk Image Pool
```bash
virsh pool-dumpxml default > pool.xml
```
 * Assumes pool name is `default`
 * Make sure disk images are moved to new location
 * Update disk image locations in XML file

Destroy existing pool, import new pool
```bash
virsh pool-destory default
virsh pool-create pool.xml
```

References
----------
[KVM on Ubuntu 18.04 Bionic][1]

[KVM on Ubuntu 18.04 Alternative][2]

[Netplan Bridging Examples][3]

[Configurating Static IP addresses with Netplan][4]

[Netplan static MAC address for Bridge][5]

[Converting Citrix XenServer XVA to KVM image][6]

[Performance/benefits of RAW versus QCOW2][7]

[Moving KVM VM's to another machine][8]

[Moving KVM Storage Pool][9]

[Remove KVM NAT Virtual Bridge][10]

[Network XML configuration for KVM][11]

[KVM Networking Overview][12]

[Configuring KVM libvirtd networking with netplan][13]

[1]: https://www.linuxtechi.com/install-configure-kvm-ubuntu-18-04-server/
[2]: https://linuxconfig.org/install-and-set-up-kvm-on-ubuntu-18-04-bionic-beaver-linux
[3]: https://netplan.io/examples#bridging
[4]: https://websiteforstudents.com/configure-static-ip-addresses-on-ubuntu-18-04-beta/
[5]: https://bugs.launchpad.net/netplan/+bug/1718607
[6]: https://chariotsolutions.com/blog/post/convert-citrix-xenserver-xva-image-to-kvm/
[7]: https://unix.stackexchange.com/questions/227792/are-there-any-benefits-of-using-qcow2-over-img-and-which-is-recommended-for-ma
[8]: https://ask.fedoraproject.org/en/question/29704/how-do-i-move-a-virtual-machine-in-gnome-boxes-to-another-host/
[9]: http://ask.xmodulo.com/change-default-location-libvirt-vm-images.html
[10]: https://www.cyberciti.biz/faq/linux-kvm-disable-virbr0-nat-interface/
[11]: https://libvirt.org/formatnetwork.html
[12]: https://wiki.libvirt.org/page/Networking
[13]: https://bugs.launchpad.net/ubuntu/+source/libvirt/+bug/1770345
[14]: https://serverfault.com/questions/162366/iptables-bridge-and-forward-chain