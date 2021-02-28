.. _service-lidarr-basic-configuration:

Basic Configuration
###################
Be sure to toggle ``advanced settings`` on; toggle back and forth to set both.
Unmentioned options are defaults.

Media Management
****************
.. gui::   Lidarr Track Naming
  :path:   Settings --> Media Management --> Track Naming
  :value0: ☑, Rename Tracks
  :value1: ☑, Replace Illegal Characters
  :value2: Standard Track Format, {track:00} - {Track Title}
  :value3: Multi Disc Track Format,
           {Medium Format} {medium:00}/{Artist Name} - {Album Title} - {track:00} - {Track Title}
  :value4: Artist Folder Format, {Artist Name}
  :value5: Album Folder Format, {Album Title}

.. gui::   Lidarr Folders
  :path:   Settings --> Media Management --> Folders
  :value0: Create empty artist folders, ☐
  :value1: Delete empty folders, ☐
  :value2: Import Extra Files, ☐

.. gui::   Lidarr Importing
  :path:   Settings --> Media Management --> Importing
  :value0: Skip Free Space Check, ☐
           Use Hardlinks Instead of Copy, ☐
           Import Extra Files, ☐

.. gui::   Lidarr File Management
  :path:   Settings --> Media Management --> File Management
  :value0: Ignore Delete Tracks, ☐
  :value1: Propers and Repacks, ☑
  :value2: Allow Fingerprinting, ☑
  :value3: Change File Date, {NONE}
  :value4: Recycling Bin, /data/downloads/media-trashed

.. gui::   Lidarr Permissions
  :path:   Settings --> Media Management --> Permissions
  :value0: Set Permissions, ☑
  :value1: File chmod mask, 2660
  :value2: Folder chmod mask, 2770
  :value3: chown User, lidarr (or docker UID)
  :value4: chown Group, media {or docker GID)

Profiles
********
.. gui::    Lidarr Profiles (Any)
  :path:    Settings --> Profiles --> Any
  :value0:  Name; Any
  :value1:  Upgrades Allowed; ☑
  :value2:  Upgrade Until; Unknown
  :value3:  ☑ WAV;
  :value4:  ☑ APE;
  :value5:  ☑ WavPack;
  :value6:  ☑ Lossless; FLAC 24bit, FLAC, ALAC
  :value7:  ☑ High Quality Lossy;
            OGG Vorbis Q10, AAC-320, OGG Vorbis Q9, MP3-320, AAC-VBR, MP3-VBR-V0
  :value8:  ☑ Mid Quality Lossy;
            AAC-256, OGG Vorbis Q8, MP3-256, MP3-VBR-V2, OGG Vorbis Q7
  :value9:  ☑ Low Quality Lossy; MP3-224, WMA, AAC-192, OGG Vorbis Q6, MP3-192
  :value10: ☑ Poor Quality Lossy;
            MP3-160, OGG Vorbis Q5, MP3-128, MP3-112, MP3-96
  :value11: ☑ Trash Quality Lossy;
            MP3-80, MP3-64, MP3-56, MP3-48, MP3-40, MP3-32, MP3-24, MP3-16, MP3-8
  :value12: ☑ Unknown;
  :delim:   ;

.. gui::    Lidarr Profiles (Lossless)
  :path:    Settings --> Profiles --> Lossless
  :value0:  Name; Lossless
  :value1:  Upgrades Allowed; ☑
  :value2:  Upgrade Until; Lossless
  :value3:  ☐ WAV;
  :value4:  ☐ APE;
  :value5:  ☐ WavPack;
  :value6:  ☑ Lossless; FLAC 24bit, FLAC, ALAC
  :value7:  ☐ High Quality Lossy;
  :value8:  ☐ Mid Quality Lossy;
  :value9:  ☐ Low Quality Lossy;
  :value10: ☐ Poor Quality Lossy;
  :value11: ☐ Trash Quality Lossy;
  :value12: ☐ Unknown;
  :delim:   ;

.. gui::    Lidarr Profiles (Standard)
  :path:    Settings --> Profiles --> Standard
  :value0:  Name; Standard
  :value1:  Upgrades Allowed; ☑
  :value2:  Upgrade Until; High Quality Lossy
  :value3:  ☐ WAV;
  :value4:  ☐ APE;
  :value5:  ☐ WavPack;
  :value6:  ☐ Lossless;
  :value7:  ☑ High Quality Lossy;
            OGG Vorbis Q10, AAC-320, OGG Vorbis Q9, MP3-320, AAC-VBR, MP3-VBR-V0
  :value8:  ☑ Mid Quality Lossy;
            AAC-256, OGG Vorbis Q8, MP3-256, MP3-VBR-V2, OGG Vorbis Q7
  :value9:  ☑ Low Quality Lossy; MP3-224, WMA, AAC-192, OGG Vorbis Q6, MP3-192
  :value10: ☐ Poor Quality Lossy;
  :value11: ☐ Trash Quality Lossy;
  :value12: ☐ Unknown;
  :delim:   ;

