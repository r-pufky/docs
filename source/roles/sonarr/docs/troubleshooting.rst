.. _service-sonarr-troubleshooting:

Troubleshooting
###############

Add Pre-existing Series to Sonarr
*********************************

#. Existing files should be in a folder for each movie.
#. :cmdmenu:`Movie --> Bulk Import Movies --> /data/tv`
#. Be sure to set appropriate import behavior.
#. Be sure to search for correct match for episode if needed.
#. Add all existing shows (even no longer aired), these are all scanned when
   adding shows and will be crufty if not set.

Changing Media Location in Series
*********************************
If series were imported under a different directory initially, these can be
updated.

#. :cmdmenu:`Series --> Series Editor`
#. Select all series that had location changes.
#. :cmdmenu:`Root Folder` (lower right) and enter new folder location.
#. :cmdmenu:`Save`

Ensure no Duplicate Plex Updates
********************************
Plex will trigger updates on ``inotify`` events if configured to do so. If that
is the case: :cmdmenu:`Connect --> Plex --> Update Library --> Disable`.

Otherwise duplicate items will appear on single files.
