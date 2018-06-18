Radarr Server
-------------
Movie Management.

All media clients should run under the same user to run correctly.

1. [Ports Exposed](#ports-exposed)
1. [Important File Locations](#important-file-locations)
1. [Server Setup](#server-setup)
1. [Add pre-existing series to Radarr](#add-pre-existing-series-to-radarr)
1. [Changing Media Location in Series](#changing-media-location-in-series)
1. [Ensure no Duplicate Plex Updates](#ensure-no-duplicate-plex-updates)
1. [References](#references)

[Ports Exposed]
---------------

| Port | Protocol | Purpose           |
|------|----------|-------------------|
| 7878 | TCP      | Radarr webservice |

Important File Locations
------------------------

| File                  | Purpose                              |
|-----------------------|--------------------------------------|
| /data/services/radarr | Radarr main service directory        |
| /data/downloads       | Radarr monitored downloads directory |

Server Setup
------------

### Add PPA and install radarr dependencies
/etc/apt/sources.list.d/mono-offical.list
```
deb http://download.mono-project.com/repo/ubuntu xenial main
```

```bash
$ sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF
apt update && apt install mono-runtime libmono-cil-dev libmediainfo0v5 curl mediainfo mono-devel mediainfo sqlite3 libmono-cil-dev
```

### Create `radarr` user and `media` group for running the service
```bash
adduser --disabled-password --system --home /data/services/radarr --gecos "radarr" --group radarr
addgroup media
adduser radarr media
```
 * Add your user account to media if needed

### Install radarr

```bash
cd /opt
curl -L -O $( curl -s https://api.github.com/repos/Radarr/Radarr/releases | grep linux.tar.gz | grep browser_download_url | head -1 | cut -d \" -f 4 )
tar -xvzf Radarr.develop.*.linux.tar.gz
sudo chown -R radarr:media /opt/Radarr
```

### Copy [systemd service template](radarr.service) to `/etc/systemd/system/radarr.service`.
 * Ensure options are updated with your settings in file

Enable the radarr service
```bash
systemctl enable radarr.service
```

```bash
systemctl start radarr
```

See [radarr configuration](radarr.config.md) for example configuration.

Add pre-existing series to Radarr
---------------------------------
 * Existing files should be in a folder for each movie
 * Import Existing Series On Disk: /data/movies
 * Be sure to set appropriate import behavior
 * Be sure to search for correct match for episode if needed
 * Import may timeout if initial import library is large. If this happens, just
   goto `Movies` and run `Update Library`

Ensure no Duplicate Plex Updates
--------------------------------
Plex will trigger updates on inotify events if configured to do so. If that is
the case, disable `update library` in `Connect > Plex` menu. Otherwise
duplicate items will appear on single files.

References
----------
[radarr website][1]

[Installing Radarr on Ubuntu][2]

[1]: https://github.com/Radarr/Radarr/wiki/Installation
[4]: https://www.htpcguides.com/install-radarr-on-debian-8-jessie/