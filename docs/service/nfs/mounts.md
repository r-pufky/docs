# Mounts

!!! info
    See [export options](options.md) for export option details.


## [Systemd Automount][a]
Preferred as these will automatically mount when needed and unmount after idle.

The [mount unit][b] defines how to mount the remote filesystem, automount unit
triggers the mount unit.

!!! tip
    Unit names **must** match **where** using only valid systemd unit
    characters. Typically just replace **/** with **-**, and drop root.

    /mnt/path ➔ mnt-path

??? abstract "/etc/systemd/system/mnt-client_test.mount"
    0644 root:root

    ``` ini
    [Unit]
    Description=NFS mount 127.0.0.1:/home/vagrant

    [Mount]
    What=127.0.0.1:/home/vagrant
    Where=/mnt/client_test
    Type=nfs
    Options=nfsvers=4,minorversion=2,proto=tcp,fsc,noauto,nofail
    TimeoutSec=30

    [Install]
    WantedBy=multi-user.target
    ```

??? abstract "/etc/systemd/system/mnt-client_test.automount"
    0644 root:root

    ``` ini
    [Unit]
    Description=Automount NFS 127.0.0.1:/home/vagrant

    [Automount]
    Where=/mnt/client_test

    [Install]
    WantedBy=multi-user.target
    ```

Enable.
``` bash
systemctl daemon-reload
sysctmctl enable mnt-client_test.mount mnt-client_test.automount
```


## FSTab
Traditional NFS share mounting.

The root directory must existing for NFS mounts. Options may be tested with
manual NFS mount before adding to fstab.

``` bash
mkdir /autofs/{EXPORT}  # Repeat for all mounts.

# Set unmounted directory immutable to prevent unmounted write attempts.
chown root:root /autofs/{EXPORT}
chmod 0755 /autofs/{EXPORT}
chattr +i /autofs/{EXPORT}

# Mount will override directory permissions.
mount -t nfs -o nfsvers=4,minorversion=2,proto=tcp,fsc,rsize=1048576,wsize=1048576,nocto 10.10.10.8:/home/vagrant /autofs/home/vagrant
```

??? abstract "/etc/fstab"
    0644 root:root

    ```bash
    # nfs4 enables automounting.
    # _netdev specifies mount is a network device and forces fstab to delay
    # mounting until after required networks are up.
    10.10.10.8:/home/vagrant /autofs/home/vagrant nfs4 rw,nfsvers=4,minorversion=2,proto=tcp,fsc,rsize=1048576,wsize=1048576,nocto,_netdev 0 0
    ```

Mount all exports.
```bash
systemctl daemon-reload
mount -a
```

[a]: https://wiki.archlinux.org/title/NFS
[b]: https://www.freedesktop.org/software/systemd/man/latest/systemd.unit.html
