.. _service-lidarr-basic-configuration:

Basic Configuration
###################
Be sure to toggle ``advanced settings`` on; toggle back and forth to set both.
Unmentioned options are defaults.

Media Management
****************
.. ggui:: Lidarr Track Naming
  :key_title: Settings --> Media Managment --> Track Naming
  :option:  ☑,
            ☑,
            Standard Track Format,
            Multi Disc Track Format,
            Artist Folder Format,
            Album Folder Format
  :setting: Rename Tracks,
            Replace Illegal Characters,
            {track:00} - {Track Title},
            {Medium Format} {medium:00}/{Artist Name} - {Album Title} - {track:00} - {Track Title},
            {Artist Name},
            {Album Title}
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: Lidarr Folders
  :key_title: Settings --> Media Managment --> Folders
  :option:  Create empty artist folders,
            Delete empty folders,
            Import Extra Files
  :setting: ☐,
            ☐,
            ☐
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: Lidarr Importing
  :key_title: Settings --> Media Managment --> Importing
  :option:  Skip Free Space Check,
            Use Hardlinks Instead of Copy,
            Import Extra Files
  :setting: ☐,
            ☐,
            ☐
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: Lidarr File Management
  :key_title: Settings --> Media Managment --> File Management
  :option:  Ignore Delete Tracks,
            Propers and Repacks,
            Allow Fingerprinting,
            Change File Date,
            Recycling Bin
  :setting: ☐,
            ☑,
            ☑,
            None,
            /data/downloads/media-trashed
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: Lidarr Permissions
  :key_title: Settings --> Media Managment --> Permissions
  :option:  Set Permissions,
            File chmod mask,
            Folder chmod mask,
            chown User,
            chown Group
  :setting: ☑,
            2660,
            2770,
            lidarr {OR DOCKER UID},
            media {OR DOCKER GID}
  :no_section:
  :no_caption:
  :no_launch:

Profiles
********
.. ggui:: Lidarr Profiles (Any)
  :key_title: Settings --> Profiles --> Any
  :option:  Name;
            Upgrades Allowed;
            Upgrade Until;
            ☑ WAV;
            ☑ APE;
            ☑ WavPack;
            ☑ Lossless;
            ☑ High Quality Lossy;
            ☑ Mid Quality Lossy;
            ☑ Low Quality Lossy;
            ☑ Poor Quality Lossy;
            ☑ Trash Quality Lossy;
            ☑ Unknown;
  :setting: Any;
            ☑;
            Unknown;
            ;
            ;
            ;
            FLAC 24bit, FLAC, ALAC;
            OGG Vorbis Q10, AAC-320, OGG Vorbis Q9, MP3-320, AAC-VBR, MP3-VBR-V0;
            AAC-256, OGG Vorbis Q8, MP3-256, MP3-VBR-V2, OGG Vorbis Q7;
            MP3-224, WMA, AAC-192, OGG Vorbis Q6, MP3-192;
            MP3-160, OGG Vorbis Q5, MP3-128, MP3-112, MP3-96;
            MP3-80, MP3-64, MP3-56, MP3-48, MP3-40, MP3-32, MP3-24, MP3-16, MP3-8;
            ;
  :delim: ;
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: Lidarr Profiles (Lossless)
  :key_title: Settings --> Profiles --> Lossless
  :option:  Name;
            Upgrades Allowed;
            Upgrade Until;
            ☐ WAV;
            ☐ APE;
            ☐ WavPack;
            ☑ Lossless;
            ☐ High Quality Lossy;
            ☐ Mid Quality Lossy;
            ☐ Low Quality Lossy;
            ☐ Poor Quality Lossy;
            ☐ Trash Quality Lossy;
            ☐ Unknown;
  :setting: Lossless;
            ☑;
            Lossless;
            ;
            ;
            ;
            FLAC 24bit, FLAC, ALAC;
            ;
            ;
            ;
            ;
            ;
            ;
  :delim: ;
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: Lidarr Profiles (Standard)
  :key_title: Settings --> Profiles --> Standard
  :option:  Name;
            Upgrades Allowed;
            Upgrade Until;
            ☐ WAV;
            ☐ APE;
            ☐ WavPack;
            ☐ Lossless;
            ☑ High Quality Lossy;
            ☑ Mid Quality Lossy;
            ☑ Low Quality Lossy;
            ☐ Poor Quality Lossy;
            ☐ Trash Quality Lossy;
            ☐ Unknown;
  :setting: Standard;
            ☑;
            High Quality Lossy;
            ;
            ;
            ;
            ;
            OGG Vorbis Q10, AAC-320, OGG Vorbis Q9, MP3-320, AAC-VBR, MP3-VBR-V0;
            AAC-256, OGG Vorbis Q8, MP3-256, MP3-VBR-V2, OGG Vorbis Q7;
            MP3-224, WMA, AAC-192, OGG Vorbis Q6, MP3-192;
            ;
            ;
            ;
  :delim: ;
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: Lidarr Metadata Profiles (Standard)
  :key_title: Settings --> Profiles --> Metadata Profiles --> Standard
  :option:  Name,
            Primary Types,
            Secondary Types,
            Release Studios
  :setting: Standard,
            ☑ Album,
            ☑ Studio,
            ☑ Official
  :no_section:
  :no_caption:
  :no_launch:

.. gtable:: Delay Profiles
  :key_title: Settings --> Profiles --> Delay Profiles --> +
  :header: Protocol,
           Usenet Delay,
           Torrent Delay,
           Tags
  :c0:     Usenet,
           60 minutes,
           No Delay,
           None
  :no_section:
  :no_caption:
  :no_launch:

Quality
*******
.. gtable:: Quality
  :header: Quality,
           Title,
           Kbps Min,
           Kbps Max
  :c0:     ALL
  :c1:     ALL
  :c2:     0
  :c3:     1500
  :no_key_title:
  :no_section:
  :no_caption:
  :no_launch:

Indexers
********
.. ggui:: Indexers
  :key_title: Settings --> Indexers --> +
  :option:  Name;
            Enable RSS;
            Enable Automatic Search;
            Enable Interactive Search;
            URL;
            API Path;
            API Key;
            Categories;
            Easrly Download Limit;
            Additional Parameters
  :setting: {INDEXER NAME};
            ☑;
            ☑;
            ☑;
            {INDEXER API URI};
            /api;
            {INDEXER API KEY};
            3000,3010,3020,3030,3040;
            None;
            None
  :no_section:
  :no_caption:
  :no_launch:
  :delim: ;

.. ggui:: Options
  :key_title: Settings --> Indexers --> Options
  :option:  Minimum Age,
            Minimum Size,
            Retention,
            RSS Sync Interval
  :setting: 0,
            0,
            0,
            0
  :no_section:
  :no_caption:
  :no_launch:

Download Clients
****************
.. ggui:: Download Clients
  :key_title: Settings --> Download Clients --> +
  :option:  Name,
            Enable,
            Host,
            Port,
            URL Base,
            Username,
            Password,
            Category,
            Recent Priority,
            Older Priority,
            Add Paused,
            Use SSL
  :setting: {INDEXER NAME},
            ☑,
            {NZBGET IP},
            {NZBGET PORT},
            ,
            {API USERNAME},
            {API PASSWORD},
            music,
            Normal,
            Normal,
            ☐,
            ☑
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: Completed Download Handling
  :key_title: Settings --> Download Clients --> Completed Download Handling
  :option:  ☑,
            ☑
  :setting: Enable,
            Remove
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: Failed Download Handing
  :key_title: Settings --> Download Clients --> Failed Download Handling
  :option:  ☐,
            ☐
  :setting: Redownload,
            Remove
  :no_section:
  :no_caption:
  :no_launch:

General
*******
.. ggui:: General Gost
  :key_title: Settings --> General --> Host
  :option:  Bind Address,
            Port Number,
            URL Base,
            Enable SSL
  :setting: *,
            8686,
            ,
            ☐
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: General Security
  :key_title: Settings --> General --> Security
  :option:  Authentication,
            API Key
  :setting: None,
            {GENERATE API KEY}
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: General Proxy
  :key_title: Settings --> General --> Proxy
  :option:  Use Proxy
  :setting: ☐
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: General Logging
  :key_title: Settings --> General --> Logging
  :option:  Log Level
  :setting: info
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: General Analytics
  :key_title: Settings --> General --> Analytics
  :option:  Send Anonymous Usage Data
  :setting: ☐
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: General Backups
  :key_title: Settings --> General --> Backups
  :option:  Folder,
            Interval,
            Retention
  :setting: Backups,
            7,
            28
  :no_section:
  :no_caption:
  :no_launch:

UI
**
.. ggui:: UI
  :key_title: Settings --> UI --> Calendar
  :option:  First Day of Week,
            Week Column Header
  :setting: Sunday,
            Tue 3/25
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: UI Dates
  :key_title: Settings --> UI --> Dates
  :option:  Short Date Format,
            Long Date Format,
            Time Format,
            Show Relative Dates
  :setting: YYYY-MM-DD,
            Tuesday March 25 2014,
            17:00/17:30,
            ☐
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: UI Style
  :key_title: Settings --> UI --> Style
  :option:  Enable Color-Impaired mode,
            Expand Items by Default
  :setting: ☐,
            ☐ (All)
  :no_section:
  :no_caption:
  :no_launch: