.. _service-sonarr-basic-configuration:

Basic Configuration
###################
Be sure to toggle ``advanced settings`` on; toggle back and forth to set both.
Unmentioned options are defaults.

Media Management
****************
.. gui::    Sonarr Episode Naming
  :path:    Settings --> Media Management --> Episode Naming
  :value0:  Rename Episodes, {YES}
  :value1:  Include Series Title, {YES}
  :value2:  Include Episode Title, {YES}
  :value3:  Include Quality, {NO}
  :value4:  Replace Spaces, {NO}
  :value5:  Separator, Dash
  :value6:  Numbering Style, S01E05
  :value7:  Season Folder Format, Season {season:00}
  :value8:  Multi-Episode Style, Prefixed Range
  :value9:  Single Episode Example,
            The Series Title (2010) - S01E01 - Episode Title (1)
  :value10: Multi-Episode Example,
            The Series Title (2010) - S01E01-E03 - Episode Title
  :value11: Daily-Episode Example,
            The Series Title (2010) - 2013-10-30 - Episode Title (1)
  :value12: Anime Episode Example,
            The Series Title (2010) - S01E01 - Episode Title (1)
  :value13: Anime Multi-Episode Example,
            The Series Title (2010) - S01E01-E03 - Episode Title
  :value14: Series Folder Example, The Series Title (2010)
  :value15: Season Folder Example, Season 01

.. gui::   Sonarr Folders
  :path:   Settings --> Media Management --> Folders
  :value0: Create empty series folders, {NO}
  :value1: Delete empty folders, {NO}

.. gui::   Sonarr Importing
  :path:   Settings --> Media Management --> Importing
  :value0: Skip Free Space Check, {NO}
  :value1: Use Hardlinks Instead of Copy, {NO}
  :value2: Import Extra Files, {NO}

.. gui::   Sonarr File Management
  :path:   Settings --> Media Management --> File Management
  :value0: Ignore Delete Episodes, {NO}
  :value1: Download Propers, {YES}
  :value2: Analyse video files, {YES}
  :value3: Change File Date, {NONE}
  :value4: Recycling Bin, /data/downloads/sonarr-recycle/

.. gui::   Sonarr Permissions
  :path:   Settings --> Media Management --> Permissions
  :value0: Set Permissions, {YES}
  :value1: File chmod mask, 664
  :value2: Folder chmod mask, 775
  :value3: chown User, sonarr (or docker UID)
  :value4: chown Group, media (or docker GID)

Profiles
********
Remove all existing profiles. Set a basic high-quality profile.

Size limits are applied using the global setting via indexer settings.

.. gui::    Sonarr Profiles (Max 720/1080: 1080p upgrade)
  :path:    Settings --> Profiles --> +
  :value0:  Name, Max 720/1080: 1080p upgrade
  :value1:  Upgrades Allowed, ☑
  :value2:  Upgrade Until, Bluray-1080p Remux
  :value3:  Language, English
  :value4:  Qualities,
  :value5:  ›, ☑ Blueray-1080p Remux
  :value6:  ›, ☑ Bluray-1080p
  :value7:  ›, ☑ WEB 1080p
  :value8:  ›, ☑ Bluray-720p
  :value9:  ›, ☑ WEB 720p
  :value10: ›, ☑ Raw-HD
  :value11: ›, ☑ HDTV-1080p
  :value12: ›, ☑ HDTV-720p
  :value13: ›, ☑ Bluray-480p
  :value14: ›, ☑ DVD
  :value15: ›, ☑ WEB 480p
  :value16: ›, ☑ SDTV
  :value17: ›, ☑ Unknown

.. gui::   Sonarr Language Profiles
  :path:   Settings --> Profiles --> Language Profiles --> +
  :value0: Name, English
  :value1: Upgrades Allowed, ☑
  :value2: Languages, English (top)

.. gui::   Sonarr Delay Profiles
  :path:   Settings --> Profiles --> Delay Profiles --> +
  :value0: Protocol, Usenet
  :value1: Usenet Delay, 60 minutes
  :value2: Torrent Delay, No Delay
  :value3: Tags, {NONE}

Quality
*******

