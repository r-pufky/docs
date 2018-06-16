Nzbget Server
-------------
Usenet downloader.

Plex/Sonarr/NZB/Torrent clients should run under the same user to run correctly.

1. [Ports Exposed](#ports-exposed)
1. [Important File Locations](#important-file-locations)
1. [Server Setup](#server-setup)
1. [SSH Tunneling](#ssh-tunneling)
1. [References](#references)

[Ports Exposed][1]
------------------

| Port | Protocol | Purpose                           |
|------|----------|-----------------------------------|
| 6789 | TCP      | Default nzbget webservice (http)  |
| 6791 | TCP      | Default nzbget webservice (https) |
 * If https is enabled, http is disabled

Important File Locations
------------------------

| File                  | Purpose                         |
|-----------------------|---------------------------------|
| /data/services/nzbget | nzbget main service directory   |
| /data/downloads       | nzbget main downloads directory |

Server Setup
------------
### Add PPA and install nzbget and dependencies
```bash
add-apt-repository ppa:modriscoll/nzbget
apt update && apt install unrar p7zip-full nzbget
```

### Create `nzbget` user and `media` group for running the service
```bash
adduser --disabled-password --system --home /data/services/nzbget --gecos "nzbget" --group nzbget
addgroup media
adduser nzbget media
```
 * Add your user account to media if needed

### Create config file
```bash
cp /usr/share/nzbget/nzbget.conf /etc/nzbget.conf
```
 * See [template values file](nzbget.conf) for some reasonable default values
 * Leaving an option blank disables it (e.g. user accounts and unencrypted
   webface)
 * No GUI configuration is needed, all GUI updates will save changes to this
   file

### Copy [systemd service template](nzbget.service) to
`/etc/systemd/system/nzbget.service`.
 * Ensure options are updated with your settings in file

Enable the nzbget service
```bash
systemctl enable nzbget.service
```

### Create OpenSSL certificates for https
This will creat self-signed certificates, you can use actual ones if you have
one.

```bash
apt install openssl
sudo openssl req -x509 -nodes -days 36500 -newkey rsa:4096 -keyout /data/services/nzbget/nzbget.key -out /data/services/nzbget/nzbget.crt
```

### Set service permissions

```bash
chown -R nzbget:media /data/services/nzbget
chmod 0600 /data/services/nzbget/nzbget.conf
```

```bash
systemctl start nzbget
```

SSH Tunneling
-------------
If you don't want to expose any service ports, you can enable local only access
then tunnel with SSH.

### Only allow localhost access to webface

nzbget.conf
```
ControlIP=127.0.0.1
```

### Tunnel with SSH

```bash
ssh -L 6791:localhost:6791 <user>@<host>
```

References
----------
[Nzbget PPA installation][1]

[Nzbget github repository][2]

[Nzbget documentation][3]

[Nzbget systemd configuration][4]

[Configuring two provider backbonese][5]

[1]: https://launchpad.net/~modriscoll/+archive/ubuntu/nzbget
[2]: https://github.com/nzbget/nzbget
[3]: https://github.com/nzbget/nzbget/wiki
[4]: http://www.htpcguides.com/install-latest-nzbget-on-ubuntu-15-x-with-easy-updates/
[5]: https://nzbgeek.info/showthread.php?tid=6720