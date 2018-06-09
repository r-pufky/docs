Transmission Dedicated Server
-----------------------------
Uses [Ubuntu 16.04 base Xen template](../templates/ubuntu-server.md), and assumes post template setup scripts have been run.

* Disk: 20GB ([Encrypted volume setup](../templates/ubuntu-server.md#creating-an-encrypted-volume))

1. [Ports Exposed](#ports-exposed)
2. [Server Setup](#server-setup)
3. [Important File Locations](#important-file-locations)
4. [Disable Insecure Services](#disable-insecure-services)
5. [Starting the Server](#starting-the-server)
6. [References](#references)

Ports Exposed
-------------

| Port        | Protocol |Purpose                      |
|-------------|----------|-----------------------------|
| 49152-65535 | TCP      | Random Peer Port (Disabled) |
| 49160       | TCP      | Peer Port                   |
| 9092        | TCP      | webface                     |

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

Important File Locations
------------------------

| File                                      | Purpose  |
|-------------------------------------------|----------|
| /etc/transmission-daemon/settings.json    | Settings |
| /var/lib/transmission-daemon              | State    |
* Settings.json is created after launching the GUI, or just use the template here. [LINK.](settings.json)

Modifying Settings
------------------
Transmission will overwrite the settings.json file when it is shutdown. Therefore stop transmission before editing settings. Most settings (after these initial ones) can be modified in the webface once launched.

sudo vim /etc/transmission-daemon/settings.json
```vim
  "bind-address-ipv4": "<YOUR-SERVER-IP>",
  "download-dir": "/data/complete",
  "incomplete-dir": "/data/incomplete",
  "open-dialog-dir": "/data",
  "peer-port": 49160,
  "peer-port-random-on-start": false,
  "port-forwarding-enabled": true,
  "rpc-enabled": true,
  "rpc-password": "<YOUR-WEBFACE-PASSWORD",
  "rpc-port": 9092,
  "rpc-username": "<YOUR-WEBFACE-USERNAME",
  "rpc-whitelist": "<ALLOWED COMPUTERS>,127.0.0.1",
  "watch-dir": "/data/watched",
```

Starting the Server
-------------------
```bash
sudo service transmission-daemon start
```