+--------------+--------------+------------+-------------+------------+-------------+
| Quality      | Title        | GB Low Min | GB High Min | GB Low Max | GB High Max |
+==============+==============+============+=============+============+=============+
| All          | ALL          | 0          | 0           | 2.93GB     | 5.86GB      |
+--------------+--------------+------------+-------------+------------+-------------+
| Raw-HD       | Raw-HD       | 0          | 0           | Unlimited  | Unlimited   |
+--------------+--------------+------------+-------------+------------+-------------+
| HDTV-2160p   | HDTV-2160p   | 0          | 0           | Unlimited  | Unlimited   |
+--------------+--------------+------------+-------------+------------+-------------+
| WEBDL-2160p  | WEBDL-2160p  | 0          | 0           | Unlimited  | Unlimited   |
+--------------+--------------+------------+-------------+------------+-------------+
| Bluray-2160p | Bluray-2160p | 0          | 0           | Unlimited  | Unlimited   |
+--------------+--------------+------------+-------------+------------+-------------+

Indexers
********
.. gui::   Sonarr Indexers
  :path:   Settings --> Indexers --> +
  :value0: Name; {INDEXER NAME}
  :value1: Enable RSS; {YES}
  :value2: Enable Search; {YES}
  :value3: URL; {INDEXER API URI}
  :value4: API Path; /api
  :value5: API Key; {KEY}
  :value6: Categories; 5030,5040
  :value7: Anime Categories;
  :value8: Additional Parameters, {NONE}
  :delim:  ;

.. gui::   Sonarr Options
  :path:   Settings --> Indexers --> Options
  :value0: Minimum Age, 0
  :value1: Retention, 0
  :value2: Maximum Size, 5000
  :value3: RSS Sync Interval, 15

Download Client
***************
.. gui:: Sonarr Download Client
  :path: Settings --> Download Client --> +
  :value0:  Name, {INDEXER NAME}
  :value1:  Enable, {YES}
  :value2:  Host, {IP}
  :value3:  Port, 6789
  :value4:  URL Base,
  :value5:  Username, {USER}
  :value6:  Password, {PASS}
  :value7:  Category, tv
  :value8:  Recent Priority, Normal
  :value9:  Older Priority, Normal
  :value10: Add Paused, {NO}
  :value11: Use SSL, {YES}

.. gui::   Sonarr Completed Download Handling
  :path:   Settings --> Download Client --> Completed Download Handling
  :value0: Enable, {YES}
  :value1: Remove, {YES}

.. gui::   Sonarr Failed Download Handing
  :path:   Settings --> Download Client --> Failed Download Handling
  :value0: Redownload, {NO}

.. gui::   Sonarr Drone Factory Options
  :path:   Settings --> Download Client --> Drone Factory Options
  :value0: Drone Factory,
  :value1: Drone Factory Interval, 0

Connect
*******
.. gui:: Sonarr Connect
  :path: Settings --> Connect --> Connections --> +
  :value0:  Name, Plex Server
  :value1:  On Grab, {NO}
  :value2:  On Download, {YES}
  :value3:  On Upgrade, {YES}
  :value4:  On Rename, {YES}
  :value5:  Filter Series Tags,
  :value6:  Host, {IP}
  :value7:  Port, {PORT}
  :value8:  Username, {USER}
  :value9:  Password, {PASS}
  :value10: Update Library, {NO}
  :value11: Use SSL, {YES}

General
*******
.. gui::   Sonarr General Host
  :path:   Settings --> General --> Start-Up
  :value0: Bind Address, *
  :value1: Port Number, 8989
  :value2: URL Base,
  :value3: Enable SSL, {NO}
  :value4: Open browser on start, {NO}

.. gui::   Sonarr General Security
  :path:   Settings --> General --> Security
  :value0: Authentication, {NONE}
  :value1: API Key, {KEY}

.. gui::   Sonarr General Proxy
  :path:   Settings --> General --> Proxy
  :value0: Use Proxy, {NO}

.. gui:: Sonarr General Logging
  :path: Settings --> General --> Logging
  :value0:  Log Level, {INFO}

.. gui::   Sonarr General Analytics
  :path:   Settings --> General --> Analytics
  :value0: Enable, {NO}

.. gui::   Sonarr General Updates
  :path:   Settings --> General --> Updates
  :value0: Branch, master
  :value1: Automatic, {ON}
  :value2: Mechanism, Built-in

UI
**
.. gui::   Sonarr UI Calendar
  :path:   Settings --> UI --> Calendar
  :value0: First Day of Week, Sunday
  :value1: Week Column Header, Tue 3/25

.. gui::   Sonarr UI Dates
  :path:   Settings --> UI --> Dates
  :value0: Short Date Format, YYYY-MM-DD
  :value1: Long Date Format, Tuesday March 25 2014
  :value2: Time Format, 17:00/17:30
  :value3: Show Relative Dates, {NO}

.. gui::   Sonarr UI Style
  :path:   Settings --> UI --> Style
  :value0: Enable Color-Impaired mode, {NO}
