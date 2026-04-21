# NFS
NFS maybe by dynamically mounted on demand in the WebUI but affects LXC/VM
starts if mapped drives are not mounted.

Automatically mount NFS via FSTAB on boot.

## Create NFS mount locations
[See NFS][a] for mounting options.

``` bash
# Set mount immutable to prevent writes when not mounted.
mkdir /d
mkdir {MOUNT}
chattr +i /d
cd /d
chattr +i *  # Changes required unsetting.
```

!!! abstract "/etc/fstab"
    0644 root:root

    ``` conf
    {SERVER}:/d/pve /d/pve nfs4 rw,nfsvers=4,minorversion=2,proto=tcp,fsc,rsize=1048576,wsize=1048576,nocto,_netdev 0 0
    ```

!!! info "Map NFS UID/GID for LXC containers"
    LXC containers using mounted NFS drives must [map the LXC UID/GID][b] to
    PVE UID/GID. Squashed NFS drives must use mapped root user (typically
    165536).

    If unsure, attempt to read/write from the LXC container and view file
    permissions on NFS server to see what the actual write permissions are.



``` bash
systemctl daemon-reload
mount -a
ls -l /d  # Mounted R/W with NFS squashed permissions.
```

### Mount PVE Storage
Cluster data storage over NFS. NFS must be mounted on all cluster nodes before
adding storage.

``` bash
pvesm add dir pve --path /d/pve --content images,vztmpl,backup,snippets,rootdir,iso
reboot  # NFS should be mounted on boot.
```

## Access Control
NFS is only exported over directly attached fiber links - acting essentially
as a local physical mounted disks. These are NEVER attached directly to
LXC/VM's. Mount as a **local disk** for each PVE cluster via **FSTAB** and not
through WebUI (WebUI will mount on demand and unmount when not in use, causing
VM/LXC/PVE delays when a resource is requested).

Files have permissions themselves.

### PVE
* NFS root mount must be **0755 root:root** (or readable by root) to mount on
  PVE cluster node.
* Effective UID/GID used to determine write permissions on NFS mount.
* LXC uses SubUID/SubGID to map internal UID/GID to PVE effective UID/GID.
* LXC default UID/GID maps to **100000+** UID/GID (w/o lxc.idmap changes).
* LXC root UID/GID maps to **100000:100000** (w/o lxc.idmap changes).
* Root squashing only applies if PVE effective UID/GID 0 is used.

### LXC
* Mount directory on PVE MUST be readable by PVE root for container mount.
* Mounts may be restricted read-only in mount.
* Allow LXC **root** write to NFS mount: set **100000:100000** on NFS server.
* Deny LXC **root** write to NFS mount: set **root:root** on NFS server.
* Anonymous UID/GID not matched in SubUID/SubGID or root mapping is mapped
  to **nobody:nobody (65534:65534)**.

[a]: ../../filesystem/nfs/README.md
[b]: https://github.com/ddimick/proxmox-lxc-idmapper
