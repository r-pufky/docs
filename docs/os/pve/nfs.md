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

[a]: ../../service/nfs/README.md
[b]: https://github.com/ddimick/proxmox-lxc-idmapper
