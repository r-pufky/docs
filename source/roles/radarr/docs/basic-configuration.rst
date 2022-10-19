.. _service-radarr-basic-configuration:

Basic Configuration
###################
Be sure to toggle ``advanced settings`` on; toggle back and forth to set both.
Unmentioned options are defaults.

Media Management
****************
.. gui::   Movie Naming
  :path:   Settings --> Media Management --> Movie Naming
  :value0: Rename Episodes, ☑
  :value1: Replace Illegal Characters, ☑
  :value2: Colon Replacement Format, Delete
  :value3: Standard Movie Format, {Movie TitleThe} ({Release Year}) {edition-{Edition Tags}}
  :value4: Movie Folder Format, {Movie TitleThe} ({Release Year}) {edition-{Edition Tags}}
  :ref: https://support.plex.tv/articles/multiple-editions/

.. gui::   Folders
  :path:   Settings --> Media Management --> Folders
  :value0: Create empty movie folders, ☐
  :value1: Delete empty folders, ☐

.. gui::   Importing
  :path:   Settings --> Media Management --> Importing
  :value0: Skip Free Space Check, ☐
  :value1: Minimum Free space, 100MB
  :value2: Use Hardlinks Instead of Copy, ☐
  :value3: Import Extra Files, ☐

.. gui::   File Management
  :path:   Settings --> Media Management --> File Management
  :value0: Unmonitor Deleted Movies, ☐
  :value1: Propers and Repacks, Prefer and Upgrade
  :value2: Analyse video files, ☑
  :value3: Rescan Movie Folder after Refresh, Always
  :value4: Change File Date, None
  :value5: Recycling Bin, /data/downloads/media-trashed
  :value6: Recycling Bin Cleanup, 7

.. gui::   Permissions
  :path:   Settings --> Media Management --> Permissions
  :value0: Set Permissions, ☑
  :value1: chmod Folder, 775
  :value2: chown Group, media

Profiles
********
Remove all existing profiles. Set a basic high-quality profile and a
max-quality profile.

Size limits are applied using the global setting via indexer settings.

.. gui::    Profiles (Max 720/1080: 1080p upgrade)
  :path:    Settings --> Profiles
  :value0:  Name, Max 720/1080: 1080p upgrade
  :value1:  Upgrades Allowed, ☑
  :value2:  Upgrade Until, HDTV-1080p
  :value3:  Language, English
  :value4:  Qualities,  
  :value5:  ›, ☑ Remux-1080p
  :value6:  ›, ☑ Bluray-1080p
  :value7:  ›, ☑ WEB 1080p
  :value8:  ›, ☑ HDTV-1080p
  :value9:  ›, ☑ Bluray-720p
  :value10: ›, ☑ WEB 720p
  :value11: ›, ☑ HDTV-720p
  :value12: ›, ☑ blueray-576p
  :value13: ›, ☑ blueray-480p
  :value14: ›, ☑ WEB 480p
  :value15: ›, ☑ DVD R
  :value16: ›, ☑ DVD
  :value17: ›, ☑ SDTV
  :value18: ›, ☑ DVDSCR
  :value19: ›, ☑ REGIONAL
  :value20: ›, ☑ TELECINE
  :value21: ›, ☑ TELESYNC
  :value22: ›, ☑ WORKPRINT
  :value23: ›, ☑ Unknown

.. gui::    Profiles (2K/4K/Raw)
  :path:    Settings --> Profiles
  :value0:  Name, 2K/4K/Raw
  :value1:  Upgrades Allowed, ☑
  :value2:  Upgrade Until, HDTV-2160p
  :value3:  Language, English
  :value4:  Qualities,  
  :value5:  ›, ☑ Raw-HD
  :value6:  ›, ☑ BR-DISK
  :value7:  ›, ☑ Remux-2160p
  :value8:  ›, ☑ Bluray-2160p
  :value9:  ›, ☑ WEB 2160p
  :value10: ›, ☑ HDTV-2160p

.. gui::   Delay Profiles
  :path:   Settings --> Profiles --> Delay Profiles
  :value0: Protocol, Usenet
  :value1: Usenet Delay, 60 Minutes
  :value2: Torrent Delay, No Delay
  :value3: Tags, {NONE}

.. gui::   Library Filters (released: missing)
  :path:   Movies --> Filter --> Custom Filters
  :value0: Label, released: missing,  
  :value1: Filters,  
  :value2: ›, Minimum Availability is Released
  :value3: ›, Size on Disk <= 100MB
  :value4: ›, Considered Available is true

  Applying this filter on the library will show all movies that are actually
  missing (default view is to show all missing, including unreleased).

