Crashplan Service
-----------------
Installing crashplan as an independent service.

1. [Ports Exposed](#ports-exposed)
2. [Server Setup](#server-setup)
3. [Important File Locations](#important-file-locations)
4. [Disable Insecure Services](#disable-insecure-services)
5. [Starting the Server](#starting-the-server)
6. [References](#references)

[Ports Exposed][1]
------------------

| Port        | Protocol | Purpose                                                                        |
|-------------|----------|--------------------------------------------------------------------------------|
| 443         | TCP      | Code42 cloud storage                                                           |
| 4243        | TCP      | Localhost Code42 app connecting to Code42 service                              |
| 1024-14500  | TCP      | (Optional) NAT traversal ranges used for connecting between computers          |
| 49000-52000 | TCP      | (Optional) NAT traversal ranges used for connecting between computers          |
| 1900        | UDP      | (Optional) Standard UPnP ports required for computer-to-computer connections   |
| 2869        | TCP      | (Optional) Standard UPnP ports required for computer-to-computer connections   |
| 5351        | UDP      | (Optional) Standard NAT-PMP port required for computer-to-computer connections |

Server Setup
-------------
Download the latest binary package from the [crashplan console][2].

```bash
tar zxvf <crashplan-binary>.tgz
cd crashplan-install
./uninstall.sh -i /usr/local/crashplan
./install.sh
```
 * This will remove an existing crashplan install with a default location,
   keeping the existing identity configuration; this should be done for every
   installation
 * defaults are fine

Bump inotify limits for crashplan

/etc/sysctl.conf
```bash
fs.inotify.max_user_watches=1048576
```

Then reload `sysctl` or `reboot`.
```bash
sysctl -p /etc/sysctl.conf
```


Connect to Crashplan using X11
------------------------------
A minimal X11 installation is needed to setup crashplan via X11.

```bash
apt install gconf-service gconf-service-backend gconf2-common libgconf-2-4 libxss1 libnss3 libasound2 libwebkitgtk-3.0-0
```

Then SSH to crashplan system with X11 forwarding enabled.

```bash
/usr/local/crashplan/bin/CrashPlanDesktop
```

[Connect to Crashplan using SSH Port Forwarding][3]
---------------------------------------------------
Alternative instructions [here][5].

### Copy the authentication token from the crashplan identity

/var/lib/crashplan/.ui_info
```bash
<port>,<auth token>,<ip>
```

### Stop the local crashplan application

Make a backup of the [local `.ui_info`][4] file and edit

c:\ProgramData\CrashPlan\.ui_info
```bash
4200, <auth token from crashplan system>,<untouched ip>
```
 * use port 4200 for remot system
 * leave ip untouched, and set authentication token

### Setup crashplan remotely

Start a SSH session with port forwarding
```bash
ssh -L 4200:localhost:4243 <user>@<crashplan-machine>
```

Open localt crashplan app and proceed as normal.

[1]: https://support.code42.com/Administrator/5/Planning_and_installing/TCP_and_UDP_ports_used_by_the_Code42_platform
[2]: https://web-ham-msp.crashplanpro.com/console/#/app-downloads
[3]: https://support.code42.com/CrashPlan/4/Configuring/Use_CrashPlan_on_a_headless_computer
[4]: https://support.code42.com/CrashPlan/4/Configuring/Use_CrashPlan_on_a_headless_computer#Locations_of_.ui_info
[5]: https://www.reddit.com/r/Crashplan/comments/82yi3t/headless_mode_working_on_67/