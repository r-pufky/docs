# Troubleshooting


## [GRUB CryptFS Password Typo][a]
Unlocked CryptFS on GRUB boot will stall if mistyping the password. Restart the
unlock and boot process without restarting:

``` bash
cryptomount -a
insmod normal
normal
```


## Remote Dropbear/Wireguard/CryptFS Rescue from Bad Upgrade
System does not boot after a dist-upgrade but Dropbear connects over wireguard.

### Connect via Dropbear and Manually Mount Drive
``` bash
# Remote unlock as normal.
ssh -i ~/.ssh/dropbear root@172.31.255.11

# Open LUKS encrypted disk.
cryptsetup luksOpen /dev/nvme0n1p3 luks

# Find mapped device.
ls /dev/mapper
> /dev/mapper/b--vg-root ../dm-1

# Mount drive for changes.
mkdir /mnt
mount -t ext4 /dev/dm-1 /mnt

# Make changes also chroot if needed.
```

### Umount and reboot
``` bash
umount /mnt
rmdir /mnt
cryptsetup luksClose /dev/mapper/b--vg-root
cryptsetup luksClose /dev/mapper/b--vg-swap-1
cryptsetup luksClose /dev/mapper/luks

reboot -f
```


## [Grub OS Prober][b]
Grub will throw the following error on 4.9+ Kernels running VM's on block
devices or ZFS during normal upgrades:

!!! danger "Error"
    device-mapper reload ioctl on osprober-linux

These devices are attempted to be unmounted while in use to detect other OS's
on those partitions. This may be safely disabled if you are only running one
OS.

??? abstract "/etc/default/grub"
    0644 root:root

    ``` bash
    GRUB_DISABLE_OS_PROBER=true
    ```

``` bash
update-grub
apt update && apt upgrade
reboot
```


## Reducing Disk Writes
Minimize disk writes to SSD devices to increase longevity.

* [Debian SSD optimization guide][c].
* [deferring disk writes][d].
* [minimizing server disk writes][e].
* [SD card optimizations][f].

[a]: https://wiki.archlinux.org/title/GRUB#GRUB_rescue_and_encrypted_/boot
[b]: https://unix.stackexchange.com/questions/347466/debian-new-error-message-upgrading-kernel-to-4-9-reload-ioctl-error
[c]: https://wiki.debian.org/SSDOptimization
[d]: https://unix.stackexchange.com/questions/275678/defer-all-disk-writes-keep-them-in-memory
[e]: https://www.hydrogen18.com/blog/minimizing-disk-activity-on-linux-server.html
[f]: https://www.dzombak.com/blog/2024/04/pi-reliability-reduce-writes-to-your-sd-card
