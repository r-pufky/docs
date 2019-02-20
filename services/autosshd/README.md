AutoSSD
=======
**DEPRECATED**: See [Configuration Management Tools][s0].

Reverse SSH tunnel for managing systems via autosshd.

1. [Ports Exposed](#ports-exposed)
1. [Important File Locations](#important-file-locations)
1. [Server Setup](#server-setup)
1. [References](#references)

Ports Exposed
-------------

| Port  | Protocol | Exposed/Public | Purpose                         |
|-------|----------|----------------|---------------------------------|
| 55555 | TCP      | Public         | Accepts reverse SSH connections |

Important File Locations
------------------------

| File          | Purpose                     |
|---------------|-----------------------------|
| /etc/autosshd | Custom SSH remote directory |

Server Setup
------------
Create custom SSH service directory and install service:
```bash
ln -s /usr/sbin/sshd /usr/sbin/autosshd
cp -av /etc/ssh /etc/autosshd
cp -av /lib/systemd/system/sshd.service /lib/systemd/system/autosshd.service
```

Modify ssh_remote _service_ to run in tandem with normal sshd. See
[autosshd.service][4l] for example.

Modify ssh_remote _config_, ensure _HostKeys_ and _AuthorizedKeysFile_ are
updated with the new location. See [sshd_config][9d] for example.

### Enable service
```bash
systemctl enable sshd_remote
sudo service sshd_remote start
```

**DEPRECATED**: See [Configuration Management Tools][s0].

[s0]: ../../configuration-management
[4l]: autosshd.service
[9d]: sshd_config
[refel]: http://ubuntuforums.org/archive/index.php/t-1497376.html