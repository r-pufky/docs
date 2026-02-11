# Promox (PVE)


## Setup

### Prep
* Make full **stop** backup of containers/vms to **pve/backups**.
* Shutdown containers.

For all cluster nodes
``` bash
mkdir -p /autofs/pve/{DATE}-upgrade/{NODE}
cp -av /etc /autofs/pve/{DATE}-upgrade/{NODE}
cp -av /root /autofs/pve/{DATE}-upgrade/{NODE}
```
* Only upgrade one cluster node at a time.

### Base Install
Create [Live USB Install][a].

Install Options

* **Graphical install**
* License: **agree**
* Default HD Setup (EXT4): **next**
* Country: **United States**
* Timezone: **UTC**
* Keyboard Layout: **U.S. English**
* Email: **root@localhost**
* Reboot when complete

### Base Networking
Use bonded interface (only the first adapter) for management IP. Always confirm
device names as they **may** change between major OS releases.

``` bash
nano /etc/network/interfaces  # No network - vim not installed.
systemctl restart networking
ping google.com
apt install vim
```

Remaining configuration may be done vis SSH (easier for copying). Leave console
open for easy rescue if networking get mis-configured.

### Enable IOMMU and Passthrough Virtualization
!!! abstract "/etc/default/grub"
    0644 root:root

    ``` ini
    # AMD: IOMMU & SVM enabled in BIOS. Use amd_iommu for grub.
    # Intel: IOMMU & VT-d enabled in BIOS. Use intel_iommu for grub.
    GRUB_CMDLINE_LINUX_DEFAULT="quiet intel_iommu=on iommu=pt"
    ```

``` bash
update-grub
reboot
```

### Update Sources
[Source list here][b].

!!! warning
    Always update Proxmox with **dist-upgrade**. Never use **upgrade**.

!!! abstract "/etc/apt/sources.list.d/debian.sources"

    ``` yaml
    Types: deb
    URIs: http://deb.debian.org/debian/
    Suites: trixie trixie-updates
    Components: main contrib non-free-firmware
    Signed-By: /usr/share/keyrings/debian-archive-keyring.gpg

    Types: deb
    URIs: http://security.debian.org/debian-security/
    Suites: trixie-security
    Components: main contrib non-free-firmware
    Signed-By: /usr/share/keyrings/debian-archive-keyring.gpg
    ```

!!! abstract "/etc/apt/sources.list.d/ceph.sources"

    ``` yaml
    Types: deb
    URIs: http://download.proxmox.com/debian/ceph-squid  # NOTE: URL, HTTP.
    Suites: trixie
    Components: no-subscription
    Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
    ```

!!! abstract "/etc/apt/sources.list.d/pve-enterprise.sources"

    ``` yaml
    Types: deb
    URIs: http://download.proxmox.com/debian/pve  # NOTE: URL, HTTP.
    Suites: trixie
    Components: pve-no-subscription
    Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
    ```

Upgrade distribution
``` bash
apt update
apt dist-upgrade
```

### Update Microcode
Trixie+ base should now include firmware by default.

Confirm update applied (Current patch for i9-13900H is **0x4128**).
``` bash
apt install intel-microcode
grep microcode /proc/cpuinfo
```

### Install Fake Subscription
```bash
wget https://github.com/Jamesits/pve-fake-subscription/releases/download/v0.0.11/pve-fake-subscription_0.0.11+git-1_all.deb
dpkg -i pve-fake-subscription_*.deb
echo "127.0.0.1 shop.maurer-it.com" | tee -a /etc/hosts
reboot
```

### Setup interfaces
Always confirm device names as they *may* change between major OS releases.

Make a backup of interfaces (this also has the detected interface names).
``` bash
cp /etc/network/interfaces /etc/network/interfaces.orig
```

#### /etc/network/interfaces
* Copy from backup or source from host_vars (verify interface names).
* **Remove** `post-up /usr/bin/systemctl restart frr.service`.
* Update host_vars.

