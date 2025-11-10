# ZFS
ZFS (Zettabyte FileSystem) storage pool. See
[ZFS Tutorial](http://kbdone.com/zfs-basics).

## Install
``` bash
apt install zfsutils-linux

# Install RAM FS tools if ZFS is to be used for root filesystem.
apt install zfs-initramfs
```

## Creating New ZFS Pool
!!! warning
    Do not encrypt the root pool or mount it. Encrypt and mount datasets
    instead. See [Encryption](encryption.md).

Best practice from years of ZFS use are:

* Use an unencrypted ZFS pool (encrypt datasets).
* Create datasets to handle specific data needs/types/etc. Keep massive files
  in one dataset (e.g. videos), versus one for running services.
* Set dataset options based on those needs (encryption, compression, etc). This
  isolates master encryption keys and makes data management easy years later.
* Set mountpoints immutable ``chattr +i {MOUNTPOINT}`` when dataset is not
  mounted. This prevents writing to those mountpoints when the pool/dataset is
  not mounted or unlocked.

### Determine disks to add to ZFS pool
``` bash
lsblk
ls -l /dev/disk/by-id
```

### Create ZFS pool
``` bash
# ZFS will handle the partitioning of raw disks automatically. There is no need
# to explicitly partition your disks beforehand.
zpool create -o autoexpand=on -o ashift=12 -O mountpoint=none {POOL} raidz2 /dev/disk/by-id/wwn-*
zpool list
zpool status {POOL}
zdb -C {POOL}
```

* **autoexpand=on** enables auto-expanding of ZFS pool when new disks are
  added.
* **ashift=12** enables 4K sectors **All > 2011** drives should have 4K
  sectors. This **cannot** be changed once set in the pool, and will lead to
  severe performance degradation if mis-matched for FS/drives. Cannot
  hotswap/replace **512** with **4K** drives in pool.
* **-O mountpoint=none** the unencrypted pool will not be mounted - mount
  datasets instead.
* **raidz2** preferred for 6+ disk arrays. **raidz** for <6.
* **www-*** replace with bash expansion to match drives to use. Can specify
  multiple block devices explicitly.
* Ensure **ashift=12** is enabled with **-C** option.

Reference:

* https://forums.freebsd.org/threads/zfs-replacing-512b-drives-by-4k-drives.29539

## ZFS Operations
ZFS can be tweaked per dataset based on the data being used. ZFS only applies
new settings on newly written data; changing options for pre-existing data
requires export/re-import of that data to the dataset.

### Mounting Existing ZFS Pool
!!! tip
    Set mountpoint to immutable without the ZFS dataset mounted. This prevents
    writes when the dataset is not ready: **chattr +i {MOUNTPOINT}**

``` bash
# -f required if pool was not exported.
zpool import {POOL}  # autodetect and import: 'zpool import -a'
zpool status {POOL}
zpool scrub {POOL}
zfs mount -l -a
```

### Enable text compression and disable atime for Maildir datasets.
``` bash
zfs set atime=off {POOL}/{DATASET}
zfs set compression=lz4 {POOL}/{DATASET}
```

### Enable high compression for backup datasets.
``` bash
zfs set compression=gzip {POOL}/{DATASET}
```

### Setup Monthly ZFS Scrub
Scrubbing verifies all blocks can be read, and marks then bad if not. This is
done while the filesystem is online, but may slightly impact performance.

**/root/bin/scrub-zpool-monthly** (1)
{ .annotate }

1. 0750 root:root
``` bash
#!/bin/bash
#
# Scrubs zpool monthly.
/sbin/zpool scrub {POOL}
```

``` bash
# Add scrub to crontab.
sudo crontab -e

@weekly /root/bin/scrub-zpool-monthly
```

Reference:

* https://docs.oracle.com/cd/E23823_01/html/819-5461/gbbwa.html
