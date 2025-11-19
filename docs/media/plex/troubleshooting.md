# Troubleshooting


## Fixing Playback Issues

### Playback Fails / App Crashes
Generally this happens when you are playing media on Plex Home Theater or Plex
app, where **transcoding** is being used. The app will crash generally with a
message:

!!! danger ""
    Conversation failed. Transcoder crashed or failed to start up

This usually happens because the transcoder was not able to write to the
transcoding directory.

1. Ensure **Transcoding** directory is setup properly on Plex Server.
2. Ensure **/tmp/Transcode** is owned by the right user. Changing the running
   user without re-creating this directory will cause this to happen.

### [Spinning playback icon, no playback][a]
Generally if transcoding is setup right, then this is related to the **audio
transcoding** failing. Turn on debug logging on the server and look for:

!!! danger ""
    EAE timeout! EAE not running, or wrong folder? Could not read

This means you need to remap the **/tmp** directory to your transcoding
directory, as plex updated transcoding and split out audio and video encoding
into separate locations. Video transcodes in **/transcode** while audio
transcodes in **/tmp**. Mapping **/tmp** to the transcoding directory fixes
this.


## Managing Duplicates

### Duplicate Files for Single Files
This happens when two refreshes for a new file happen at the same time.
Generally this occurs because inotify detection is turned on in Plex, and
Sonarr is set to push a manual **update library** command to plex on
completion. Only **one** of these things should be enabled at once.

1. Move duplicate file out of Plex library.
2. Wait for episode refresh trigger / trigger manually (episode should be
   removed).
3. Move duplicate file into Plex library.
4. Wait for episode refresh trigger / trigger manually (episode should be
   removed). Dupe should be removed.


## Finding Duplicates
To show all detected duplicates in plex:

!!!tip "Plex ➔ TV Shows ➔ {TV Shows Dropdown in main window} ➔ Episodes"

!!!tip "Plex ➔ TV Shows ➔ {All in main window} ➔ Duplicates"

From there you can Inspect all shows.


## Legacy Plex Fixes
Fixes for early Plex servers. These generally do not appear anymore.

### [Backup State Configuration][b]
``` bash
cd /var/lib/plexmediaserver/Library/Application\ Support/Plex\ Media\ Server/Plugin\ Support/Databases
echo ".dump metadata_item_settings" | sudo sqlite3 com.plexapp.plugins.library.db | grep -v TABLE | grep -v INDEX > viewstate-information-settings.sql
cd /var/lib/plexmediaserver/Library/Application\ Support/Plex\ Media\ Server
sudo cp -av Media /tmp/media-backup
sudo cp -av Metadata /tmp/metadata-backup
```

### Restoring Plex State Configuration
``` bash
cd /var/lib/plexmediaserver/Library/Application\ Support/Plex\ Media\ Server/Plugin\ Support/Databases
cat viewstate-information-settings.sql | sudo sqlite3 com.plexapp.plugins.library.db
cd /var/lib/plexmediaserver/Library/Application\ Support/Plex\ Media\ Server
sudo cp -av /tmp/media-backup Media
sudo cp -av /tmp/metadata-backup Metadata
```

### Plex Stuck at Initial Startup
``` bash
# Stop Plex and remove Service Bundle Framework.
sudo service plexmediaserver stop
sudo ps -ef | grep -i plex
sudo kill -9 {REMAINING PIDS}
cd /var/lib/plexmediaserver/Library/Application\ Support/Plex\ Media\ Server/Plugins
rm -f Service.bundle Framwork.bundle
sudo service plexmediaserver start
sudo reboot
```

[a]: https://forums.plex.tv/t/transcoder-fails-when-transcode-is-on-a-network-share/186681
[b]: https://plexapp.zendesk.com/hc/en-us/articles/201154527-Move-Viewstate-Ratings-from-One-Install-to-Another
