# Exports (Shares)
!!! tip
    A unified export directory is automatically created in NFSv4.2.

!!! info
    See [export options](options.md) for export option details.

## ZFS NFS Exports
ZFS will export datasets directly to **nfs-kernel-server** on the host enabling
portable NFS configurations with the respective datasets.

Each ZFS dataset has it's own unique **FSID**, so it does not need to be
specified unless there are sub-directories inside that dataset that are shared
as well.

Reference:

* https://github.com/openzfs/zfs/issues/1442
* https://zfsonlinux.topicbox.com/groups/zfs-discuss/Te01cb36d11affb4f/zfs-share-and-the-linux-nfs-kernel-server-how-do-they-interact

### Enable Extended Attributes
Reduces I/O requests and latency via enabling larger inode allocations for
attributes. Enable large dynamic inode sizes (>512B) for all exported datasets.

```bash
# large_dnode is automatically enabled when dnodesize != legacy.
zfs set xattr=sa dnodesize=auto {POOL}/{DATASET}
```

Reference:

* https://wiki.debian.org/ZFS
* https://openzfs.org/wiki/Features#SA_based_xattrs
* https://openzfs.github.io/openzfs-docs/man/master/7/zfsprops.7.html

### Create NFS exports on ZFS filesystem.
Specify **rw=**, **ro=** before other options. Use **mountpoint** to
automatically export based on the dataset mount point.

!!! tip
    Commas (**,**) should be used to separate multiple **rw=**, **ro=** host
    definitions. These will be auto-exported as separate lines in
    **/etc/exportfs.d/zfs.exports**.

``` bash
# ZFS mount point required.
zfs set mountpoint=/d/backup {POOL}/backup

# zfs set sharenfs="{HOST},{HOST_N},{OPTION},{OPTION_N}" {POOL}/{DATASET}
zfs set sharenfs="rw=10.10.10.0/24,sec=sys,fsc,mountpoint,no_all_squash,crossmnt,nohide,no_subtree_check,anonuid=65534,anongid=65534" {POOL}/backup
zfs share {POOL}/backup
```

* Exports are restricted based on the host restrictions; ensure networks are
  wire isolated or use full encryption (**sec=krbp**).
* Exported directory is the **ZFS mountpoint** not the ZFS dataset name.

Refresh ZFS NFS exports if the haven't automatically been refreshed.
``` bash
systemctl restart zfs-share.service  # Automatically runs 'exportfs -a'.
exportfs  # Show currently exported filesystems.
```

Reference:

* https://www.theurbanpenguin.com/configuring-nfs-exports-using-zfs-data-sets/
* https://github.com/openzfs/zfs/issues/3738
* https://github.com/openzfs/zfs/issues/3860
* https://klarasystems.com/articles/nfs-shares-with-zfs/
* https://www.ronny-mueller.com/2017/02/18/howto-kerberos-nfsv4-zfs-kerberized-nfs/

## Exports via /etc/exports
Traditional NFS exports. Prefer [ZFS Exports](#zfs-nfs-exports).

**/etc/exports** (1)
{ .annotate}

1. 0644 root:root
``` bash
# {EXPORT} {HOST}({OPTIONS}) ... {HOST_N}({OPTIONS})
/exported 10.10.10.0/24(sec=sys,fsc,no_all_squash,crossmnt,nohide,no_subtree_check,anonuid=65534,anongid=65534)
```

Refresh exports.
``` bash
exportfs -a  # Refresh NFS kernel server exports (done automatically).
exportfs  # Show currently exported filesystems.
```
