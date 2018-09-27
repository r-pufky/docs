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

```bash
sudo apt install linux-headers-$(uname -r) build-essential
sudo apt install spl-dkms
sudo apt install zfs-dkms zfsutils-linux
sudo modprobe zfs
ls -l /dev/disk/by-id
```
* Find the serial for the drives, match to the sd# address, then map to the WWN
  (world wide name) of that device -- that will be unique to that drive across
  any system you put the drive in
* This is no longer needed for the latest ZFS packages for ubuntu; containers are
  automatically identified on boot and mounted. However, this still does provide
  an easy to use reference mapping for physical drives, should one go bad.

#### /etc/zfs/vdev_id.conf
```config
#<type> <label> <location> #<comment>

# ZFS disk set
alias zfs1 wwn-XXXXXXXXXXXXXXXXXX # drive serial (location)
alias zfs2 wwn-XXXXXXXXXXXXXXXXXX # drive serial (location)
alias zfs3 wwn-XXXXXXXXXXXXXXXXXX # drive serial (location)
alias zfs4 wwn-XXXXXXXXXXXXXXXXXX # drive serial (location)
alias zfs5 wwn-XXXXXXXXXXXXXXXXXX # drive serial (location)
````

```bash
sudo udevadm trigger
ls -l /dev/disk/by-vdev/
```

* Verify by-vdevs is populated with zfs disks properly

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
```bash
for x in `seq 5`; do
  sudo parted /dev/disk/by-vdev/zfs${x} mklabel gpt quit;
done
sudo zpool create -o autoexpand=on -o ashift=12 -m /data CONTAINER raidz /dev/disk/by-vdev/disk{1..5}
sudo zpool list
sudo zpool status CONTAINER
sudo zdb -C CONTAINER
```

* Use GPT partitions for [2TB+ disk support][2]
* autoexpand=on - enable auto-expanding of ZFS pool when new disks are added
* ashift=12 - [Enable 4K sectors][7]. All > 2011 drives should have 4K sectors.
  This cannot be changed once set in the pool, and will lead to severe
  performance degradation if mis-matched for FS/drives. Cannot hotswap/replace
  512 with 4K drives in pool
* With -C option, ensure ashift=12 is enabled

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
