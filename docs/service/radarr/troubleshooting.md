# Troubleshooting

## Add Pre-existing Series to Radarr

1. Existing files should be in a folder for each movie.
2. Movie ➔ Bulk Import Movies ➔ /data/movies
3. Be sure to set appropriate import behavior.
4. Be sure to search for correct match for episode if needed.
5. Import may timeout if initial import library is large. Restart import.

   Movies ➔ Update Library

## Ensure no Duplicate Plex Updates
Plex will trigger updates on **inotify** events if configured to do so. If that
is the case:

Connect ➔ Plex ➔ Update Library ➔ Disable

Otherwise duplicate items will appear on single files.
