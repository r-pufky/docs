# GPU Passthrough
All PVE nodes must be configured for LXC/VM migration support.

## Host (PVE)

### Kernel Options
=== "AMD"

    !!! abstract "/etc/default/grub"
        0644 root:root

        ``` ini
        GRUB_CMDLINE_LINUX_DEFAULT="quiet amd_iommu=on iommu=pt"
        ```

    !!! abstract "/etc/modules-load.d/video.conf"
        0644 root:root

        ``` ini
        # /etc/modules is obsolete and has been replaced by /etc/modules-load.d/.
        # Please see modules-load.d(5) and modprobe.d(5) for details.
        vfio
        vfio_iommu_type1
        vfio_pci
        ```

=== "Intel"

    !!! abstract "/etc/default/grub"
        0644 root:root

        ``` ini
        GRUB_CMDLINE_LINUX_DEFAULT="quiet intel_iommu=on iommu=pt i915.enable_gvt=1"
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

``` bash
# Update GRUB, reboot, and confirm GPU reported.
update-grub
reboot

dmesg | grep -e DMAR -e IOMMU  # IOMMU enabled w. graphics passthrough.
lspci -nnv | grep -i vga  # PCI device reported.

# Confirm kernel booted with para-virtualization enabled.
cat /proc/cmdline

# Confirm GPU is associated with kernel driver.
lspci -k | grep -A 3 -i "VGA"
```


!!! abstract "/etc/udev/rules.d/59-igpu-passthrough.rules"
    0644 root:root

    ``` bash
    # Unprivileged containers require **other** R/W permissions on GPU.
    # Map others R/W to GPU on boot.
    KERNEL=="renderD128", MODE="0666"
    KERNEL=="card1", MODE="0666"
    ```

## Container configuration
``` bash
# Add root user to render, video groups.
usermod -aG render,video root

# Get LXC GPU groups and major device ID
getent group video
> video:x:44:root  # LXC GID: 44
getent group render
> render:x:992:root  # LXC GID: 992
```



=== "New Method"
    Requires PVE9+. Preferred.

    On PVE Host.

    ``` bash
    # Passthrough GPU to LXC container 100. Automatically map these to the
    # CONTAINER GID's found above.
    pct set 100 -dev0 /dev/dri/card1,gid=44,uid=0
    pct set 100 -dev1 /dev/dri/renderD128,gid=992,uid=0
    ```

=== "Old Method"
    Previous PVE versions required manually mapping subordinate ID's as well as
    mapping container ID's. This documentation will be removed on next major
    PVE release if no issues are discovered.

    ### Map non-root users to GPU

    ``` bash
    # Get PVE GPU groups and major device ID
    getent group video
    > video:x:44:root  # PVE GID: 44
    getent group render
    > render:x:993:root  # PVE GID: 993

    ls -l /dev/dri
    # Major ID 226.
    > crw-rw---- 1 root video  226,   0 May 12 21:54 card1
    > crw-rw---- 1 root render 226, 128 May 12 21:54 renderD128
    ```

    !!! abstract "/etc/subgid"
        0644 root:root

        ``` bash
        # Enable root mapping of PVE render, video groups for unprivileged
        # containers. ALWAYS confirm group ID's as they may change between
        # major OS versions.
        root:44:1
        root:993:1
        ```

    ### Map LXC groups to PVE
    On PVE Host

    !!! abstract "/etc/pve/lxc/{ID}.conf"
        0644 root:root

        ``` yaml
        # Map major device ID to LXC container.
        lxc.cgroup2.devices.allow: c 226:* rwm
        lxc.mount.entry: /dev/dri/card1 dev/dri/card1 none bind,optional,create=file,mode=0666
        lxc.mount.entry: /dev/dri/renderD128 dev/dri/renderD128 none bind,optional,create=file,mode=0666
        # Map LXC render,video groups to PVE render,video groups.
        #
        # Generate base mapping with: https://github.com/ddimick/proxmox-lxc-idmapper
        #
        #   run.py :{LXC GID}=:{PVE GID}
        #
        #   run.py :44=:44 :992=:993
        lxc.idmap: u 0 100000 65536   # UID 0-65536 (LXC) to 100000-165535 (PVE).
        lxc.idmap: g 0 100000 44      # GID 0-43 (LXC) to 100000-100043 (PVE).
        lxc.idmap: g 44 44 1          # GID 44 same on LXC/PVE.
        lxc.idmap: g 45 100045 947    # GID 45-992 (LXC) to 100045-100992 (PVE).
        lxc.idmap: g 992 993 1        # GID 992 (LXC) to 993 (PVE).
        lxc.idmap: g 994 100994 64543 # GID 994-65535 (LXC) to 100994-165535 (PVE).
        ```

``` bash
# Restart LXC container and verify device appears with video, render groups.
ls -l /dev/dri
```

## Reference[^1][^2][^3]
[^1]: https://bookstack.swigg.net/books/linux/page/lxc-gpu-access
[^2]: https://forum.proxmox.com/threads/proxmox-lxc-igpu-passthrough.141381/
[^3]: https://www.youtube.com/watch?v=0ZDr5h52OOE
[^4]: https://medium.com/@jakeasmith/running-a-vllm-lxc-on-proxmox-9-f7fbb8a7db2f