Steam - 7 Days to Die Dedicated Server
--------------------------------------
Uses [Ubuntu 16.04 base Xen template](../templates/ubuntu-server.md), and assumes post template setup scripts have been run.

* Memory: 2048MB-8096MB

1. [Ports Exposed](#ports-exposed)
2. [Server Setup](#server-setup)
3. [Important File Locations](#important-file-locations)
4. [Disable Insecure Services](#disable-insecure-services)
5. [Starting the Server](#starting-the-server)
6. [References](#references)


Ports Exposed
-------------

| Port        | Protocol |Purpose                     |
|-------------|----------|----------------------------|
| 8080        | TCP      | Control Panel              |
| 8081        | TCP      | Telnet Port                |
| 26900       | TCP      | Dedicated Server (steam)   |
| 26900-26902 | UDP      | Dedicated Server (clients) |
* Control Panel and Telnet are insecure and should be
  disabled and blocked.


Server Setup
-------------
Install steamCMD and dedicated server

```bash
sudo apt install steamcmd
steamcmd
```

From steamcmd, install the server
* -beta \<version> will load beta channels
```steam
login anonymous
app_update 294420
```


Important File Locations
------------------------

| File                                                                    | Purpose                                                   |
|------------------------------------------------------------------------------|-------------------------------------------------------------|
| .local/share/7DaysToDie/Saves/[gametype]/[gameseed]/serveradmin.xml          | defines user bans, whitelists, admins and server commands |
| .steam/SteamApps/common/7 Days to Die Dedicated Server/serverconfig.xml      | server configuration                                         |
| .steam/SteamApps/common/7 Days to Die Dedicated Server/startserver.sh        | starts server                                               |
| .steam/SteamApps/common/7 Days to Die Dedicated Server/7DaysToDieServer_Data | server logs                                                 |

serveradmin.xml does not exist by default in game saves, and needs to be created. A template
is here: [LINK](steam-7-days-to-die/serveradmin.xml)


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
Start or resume a screen session and launch server with configuration file
```bash
src
cd .steam/SteamApps/common/7 Days to Die Dedicated Server/
./startserver.sh -configfile=serverconfig.xml
```


References
----------
[7 Days to Die Dedicated Server](
https://developer.valvesoftware.com/wiki/7_Days_to_Die_Dedicated_Server#Installation)

[SteamCMD Reference](https://developer.valvesoftware.com/wiki/SteamCMD)
