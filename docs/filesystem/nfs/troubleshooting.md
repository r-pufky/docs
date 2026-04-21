# Troubleshooting

### PVE (All Nodes)
!!! abstract "/etc/fstab"
    0644 root:root

    ``` bash
    10.10.10.8:/d/backup /autofs/backup nfs4 ro,nfsvers=4,minorversion=2,proto=tcp,fsc,rsize=1048576,wsize=1048576,nocto,_netdev 0 0
    ```

### [LXC Container][a]
Add a standard container mountpoint directed at the NFS mount.

!!! abstract "/etc/pve/lxc/{ID}.conf"
    0644 root:root

    ``` ini
    mp0: volume=/autofs/backup,mp=/data/backup,ro=1
    ```

## [blocklayout failed][b]
Message [may be ignored][c].

!!! danger ""
    open pipe file /run/rpc_pipefs/nfs/blocklayout failed: No such file or directory

Loading the **blocklayoutdriver** resolves the message but creates another one.
[Upstream bug][d] is closed as **will not fix**.

## Reference[^1][^2]
[^1]: https://github.com/zilexa/Homeserver/tree/master/Filesystems-guide/networkshares_HowTo-NFSv4.2
[^2]: https://forum.proxmox.com/threads/best-practise-sharing-nfs-to-proxmox-cluster.145590

[a]: https://forum.proxmox.com/threads/tutorial-mounting-nfs-share-to-an-unprivileged-lxc.138506
[b]: https://bugs.launchpad.net/ubuntu/+source/nfs-utils/+bug/1907141
[c]: https://forums.raspberrypi.com/viewtopic.php?t=323585
[d]: https://bugzilla.redhat.com/show_bug.cgi?id=1753870
