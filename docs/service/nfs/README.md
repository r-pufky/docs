# NFS
Network File System: The venerable king of network shares. Now in NFSv4
flavors.

!!! example "Migrated to ansible collection"
    Use [r_pufky.deb.nfs][a].

!!! danger "Migrate to NFSv4"
    NFSv4 removes a **lot** of cruft focusing on supporting single socket local
    file copies, state, authentication, and encryption. Configuration is now in
    **/etc/nfs.conf.d/** and actively migrated to this location if detected.


## Client
``` bash
apt install nfs-common
systemctl list-dependencies {UNIT}  # Confirm no other dependencies.

# RPC/sockets not needed in NFSv4.
systemctl mask rpcbind rpcbind.socket
systemctl stop rpcbind rpcbind.socket
systemctl mask rpc-statd rpc-statd-notify
systemctl stop rpc-statd rpc-statd-notify
```


## Server
``` bash
apt install nfs-kernel-server
systemctl stop nfs-server
systemctl list-dependencies {UNIT}  # Confirm no other dependencies.

# RPC/sockets not needed in NFSv4.
systemctl mask rpcbind rpcbind.socket
systemctl stop rpcbind rpcbind.socket
systemctl mask rpc-statd rpc-statd-notify
systemctl stop rpc-statd rpc-statd-notify
```

!!! tip
    PVE clusters can [safely remove these services][b] as well.

### Disable NFSv3 support

??? abstract "/etc/systemd/system/nfs-server.service.d/override.conf"
    0644 root:root

    ``` bash
    # Alternatively: systemctl edit nfs-server
    #
    # Version 2 is explicitly disabled in Debian - adding
    # '--no-nfs-version 2' will cause the service to fail to start.
    [Service]
    ExecStart=
    ExecStart=/usr/sbin/rpc.nfsd --no-nfs-version 3
    ```

### Disable NFSv2 support on mounts

??? abstract "/etc/systemd/system/nfs-mountd.service.d/override.conf"
    0644 root:root

    ``` bash
    # Alternatively: systemctl edit nfs-mountd
    [Service]
    ExecStart=
    ExecStart=/usr/sbin/rpc.mountd --no-nfs-version 2 --no-nfs-version 3
    ```

### Enforce NFSv4.2 only
``` bash
cp /etc/nfs.conf /etc/nfs.conf.d/local.conf
```

??? abstract "/etc/nfs.conf.d/local.conf"
    0644 root:root

    ``` conf
    # Only specified options are changed.
    manage-gids=y  # Map restricted UID/GID's to server.
    vers3=n
    vers4=y  # Major version must be enabled to enable minor versions.
    vers4.0=n
    vers4.1=n
    vers4.2=y
    ```

### Start NFS
``` bash
systemctl restart nfs-server nfs-mountd
cat /proc/fs/nfsd/versions
> -3 +4 -4.0 -4.1 +4.2

# Only TCP port 2049 is required in NFSv2.
ss -lutpn
> tcp  LISTEN  0  64  0.0.0.0:2049  0.0.0.0:*
> tcp  LISTEN  0  64     [::]:2049     [::]:*
```


## Reference[^1][^2][^3][^4][^5][^6][^7]

[^1]: https://orca.pet/nfs4debian
[^2]: https://www.suse.com/support/kb/doc/?id=000019530
[^3]: https://github.com/zilexa/Homeserver/tree/master/Filesystems-guide/networkshares_HowTo-NFSv4.2
[^4]: https://forum.proxmox.com/threads/nfsv4-server-disabled-under-pve-8.129803/
[^5]: https://old.reddit.com/r/linux/comments/sb05kw/nfs_v42_and_serverside_copying_and_how_i_got_it/
[^6]: https://wiki.archlinux.org/title/NFS
[^7]: https://wiki.debian.org/NFSServerSetup

[a]: https://galaxy.ansible.com/ui/repo/published/r_pufky/deb/docs
[b]: https://forum.proxmox.com/threads/rpcbind.142493/
