# Debian

!!! example "Migrated to ansible collection"
    Use [r_pufky.deb](https://galaxy.ansible.com/ui/repo/published/r_pufky/deb/docs/).

## Install TCP BBR Kernel Patches
TCP BBR is a new congestion controlling algorithm that is designed to respond
to actual congestion instead of packet loss. This results in a dramatic
increase in transfer speeds. This applies to **any** Linux distribution running
Kernel **4.9+** with BBR patches.

``` bash
# Check TCP BBR supported.
uname -r

# Both parameters should be returned.
egrep 'CONFIG_TCP_CONG_BBR|CONFIG_NET_SCH_FQ' /boot/config-$(uname -r)
```

### Enable BBR Support
**/etc/sysctl.d/10_custom_kernel_bbr.conf** (1)
{ .annotate }

1. 0644 root:root
``` bash
net.core.default_qdisc=fq
net.ipv4.tcp_congestion_control=bbr
```

``` bash
sysctl -p  # Or reboot.
```

Reference:

* https://cloud.google.com/blog/products/gcp/tcp-bbr-congestion-control-comes-to-gcp-your-internet-just-got-faster

## Disable IPv6
Disable if IPv6 is not being actively used to prevent any IPv6 misconfiguration
attacks.

**/etc/sysctl.d/10_disable_ipv6.conf** (1)
{ .annotate }

1. 0644 root:root
``` bash
net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.default.disable_ipv6 = 1
net.ipv6.conf.lo.disable_ipv6 = 1
```

``` bash
sysctl -p  # Or reboot.
```

## Operations

### Make RAW Disk Image of Physical Disk
DD can be used to make a RAW image of a disk, and can be mounted in other linux
systems for use.

``` bash
# Copy disk block device to a file.
dd if=/dev/{BLOCK} of=/some/filesystem/{IMAGE}.raw bs=1M conv=noerror,sync status=progress

# Mount RAW disk image for use.
losetup -f -P /some/filesystem/{IMAGE}.raw
losetup -l
mount /dev/loop0p1 /mnt/test/
umount /dev/loop0p1
losetup -d /dev/loop0
```

Reference:

* https://blog.tinned-software.net/mount-raw-image-of-entire-disc/
* https://blog.tinned-software.net/mount-raw-image-of-entire-disc/

### Apt Auto Selection
Automatically select user-required options during package install.

This is used for configuration management and preseeding for automatic installs
that require user input.

#### Get debconf Options
Determine **debconf** options used by installing the package with the options
set.

``` bash
apt install debconf-utils
apt install {PACKAGE}
debconf-get-selections | grep {PACKAGE}
```

#### Set debconf Options
On target machines, set options before installing the package. This will remove
the prompts from apt.

!!! tip
    debconf will list with tabs for easy reading. When setting selections
    separate with a **space**, otherwise the extra whitespace will be included
    with the option.

``` bash
echo "{PACKAGE}-{VERSION} package/option {NAME} {VALUE}" | debconf-set-selections
apt install {PACKAGE}
```

#### Example
``` bash
apt install mysql-server debconf-utils
debconf-get-selections | grep mysql-server
> mysql-server-5.5        mysql-server/root_password_again        password
> mysql-server-5.5        mysql-server/root_password      password
> mysql-server-5.5        mysql-server/error_setting_password     error
> mysql-server-5.5        mysql-server-5.5/postrm_remove_databases        boolean false
> mysql-server-5.5        mysql-server-5.5/start_on_boot  boolean true
> mysql-server-5.5        mysql-server-5.5/nis_warning    note
> mysql-server-5.5        mysql-server-5.5/really_downgrade       boolean false
> mysql-server-5.5        mysql-server/password_mismatch  error
> mysql-server-5.5        mysql-server/no_upgrade_when_using_ndb  error

echo "mysql-server-5.5        mysql-server-5.5/start_on_boot  boolean true"  | debconf-set-selections
apt install mysql-server-5.5
```

Reference:

* https://serverfault.com/questions/407317/passing-default-answers-to-apt-get-package-install-questions
