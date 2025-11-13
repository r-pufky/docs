# Optimizations
Speed up NFS shares.

!!! tip
    Double check **any** guidance that does not explicitly specify NFSv4.2. The
    massive changes in NFSv4.2 means most guidance no longer applies, or should
    be applied only **after** reconsideration.

## Server

### Use SLOG for exported ZFS datasets
More than a **12x** throughput improvement by using synchronous flush based log
for ZIL writes. See [ZFS increase write
throughput](../zfs/README.md#increase-write-throughput).

### Set large chunk size
A large chunk size will minimize network traffic.

**/etc/nfs.conf.d/local.conf** (1)
{ .annotate }

1. 0644 root:root
``` bash
# Use 15MB chunks to optimize for streaming large files.
nfs_conf_nfsrahead_nfsv4: 15360 # 15 * 1024KB (minimum chunk size).
nfs_conf_nfsrahead_default: 15360
```

### Allow More Threads

**/etc/nfs.conf.d/local.conf** (1)
{ .annotate }

1. 0644 root:root
``` bash
# number of shares * mounts + 8
nfs_conf_nfsd_threads: 75
```

## Client

### Set 1MB read and write sizes
A large chunk size will minimize network traffic.

``` bash
# NFS mount command
... nfs4 ... rsize=1048576,wsize=1048576 ...
```

## Reference

* https://linux.die.net/man/5/nfs
* https://cromwell-intl.com/open-source/performance-tuning/nfs.html
* https://www.ibm.com/docs/en/aix/7.2?topic=tuning-tcpip-guidelines-nfs-performance
* https://www.admin-magazine.com/HPC/Articles/Useful-NFS-Options-for-Tuning-and-Management
* https://www.truenas.com/community/threads/slow-nfs-read-performance-over-10-gbe.90759/
* https://forum.netgate.com/topic/131645/10gbe-tuning-do-net-inet-tcp-recvspace-kern-ipc-maxsockbuf-etc-matter
