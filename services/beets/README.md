beets.io Media Server
---------------------
Music organizer.

[Docker repository][1]

1. [Docker Ports Exposed](#docker-ports-exposed)
1. [Important File Locations](#important-file-locations)
1. [Docker Creation](#docker-creation)
1. [Managing Library](#managing-library)
1. [Importing Gotchas](#importing-gotchas)

[Docker Ports Exposed][2]
-------------------------

| Port | Protocol | Purpose                       |
|------|----------|-------------------------------|
| 8337 | TCP      | Web GUI frontend for playback |

Important File Locations
------------------------
Relative to docker container

| File                | Purpose                             |
|---------------------|-------------------------------------|
| /config.yaml        | beets.io configuration.             |
| /library.sqlite3.db | beets.io library metadata database. |

Docker Creation
---------------

```bash
docker run -t -d \
  --name beets \
  --restart unless-stopped \
  -p 8337:8337 \
  -e PGID=5555 \
  -e PUID=900 \
  -e TZ=America/Los_Angeles \
  -v /data/downloads/complete/music:/data/downloads/complete/music \
  -v /data/media/music:/data/media/music \
  -v /data/services/beets:/config \
  -v /etc/localtime:/etc/localtime:ro \
  linuxserver/beets:latest
```
 * The UID/GID should be set to a user/group that have access to your media.
 * Map your media directly to where it was before on the docker container to
   prevent needing to modify any libraries.
 * See [config.yaml](config.yaml) for example configuration.
 * Use should use [`-t -d`][3] is needed to keep the container in interactive
   mode otherwise as soon as the container is idle it will sleep, which will
   stop background running services.

Managing Library
----------------
### Beets CLI interface
Interactive shell for importing music.

```bash
sudo docker exec -it -u abc beets bash
```
### [Importing music][5]
This will use the default configuation options from the config file.

```bash
beet import /path/to/music
```
 * Note: chroma (fingerprinting), musicbrainz, and other background tasks will
   be executed simultaneously in the background for the given directory. This
   should be kept small, such as a single album or artist
 * All albums need to be decided on before import starts. Keep import small
 * It may 'freeze' importing. Generally this is fingerprinting music and
   updating metadata with correct info/art. Let this run. Will be longer for
   larger number of imported items
 * Generally, go through potential matches. Any non-exact matches are usually
   fairly in accurate
 * Use `i` for musicbrainz ID if the top guesses are not accurate. This is
   helpful to force a specific ID
 * Pay attentions to `unmatched` tracks, these will **not** be imported if the
   current selection is choosen
 * **Duplicate** albums that need to be disambiguated should be imported as
   normal. When prompted `This album is already in the library`, select the
   **K**eep option. This will use aunique to disambiguate the albums.

### Re-importing music
Music may be re-imported if already existing. just use the library path.

```bash
beet import /data/media/music/existing/artist/album
```
 * If you have `incremental` enabled, you may have to remove the metadata
   from the library before importing

### Adding to an existing album
Adding a track to an existin album is a bit confusing, especially if it is a
compilation/various artist album. Follow these steps.

1. Determine the existing album metadata:
   ```bash
   beet info [query]
   ```
    * Make sure to select the metadata tracks that match the album
1. Select the correct album on the import prompt
1. Beets will ask to merge, list a summary of existing and new tracks; open
   an additional shell, find the track locally and ensure there's no collisions
   with the merge
1. Select the correct album on the merged import prompt

### Fixing 'featuring' tracks.
The plugin ftintitle generally takes care of this, but there are certain cases
where this is not the case. This addresses those cases.

[ftintitle works][3] by using the `albumartist` is the 'real' artist and `artist`
field has 'feat.' in it.

Set the albumartist to the appropriate artist
```bash
beet modify albumartist='single artist' [query]
```
 * You should use `list` to find appropriate data to match

Set artist to appropriate 'feat.' text, if needed
```bash
beet modify artist='single artist feat. other artist' [query]
```
 * Generally this is setup correctly in musicbrainz

Re-run ftintitle
```bash
beet -v ftintitle [query]
```
 * This should pickup your artist changes and act appropriately

### Manually moving files
Sometimes if an import half-way through, some files will be imported, others
will not. This will execute moves based on existing music metadata.

```bash
beet move
```
 * use `-p` to test before applying

### Update the library
This will update the database with any new file metadata, as well as organize
existing files according to metadata.

```bash
beet update
```
 * use `-p` to test before applying

### Changing music metadata
Useful for fixing bad imports, or for getting music to re-import correctly.

```bash
beet modify [attribute]=[value] [query]
```
 * Ensure to use `list` to make sure you are only modifying the tracks that
   you want.

### Removing tracks
This is useful for re-importing tracks, as well as permenant deletion.

```bash
beet remove [query]
```
 * This will remove file metadata from library (does not delete files)
 * use `-d` to actually delete files

### Querying
By default queries all fields for matches. Can use `path` specificier to
specify an exact file, as well as attribute matching. [See Reference][4]
for additional querying options.

#### Matching fields
```bash
beet list [field]:[value]
```

#### Matching exact string
```bash
beet list 'some exact title'
```

#### Finding empty fields
Uses regex matching.

```bash
beet list [field]::^$
```

For matching on all fields
```bash
beet list ":^$"
```

### Path matching
Useful for files with exact same metadata

```bash
beet list path:/my/music/directory/or/file
```

Path is implied with '/'
```bash
beet list /my/music/directory/or/file
```

Importing Gotchas
-----------------
Sometimes beets just doesn't import correctly.

### Use `avprobe` and [`mid3v2`][6] modify pre-import metadata.
For cases where pre-manipulation of track data will help for a better
match, or fixing a bad match detection.

#### List current metadata
```bash
mid3v2 -l [file]
```

#### Update metadata
```bash
mid3v2 -t 'new title' [file]
mid3v2 -T '1/5' [file]
mid3v2 -A 'new album' [file]
mid3v2 -a 'new artist' [file]
```
 * In practice, usually just the track and title need to be changed
 * See man page for all options

#### Get file info/track length/bitrate
Useful for matching duplicates in beets, or track lengths to albums

```bash
avprobe [file]
```

### Force import a track as a single specific track
This will resolve tracks that are consistently mis-identified even
after munging the metadata.

Find the recording ID for musicbrains (the individual track ID on
musicbrainz), and import singleton track
```bash
beet import /import/album/track.mp3
```
 * **T** option to specify a single track
 * **I** to select a `recording ID`

Re-import the now correct track into the existing album. Find the
album ID from musicbrains or existing album in beets.
```beets
beet import /data/media/music/Non-Albums/imported-track-from-above.mp3
```
 * **I** to select a `release ID`
 * **M** merge tracks into album

[1]: https://hub.docker.com/r/linuxserver/beets/
[2]: https://beets.readthedocs.io/en/latest/reference/index.html
[3]: https://github.com/beetbox/beets/issues/1766
[4]: https://beets.readthedocs.io/en/latest/reference/query.html
[5]: http://beets.readthedocs.io/en/latest/guides/tagger.html
[6]: https://unix.stackexchange.com/questions/4961/which-mp3-tagging-tool-for-linux