.. gui::   Movie Search Filters (<15GB)
  :path:   Movies --> {Any Movie --> Search --> Filter --> Custom Filters
  :value0: Label, <15GB
  :value1: Filters,  
  :value2: ›, Size less than 15GB

  Limits manual search to specific NZB sizes, regardless of quality.

Quality
*******

+------------------+-------+------------+-------------+------------+-------------+
| Quality          | Title | GB Low Min | GB High Min | GB Low Max | GB High Max |
+==================+=======+============+=============+============+=============+
| {<= WEBDL-1080p} | ALL   | 0          | 0           | 8.79GB     | 13.67GB     |
+------------------+-------+------------+-------------+------------+-------------+
| {> WEBDL-1080p}  | ALL   | 0          | 0           | Unlimited  | Unlimited   |
+------------------+-------+------------+-------------+------------+-------------+

Indexers
********
.. gui::    Indexers
  :path:    Settings --> Indexers
  :value0:  Name; {INDEXER NAME}
  :value1:  Enable RSS; ☑
  :value2:  Enable Automatic Search; ☑
  :value3:  Enable Interactive Search; ☑
  :value4:  URL; {INDEXER API URI}
  :value5:  API Path; /api
  :value6:  Multi Languages; {NONE}
  :value7:  API Key; {KEY}
  :value8:  Categories; ☑ (All)
  :value9:  Additional Parameters; {NONE}
  :value10: Remove year from search string; ☐
  :value11: Indexer Priority; 25
  :value12: Download Client; (Any)
  :value13: Tags; {NONE}
  :delim:   ;

.. gui::   Options
  :path:   Settings --> Indexers --> Options
  :value0: Minimum Age, 0
  :value1: Retention, 0
  :value2: Maximum Size, 15360
  :value3: Prefer Indexer Flags, ☐
  :value4: Availability Delay, 0
  :value5: RSS Sync Interval, 0
  :value6: Whiteliste Subtitle Tags, {NONE}
  :value7: Allow Hardcoded Subs, ☐

  Maximum size sets a hard limit for file download size, regardless of Quality
  options.

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
  :value8:  Category, movies
  :value9:  Recent Priority, Normal
  :value10: Older Priority, Normal
  :value11: Add Paused, ☐
  :value12: Client Priority, 1
  :value13: Remove Completed, ☑
  :value14: Remove Failed, ☑

.. gui::   Completed Download Handling
  :path:   Settings --> Download Client --> Completed Download Handling
  :value0: Enable, ☑
  :value1: Check For Finished Downloads Interval, 1

.. gui::   Failed Download Handing
  :path:   Settings --> Download Client --> Failed Download Handling
  :value0: Redownload, ☑

Connect
*******
.. gui::    Connect
  :path:    Settings --> Connect --> Connections
  :value0:  Name, Plex Server
  :value1:  ☐, On Grab
  :value2:  ☑, On Download
  :value3:  ☑, On Upgrade
  :value4:  ☑, On Rename
  :value5:  ☐, On Movie Added
  :value6:  ☑, On Movie Delete
  :value7:  ☑, On Movie File Delete
  :value8:  ☑, On Movie File Delete For Upgrade
  :value9:  ☐, On Health Issue
  :value10: ☐, On Application Update
  :value11: Tags, {NONE}
  :value12: Host, {IP}
  :value13: Port, {PASS}
  :value14: Use SSL, ☑
  :value15: Auth Token, {Token}
  :value16: Authenticate with Plex.tv, {Authenticate}
  :value17: Update Library, ☐
  :value18: Map Paths From, {NONE}
  :value19: Map Paths To, {NONE}

  Re-authenticate to plex.tv only if there is no auth token, or it does not
  work.

General
*******
.. gui::   Host
  :path:   Settings --> General --> Host
  :value0: Bind Address, *
  :value1: Port Number, 7878
  :value2: Instance Name, Radarr
  :value3: Application URL, {NONE}
  :value4: Enable SSL, ☐
  :value5: Open browser on start, {NO}

.. gui::   Security
  :path:   Settings --> General --> Security
  :value0: Authentication, {NONE}
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

.. gui::   Movies
  :path:   Settings --> UI --> Movies
  :value0: Runtime Format, 1h 15m

.. gui::   Dates
  :path:   Settings --> UI --> Dates
  :value0: Short Date Format, YYYY-MM-DD
  :value1: Long Date Format, Tuesday March 25 2014
  :value2: Time Format, 17:00/17:30
  :value3: Show Relative Dates, ☐

.. gui::   Style
  :path:   Settings --> UI --> Style
  :value0: Enable Color-Impaired mode, ☐

.. gui::   Language
  :path:   Settings --> UI --> Language
  :value0: Movie Info Language, English
  :value1: UI Language, English