.. gui::   Lidarr Metadata Profiles (Standard)
  :path:   Settings --> Profiles --> Metadata Profiles --> Standard
  :value0: Name, Standard
  :value1: Primary Types, ☑ Album
  :value2: Secondary Types, ☑ Studio
  :value3: Release Studios, ☑ Official

.. gui::   Lidarr Delay Profiles
  :path:   Settings --> Profiles --> Delay Profiles --> +
  :value0:      Protocol, Usenet
  :value1:  Usenet Delay, 60 minutes
  :value2: Torrent Delay, No Delay
  :value3:          Tags, {NONE}

Quality
*******

+---------+-------+----------+----------+
| Quality | Title | Kbps Min | Kbps Max |
+=========+=======+==========+==========+
| ALL     | ALL   | 0        | 1500     |
+---------+-------+----------+----------+

Indexers
********
.. gui::   Lidarr Indexers
  :path:   Settings --> Indexers --> +
  :value0: Name; {INDEXER NAME}
  :value1: Enable RSS; ☑
  :value2: Enable Automatic Search; ☑
  :value3: Enable Interactive Search; ☑
  :value4: URL; {INDEXER API URI}
  :value5: API Path; /api
  :value6: API Key; {KEY}
  :value7: Categories; 3000,3010,3020,3030,3040
  :value8: Early Download Limit; {NONE}
  :value9: Additional Parameters; {NONE}
  :delim:  ;

.. gui::   Lidarr Options
  :path:   Settings --> Indexers --> Options
  :value0: Minimum Age, 0
  :value1: Minimum Size, 0
  :value2: Retention, 0
  :value3: RSS Sync Interval, 0

Download Clients
****************
.. gui::    Lidarr Download Clients
  :path:    Settings --> Download Clients --> +
  :value0:  Name, {INDEXER NAME}
  :value1:  Enable, ☑
  :value2:  Host, {IP}
  :value3:  Port, 6789
  :value4:  URL Base,
  :value5:  Username, {USER}
  :value6:  Password, {PASS}
  :value7:  Category, music
  :value8:  Recent Priority, Normal
  :value9:  Older Priority, Normal
  :value10: Add Paused, ☐
  :value11: Use SSL, ☑

.. gui::   Lidarr Completed Download Handling
  :path:   Settings --> Download Clients --> Completed Download Handling
  :value0: ☑, {ENABLE}
  :value1: ☑, Remove

.. gui::   Lidarr Failed Download Handing
  :path:   Settings --> Download Clients --> Failed Download Handling
  :value0: ☐, Redownload
  :value1: ☐, Remove

General
*******
.. gui::   Lidarr General Host
  :path:   Settings --> General --> Host
  :value0: Bind Address, *
  :value1: Port Number, 8686
  :value2: URL Base,
  :value3: Enable SSL, ☐

.. gui::   Lidarr General Security
  :path:   Settings --> General --> Security
  :value0: Authentication, {NONE}
  :value1: API Key, {KEY}

.. gui::   Lidarr General Proxy
  :path:   Settings --> General --> Proxy
  :value0: Use Proxy, ☐

.. gui::   Lidarr General Logging
  :path:   Settings --> General --> Logging
  :value0: Log Level, {INFO}

.. gui::   Lidarr General Analytics
  :path:   Settings --> General --> Analytics
  :value0: Send Anonymous Usage Data, ☐

.. gui::   Lidarr General Backups
  :path:   Settings --> General --> Backups
  :value0: Folder, Backups
  :value1: Interval, 7
  :value2: Retention, 28

UI
**
.. gui::   Lidarr UI
  :path:   Settings --> UI --> Calendar
  :value0: First Day of Week, Sunday
  :value1: Week Column Header, Tue 3/25

.. gui::   Lidarr UI Dates
  :path:   Settings --> UI --> Dates
  :value0: Short Date Format, YYYY-MM-DD
  :value1: Long Date Format, Tuesday March 25 2014
  :value2: Time Format, 17:00/17:30
  :value3: Show Relative Dates, ☐

.. gui::   Lidarr UI Style
  :path:   Settings --> UI --> Style
  :value0: Enable Color-Impaired mode, ☐
  :value1: Expand Items by Default, ☐ (All)
