# Promox (PVE)

## Setup
!!! warning "Make full **stop** backup of containers/vms to **pve/backups**"

Only install/upgrade one cluster node at a time. Configure all nodes
homogeneously.

``` bash
# Backup each node.
mkdir -p /autofs/pve/{DATE}-upgrade/{NODE}
cp -av /etc /autofs/pve/{DATE}-upgrade/{NODE}
cp -av /root /autofs/pve/{DATE}-upgrade/{NODE}
```

### Install
Create [Live USB Install][a] and [boot](../pikvm.md#remote-iso-mount).

!!! example "Install Options"
    * **Graphical install**
    * License: **agree**
    * Default HD Setup (EXT4): **next**
    * Country: **United States**
    * Timezone: **UTC**
    * Keyboard Layout: **U.S. English**
    * Email: **root@localhost**
    * Management Network Configuration:
        * [Pin network interface names][i]: **enabled**
        * Options: Align all **interface names** to **same hardware** for all nodes.
    * Reboot when complete

!!! tip "Always use name pinning"
    Prevents sudden interface name changes between updates and Major OS
    releases.

### Base Networking
Use bonded interface (only the first adapter) for management IP.

``` bash
nano /etc/network/interfaces  # No network - vim not installed.
systemctl restart networking
ping google.com
apt install vim
```

Remaining configuration may be done vis SSH (easier for copying). Leave console
open for easy rescue if networking get mis-configured.

### Enable IOMMU and Passthrough Virtualization
=== "AMD"

    !!! abstract "/etc/default/grub"
        0644 root:root

        ``` ini
        # IOMMU & SVM enabled in BIOS.
        GRUB_CMDLINE_LINUX_DEFAULT="quiet amd_iommu=on iommu=pt"
        ```

=== "Intel"

    !!! abstract "/etc/default/grub"
        0644 root:root

        ``` ini
        # IOMMU & VT-d enabled in BIOS.
        GRUB_CMDLINE_LINUX_DEFAULT="quiet intel_iommu=on iommu=pt"
        ```

``` bash
# Remove legacy module configs (future Debian releases will remove these).
rm /etc/modules-load.d/modules.conf  # Remove symlink to /etc/modules.
rm /etc/modules

update-grub
reboot
```

### [Packages][b]
Comment out original sources as needed.

!!! warning
    Always update Proxmox with **dist-upgrade**. Never use **upgrade**.

!!! abstract "/etc/apt/sources.list.d/debian.sources"
    0644 root:root

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
    0644 root:root

    ``` yaml
    Types: deb
    URIs: http://download.proxmox.com/debian/ceph-squid  # NOTE: URL, HTTP.
    Suites: trixie
    Components: no-subscription
    Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
    ```

!!! abstract "/etc/apt/sources.list.d/pve-enterprise.sources"
    0644 root:root

    ``` yaml
    Types: deb
    URIs: http://download.proxmox.com/debian/pve  # NOTE: URL, HTTP.
    Suites: trixie
    Components: pve-no-subscription
    Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
    ```

``` bash
apt modernize-sources
apt update
apt dist-upgrade
```

#### Update Microcode
Trixie+ base should now include firmware by default.

=== "AMD"

    ``` bash
    apt install amd64-microcode
    grep microcode /proc/cpuinfo
    ```

=== "Intel"

    ``` bash
    apt install intel-microcode
    grep microcode /proc/cpuinfo
    ```

#### Install Fake Subscription
Disables subscription notification for servers not using enterprise support.

```bash
wget https://github.com/Jamesits/pve-fake-subscription/releases/download/v0.0.11/pve-fake-subscription_0.0.11+git-1_all.deb
dpkg -i pve-fake-subscription_*.deb
echo "127.0.0.1 shop.maurer-it.com" | tee -a /etc/hosts
reboot
```

## Networking
Update interfaces definitions as needed for new/upgrade installs, including
ansible inventory.

### /etc/network/interfaces

``` bash
cp /etc/network/interfaces /etc/network/interfaces.orig

# Previous config may be transferred and updated.
vim /etc/network/interfaces
```

!!! info "post-up restart for FRR service not needed in PVE9+"
    Bug has been resolved and service is automatically trigger on refresh.

### FRR

#### [Fabricd][c]
Cluster traffic setup with simple routed direct mech networking using fabricd.
PVE9+ enables FRR by default.


!!! warning
    FRR does **not** need `post-up /usr/bin/systemctl restart frr.service` as
    of **PVE9+/Trixie**. Issue has been resolve in base OS and will cause
    hard-locks during boot requiring console access to resolve.

    Using FRR for cluster network will **not** show network in WebUI; cluster
    configuration **must** be done on CLI and node additions via SSH.

```bash
# Get Interface Addresses.
apt install frr pciutils  # lspci now in pciutils.
ls -l /sys/class/net
lspci
lspci -nn
lspci -k
```

!!! info "Example Cluster Network"
    Do **NOT** blindly copy FRR configuration. Network configuration provided
    for a anonymized working example that uses **is-is** routing, subnet for
    area ID, and IP address with padding for system identifier.

    Ensure network is not an existing routed VLAN on router/switches or
    requests will be routed instead of sent via links (VLAN may be defined and
    exist but no interfaces should be defined to use them or serve DHCP/DNS).

    See references for detailed FRR configuration.

!!! abstract "/etc/frr/daemons"
    0640 frr:frr

    ``` ini
      fabricd=yes  # Other FRR daemons already enabled in PVE9+.
    ```

=== "Node 1"

    !!! abstract "/etc/frr/frr.conf"
        0640 frr:frr

        ``` ini
        # Or copy from existing backup.
        network_frr_config: |
          frr defaults traditional
          hostname node1
          log syslog warning
          ip forwarding
          no ipv6 forwarding
          service integrated-vtysh-config
          !
          interface lo
           ip address 10.11.11.10/32
           ip router openfabric 1
           openfabric passive
          !
          interface nic4
           ip router openfabric 1
           openfabric csnp-interval 2
           openfabric hello-interval 1
           openfabric hello-multiplier 2
          !
          interface nic5
           ip router openfabric 1
           openfabric csnp-interval 2
           openfabric hello-interval 1
           openfabric hello-multiplier 2
          !
          line vty
          !
          router openfabric 1
           net 49.0011.0010.1111.0010.00
           lsp-gen-interval 1
           max-lsp-lifetime 600
           lsp-refresh-interval 180
        ```

=== "Node 2"

    !!! abstract "/etc/frr/frr.conf"
        0640 frr:frr

        ``` ini
        # Or copy from existing backup.
        network_frr_config: |
          frr defaults traditional
          hostname node2
          log syslog warning
          ip forwarding
          no ipv6 forwarding
          service integrated-vtysh-config
          !
          interface lo
           ip address 10.11.11.20/32
           ip router openfabric 1
           openfabric passive
          !
          interface nic4
           ip router openfabric 1
           openfabric csnp-interval 2
           openfabric hello-interval 1
           openfabric hello-multiplier 2
          !
          interface nic5
           ip router openfabric 1
           openfabric csnp-interval 2
           openfabric hello-interval 1
           openfabric hello-multiplier 2
          !
          line vty
          !
          router openfabric 1
           net 49.0011.0010.1111.0020.00
           lsp-gen-interval 1
           max-lsp-lifetime 600
           lsp-refresh-interval 180
        ```

``` bash
# Confirm FRR configured correctly.
systemctl restart frr.service  # FRR non-root. Config must be owned by FRR.
systemctl enable frr.service
vtysh -c "show openfabric topology"

# Restart Networking; may take up to 1 minute over SSH.
systemctl restart networking
reboot
```

## Create Cluster

### [First Node][e]
The first node will create the cluster configuration used for other cluster
nodes to join. Only apply these commands on the first node.

``` bash
# Use FRR Fabricd address for cluster network.
pvecm create hv --link0 10.11.11.10 --nodeid 1
pvecm status
```

### [All Other Nodes][e]
``` bash
# Node2: Add node 2 to node 1.
ssh node2
pvecm add 10.11.11.10 --link0 10.11.11.20 --use_ssh
# Node3: Add node 3 to node 1.
ssh node3
pvecm add 10.11.11.10 --link0 10.11.11.30 --use_ssh

pvecm status
```

### [Backup Initial SSH Config][f]
!!! warning
    Proxmox uses host keys and root user for intra-cluster traffic. Changing
    SSH settings may break this.

    Create a backup to ensure a default working state can be restored.

``` bash
# Backup each node.
cp -av /root /autofs/pve/{DATE}-upgrade/{NODE}/complete
cp -av /etc /autofs/pve/{DATE}-upgrade/{NODE}/complete
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
[e]: https://pve.proxmox.com/wiki/Cluster_Manager
[f]: https://forum.proxmox.com/threads/2025-pve9-x-warning-remote-host-identification-has-changed-analysis-resolution.174262
[i]: https://pve.proxmox.com/pve-docs/pve-admin-guide.html#_using_the_pve_network_interface_pinning_tool
