# Troubleshooting

## GRUB CryptFS Password Typo
Unlocked CryptFS on GRUB boot will stall if typoing the password. Restart the
unlock and boot process without restarting:

``` bash
cryptomount -a
insmod normal
normal
```

Reference:

* https://wiki.archlinux.org/title/GRUB#GRUB_rescue_and_encrypted_/boot

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

## Grub OS Prober
Grub will throw the following error on 4.9+ Kernels running VM's on block
devices or ZFS during normal upgrades:

!!! danger "Error"
    device-mapper reload ioctl on osprober-linux

These devices are attempted to be unmounted while in use to detect other OS's
on those partitions. This may be safely disabled if you are only running one
OS.

**/etc/default/grub** (1)
{ .annotate }

1. 0644 root:root
``` bash
GRUB_DISABLE_OS_PROBER=true
```

``` bash
update-grub
apt update && apt upgrade
reboot
```

Reference:

* https://unix.stackexchange.com/questions/347466/debian-new-error-message-upgrading-kernel-to-4-9-reload-ioctl-error
