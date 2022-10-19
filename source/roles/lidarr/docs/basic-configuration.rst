.. _service-lidarr-basic-configuration:

Basic Configuration
###################
Be sure to toggle ``advanced settings`` on; toggle back and forth to set both.
Unmentioned options are defaults.

Media Management
****************
.. gui::   Track Naming
  :path:   Settings --> Media Management --> Track Naming
  :value0: Rename Tracks, ☑
  :value1: Replace Illegal Characters, ☑
  :value2: Standard Track Format, {Album Title}/{track:00} - {Track Title}
  :value3: Multi Disc Track Format,  
           {Album Title}/{Medium Format} {medium:00}/{track:00} - {Track Title}
  :value4: Artist Folder Format, {Artist NameThe}

.. gui::   Folders
  :path:   Settings --> Media Management --> Folders
  :value0: Create empty artist folders, ☐
  :value1: Delete empty folders, ☐

.. gui::   Importing
  :path:   Settings --> Media Management --> Importing
  :value0: Skip Free Space Check, ☐
  :value1: Minimum Free Space, 100MB
  :value2: Use Hardlinks Instead of Copy, ☐
  :value3: Import Extra Files, ☐

.. gui::   File Management
  :path:   Settings --> Media Management --> File Management
  :value0: Propers and Repacks, Prefer and Upgrade
  :value1: Watch Root Folders for file changes, ☑
  :value2: Rescan Artist Folder after Refresh, Always
  :value3: Allow Fingerprinting, For new imports only
  :value4: Change File Date, None
  :value5: Recycling Bin, /data/downloads/media-trashed
  :value6: Recycle Bin Cleanup, 7

.. gui::   Permissions
  :path:   Settings --> Media Management --> Permissions
  :value0: Set Permissions, ☑
  :value1: Folder chmod mask, 775
  :value2: chown Group, media

Profiles
********
.. gui::    Profiles (Any, upgrade: lossless)
  :path:    Settings --> Profiles --> Any
  :value0:  Name; Any, upgrade: lossless
  :value1:  Upgrades Allowed; ☑
  :value2:  Upgrade Until; Lossless
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

.. gui::    Metadata Profiles (All)
  :path:    Settings --> Profiles --> Metadata Profiles --> Standard
  :value0:  Name, All
  :value1:  Primary Types, ☑ Album
  :value2:  ›, ☑ Broadcast
  :value3:  ›, ☑ EP
  :value4:  ›, ☑ Other
  :value5:  ›, ☑ Single
  :value6:  Secondary Types, ☑ Studio
  :value7:  ›, ☑ Spokenword
  :value8:  ›, ☑ Soundtrack
  :value9:  ›, ☑ Remix
  :value10: ›, ☑ Mixtape/Street
  :value11: ›, ☑ Live
  :value12: ›, ☑ Interview
  :value13: ›, ☑ DJ-mix
  :value14: ›, ☑ Compilation
  :value15: Release Statuses, ☑ Pseudo-Release
  :value16: ›, ☑ Promotion
  :value17: ›, ☑ Official
  :value18: ›, ☑ Bootleg

.. gui::   Delay Profiles
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
.. gui::    Indexers
  :path:    Settings --> Indexers --> +
  :value0:  Name; {INDEXER NAME}
  :value1:  Enable RSS; ☑
  :value2:  Enable Automatic Search; ☑
  :value3:  Enable Interactive Search; ☑
  :value4:  URL; {INDEXER API URI}
  :value5:  API Path; /api
  :value6:  API Key; {KEY}
  :value7:  Categories; ☑ (All)
  :value8:  Early Download Limit; {NONE}
  :value9:  Additional Parameters; {NONE}
  :value10: Indexer Priority; 25
  :delim:   ;

.. gui::   Options
  :path:   Settings --> Indexers --> Options
  :value0: Minimum Age, 0
  :value1: Minimum Size, 0
  :value2: Retention, 0
  :value3: RSS Sync Interval, 0

Download Clients
****************
.. gui::    Download Clients
  :path:    Settings --> Download Clients --> +
  :value0:  Name, {INDEXER NAME}
  :value1:  Enable, ☑
  :value2:  Host, {IP}
  :value3:  Port, 6789
  :value4:  Use SSL, ☐
  :value5:  URL Base, {NONE}
  :value6:  Username, {USER}
  :value7:  Password, {PASS}
  :value8:  Category, music
  :value9:  Recent Priority, Normal
  :value10: Older Priority, Normal
  :value11: Add Paused, ☐
  :value12: Client Priority, 1
  :value13: Remove Completed, ☑
  :value14: Remove Failed, ☐

.. gui::   Completed Download Handling
  :path:   Settings --> Download Clients --> Completed Download Handling
  :value0: Enable, ☑

.. gui::   Failed Download Handing
  :path:   Settings --> Download Clients --> Failed Download Handling
  :value0: Redownload, ☐

Metadata
********
.. gui::   Metadata Provider Source
  :path:   Settings --> General --> Metadata Provider Source
  :value0: Metadata Source, {NONE}

.. gui::   Write Metadata to Audio Files
  :path:   Settings --> General --> Write Metadata to Audio Files
  :value0: Tag Audio Files with Metadata, For new downloads only
  :value1: Scrub Existing Tags, ☐

General
*******
.. gui::   Host
  :path:   Settings --> General --> Host
  :value0: Bind Address, *
  :value1: Port Number, 8686
  :value2: URL Base,  
  :value3: Instance Name, Lidarr
  :value4: Enable SSL, ☐

.. gui::   Security
  :path:   Settings --> General --> Security
  :value0: Authentication, {NONE}
  :value1: API Key, {KEY}
  :value2: Certificate Validation, Disabled

.. gui::   Proxy
  :path:   Settings --> General --> Proxy
  :value0: Use Proxy, ☐

.. gui::   Logging
  :path:   Settings --> General --> Logging
  :value0: Log Level, {INFO}

.. gui::   Analytics
  :path:   Settings --> General --> Analytics
  :value0: Send Anonymous Usage Data, ☐

.. gui::   Updates
  :path:   Settings --> General --> Updates
  :value0: Branch, master
  :value1: Automatic, ☑
  :value2: Mechanism, Built-in

.. gui::   Backups
  :path:   Settings --> General --> Backups
  :value0: Folder, Backups
  :value1: Interval, 7
  :value2: Retention, 28

UI
**
.. gui::   Calendar
  :path:   Settings --> UI --> Calendar
  :value0: First Day of Week, Sunday
  :value1: Week Column Header, Tue 3/25

.. gui::   Dates
  :path:   Settings --> UI --> Dates
  :value0: Short Date Format, YYYY-MM-DD
  :value1: Long Date Format, Tuesday March 25 2014
  :value2: Time Format, 17:00/17:30
  :value3: Show Relative Dates, ☐

.. gui::   Style
  :path:   Settings --> UI --> Style
  :value0: Enable Color-Impaired mode, ☐
  :value1: Expand Items by Default, ☐ (All)

.. gui::   Language
  :path:   Settings --> UI --> Language
  :value0: UI Language, English