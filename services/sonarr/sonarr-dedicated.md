Sonarr Server
-------------
Media Management.

All media clients should run under the same user to run correctly.

1. [Ports Exposed](#ports-exposed)
1. [Important File Locations](#important-file-locations)
1. [Server Setup](#server-setup)
1. [Add pre-existing series to Sonarr](#add-pre-existing-series-to-sonarr)
1. [Changing Media Location in Series](#changing-media-location-in-series)
1. [Ensure no Duplicate Plex Updates](#ensure-no-duplicate-plex-updates)
1. [References](#references)

[Ports Exposed][1]
------------------

| Port | Protocol | Purpose           |
|------|----------|-------------------|
| 8989 | TCP      | Sonarr webservice |

Important File Locations
------------------------

| File                  | Purpose                              |
|-----------------------|--------------------------------------|
| /data/services/sonarr | sonarr main service directory        |
| /data/downloads       | sonarr monitored downloads directory |

Server Setup
------------

### Add PPA and install sonarr and dependencies

/etc/apt/sources.list.d/sonarr.list
```
deb http://apt.sonarr.tv/ master main
```

```bash
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys FDA5DFFC
apt update && apt install mono-runtime libmono-cil-dev libmediainfo0v5 nzbdrone
```

### Create `sonarr` user and `media` group for running the service
```bash
adduser --disabled-password --system --home /data/services/sonarr --gecos "sonarr" --group sonarr
addgroup media
adduser sonarr media
```
 * Add your user account to media if needed

### Copy [systemd service template](sonarr.service) to `/etc/systemd/system/sonarr.service`.
 * Ensure options are updated with your settings in file

Enable the sonarr service
```bash
systemctl enable sonarr.service
```

### Set service permissions

```bash
chown -R sonarr:media {/opt/NzbDrone,/data/services/nzbdrone}
chmod -R 0700 {/opt/NzbDrone,/data/services/nzbdrone}
```

```bash
systemctl start sonarr
```

See [sonarr configuration](sonarr.config.md) for example configuration.

Add pre-existing series to Sonarr
---------------------------------
 * Import Existing Series On Disk: /data/tv
 * Be sure to set appropriate import behavior
 * Be sure to search for correct match for episode if needed
 * Add all existing shows (even no longer aired), these are all scanned when
   adding shows and will be crufty if not set

Changing Media Location in Series
---------------------------------
If series were imported under a different directory initially, these can be
updated

 * Series -> Series Editor
 * Select all series that had location changes
 * Select `Root Folder` (lower right) and enter new folder location
 * Click `Save`

Ensure no Duplicate Plex Updates
--------------------------------
Plex will trigger updates on inotify events if configured to do so. If that is
the case, disable `update library` in `Connect > Plex` menu. Otherwise
duplicate items will appear on single files.

References
----------
[nzbdrone website][1]

[Installing nzbdrone in Ubuntu 14.04][2]

[Installing nzbdrone (github)][3]

[nzbdrone systemd service][4]

[1]: https://sonarr.tv/
[2]: http://dominicm.com/install-nzbdrone-sonarr-on-ubuntu-14-04/
[3]: https://github.com/Sonarr/Sonarr/wiki/Installation
[4]: https://github.com/Sonarr/Sonarr/wiki/Autostart-on-Linux