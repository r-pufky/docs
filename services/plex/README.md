[Plex][8x] Media Server
=======================
Media streaming service.

1. [Ports](#ports)
1. [Important File Locations](#important-file-locations)
1. [Docker Creation](#docker-creation)
1. [Fixing Playback Issues](#fixing-playback-issues)
1. [Managing Duplicates](#managing-duplicates)
1. [Legacy Plex Fixes](#legacy-plex-fixes)

[Ports][dp]
-----------
Docker reverse-proxy.

| Port  | Protocol | Exposed/Public | Purpose                                                  |
|-------|----------|----------------|----------------------------------------------------------|
| 32400 | TCP      | Public         | Plex Media Server Access.                                |
| 1900  | UDP      | Public         | (Optional) Plex DLNA Server.                             |
| 3005  | TCP      | Public         | (Optional) Control Plex Home Theater via Plex Companion. |
| 5353  | UDP      | Public         | (Optional) Bonjour/Avahi discovery.                      |
| 8324  | TCP      | Public         | (Optional) Control Plex for Roku via Plex Companion.     |
| 32410 | UDP      | Public         | (Optional) GDM network discovery.                        |
| 32412 | UDP      | Public         | (Optional)  GDM network discovery.                       |
| 32413 | UDP      | Public         | (Optional) GDM network discovery.                        |
| 32414 | UDP      | Public         | (Optional) GDM network discovery.                        |
| 32469 | TCP      | Public         | (Optional) Plex DLNA Server.                             |
* Using host networking will expose all of these ports. It may be better to
  specify just `32400`.

Important File Locations
------------------------
Relative to docker container.

| File    | Purpose                    |
|---------|----------------------------|
| /config | Plex media server library. |

Docker Creation
---------------
You can copy your existing library from _/var/lib/plexmediaserver/*_ to docker
_/config_ directory to auto-import your existing plex library.

* The UID/GID should be set to a user/group that have access to your media. All
  media clients should run under the same user to run correctly.
* Map your media directly to where it was before on the docker container to
  prevent needing to modify any libraries. This should be read-only.
* _/transcode_ needs to be mapped to a **fast** drive. See
  [setup /transcode with tempfs][ll] to run transcoding in memory.
* We additionally map the plex _/tmp_ directory to a subdirectory for the
  transcoding directory. Plex updated transcoding to split video encoding to
  _/transcode_ while the audio encoding is transcoded in _/tmp_. This causes the
  _EAE timeout! EAE not running, or wrong folder? Could not read_ Error. Moving
  _/tmp_ fixes this.
* `PLEX_CLAIM` token is used to identify the server for your account. This is
  only used on initial startup without a pre-existing config. Generate a token
  here: https://www.plex.tv/claim.

Docker Compose:
```yaml
plex:
  image: plexinc/pms-docker:plexpass
  restart: unless-stopped
  network_mode: host
  environment:
    - CHANGE_CONFIG_DIR_OWNERSHIP=False
    - PLEX_GID=1001
    - PLEX_UID=1001
    - PLEX_CLAIM={CLAIM TOKEN}
    - TZ=America/Los_Angeles
  volumes:
    - /data/media:/data/media:ro
    - /data/services/plexmediaserver:/config
    - /etc/localtime:/etc/localtime:ro
    - /tmp/Transcode/tmp:/tmp
    - /tmp:/transcode
```

```bash
docker-compose stop plex
```

### Setup /transcode with tmpfs
Transcoding is disk intensive and requires a fast (SSD or better) drive to make
latencies transparent. This will setup /tmp with tmpfs (running in memory) to
do transcoding in RAM, which will make playback and seeks nearly instantanenous.

On the docker host:

/etc/fstab `root:root 0644`
```bash
tmpfs  /tmp  tmpfs  defaults,size=4G  0  0
```
* Setup /tmp to use at most 4G of RAM for storage (tmpfs only allocates space
  from actual items stored).
* Note: Ensure that **/transcode** is set on the plex server to properly map to
  the docker host _/tmp_ directory.

Reboot to enable.

### Enable secure server connection

* Ensure `32400` is forwarded to the router.
* Enable [DNS Rebinding][yu] on router.

### Initial setup
If not using a plex claim token or manual port forwarding you may need to setup
plex manually from the machine. Setup a SSH port forward:

```bash
ssh -L 32400:<Server IP>:32400 -N <user>@<host>
```

Then nagivate to `http://localhost:32400/web` to finish setup.

```bash
docker start plex
```

Fixing Playback Issues
----------------------
### Playback Fails / App Crashes
Generally this happens when you are playing media on Plex Home Theater or Plex
app, where _transcoding_ is being used. The app will crash generally with a
message of _Conversation failed. Transcoder crashed or failed to start up_. This
usually happens because the transcoder was not able to write to the transcoding
directory.

* Ensure `Transcoding` directory is setup properly on Plex Server.
* Ensure `/tmp/Transcode` is owned by the right user. Changing the running user
  on docker without re-creating this directory will cause this to happen.

### [Spinning playback icon, no playback][bi]
Generally if transcoding is setup right, then this is related to the _audio
transcoding_ failing. Turn on debug logging on the server and look for the
_EAE timeout! EAE not running, or wrong folder? Could not read_ error. This
means you need to remap the docker _/tmp_ directory to your transcoding
directory, as plex updated transcoding and split out audio and video encoding
into separate locations. Video transcodes in _/transcode_ while audio transcodes
in _/tmp_. Mapping _/tmp_ in docker to the transcoding directory fixes this.

```docker
volumes:
  - /tmp/Transcode/tmp:/tmp
```

Managing Duplicates
-------------------
### Duplicate Files for Single Files
This happens when two refreshes for a new file happen at the same time.
Generally this occurs because inotify detection is turned on in Plex, and
Sonarr is set to push a manual _update library_ command to plex on completion.
Only **one** of these things should be enabled at once.

To correct this
* Move duplicate file out of Plex library.
* Wait for episode refresh trigger / trigger manually (episode should be
  removed).
* Move duplicate file into Plex library.
* Wait for episode refresh trigger / trigger manually (episode should be
  removed). Dupe should be removed.

### Finding Duplicates
To show all detected duplicates in plex:
* `Plex > TV Shows > [TV Shows Dropdown in main window] > Episodes`
* `Plex > TV Shows > [All in main window] > Duplicates`

From there you can Inspect all shows.

Legacy Plex Fixes
-----------------
### [Backup state configuration][tp]

```bash
cd /var/lib/plexmediaserver/Library/Application\ Support/Plex\ Media\ Server/Plugin\ Support/Databases
echo ".dump metadata_item_settings" | sudo sqlite3 com.plexapp.plugins.library.db | grep -v TABLE | grep -v INDEX > viewstate-information-settings.sql
cd /var/lib/plexmediaserver/Library/Application\ Support/Plex\ Media\ Server
sudo cp -av Media /tmp/media-backup
sudo cp -av Metadata /tmp/metadata-backup
```
* This exports the viewstate.

### Restoring Plex State Configuration

```bash
cd /var/lib/plexmediaserver/Library/Application\ Support/Plex\ Media\ Server/Plugin\ Support/Databases
cat viewstate-information-settings.sql | sudo sqlite3 com.plexapp.plugins.library.db
cd /var/lib/plexmediaserver/Library/Application\ Support/Plex\ Media\ Server
sudo cp -av /tmp/media-backup Media
sudo cp -av /tmp/metadata-backup Metadata
```

### Plex Stuck at Initial Startup

```bash
sudo service plexmediaserver stop
sudo ps -ef | grep -i plex
sudo kill -9 <any remaining PID’s>
cd /var/lib/plexmediaserver/Library/Application\ Support/Plex\ Media\ Server/Plugins
rm -f Service.bundle Framwork.bundle
sudo service plexmediaserver start
sudo reboot
```

[docker-service-template.md|c9067f2][XX]

[ll]: #setup-transcode-with-tempfs
[8x]: https://hub.docker.com/r/plexinc/pms-docker/
[dp]: https://support.plex.tv/articles/201543147-what-network-ports-do-i-need-to-allow-through-my-firewall/
[yu]: https://support.plex.tv/articles/206225077-how-to-use-secure-server-connections/
[bi]: https://forums.plex.tv/discussion/265492/transcoder-fails-when-transcode-is-on-a-network-share/p4
[tp]: https://plexapp.zendesk.com/hc/en-us/articles/201154527-Move-Viewstate-Ratings-from-One-Install-to-Another
[XX]: https://github.com/r-pufky/docs/blob/c9067f2bc3d0aeb0f2915e63f8cd9515c00640a2/services/docker-service-template.md

[refwe]: https://www.cb-net.co.uk/linux/running-plex-from-a-docker-container-on-ubuntu-16-04-lts-16-10/