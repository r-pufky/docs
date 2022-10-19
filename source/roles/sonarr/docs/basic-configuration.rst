.. _service-sonarr-basic-configuration:

Basic Configuration
###################
Be sure to toggle ``advanced settings`` on; toggle back and forth to set both.
Unmentioned options are defaults.

Media Management
****************
.. gui::   Episode Naming
  :path:   Settings --> Media Management --> Episode Naming
  :value0: Rename Episodes, ☑
  :value1: Replace Illegal Characters, ☑
  :value2: Standard Episode Format,
           {Series TitleTheYear} - S{season:00}E{episode:00} - {Episode Title}
  :value3: Daily Episode Format,
           {Series TitleTheYear} - {Air-Date} - {Episode Title}
  :value4: Anime Episode Format,
           {Series TitleTheYear} - S{season:00}E{episode:00} - {Episode Title}
  :value5: Series Folder Format,   {Series TitleTheYear}
  :value6: Season Folder Format,   Season {season:00}
  :value7: Specials Folder Format, Specials
  :value8: Multi-Episode Style,    Prefixed Range

.. gui::   Folders
  :path:   Settings --> Media Management --> Folders
  :value0: Create empty series folders, ☐
  :value1: Delete empty folders, ☐

.. gui::   Importing
  :path:   Settings --> Media Management --> Importing
  :value0: Episode title Required, Always
  :value1: Skip Free Space Check, ☐
  :value2: Minimum Free Space, 100MB
  :value3: Use Hardlinks Instead of Copy, ☐
  :value4: Import Extra Files, ☐

.. gui::   File Management
  :path:   Settings --> Media Management --> File Management
  :value0: Unmonitor Deleted Episodes, ☐
  :value1: Propers and Repacks, Prefer and Upgrade
  :value2: Analyse video files, ☑
  :value3: Rescan Series Folder after Refresh, Always
  :value4: Change File Date, None
  :value5: Recycling Bin, /data/downloads/sonarr-recycle/
  :value6: Recycling Bin Cleanup, 7

.. gui::   Permissions
  :path:   Settings --> Media Management --> Permissions
  :value0: Set Permissions, ☑
  :value1: chmod Folder, 775
  :value2: chmod Group, media

Profiles
********
Remove all existing profiles. Set a basic high-quality profile.

Size limits are applied using the global setting via indexer settings.

.. gui::    Profiles (Max 720/1080: 1080p upgrade)
  :path:    Settings --> Profiles
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

.. gui::   Language Profiles
  :path:   Settings --> Profiles --> Language Profiles
  :value0: Name, English
  :value1: Upgrades Allowed, ☑
  :value2: Languages, English (top)

.. gui::   Delay Profiles
  :path:   Settings --> Profiles --> Delay Profiles
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
.. gui::    Indexers
  :path:    Settings --> Indexers
  :value0:  Name; {INDEXER NAME}
  :value1:  Enable RSS; {YES}
  :value2:  Enable Automatic Search; ☑
  :value3:  Enable Interactive Search; ☑
  :value4:  URL; {INDEXER API URI}
  :value5:  API Path; /api
  :value6:  API Key; {KEY}
  :value7:  Categories; ☑ (All)
  :value8:  Anime Categories; ☑ (All)
  :value9:  Anime Standard Format Search; ☐
  :value10: Additional Parameters; {NONE}
  :value11: Indexer Priority; 25
  :value12: DownloadClient; (Any)
  :value13: Tags; {NONE}
  :delim:   ;

.. gui::   Options
  :path:   Settings --> Indexers --> Options
  :value0: Minimum Age, 0
  :value1: Retention, 0
  :value2: Maximum Size, 5120
  :value3: RSS Sync Interval, 15

Download Client
***************
.. gui::    Download Client
  :path:    Settings --> Download Client
  :value0:  Name, {INDEXER NAME}
  :value1:  Enable, ☑
  :value2:  Host, {IP}
  :value3:  Port, 6789
  :value4:  Use SSL, ☐
  :value5:  URL Base, {NONE}
  :value6:  Username, {USER}
  :value7:  Password, {PASS}
  :value8:  Category, tv
  :value9:  Recent Priority, Normal
  :value10: Older Priority, Normal
  :value11: Add Paused, ☐
  :value12: Client Priority, 1
  :value13: Remove Completed, ☑
  :value14: Remove Failed, ☑

.. gui::   Completed Download Handling
  :path:   Settings --> Download Client --> Completed Download Handling
  :value0: Enable, ☑
  :value1: Redownload Failed, ☑

Connect
*******
.. gui::    Connect
  :path:    Settings --> Connect --> Connections
  :value0:  Name, Plex Server
  :value1:  ☐, On Grab
  :value2:  ☑, On Import
  :value3:  ☑, On Upgrade
  :value4:  ☑, On Rename
  :value5:  ☑, On Sereis Delete
  :value6:  ☑, On Episode File Delete
  :value7:  ☑, On Episode File Delete For Upgrade
  :value8:  ☐, On Health Issue
  :value9:  ☐, On Application Update
  :value10: Tags, {NONE}
  :value11: Host, {IP}
  :value12: Port, {PORT}
  :value13: Use SSL, ☑
  :value14: Update Library, {NO}
  :value15: Auth Token, {Token}
  :value16: Authenticate with Plex.tv, {Authenticate}
  :value17: Update Library, ☐

  Re-authenticate to plex.tv only if there is no auth token, or it does not
  work.

General
*******
.. gui::   Host
  :path:   Settings --> General --> Host
  :value0: Bind Address, *
  :value1: Port Number, 8989
  :value2: URL Base, {NONE}
  :value3: Instance Name, Sonarr
  :value4: Enable SSL, ☐
  :value5: Open browser on start, {NO}

.. gui::   Security
  :path:   Settings --> General --> Security
  :value0: Authentication, None
  :value1: API Key, {KEY}
  :value2: Certificate Validation, Disabled for Local Addresses
  :ref:    https://old.reddit.com/r/radarr/comments/k3pifj/connection_to_sabnzbd_broken_after_update/

  Certificate validation needs to be disabled for local addresses as let's
  encrypt certs presented using a non-routable IP will fail full-chain
  validation, which is the default validation method as of 2020-11-01.

.. gui::   Proxy
  :path:   Settings --> General --> Proxy
  :value0: Use Proxy, ☐

.. gui::   Logging
  :path:   Settings --> General --> Logging
  :value0: Log Level, {INFO}

.. gui::   Analytics
  :path:   Settings --> General --> Analytics
  :value0: Enable, ☐

.. gui::   Updates
  :path:   Settings --> General --> Updates
  :value0: Branch, main
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
