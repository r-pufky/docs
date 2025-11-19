# Troubleshooting


## Add Pre-existing Series to Sonarr

1. Existing files should be in a folder for each movie.
2. Movie ➔ Bulk Import Movies ➔ /data/tv
3. Set appropriate import behavior.
4. Search for correct match for episode if needed.
5. Add all existing shows (even no longer aired), these are all scanned when
   adding shows and will be crufty if not set.


## Changing Media Location in Series
If series were imported under a different directory initially, these can be
updated.

1. Series ➔ Series Editor
2. Select all series that had location changes.
3. Root Folder (lower right) and enter new folder location.
4. Save.


## Ensure no Duplicate Plex Updates
Plex will trigger updates on **inotify** events if configured to do so. If that
is the case:

Connect ➔ Plex ➔ Update Library ➔ Disable.

Otherwise duplicate items will appear on single files.


## Failures with Searches
These are DNS resolution failures. Generally these happened because of rate
limiting due to large number of changes at one time. Upgrade system packages or
re-apply role to ensure the latest mono project certificates are installed as
well.

``` bash
apt update && apt upgrade
```
