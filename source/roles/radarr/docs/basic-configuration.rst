.. _service-radarr-basic-configuration:

Basic Configuration
###################
Be sure to toggle ``advanced settings`` on; toggle back and forth to set both.
Unmentioned options are defaults.

Media Management
****************
.. gui::   Radarr Movie Naming
  :path:   Settings --> Media Management --> Movie Naming
  :value0: Rename Episodes, {YES}
  :value1: Replace Illegal Characters, {YES}
  :value2: Colon Replacement Format, {DELETE}
  :value3: Standard Movie Format, {Movie TitleThe} ({Release Year}) {edition-{Edition Tags}}
  :value4: Movie Folder Format, {Movie TitleThe} ({Release Year})
  :ref: https://support.plex.tv/articles/multiple-editions/

.. gui::   Radarr Folders
  :path:   Settings --> Media Management --> Folders
  :value0: Create empty movie folders, {NO}
  :value1: Automatically Rename Folders, {YES}
  :value2: Movie Paths Default to Static, {YES}

.. gui::   Radarr Importing
  :path:   Settings --> Media Management --> Importing
  :value0: Skip Free Space Check, {NO}
  :value1: Use Hardlinks Instead of Copy, {NO}
  :value2: Import Extra Files, {NO}

.. gui::   Radarr File Management
  :path:   Settings --> Media Management --> File Management
  :value0: Unmonitor Deleted Movies, {NO}
  :value1: Download Propers, {YES}
  :value2: Analyse video files, {YES}
  :value3: Change File Date, {NONE}
  :value4: Recycling Bin, /data/downloads/media-trashed

.. gui::   Radarr Permissions
  :path:   Settings --> Media Management --> Permissions
  :value0: Set Permissions, {YES}
  :value1: File chmod mask, 664
  :value2: Folder chmod mask, 775
  :value3: chown User, radarr (or docker UID)
  :value4: chown Group, media (or docker GID)

Profiles
********
Remove all existing profiles. Set a basic high-quality profile and a
max-quality profile.

Size limits are applied using the global setting via indexer settings.

.. gui::    Radarr Profiles (Max 720/1080: 1080p upgrade)
  :path:    Settings --> Profiles --> +
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

.. gui::    Radarr Profiles (2K/4K/Raw)
  :path:    Settings --> Profiles --> +
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

.. gui::   Radarr Delay Profiles
  :path:   Settings --> Profiles --> Delay Profiles --> +
  :value0: Protocol, Usenet
  :value1: Usenet Delay, 60 Minutes
  :value2: Torrent Delay, No Delay
  :value3: Tags, {NONE}

.. gui::   Radarr Library Filters (released: missing)
  :path:   Movies --> Filter --> Custom Filters --> +
  :value0: released: missing
  :value1: Minimum Availability, is Released
  :value2: Size on Disk, <= 100MB
  :value3: Considered Available, is true

  Applying this filter on the library will show all movies that are actually
  missing (default view is to show all missing, including unreleased).

