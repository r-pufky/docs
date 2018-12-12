ZFS Setup
-------------
Setting up and maintaining a ZFS pool

Ubunutu 16.04

1. [Installing Base Packages, Existing Drive Mappings](#installing-base-packages-existing-drive-mappings)
1. [Mounting Existing ZFS Pool](#mounting-existing-zfs-pool)
1. [Creating New ZFS Pool](#creating-new-zfs-pool)
1. [Upgrading ZFS with Larger Disks](#upgrading-zfs-with-larger-disks)
1. [Setup Monthly ZFS Scrub](#setup-monthly-zfs-scrub)

[Installing Base Packages, Existing Drive Mappings][3]
------------------------------------------------------
This is now in the default repositories for ubuntu. The old PPA [archive is
here][1].

Note: The new HWE kernel currently does not build properly, you need to use the
generic kernel until [the bug is resolved.][10]

[Ubuntu 16.04+ has native ZFS kernel level support built in][11]. Only user
tools need to be installed.

```bash
apt install zfsutils-linux
```

Install RAM FS tools if ZFS is to be used for the _root_ filesystem as well.

```bash
apt install zfs-initramfs
```

Mounting Existing ZFS Pool
--------------------------
```bash
sudo zpool import CONTAINER
sudo zpool status CONTAINER
sudo zpool scrub CONTAINER
```
* A container name does not need to be used to identify a ZFS container,
  it will be detected automatically. `sudo zpool import`
* Ensure low-level disks are setup properly
* Search for the pool, then mount it, use -f if it wasn't exported before. Scrub.

Creating New ZFS Pool
---------------------
Create a GPT partition for each disk to be used.

```bash
ls -l /dev/disk/by-id
for x in `ls -1 /dev/disk/by-id/ata-*`; do
  sudo parted /dev/disk/by-id/${x} mklabel gpt quit;
done
```
* by-id is the easiest to use as it identifies drives by the WWN (World Wide
  Name) or a composite of the model and serial number.
* Use GPT partitions for [2TB+ disk support][2].
* Use [`smartctl -i <dev>`][12] to get detailed information on disk.

Create a ZFS container

```
sudo zpool create -o autoexpand=on -o ashift=12 -m /data CONTAINER raidz /dev/disk/by-id/ata-*
sudo zpool list
sudo zpool status CONTAINER
sudo zdb -C CONTAINER
```
* autoexpand=on - enable auto-expanding of ZFS pool when new disks are added
* ashift=12 - [Enable 4K sectors][7]. All > 2011 drives should have 4K sectors.
  This cannot be changed once set in the pool, and will lead to severe
  performance degradation if mis-matched for FS/drives. Cannot hotswap/replace
  512 with 4K drives in pool
* With -C option, ensure ashift=12 is enabled
* _ata-*_ should be replaced with a filter to match drives to use. Can specify
  multiple drives explicitly.
* ZFS will automatically create partitions on drives.

[Upgrading ZFS with Larger Disks][5]
------------------------------------
```bash
sudo zpool scrub CONTAINER
sudo zpool status CONTAINER
ls -l /dev/disk/by-id
ls -l /dev/disk/by-vdev
sudo parted /dev/disk/by-id/<disk>
mklabel gpt
quit
sudo zpool replace CONTAINER sdb
```

* Ensure right drive - this is __data destructive__

[Setup Monthly ZFS Scrub][8]
----------------------------
Scrubbing verifies all blocks can be read, and marks then bad if not. This
is done while the filesystem is online, but may slightly impact performance.

#### /root/bin/scrub-zpool-monthly
```bash
#!/bin/bash
#
# Scrubs zpool set at the beginning of the month
# Note: cronjob should run set to run on a day of the week

if [ $(date +\%d) -le 07 ]; then
  /sbin/zpool scrub CONTAINER
fi
```

### Add to [root crontab][9] to run monthly
```crontab
@weekly /root/bin/scrub-zpool-monthly
```

[1]: https://launchpad.net/~zfs-native/+archive/stable
[2]: http://www.cyberciti.biz/tips/fdisk-unable-to-create-partition-greater-2tb.html
[3]: http://flux.org.uk/howto/solaris/zfs_tutorial_01
[4]: https://github.com/zfsonlinux/zfs/issues/381
[5]: http://www.itsacon.net/computers/unix/growing-a-zfs-pool/
[6]: https://github.com/zfsonlinux/pkg-zfs/wiki/Ubuntu-ZFS-mountall-FAQ-and-troubleshooting
[7]: http://forums.freebsd.org/showthread.php?t=29539
[8]: https://docs.oracle.com/cd/E23823_01/html/819-5461/gbbwa.html
[9]: https://en.wikipedia.org/wiki/Cron
[10]: https://bugs.launchpad.net/ubuntu/+source/linux-hwe/+bug/1693757
[11]: https://wiki.ubuntu.com/ZFS
[12]: https://www.techrepublic.com/blog/linux-and-open-source/using-smartctl-to-get-smart-status-information-on-your-hard-drives/