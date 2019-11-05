Steam - Conan Exiles (Linux) Dedicated Server
---------------------------------------------
Uses [Ubuntu 16.04 VM template](../../../operating-systems/ubuntu/16.04/server.md),
and assumes post template setup scripts have been run.

* Memory: 2048MB-8096MB
* Disk: 20GB

1. [Ports Exposed](#ports-exposed)
1. [Server Setup](#server-setup)
1. [Important File Locations](#important-file-locations)
1. [Running as a Service](#running-as-a-service)
1. [Installing Mods](#installing-mods)
1. [Updating Server](#updating-server)
1. [References](#references)

Ports Exposed
-------------

| Port  | Protocol | Purpose                             |
|-------|----------|-------------------------------------|
| 27015 | UDP      | Dedicated Server (steam)            |
| 27016 | UDP      | Dedicated Server (steam announce)   |
| 7777  | UDP      | Dedicated Server (clients direct)   |
| 7778  | UDP      | Dedicated Server (client via steam) |
 * 7778,27016 should be opened for server to appear in steam public lists or
   in player's history. Public lists are buggy and will not always appear.
 * If connecting on local network, use the private IP of the server, not the
   public IP address.

Important File Locations
------------------------

| File                                                                | Purpose                           |
|---------------------------------------------------------------------|-----------------------------------|
| <target>/ConanSandbox/Saved/Config/WindowsServer/Engine.ini         | Core engine settings, e.g. ports. |
| <target>/ConanSandbox/Saved/Config/WindowsServer/ServerSettings.ini | Specific game instance settings.  |
| <target>/ConanSandbox/Saved/game.db                                 | Game database and saves.          |
 * See `<target>/ConanSandbox/Config/` for default files with all avaliable options

Server Setup
-------------
Since the dedicated server only runs on windows, force steam to detect windows
and run under wine.

```bash
sudo apt install --install-recommends steamcmd lib32gcc1 wine-stable xvfb
```

#### Force steam to detect 'windows' platform, download dedicated server to target
```bash
steamcmd +@sSteamCmdForcePlatformType windows +force_install_dir /data/conan-exiles-server +login anonymous +app_update 443030 validate +quit
```

#### Run initial server to create config templates
```bash
/opt/wine-stable/bin/wine /data/conan-exiles-server/ConanExilesServer.exe -log
```
 * run for about 5 minutes for all configs to be generated
 * should run through 2 cycles (two report cycles after loading/errors)
 * configs should appear in `ConanSandbox/Saved/Config/WindowsServer`

#### vim /data/conan-exiles-server/ConanSandbox/Saved/Config/WindowsServer/[Engine.ini](Engine.ini)
```vim
[URL]
Port=7777

[OnlineSubsystem]
bHasVoiceEnabled=False                   Global disable/enable voice.
ServerPassword=<PASSWORD>                Global platform independent password.
ServerName=<YOUR_SERVER_NAME>            Global platform independent name.

[OnlineSubsystemSteam]
ServerQueryPort=27015

[Voice]
bEnabled=False
```
 * add sections if they do not exist
 * on initial creation, most options will be removed and stored in the game
   database

#### vim /data/conan-exiles-server/ConanSandbox/Saved/Config/WindowsServer/[ServerSettings.ini](ServerSettings.ini)
```vim
MaxNudity=2                              2=Full, 1=Partial, 0=None
LogoutCharactersRemainInTheWorld=False   This option currently should be
                                         disabled as there is an issue with
                                         bodies.
IsBattleEyeEnabled=False                 Disable for linux.
IsVACEnabled=False                       Disable for linux.
serverRegion=2                           3=Asia, 2=Americas, 1/0=Europe. Tested
                                         as of 2018-06-19.
PVPEnabled=False
AdminPassword=<ADMIN_PASSWORD> 
```
 * all other settings can be changed in `admin panel` when connected
 * see `<target>/ConanSandbox/Config` for all options

Running as a Service
--------------------
Use xvfb to emulate correct environment for wine to function as a server.
If it runs correctly in a shell but not as a service, this is why.

### Create conan system user and set permissions

```bash
adduser --system --home /data/conan-exiles-server conan
cp -av ~/.wine /data/conan-exiles-server/.wine
chown -R conan /data/conan-exiles-server
```

### vim /etc/systemd/system/[conan.service](conan.service)
```bash
[Unit]
Description=Conan Exiles
After=syslog.target network.target

[Service]
Environment="WINEPREFIX=/data/conan-exiles-server/.wine"
ExecStart=/usr/bin/xvfb-run --auto-servernum --server-args='-screen 0 640x480:32' /opt/wine-stable/bin/wine /data/conan-exiles-server/ConanSandboxServer.exe -log
WorkingDirectory=/data/conan-exiles-server/
User=conan
Type=simple
Restart=on-failure
RestartSec=42s

[Install]
WantedBy=multi-user.target
```

Reload the service, start and watch the logs
```bash
systemctl daemon-reload
systemctl enable conan.service
systemctl start conan
journalctl -f -u conan
```

Installing Mods
---------------
Mods can be used for conan running on linux; though installing these mods
automatically from the workshop with wine doesn't work consistently.

### Obtain workshop mods
 * Download the mods wanted using the steam workshop and your game client
 * These should appear in `<STEAM>/content/440900/<MOD_ID>/MOD_NAME.pak`
 * Copy all `pak` files to linux server

### Setup linux server with mods
Create a `Mods` folder within `ConanSandbox` and place all `pak` files within.

```bash
mkdir /data/conan-exiles-server/ConanSandbox/Mods
cp *.pak /data/conan-exiles-server/ConanSandbox/Mods
```

### Enable modlist
Place each mod on a separate line, prefaced with '*', which will enable the
server to find the mod in this directory.

vim /data/conan-exiles/server/ConanSandbox/Mods/modlist.txt
```vim
*MyAwesomeMod.pak
*MyAwesomeOtherMod.pak
```

Ensure permissions are correct and start server

```bash
chown -R conan /data/conan-exiles-server
systemctl start conan
```

Updating Server
---------------
The server may be updated by stopping it, and running the update command. You will
need permissions to the directory to do the update.

It's a good idea to backup the install incase something goes wrong.

```bash
systemctl stop conan
su - conan
cp -av /data/conan-exiles-server /data/backups/<date>-conan-exiles-server
steamcmd +@sSteamCmdForcePlatformType windows +force_install_dir /data/conan-exiles-server +login anonymous +app_update 443030 validate +quit
systemctl start conan
```
 * If you get `0x0` or `disk write errors`, you need to explicitly own the files
   to modify them via steamcmd. `su` to the user or temporarily chown them.

References
----------
[Conan Exiles Dedicated Server][1]

[Conan Exiles CentOS][2]

Open references:
https://steamcommunity.com/sharedfiles/filedetails/?id=858035949
https://hub.docker.com/r/alinmear/docker-conanexiles/
https://tecadmin.net/install-wine-on-ubuntu/

[1]: https://conanexiles.gamepedia.com/Dedicated_Server_Setup:_Linux_and_Windows#Linux
[2]: https://steamcommunity.com/sharedfiles/filedetails/?id=858035949
[3]: https://old.reddit.com/r/ConanExiles/comments/5tgbsh/lets_discuss_ports/
