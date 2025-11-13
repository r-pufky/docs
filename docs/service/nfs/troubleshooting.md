# Troubleshooting

## Mounting NFS shares in LXC containers
Mounting NFS shares require elevated privileges. A better pattern is to mount
the NFS shares on the cluster node and map the mount point directly in the
container. These should be mapped with minimum permissions.

On the proxmox node mount NFS shares using [FSTab](mounts.md#fstab) instead
of the WebGUI. Mounts created using the WebGUI are only mounted on first use,
which generally leads to container mounting failures due to timeouts on the PVE
host.

### PVE (All Nodes)
**/etc/fstab** (1)
{ .annotate }

1. 0644 root:root
``` bash
10.10.10.8:/d/backup /autofs/backup nfs4 ro,nfsvers=4,minorversion=2,proto=tcp,fsc,rsize=1048576,wsize=1048576,nocto,_netdev 0 0
```

### LXC Container
Add a standard container mountpoint directed at the NFS mount.

**/etc/pve/lxc/{ID}.conf** (1)
{ .annotate }

1. 0644 root:root
``` ini
mp0: volume=/autofs/backup,mp=/data/backup,ro=1
```

Reference:

* https://forum.proxmox.com/threads/tutorial-mounting-nfs-share-to-an-unprivileged-lxc.138506/
* https://github.com/zilexa/Homeserver/tree/master/Filesystems-guide/networkshares_HowTo-NFSv4.2
* https://forum.proxmox.com/threads/best-practise-sharing-nfs-to-proxmox-cluster.145590

## blocklayout failed
Message may be ignored.

!!! danger "Error"
    open pipe file /run/rpc_pipefs/nfs/blocklayout failed: No such file or directory

Loading the **blocklayoutdriver** resolves the message but creates another one.
[Upstream bug](https://bugzilla.redhat.com/show_bug.cgi?id=1753870) is closed
as **will not fix**.

Reference:

* https://bugs.launchpad.net/ubuntu/+source/nfs-utils/+bug/1907141
* https://forums.raspberrypi.com/viewtopic.php?t=323585