#### [Direct mesh networking (routed, simple).][c]
Ensure network is not an existing routed VLAN on router/switches or requests
will be routed instead of sent via links (VLAN may be defined and exist but
no interfaces should be defined to use them or serve DHCP/DNS).

### PVE9+ default enables FRR.

!!! warning
    FRR does **not** need `post-up /usr/bin/systemctl restart frr.service` as
    of **PVE9+/Trixie**. Issue has been resolve in base OS and will cause
    hard-locks during boot requiring console access to resolve.

    Using FRR for cluster network will **not** show network in WebUI; cluster
    configuration **must** be done on CLI and node additions via SSH.

```bash
# Get Interface Addresses
apt install frr pciutils  # lspci now in pciutils.
ls -l /sys/class/net
lspci
lspci -nn
lspci -k
```

!!! abstract "/etc/frr/daemons"
    0640 frr:frr

    ``` ini
      fabricd=yes  # Other FRR daemons already enabled in PVE9+.
    ```

!!! abstract "/etc/frr/frr.conf"
    0640 frr:frr

    Copy from backup or source from host_vars (verify interface names):

    * See **is-is** routing for net definition.
    * Use subnet for area ID.
    * IP address with padding for system identifier.
    * Update host_vars.

#### [Confirm FRR configured correctly.][d]
``` bash
systemctl restart frr.service  # FRR non-root. Config must be owned by FRR.
systemctl enable frr.service
vtysh -c "show openfabric topology"

# Restart Networking
systemctl restart networking  # May take up to 1 minute over SSH.
reboot
```

* Alternatively use console.
* Reboot and confirm node networking working.

### [Create Cluster (First Node)][e]
Only use on first first node.

``` bash
pvecm create hv --link0 10.11.11.10 --nodeid 1
pvecm status
```

### [Add Node to Cluster (All Other Nodes)][e]
``` bash
# Node2: Add node 2 to node 1.
pvecm add 10.11.11.10 --link0 10.11.11.20 --use_ssh
# Node3: Add node 3 to node 1.
pvecm add 10.11.11.10 --link0 10.11.11.30 --use_ssh

pvecm status
```

### [Enable ACME Cluster Node Certificates][h]

### [Backup Initial SSH Config][f]
!!! warning
    Proxmox uses host keys and root user for intra-cluster traffic. Changing
    SSH settings may break this.

    Create a backup to ensure a default working state can be restored.

Backup each node.
``` bash
cp -av /root /autofs/pve/{DATE}-upgrade-8-to-9/{NODE}/complete
cp -av /etc /autofs/pve/{DATE}-upgrade-8-to-9/{NODE}/complete
```


## GPU Passthrough
Configure for all nodes.

!!! abstract "/etc/default/grub"
    0644 root:root

    ``` ini
    GRUB_CMDLINE_LINUX_DEFAULT="quiet intel_iommu=on iommu=pt i915.enable_gvt=1"
    ```

See [IMMOU and Passthrough Virtualization][g] for other GRUB options.

Remove legacy module configs (future Debian release will remove these).
``` bash
rm /etc/modules-load.d/modules.conf  # Remove symlink to /etc/modules.
rm /etc/modules
```

!!! abstract "/etc/modules-load.d/video.conf"
    0644 root:root

    ``` ini
    # /etc/modules is obsolete and has been replaced by /etc/modules-load.d/.
    # Please see modules-load.d(5) and modprobe.d(5) for details.
    vfio
    vfio_iommu_type1
    vfio_pci
    kvmgt
    ```

### Map non-root users to GPU
Unmapped containers require **other** R/W permissions on GPU.

!!! abstract "/etc/udev/rules.d/59-igpu-passthrough.rules"
    0644 root:root

    ``` bash
    KERNEL=="renderD128", MODE="0666"
    KERNEL=="card1", MODE="0666"
    ```

