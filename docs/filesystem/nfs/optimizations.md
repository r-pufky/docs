# Optimizations
Speed up NFS shares.

!!! tip
    Double check **any** guidance that does not explicitly specify NFSv4.2. The
    massive changes in NFSv4.2 means most guidance no longer applies, or should
    be applied only **after** reconsideration.

## Server

### Use SLOG for exported ZFS datasets
More than a **12x** throughput improvement by using synchronous flush based log
for ZIL writes. See [ZFS increase write throughput][a].

### Set large chunk size
A large chunk size will minimize network traffic.

!!! abstract "/etc/nfs.conf.d/local.conf"
    0644 root:root

    ``` bash
    # Use 15MB chunks to optimize for streaming large files.
    nfs_conf_nfsrahead_nfsv4: 15360 # 15 * 1024KB (minimum chunk size).
    nfs_conf_nfsrahead_default: 15360
    ```

### Allow More Threads

!!! abstract "/etc/nfs.conf.d/local.conf"
    0644 root:root

    ``` bash
    # number of shares * mounts + 8
    nfs_conf_nfsd_threads: 75
    ```

## Client

### Use [multiple TCP connections][b]
Typically a **3-6x** throughput improvement by using multiple TCP connections
to NFS server with nconnect.

Refer to the recommended table and adjust based on real-world performance as
well as the number of NIC's used for server connections.

 NIC     | Connections | [Notes][c]
---------|-------------|-------
 10 GbE  | 2-4         | Moderate parallelism, avoid overhead
 25 GbE  | 4-8         | Balance throughput and connection overhead
 100 GbE | 8-16        | Maximum parallelism for high-bandwidth workloads

!!! abstract "/etc/fstab"
    0644 root:root

    ```bash
    # Add nconnect=4 to enable 4 simultaneous TCP connections to the server.
    # Requires re-mounting all NFS mounts for change to take affect.
    10.10.10.8:/d /autofs/d nfs4 rw,nfsvers=4,minorversion=2,proto=tcp,...,nconnect=4 0 0
    ```

### Set 1MB read and write sizes
A large chunk size will minimize network traffic.

``` bash
# NFS mount command
... nfs4 ... rsize=1048576,wsize=1048576 ...
```

## Reference[^1][^2][^3][^4][^5][^6][^7]
[^1]: https://linux.die.net/man/5/nfs
[^2]: https://cromwell-intl.com/open-source/performance-tuning/nfs.html
[^3]: https://www.ibm.com/docs/en/aix/7.2?topic=tuning-tcpip-guidelines-nfs-performance
[^4]: https://www.admin-magazine.com/HPC/Articles/Useful-NFS-Options-for-Tuning-and-Management
[^5]: https://www.truenas.com/community/threads/slow-nfs-read-performance-over-10-gbe.90759/
[^6]: https://forum.netgate.com/topic/131645/10gbe-tuning-do-net-inet-tcp-recvspace-kern-ipc-maxsockbuf-etc-matter
[^7]: https://dinocloud.net/2025/06/13/the-unofficial-proxmox-pure-storage-cookbook-nfs-with-nconnect/

[a]: ../zfs/README.md#increase-write-throughput
[b]: https://medium.com/@emilypotyraj/use-nconnect-to-effortlessly-increase-nfs-performance-4ceb46c64089
[c]: https://support.purestorage.com/bundle/m_linux/page/Solutions/Linux/topics/c_rhel_nfs_best-practices_performance_optimization.html
