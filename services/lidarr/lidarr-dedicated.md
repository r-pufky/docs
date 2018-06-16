Lidarr Server
-------------
Music Management.

All media clients should run under the same user to run correctly.

1. [Ports Exposed](#ports-exposed)
1. [Important File Locations](#important-file-locations)
1. [Server Setup](#server-setup)
1. [Add pre-existing series to Lidarr](#add-pre-existing-series-to-lidarr)
1. [Changing Media Location in Series](#changing-media-location-in-series)
1. [Ensure no Duplicate Plex Updates](#ensure-no-duplicate-plex-updates)
1. [References](#references)

[Ports Exposed]
---------------

| Port | Protocol | Purpose           |
|------|----------|-------------------|
| 8686 | TCP      | Lidarr webservice |

Important File Locations
------------------------

| File                  | Purpose                              |
|-----------------------|--------------------------------------|
| /data/services/lidarr | Lidarr main service directory        |
| /data/downloads       | Lidarr monitored downloads directory |

Server Setup
------------

### Add PPA and install lidarr dependencies
/etc/apt/sources.list.d/mono-offical.list
```
deb http://download.mono-project.com/repo/ubuntu xenial main
```

```bash
$ sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF
apt update && apt install mono-runtime libmono-cil-dev libmediainfo0v5 curl mediainfo mono-devel mediainfo sqlite3 libmono-cil-dev
```

### Create `lidarr` user and `media` group for running the service
```bash
adduser --disabled-password --system --home /data/services/lidarr --gecos "lidarr" --group lidarr
addgroup media
adduser lidarr media
```
 * Add your user account to media if needed

### Install lidarr

```bash
cd /opt
curl -L -O $( curl -s https://api.github.com/repos/Lidarr/Lidarr/releases | grep linux.tar.gz | grep browser_download_url | head -1 | cut -d \" -f 4 )
tar -xvzf Lidarr.develop.*.linux.tar.gz
sudo chown -R lidarr:media /opt/Lidarr
```

### Copy [systemd service template](lidarr.service) to `/etc/systemd/system/lidarr.service`.
 * Ensure options are updated with your settings in file

Enable the lidarr service
```bash
systemctl enable lidarr.service
```

```bash
systemctl start lidarr
```

See [lidarr configuration](lidarr.config.md) for example configuration.

Add pre-existing series to Lidarr
---------------------------------
 * Existing files should be in a folder for each movie.
 * Import Existing Series On Disk: /data/music
 * Be sure to set appropriate import behavior
 * Add all existing music (even tapings), these are all scanned when adding
   music and will be crufty if not set.

Ensure no Duplicate Plex Updates
--------------------------------
Plex will trigger updates on inotify events if configured to do so. If that is
the case, disable `update library` in `Connect > Plex` menu. Otherwise
duplicate items will appear on single files.

References
----------
[lidarr website][1]

[Installing Lidarr on Ubuntu][2]

[1]: https://github.com/lidarr/Lidarr
[2]: https://github.com/Lidarr/Lidarr/wiki/Installation