.. _service-radarr-basic-configuration:

Basic Configuration
###################
Be sure to toggle ``advanced settings`` on; toggle back and forth to set both.
Unmentioned options are defaults.

Media Management
****************
.. ggui:: Radarr Track Naming
  :key_title: Settings --> Media Managment --> Movie Naming
  :option:  Rename Episodes,
            Replace Illegal Characters,
            Colon Replacement Format,
            Standard Movie Format,
            Movie Folder Format
  :setting: Yes,
            Yes,
            Delete,
            {Movie TitleThe} ({Release Year}){ - Edition Tags},
            {Movie TitleThe} ({Release Year})
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: Radarr Folders
  :key_title: Settings --> Media Managment --> Folders
  :option:  Create empty movie folders,
            Automatically Rename Folders,
            Movie Paths Default to Static
  :setting: No,
            Yes,
            Yes
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: Radarr Importing
  :key_title: Settings --> Media Managment --> Importing
  :option:  Skip Free Space Check,
            Use Hardlinks Instead of Copy,
            Import Extra Files
  :setting: No,
            No,
            No
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: Radarr File Management
  :key_title: Settings --> Media Managment --> File Management
  :option:  Unmonitor Deleted Movies,
            Download Propers,
            Analyse video files,
            Change File Date,
            Recycling Bin
  :setting: No,
            Yes,
            Yes,
            None,
            /data/downloads/media-trashed
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: Radarr Permissions
  :key_title: Settings --> Media Managment --> Permissions
  :option:  Set Permissions,
            File chmod mask,
            Folder chmod mask,
            chown User,
            chown Group
  :setting: Yes,
            2660,
            2770,
            lidarr {OR DOCKER UID},
            media {OR DOCKER GID}
  :no_section:
  :no_caption:
  :no_launch:

Profiles
********
.. ggui:: Radarr Profiles (Any)
  :key_title: Settings --> Profiles --> Any
  :option:  Name,
            Language,
            Preferred Tags,
            Cutoff,
            Custom Format Cutoff,
            Qualities,
            ›,
            ›,
            ›,
            ›,
            ›,
            ›,
            ›,
            ›,
            ›,
            ›,
            ›,
            ›,
            ›,
            ›,
            ›,
            ›,
            ›,
            ›,
            ›,
            ›,
            ›,
            ›,
            ›,
            ›,
            ›,
            ›,
            Custom Formats
  :setting: Any,
            English,
            ,
            Bluray-480p,
            None,
            ,
            ☐ Raw HD,
            ☑ BR-DISK,
            ☑ Remux-2160p,
            ☑ Bluray-2160p,
            ☑ WEBDL-2160p,
            ☑ HDTV-2160p,
            ☑ Remux-1080p,
            ☑ Bluray-1080p,
            ☑ WEBDL-1080p,
            ☑ HDTV-1080p,
            ☑ Bluray-720p,
            ☑ WEBDL-720p,
            ☑ HDTV-720p,
            ☑ Bluray-576p,
            ☑ Bluray-480p,
            ☑ WEBDL-480p,
            ☑ DVD-R,
            ☑ DVD,
            ☑ SDTV,
            ☑ DVDSCR,
            ☑ REGIONAL,
            ☑ TELECINE,
            ☑ TELESYNC,
            ☑ CAM,
            ☑ WORKPRINT,
            ☐ Unknown,
            ☑ None
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: Radarr Profiles (SD)
  :key_title: Settings --> Profiles --> SD
  :option:  Name,
            Language,
            Preferred Tags,
            Cutoff,
            Custom Format Cutoff,
            Qualities,
            ›,
            ›,
            ›,
            ›,
            ›,
            ›,
            ›,
            ›,
            ›,
            ›,
            ›,
            Custom Formats
  :setting: SD,
            English,
            ,
            Bluray-480p,
            None,
            ,
            ☑ Bluray-576p,
            ☑ Bluray-480p,
            ☑ WEBDL-480p,
            ☑ DVD,
            ☑ SDTV,
            ☑ DVDSCR,
            ☑ REGIONAL,
            ☑ TELECINE,
            ☑ TELESYNC,
            ☑ CAM,
            ☑ WORKPRINT,
            ☑ None
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: Radarr Profiles (HD-720p)
  :key_title: Settings --> Profiles --> HD-720p
  :option:  Name,
            Language,
            Preferred Tags,
            Cutoff,
            Custom Format Cutoff,
            Qualities,
            ›,
            ›,
            ›,
            Custom Formats
  :setting: HD-720p,
            English,
            ,
            Bluray-720p,
            None,
            ,
            ☑ Bluray-720p,
            ☑ WEBDL-720p,
            ☑ HDTV-720p,
            ☑ None
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: Radarr Profiles (HD-1080p)
  :key_title: Settings --> Profiles --> HD-1080p
  :option:  Name,
            Language,
            Preferred Tags,
            Cutoff,
            Custom Format Cutoff,
            Qualities,
            ›,
            ›,
            ›,
            ›,
            Custom Formats
  :setting: HD-1080p,
            English,
            ,
            Bluray-480p,
            None,
            ,
            ☑ Remux-1080p,
            ☑ Bluray-1080p,
            ☑ WEBDL-1080p,
            ☑ HDTV-1080p,
            ☑ None
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: Radarr Profiles (Ultra-HD)
  :key_title: Settings --> Profiles --> Ultra-HD
  :option:  Name,
            Language,
            Preferred Tags,
            Cutoff,
            Custom Format Cutoff,
            Qualities,
            ›,
            ›,
            ›,
            ›,
            Custom Formats
  :setting: Ultra-HD,
            English,
            ,
            Remux-2160p,
            None,
            ,
            ☑ Remux-2160p,
            ☑ Bluray-2160p,
            ☑ WEBDL-2160p,
            ☑ HDTV-2160p,
            ☑ None
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: Radarr Profiles (HD - 720p/1080p)
  :key_title: Settings --> Profiles --> HD - 720p/1080p
  :option:  Name,
            Language,
            Preferred Tags,
            Cutoff,
            Custom Format Cutoff,
            Qualities,
            ›,
            ›,
            ›,
            ›,
            ›,
            ›,
            ›,
            ›,
            Custom Formats
  :setting: HD - 720p/1080p,
            English,
            ,
            Bluray-720p,
            None,
            ,
            ☑ Remux-2160p,
            ☑ Remux-1080p,
            ☑ Bluray-1080p,
            ☑ WEBDL-1080p,
            ☑ HDTV-1080p,
            ☑ Bluray-720p,
            ☑ WEBDL-720p,
            ☑ HDTV-720p,
            ☑ None
  :no_section:
  :no_caption:
  :no_launch:

.. gtable:: Radarr Delay Profiles
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
.. gtable:: Radarr Quality
  :header: Quality,
           Title,
           GB Low Min,
           GB High Min,
           GB Low Max,
           GB High Max
  :c0:     {<= WEBDL-1080p},
           {> WEBDL-1080p}
  :c1:     ALL,
           ALL
  :c2:     0,
           0
  :c3:     0,
           0
  :c4:     8.79GB,
           Unlimited
  :c5:     13.67GB,
           Unlimited
  :no_key_title:
  :no_section:
  :no_caption:
  :no_launch:

Indexers
********
.. ggui:: Radarr Indexers
  :key_title: Settings --> Indexers --> +
  :option:  Name;
            Enable RSS;
            Enable Search;
            URL;
            Multi Languages;
            API Key;
            Categories;
            Anime Categories;
            Additional Parameters;
            Remove year from search string;
            Search by Title
  :setting: {INDEXER NAME};
            Yes;
            Yes;
            {INDEXER API URI};
            ;
            {INDEXER API KEY};
            2000,2010,2020,2030,2035,2040,2045,2050,2060;
            ;
            ;
            No;
            No
  :no_section:
  :no_caption:
  :no_launch:
  :delim: ;

.. ggui:: Radarr Options
  :key_title: Settings --> Indexers --> Options
  :option:  Minimum Age,
            Retention,
            Maximum Size,
            Prefer Special Indexer Flags,
            RSS Sync Interval,
            Whiteliste Subtitle Tags,
            Allow Hardcoded Subs,
            Parser Leniency
  :setting: 0,
            0,
            0,
            No,
            0,
            ,
            No,
            Strict
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: Radarr Availability Options
  :key_title: Settings --> Indexers --> Availability Options
  :option:  Availability Delay
  :setting: 0
  :no_section:
  :no_caption:
  :no_launch:

Download Clients
****************
.. ggui:: Radarr Download Client
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
            Use SSL,
            Add Paused
  :setting: {INDEXER NAME},
            Yes,
            {NZBGET IP},
            {NZBGET PORT},
            ,
            {API USERNAME},
            {API PASSWORD},
            movies,
            Normal,
            Normal,
            Yes,
            No
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: Radarr Completed Download Handling
  :key_title: Settings --> Download Client --> Completed Download Handling
  :option:  Enable,
            Remove,
            Check For Finished Downloads Interval
  :setting: Yes,
            Yes,
            1
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: Radarr Failed Download Handing
  :key_title: Settings --> Download Client --> Failed Download Handling
  :option:  Redownload
  :setting: No
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: Radarr Drone Factory Options
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
.. ggui:: Radarr Connect
  :key_title: Settings --> Connect --> Connections --> +
  :option:  Name,
            On Grab,
            On Download,
            On Upgrade,
            On Rename,
            Filter Movie Tags,
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
.. ggui:: Radarr General Host
  :key_title: Settings --> General --> Start-Up
  :option:  Bind Address,
            Port Number,
            URL Base,
            Enable SSL,
            Open browser on start
  :setting: *,
            7878,
            ,
            No,
            No
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: Radarr General Security
  :key_title: Settings --> General --> Security
  :option:  Authentication,
            API Key
  :setting: None,
            {GENERATE API KEY}
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: Radarr General Proxy
  :key_title: Settings --> General --> Proxy
  :option:  Use Proxy
  :setting: No
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: Radarr General Logging
  :key_title: Settings --> General --> Logging
  :option:  Log Level
  :setting: info
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: Radarr General Analytics
  :key_title: Settings --> General --> Analytics
  :option:  Enable
  :setting: No
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: Radarr General Updates
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
.. ggui:: Radarr UI Movies
  :key_title: Settings --> UI --> Movies
  :option:  Page Size
  :setting: 250
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: Radarr UI Calendar
  :key_title: Settings --> UI --> Calendar
  :option:  First Day of Week,
            Week Column Header
  :setting: Sunday,
            Tue 3/25
  :no_section:
  :no_caption:
  :no_launch:

.. ggui:: Radarr UI Dates
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

.. ggui:: Radarr UI Style
  :key_title: Settings --> UI --> Style
  :option:  Enable Color-Impaired mode
  :setting: No
  :no_section:
  :no_caption:
  :no_launch: