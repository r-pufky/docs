.. _service-sonarr-basic-configuration:

Basic Configuration
###################
Be sure to toggle ``advanced settings`` on; toggle back and forth to set both.
Unmentioned options are defaults.

Media Management
****************
.. ggui:: Sonarr Episode Naming
  :key_title: Settings --> Media Management --> Episode Naming
  :option:  Rename Episodes,
            Include Series Title,
            Include Episode Title,
            Include Quality,
            Replace Spaces,
            Separator,
            Numbering Style,
            Season Folder Format,
            Multi-Episode Style,
            Single Episode Example,
            Multi-Episode Example,
            Daily-Episode Example,
            Anime Episode Example,
            Anime Multi-Episode Example,
            Series Folder Example,
            Season Folder Example
  :setting: Yes,
            Yes,
            Yes,
            No,
            No,
            Dash,
            S01E05,
            Season {season:00},
            Prefixed Range,
            The Series Title (2010) - S01E01 - Episode Title (1),
            The Series Title (2010) - S01E01-E03 - Episode Title,
            The Series Title (2010) - 2013-10-30 - Episode Title (1),
            The Series Title (2010) - S01E01 - Episode Title (1),
            The Series Title (2010) - S01E01-E03 - Episode Title,
            The Series Title (2010),
            Season 01
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: Sonarr Folders
  :key_title: Settings --> Media Management --> Folders
  :option:  Create empty series folders,
            Delete empty folders
  :setting: No,
            No
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: Sonarr Importing
  :key_title: Settings --> Media Management --> Importing
  :option:  Skip Free Space Check,
            Use Hardlinks Instead of Copy,
            Import Extra Files
  :setting: No,
            No,
            No
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: Sonarr File Management
  :key_title: Settings --> Media Management --> File Management
  :option:  Ignore Delete Episodes,
            Download Propers,
            Analyse video files,
            Change File Date,
            Recycling Bin
  :setting: No,
            Yes,
            Yes,
            None,
            /data/downloads/sonarr-recycle/
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: Sonarr Permissions
  :key_title: Settings --> Media Management --> Permissions
  :option:  Set Permissions,
            File chmod mask,
            Folder chmod mask,
            chown User,
            chown Group
  :setting: Yes,
            2660,
            2770,
            sonarr {OR DOCKER UID},
            media {OR DOCKER GID}
  :no_section:
  :no_caption:
  :no_launch:

Profiles
********
.. ggui:: Sonarr Profiles (Any)
  :key_title: Settings --> Profiles --> Any
  :option:  Name,
            Language,
            Cutoff,
            Qualities,
            ›,
            ›,
            ›,
            ›,
            ›,
            ›,
            ›,
            ›,
            ›
  :setting: Any,
            English,
            SDTV,
            ,
            ☑ HDTV-720p,
            ☑ WEBDL-720p,
            ☑ Bluray-720p,
            ☑ HDTV-1080p,
            ☑ WEBDL-1080p,
            ☑ Bluray-1080p,
            ☑ DVD,
            ☑ WEBDL-480p,
            ☑ SDTV
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: Sonarr Profiles (SD)
  :key_title: Settings --> Profiles --> SD
  :option:  Name,
            Language,
            Cutoff,
            Qualities,
            ›,
            ›,
            ›
  :setting: SD,
            English,
            SDTV,
            ,
            ☑ DVD,
            ☑ WEBDL-480p,
            ☑ SDTV
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: Sonarr Profiles (HD-720p)
  :key_title: Settings --> Profiles --> HD-720p
  :option:  Name,
            Language,
            Cutoff,
            Qualities,
            ›,
            ›,
            ›
  :setting: HD-720p,
            English,
            SDTV,
            ,
            ☑ HDTV-720p,
            ☑ WEBDL-720p,
            ☑ Bluray-720p
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: Sonarr Profiles (HD-1080p)
  :key_title: Settings --> Profiles --> HD-1080p
  :option:  Name,
            Language,
            Cutoff,
            Qualities,
            ›,
            ›,
            ›
  :setting: HD-1080p,
            English,
            HD-1080p,
            ,
            ☑ HDTV-1080p,
            ☑ WEBDL-1080p,
            ☑ Bluray-1080p
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: Sonarr Profiles (All)
  :key_title: Settings --> Profiles --> All
  :option:  Name,
            Language,
            Cutoff,
            Qualities,
            ›,
            ›,
            ›,
            ›,
            ›,
            ›
  :setting: All,
            English,
            HD-720p,
            ,
            ☑ HDTV-720p,
            ☑ WEBDL-720p,
            ☑ Bluray-720p,
            ☑ HDTV-1080p,
            ☑ WEBDL-1080p,
            ☑ Bluray-1080p
  :no_section:
  :no_caption:
  :no_launch:

.. gtable:: Sonarr Delay Profiles
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
.. gtable:: Sonarr Quality
  :header: Quality,
           Title,
           GB Low Min,
           GB High Min,
           GB Low Max,
           GB High Max
  :c0:     All,
           Raw-HD,
           HDTV-2160p,
           WEBDL-2160p,
           Bluray-2160p
  :c1:     ALL,
           Raw-HD,
           HDTV-2160p,
           WEBDL-2160p,
           Bluray-2160p
  :c2:     0,
           0,
           0,
           0,
           0
  :c3:     0,
           0,
           0,
           0,
           0
  :c4:     2.93GB,
           Unlimited,
           Unlimited,
           Unlimited,
           Unlimited
  :c5:     5.86GB,
           Unlimited,
           Unlimited,
           Unlimited,
           Unlimited
  :no_key_title:
  :no_section:
  :no_caption:
  :no_launch:

Indexers
********
.. ggui:: Sonarr Indexers
  :key_title: Settings --> Indexers --> +
  :option:  Name;
            Enable RSS;
            Enable Search;
            URL;
            API Path;
            API Key;
            Categories;
            Anime Categories;
            Additional Parameters
  :setting: {INDEXER NAME};
            Yes;
            Yes;
            {INDEXER API URI};
            /api;
            {INDEXER API KEY};
            5030,5040;
            ;
            None
  :no_section:
  :no_caption:
  :no_launch:
  :delim: ;

.. ggui:: Sonarr Options
  :key_title: Settings --> Indexers --> Options
  :option:  Minimum Age,
            Retention,
            Maximum Size,
            RSS Sync Interval
  :setting: 0,
            0,
            0,
            15
  :no_section:
  :no_caption:
  :no_launch:

Download Client
***************
.. ggui:: Sonarr Download Client
  :key_title: Settings --> Download Client --> +
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
            Yes,
            {NZBGET IP},
            {NZBGET PORT},
            ,
            {API USERNAME},
            {API PASSWORD},
            tv,
            Normal,
            Normal,
            No,
            Yes
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: Sonarr Completed Download Handling
  :key_title: Settings --> Download Client --> Completed Download Handling
  :option:  Enable,
            Remove
  :setting: Yes,
            Yes
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: Sonarr Failed Download Handing
  :key_title: Settings --> Download Client --> Failed Download Handling
  :option:  Redownload
  :setting: No
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: Sonarr Drone Factory Options
  :key_title: Settings --> Download Client --> Drone Factory Options
  :option:  Drone Factory,
            Drone Factory Interval
  :setting: ,
            0
  :no_section:
  :no_caption:
  :no_launch:

Connect
*******
.. ggui:: Sonarr Connect
  :key_title: Settings --> Connect --> Connections --> +
  :option:  Name,
            On Grab,
            On Download,
            On Upgrade,
            On Rename,
            Filter Series Tags,
            Host,
            Port,
            Username,
            Password,
            Update Library,
            Use SSL
  :setting: Plex Server,
            No,
            Yes,
            Yes,
            Yes,
            ,
            {PLEX IP},
            {PLEX PORT},
            {PLEX USERNAME},
            {PLEX PASSWORD},
            No,
            Yes
  :no_section:
  :no_caption:
  :no_launch:

General
*******
.. ggui:: Sonarr General Host
  :key_title: Settings --> General --> Start-Up
  :option:  Bind Address,
            Port Number,
            URL Base,
            Enable SSL,
            Open browser on start
  :setting: *,
            8989,
            ,
            No,
            No
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: Sonarr General Security
  :key_title: Settings --> General --> Security
  :option:  Authentication,
            API Key
  :setting: None,
            {GENERATE API KEY}
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: Sonarr General Proxy
  :key_title: Settings --> General --> Proxy
  :option:  Use Proxy
  :setting: No
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: Sonarr General Logging
  :key_title: Settings --> General --> Logging
  :option:  Log Level
  :setting: info
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: Sonarr General Analytics
  :key_title: Settings --> General --> Analytics
  :option:  Enable
  :setting: No
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: Sonarr General Updates
  :key_title: Settings --> General --> Updates
  :option:  Branch,
            Automatic,
            Mechanism
  :setting: master,
            On,
            Built-in
  :no_section:
  :no_caption:
  :no_launch:

UI
**
.. ggui:: Sonarr UI Calendar
  :key_title: Settings --> UI --> Calendar
  :option:  First Day of Week,
            Week Column Header
  :setting: Sunday,
            Tue 3/25
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: Sonarr UI Dates
  :key_title: Settings --> UI --> Dates
  :option:  Short Date Format,
            Long Date Format,
            Time Format,
            Show Relative Dates
  :setting: YYYY-MM-DD,
            Tuesday March 25 2014,
            17:00/17:30,
            No
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: Sonarr UI Style
  :key_title: Settings --> UI --> Style
  :option:  Enable Color-Impaired mode
  :setting: No
  :no_section:
  :no_caption:
  :no_launch: