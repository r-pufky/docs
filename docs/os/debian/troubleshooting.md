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