.. gui::   Radarr Movie Search Filters (<15GB)
  :path:   Movies --> {Any Movie --> Search --> Filter --> Custom Filters
  :value0: <15GB
  :value1: Size, less than 15GB

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
.. gui::    Radarr Indexers
  :path:    Settings --> Indexers --> +
  :value0:  Name; {INDEXER NAME}
  :value1:  Enable RSS; {YES}
  :value2:  Enable Search; {YES}
  :value3:  URL; {INDEXER API URI}
  :value4:  Multi Languages;
  :value5:  API Key; {KEY}
  :value6:  Categories; 2000,2010,2020,2030,2035,2040,2045,2050,2060
  :value7:  Anime Categories;
  :value8:  Additional Parameters;
  :value9:  Remove year from search string; {NO}
  :value10: Search by Title, {NO}
  :delim:   ;

.. gui::   Radarr Options
  :path:   Settings --> Indexers --> Options
  :value0: Minimum Age, 0
  :value1: Retention, 0
  :value2: Maximum Size, 15360
  :value3: Prefer Special Indexer Flags, {NO}
  :value4: RSS Sync Interval, 0
  :value5: Whiteliste Subtitle Tags,
  :value6: Allow Hardcoded Subs, {NO}
  :value7: Parser Leniency, Strict

  Maximum size sets a hard limit for file download size, regardless of Quality
  options.

.. gui::   Radarr Availability Options
  :path:   Settings --> Indexers --> Availability Options
  :value0: Availability Delay, 0

Download Client
***************
.. gui::    Radarr Download Client
  :path:    Settings --> Download Client --> +
  :value0:  Name, {INDEXER NAME}
  :value1:  Enable, {YES}
  :value2:  Host, {IP}
  :value3:  Port, 6789
  :value4:  URL Base,
  :value5:  Username, {USER}
  :value6:  Password, {PASS}
  :value7:  Category, movies
  :value8:  Recent Priority, Normal
  :value9:  Older Priority, Normal
  :value10: Use SSL, {YES}
  :value11: Add Paused, {NO}

.. gui::   Radarr Completed Download Handling
  :path:   Settings --> Download Client --> Completed Download Handling
  :value0: Enable, {YES}
  :value1: Remove, {YES}
  :value2: Check For Finished Downloads Interval, 1

.. gui::   Radarr Failed Download Handing
  :path:   Settings --> Download Client --> Failed Download Handling
  :value0: Redownload, {NO}

.. gui::   Radarr Drone Factory Options
  :path:   Settings --> Download Client --> Drone Factory Options
  :value0: Drone Factory,
  :value1: Drone Factory Interval, 0

Connect
*******
.. gui::    Radarr Connect
  :path:    Settings --> Connect --> Connections --> +
  :value0:  Name, Plex Server
  :value1:  On Grab, {NO}
  :value2:  On Download, {YES}
  :value3:  On Upgrade, {YES}
  :value4:  On Rename, {YES}
  :value5:  Filter Movie Tags,
  :value6:  Host, {IP}
  :value7:  Port, {PASS}
  :value8:  Username, {USER}
  :value9:  Password, {PASS}
  :value10: Update Library, {NO}
  :value11: Use SSL, {YES}

General
*******
.. gui::   Radarr General Host
  :path:   Settings --> General --> Start-Up
  :value0: Bind Address, *
  :value1: Port Number, 7878
  :value2: URL Base,
  :value3: Enable SSL, {NO}
  :value4: Open browser on start, {NO}

.. gui::   Radarr General Security
  :path:   Settings --> General --> Security
  :value0: Authentication, {NONE}
  :value1: API Key, {KEY}
  :value2: Certificate Validation, Disabled for Local Addresses
  :ref:    https://old.reddit.com/r/radarr/comments/k3pifj/connection_to_sabnzbd_broken_after_update/

  Certificate validation needs to be disabled for local addresses as let's
  encrypt certs presented using a non-routable IP will fail full-chain
  validation, which is the default validation method as of 2020-11-01.

.. gui::   Radarr General Proxy
  :path:   Settings --> General --> Proxy
  :value0: Use Proxy, {NO}

.. gui::   Radarr General Logging
  :path:   Settings --> General --> Logging
  :value0: Log Level, {INFO}

.. gui::   Radarr General Analytics
  :path:   Settings --> General --> Analytics
  :value0: Enable, {NO}

.. gui::   Radarr General Updates
  :path:   Settings --> General --> Updates
  :value0: Branch, master
  :value1: Automatic, {ON}
  :value2: Mechanism, Built-in

UI
**
.. gui::   Radarr UI Movies
  :path:   Settings --> UI --> Movies
  :value0: Page Size, 250

.. gui::   Radarr UI Calendar
  :path:   Settings --> UI --> Calendar
  :value0: First Day of Week, Sunday
  :value1: Week Column Header, Tue 3/25

.. gui::   Radarr UI Dates
  :path:   Settings --> UI --> Dates
  :value0: Short Date Format, YYYY-MM-DD
  :value1: Long Date Format, Tuesday March 25 2014
  :value2: Time Format, 17:00/17:30
  :value3: Show Relative Dates, {NO}

.. gui::   Radarr UI Style
  :path:   Settings --> UI --> Style
  :value0: Enable Color-Impaired mode, {NO}
