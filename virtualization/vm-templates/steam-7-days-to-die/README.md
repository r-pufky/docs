Steam - 7 Days to Die Dedicated Server
--------------------------------------
Uses [Ubuntu 16.04 base Xen template](../../templates/ubuntu-server.md), and
assumes post template setup scripts have been run.

* Memory: 2048MB-8096MB
* Disk: 20GB ([Encrypted volume setup](../../templates/ubuntu-server.md#creating-an-encrypted-volume))

1. [Ports Exposed](#ports-exposed)
1. [Server Setup](#server-setup)
1. [Important File Locations](#important-file-locations)
1. [Disable Insecure Services](#disable-insecure-services)
1. [Starting the Server](#starting-the-server)
1. [References](#references)

Ports Exposed
-------------

| Port        | Protocol |Purpose                     |
|-------------|----------|----------------------------|
| 8080        | TCP      | Control Panel (Disabled)   |
| 8081        | TCP      | Telnet Port (Disabled)     |
| 26900       | TCP      | Dedicated Server (steam)   |
| 26900-26902 | UDP      | Dedicated Server (clients) |
* Control Panel and Telnet are insecure and should be
  disabled and blocked.

Server Setup
-------------
Install steamCMD and dedicated server; then migrate data to secondary disk.

```bash
sudo apt install steamcmd
steamcmd
exit
mv ~/.steam /data/steam
mv ~/.local /data/local
ln -s /data/steam .steam
ln -s /data/local .local
mkdir /data/saves /data/config
```

From steamcmd, install the server
* `-beta latest_experimental` will load beta channels
```steam
login anonymous
app_update 294420
```

Create a systemd service
* Assumes server directory is symlinked to steam server location

vim /etc/systemd/system/7days.service
```systemd
[Unit]
Description=7 Days to Die Dedicated Server
After=network.target nss-lookup.target

[Service]
User=7days
Group=7days
Type=simple
PIDFile=/run/7days.pid
ExecStart=/home/7days/server/startserver.sh -configfile=/home/7days/server/serverconfig.xml
ExecReload=/bin/kill -s HUP $MAINPID
ExecStop=/bin/kill -s QUIT $MAINPID
Restart=always

[Install]
WantedBy=multi-user.target
```
```bash
systemctl enable 7days
```

Important File Locations
------------------------

| File                                                                         | Purpose                                                   |
|------------------------------------------------------------------------------|-----------------------------------------------------------|
| .local/share/7DaysToDie/Saves/[gametype]/[gameseed]/serveradmin.xml          | defines user bans, whitelists, admins and server commands |
| .steam/SteamApps/common/7 Days to Die Dedicated Server/serverconfig.xml      | server configuration                                      |
| .steam/SteamApps/common/7 Days to Die Dedicated Server/startserver.sh        | starts server                                             |
| .steam/SteamApps/common/7 Days to Die Dedicated Server/7DaysToDieServer_Data | server logs                                               |

serveradmin.xml does not exist by default in game saves, and needs to be
created. A template is here: [LINK](serveradmin.xml)
* It might be pertinient to link directories to home directory.

Disable Insecure Services
-------------------------
Disable these services and set long random passwords.

vim .steam/SteamApps/common/7 Days to Die Dedicated Server/serverconfig.xml
```xml
<property name="ControlPanelEnabled" value="false"/>
<property name="ControlPanelPassword" value="<enter-a-password-scramble>"/>
<property name="TelnetEnabled" value="false"/>
<property name="TelnetPassword" value="<enter-a-password-scramble>"/>
```

Starting the Server
-------------------
Use systemd to start the service
```bash
service 7days start
```

or manually
```bash
src
cd .steam/SteamApps/common/7 Days to Die Dedicated Server/
./startserver.sh -configfile=serverconfig.xml
```

References
----------
[7 Days to Die Dedicated Server][1]

[SteamCMD Reference][2]

[1]: https://developer.valvesoftware.com/wiki/7_Days_to_Die_Dedicated_Server#Installation
[2]: https://developer.valvesoftware.com/wiki/SteamCMD
