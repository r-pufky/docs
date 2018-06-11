AutoSSD
-------
Reverse SSH tunnel for managing systems via autosshd.

**DEPRECATED**: See [Configuration Management Tools](../../configuration-management)

1. [Docker Ports Exposed](#docker-ports-exposed)
1. [Important File Locations](#important-file-locations)
1. [Docker Creation](#docker-creation)
1. [Modifying Settings](#modifying-settings)

Ports Exposed
-------------

| Port  | Protocol | Purpose                         |
|-------|----------|---------------------------------|
| 55555 | TCP      | Accepts reverse SSH connections |

Important File Locations
------------------------

| File          | Purpose                     |
|---------------|-----------------------------|
| /etc/autosshd | Custom SSH remote directory |

Server Setup
------------
Create custom SSH service directory and install service.

```bash
ln -s /usr/sbin/sshd /usr/sbin/autosshd
cp -av /etc/ssh /etc/autosshd
cp -av /lib/systemd/system/sshd.service /lib/systemd/system/autosshd.service
```

Modify ssh_remote service to run in tandem with normal sshd. See
[autosshd.service](autosshd.service) for example.

Modify ssh_remote config, ensure `HostKeys` and `AuthorizedKeysFile` are updated
with the new location. See [sshd_config](#sshd_config) for example.

### Enable service
```bash
systemctl enable sshd_remote
sudo service sshd_remote start
```

References
----------
[Creating a second SSHD Service][1]

[1]: http://ubuntuforums.org/archive/index.php/t-1497376.html