Steam - Conan Exiles (Linux) Dedicated Server
---------------------------------------------
Uses [Ubuntu 16.04 base Xen template](../templates/ubuntu-server.md), and
assumes post template setup scripts have been run.

* Memory: 2048MB-8096MB
* Disk: 20GB

1. [Ports Exposed](#ports-exposed)
1. [Server Setup](#server-setup)
1. [Important File Locations](#important-file-locations)
1. [Starting the Server](#starting-the-server)
1. [References](#references)

Ports Exposed
-------------

| Port  | Protocol | Purpose                    |
|-------|----------|----------------------------|
| 27015 | UDP      | Dedicated Server (steam)   |
| 7777  | UDP      | Dedicated Server (clients) |

Important File Locations
------------------------

| File                                                                | Purpose                           |
|---------------------------------------------------------------------|-----------------------------------|
| <target>/ConanSandbox/Saved/Config/WindowsServer/Engine.ini         | Core engine settings, e.g. ports. |
| <target>/ConanSandbox/Saved/Config/WindowsServer/ServerSettings.ini | Specific game instance settings.  |
| <target>/ConanSandbox/Saved/                                        | Game database and saves.          |
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
/opt/wine-stable/bin/wine ConanExilesServer.exe -log
```
 * run for about 5 minutes for all configs to be generated
 * should run through 2 cycles (two report cycles after loading/errors)
 * configs should appear in `ConanSandbox/Saved/Config/WindowsServer`

#### vim /data/conan-exiles-server/ConanSandbox/Saved/Config/WindowsServer/[Engine.ini](Engine.ini)
```vim
[URL]
Port=7777

[OnlineSubsystemSteam]
ServerName=Conan Exiles
ServerQueryPort=27015
ServerPassword=<PASSWORD>
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
PVPEnabled=False
AdminPassword=<ADMIN_PASSWORD> 
```
 * all other settings can be changed in `admin panel` when connected
 * see `<target>/ConanSandbox/Config` for all options

### Running as service
Use xvfb to emulate correct environment for wine to function as a server.
If it runs correctly in a shell but not as a service, this is why.

#### Create conan system user and set permissions

```bash
adduser --system --home /data/conan-exiles-server conan
cp -av ~/.wine /data/conan-exiles/server/.wine
chown -R conan /data/conan-exiles-server
```

#### vim /etc/systemd/system/[conan.service](conan.service)
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

```bash
systemctl daemon-reload
systemctl enable conan.service
systemctl start conan
journalctl -f -u conan
```

References
----------
[Conan Exiles Dedicated Server][1]

[Conan Exiles CentOS][2]

[1]: https://conanexiles.gamepedia.com/Dedicated_Server_Setup:_Linux_and_Windows#Linux
[2]: https://steamcommunity.com/sharedfiles/filedetails/?id=858035949
