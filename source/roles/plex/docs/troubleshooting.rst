.. _service-plex-troubleshooting:

Troubleshooting
###############

Fixing Playback Issues
**********************

Playback Fails / App Crashes
============================
Generally this happens when you are playing media on Plex Home Theater or Plex
app, where **transcoding** is being used. The app will crash generally with a
message:

.. pull-quote::
  *Conversation failed. Transcoder crashed or failed to start up*

This usually happens because the transcoder was not able to write to the
transcoding directory.

#. Ensure ``Transcoding`` directory is setup properly on Plex Server.
#. Ensure ``/tmp/Transcode`` is owned by the right user. Changing the running
   user on docker without re-creating this directory will cause this to happen.

Spinning playback icon, no playback
===================================
Generally if transcoding is setup right, then this is related to the *audio
transcoding* failing. Turn on debug logging on the server and look for:

.. pull-quote::
  *EAE timeout! EAE not running, or wrong folder? Could not read*

This means you need to remap the docker ``/tmp`` directory to your transcoding
directory, as plex updated transcoding and split out audio and video encoding
into separate locations. Video transcodes in ``/transcode`` while audio
transcodes in ``/tmp``. Mapping ``/tmp`` in docker to the transcoding directory
fixes this.

.. code-block:: yaml
  :caption: Correctly mapping Plex ``/tmp`` to tmpfs.

  volumes:
    - /tmp/Transcode/tmp:/tmp

`Reference <https://forums.plex.tv/t/transcoder-fails-when-transcode-is-on-a-network-share/186681>`__

Managing Duplicates
*******************

Duplicate Files for Single Files
================================
This happens when two refreshes for a new file happen at the same time.
Generally this occurs because inotify detection is turned on in Plex, and Sonarr
is set to push a manual **update library** command to plex on completion. Only
**one** of these things should be enabled at once.

#. Move duplicate file out of Plex library.
#. Wait for episode refresh trigger / trigger manually (episode should be
   removed).
#. Move duplicate file into Plex library.
#. Wait for episode refresh trigger / trigger manually (episode should be
   removed). Dupe should be removed.

Finding Duplicates
===================
To show all detected duplicates in plex:

#. :cmdmenu:`Plex --> TV Shows --> {TV Shows Dropdown in main window} --> Episodes`
#. :cmdmenu:`Plex --> TV Shows --> {All in main window} --> Duplicates`

From there you can Inspect all shows.

Legacy Plex Fixes
*****************
Fixes for early Plex servers. These generally do not appear anymore.

Backup State Configuration
==========================
.. code-block:: bash
  :caption: Export viewstate database and files.

  cd /var/lib/plexmediaserver/Library/Application\ Support/Plex\ Media\ Server/Plugin\ Support/Databases
  echo ".dump metadata_item_settings" | sudo sqlite3 com.plexapp.plugins.library.db | grep -v TABLE | grep -v INDEX > viewstate-information-settings.sql
  cd /var/lib/plexmediaserver/Library/Application\ Support/Plex\ Media\ Server
  sudo cp -av Media /tmp/media-backup
  sudo cp -av Metadata /tmp/metadata-backup

`Reference <https://plexapp.zendesk.com/hc/en-us/articles/201154527-Move-Viewstate-Ratings-from-One-Install-to-Another>`__

Restoring Plex State Configuration
==================================
.. code-block:: bash
  :caption: Restore viewstate database and files.

  cd /var/lib/plexmediaserver/Library/Application\ Support/Plex\ Media\ Server/Plugin\ Support/Databases
  cat viewstate-information-settings.sql | sudo sqlite3 com.plexapp.plugins.library.db
  cd /var/lib/plexmediaserver/Library/Application\ Support/Plex\ Media\ Server
  sudo cp -av /tmp/media-backup Media
  sudo cp -av /tmp/metadata-backup Metadata

Plex Stuck at Initial Startup
=============================

.. code-block:: bash
  :caption: Stop Plex and remove Service Bundle Framework.

  sudo service plexmediaserver stop
  sudo ps -ef | grep -i plex
  sudo kill -9 {REMAINING PIDS}
  cd /var/lib/plexmediaserver/Library/Application\ Support/Plex\ Media\ Server/Plugins
  rm -f Service.bundle Framwork.bundle
  sudo service plexmediaserver start
  sudo reboot
