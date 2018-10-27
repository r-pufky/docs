Service Configuration Template
------------------------------
Background notes on service, VM requirements. TOC is a rought layout adjust as
needed (e.g. docker setups, xen setups, etc).

[docker example](gogs/README.md)
[xen example](../virtualization/vm-templates/steam-7-days-to-die/README.md)

* Disk: 20GB ([Encrypted volume setup](../operating-systems/ubuntu/ubuntu-server.md#creating-an-encrypted-volume))

1. [Ports Exposed](#ports-exposed)
1. [Important File Locations](#important-file-locations)
1. [Server Setup](#server-setup)
1. [Starting the Server](#starting-the-server)
1. [References](#references)

Ports Exposed
-------------

| Port        | Protocol |Purpose                      |
|-------------|----------|-----------------------------|
| 49152-65535 | TCP      | Random Peer Port (Disabled) |
| 49160       | TCP      | Peer Port                   |
| 9092        | TCP      | webface                     |

Important File Locations
------------------------

| File                                      | Purpose  |
|-------------------------------------------|----------|
| /etc/transmission-daemon/settings.json    | Settings |
| /var/lib/transmission-daemon              | State    |
* Settings.json is created after launching the GUI, or just use the template
  here.

Server Setup
-------------
Install transmission

```bash
sudo add-apt-repository ppa:transmissionbt/ppa
sudo apt update && sudo apt install transmission-daemon
sudo service transmission-daemon stop
```

Link to Relative transmission locations
```bash
sudo ln -s /etc/transmission-daemon settings-transmission
sudo ln -s /var/lib/transmission-daemon state-transmission
```

Create directories for transfer
```bash
sudo mkdir /data/{complete,incomplete,watched}
sudo chown -Rv debian-transmission:debian-transmission /data/{complete,incomplete,watched}
```

Modifying Settings
------------------
Transmission will overwrite the settings.json file when it is shutdown. Therefore stop transmission before editing settings. Most settings (after these initial ones) can be modified in the webface once launched.

sudo vim /etc/transmission-daemon/settings.json
```vim
listing
```

Starting the Server
-------------------
```bash
sudo service transmission-daemon start
```

References
----------
[reference note][1]

[1]: refernce link
[2]: other non-listed link