Update grub.
``` bash
update-grub
reboot

# Confirm card reported.
dmesg | grep -e DMAR -e IOMMU  # IOMMU enabled w. graphics passthrough.
lspci -nnv | grep -i vga  # PCI device reported.
```

### Container configuration

#### Get GPU major device ID
``` bash
getent group video
> video:x:44:root  # GID: 44
getent group render
> render:x:993:root  # GID: 993

id -g render
ls -l /dev/dri
# Major ID is 226.
> crw-rw---- 1 root video  226,   0 May 12 21:54 card1
> crw-rw---- 1 root render 226, 128 May 12 21:54 renderD128
```

!!! abstract "/etc/pve/lxc/{ID}.conf"
    0644 root:root

    ``` yaml
    # Map major device ID to LXC container.
    lxc.cgroup2.devices.allow: c 226:* rwm
    lxc.mount.entry: /dev/dri/card1 dev/dri/card1 none bind,optional,create=file,mode=0666
    lxc.mount.entry: /dev/dri/renderD128 dev/dri/renderD128 none bind,optional,create=file,mode=0666
    ```

!!! abstract "/etc/subgid"
    0644 root:root

    ``` bash
    # Map render, video groups for unprivileged containers.
    # ALWAYS confirm group ID's as they may change between major OS versions.
    root:44:1
    root:993:1  # 108 in Bookworm.
    ```

``` bash
# Host dev/dri permissions do not require containers to set groups with.
usermod -aG render,video root
```


## Add NFS mounted volumes

### Add UID/GID mappings for NFS mounts.
Use https://github.com/ddimick/proxmox-lxc-idmapper to generate mappings or
copy existing mappings from backups.

!!! abstract "/etc/subuid"
    0644 root:root

!!! abstract "/etc/subgid"
    0644 root:root

### Create NFS mount locations
Set mounts immutable to prevent writes when not mounted.

``` bash
mkdir /autofs
mkdir {MOUNT}
chattr +i /autofs
cd /autofs
chattr +i *
```

!!! abstract "/etc/fstab"
    0644 root:root

    ``` conf
    {SERVER}:/d/pve /autofs/pve nfs4 rw,nfsvers=4,minorversion=2,proto=tcp,fsc,rsize=1048576,wsize=1048576,nocto,_netdev 0 0
    ```

``` bash
systemctl daemon-reload
mount -a
ls -l /autofs  # Mounted R/W with NFS squashed permissions.
```

### Mount PVE Storage
Cluster data storage over NFS.

``` bash
pvesm add dir pve --path /autofs/pve --content images,vztmpl,backup,snippets,rootdir,iso
reboot  # NFS should be mounted on boot.
```


## Reference[^1][^2][^3][^4][^5][^6]

[^1]: https://www.juniper.net/documentation/us/en/software/junos/is-is/topics/concept/is-is-routing-overview.html#routing-is-is-overview__id-11020505
[^2]: https://gist.github.com/scyto/4c664734535da122f4ab2951b22b2085
[^3]: https://www.baeldung.com/linux/ethernet-dual-cards-increase-throughput
[^4]: https://bookstack.swigg.net/books/linux/page/lxc-gpu-access
[^5]: https://forum.proxmox.com/threads/proxmox-lxc-igpu-passthrough.141381/
[^6]: https://www.youtube.com/watch?v=0ZDr5h52OOE

[a]: https://www.proxmox.com/en/downloads/proxmox-virtual-environment/iso
[b]: https://pve.proxmox.com/wiki/Package_Repositories
[c]: https://pve.proxmox.com/wiki/Full_Mesh_Network_for_Ceph_Server#Routed_Setup_(Simple)
[d]: https://pve.proxmox.com/wiki/Full_Mesh_Network_for_Ceph_Server
[e]: https://pve.proxmox.com/wiki/Cluster_Manager
[f]: https://forum.proxmox.com/threads/2025-pve9-x-warning-remote-host-identification-has-changed-analysis-resolution.174262
[g]: #enable-iommu-and-passthrough-virtualization
[h]: acme.md
