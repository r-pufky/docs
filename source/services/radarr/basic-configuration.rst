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
  :value3: Standard Movie Format, {Movie TitleThe} ({Release Year}){ - Edition Tags}
  :value4: Movie Folder Format, {Movie TitleThe} ({Release Year})

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
  :value1: File chmod mask, 2660
  :value2: Folder chmod mask, 2770
  :value3: chown User, radarr (or docker UID)
  :value4: chown Group, media (or docker GID)

Profiles
********
.. gui::    Radarr Profiles (Any)
  :path:    Settings --> Profiles --> Any
  :value0:  Name, {ANY}
  :value1:  Language, English
  :value2:  Preferred Tags,
  :value3:  Cutoff, Bluray-480p
  :value4:  Custom Format Cutoff, {NONE}
  :value5:  Qualities,
  :value6:  ›, ☐ Raw HD
  :value7:  ›, ☑ BR-DISK
  :value8:  ›, ☑ Remux-2160p
  :value9:  ›, ☑ Bluray-2160p
  :value10: ›, ☑ WEBDL-2160p
  :value11: ›, ☑ HDTV-2160p
  :value12: ›, ☑ Remux-1080p
  :value13: ›, ☑ Bluray-1080p
  :value14: ›, ☑ WEBDL-1080p
  :value15: ›, ☑ HDTV-1080p
  :value16: ›, ☑ Bluray-720p
  :value17: ›, ☑ WEBDL-720p
  :value18: ›, ☑ HDTV-720p
  :value19: ›, ☑ Bluray-576p
  :value20: ›, ☑ Bluray-480p
  :value21: ›, ☑ WEBDL-480p
  :value22: ›, ☑ DVD-R
  :value23: ›, ☑ DVD
  :value24: ›, ☑ SDTV
  :value25: ›, ☑ DVDSCR
  :value26: ›, ☑ REGIONAL
  :value27: ›, ☑ TELECINE
  :value28: ›, ☑ TELESYNC
  :value29: ›, ☑ CAM
  :value30: ›, ☑ WORKPRINT
  :value31: ›, ☐ Unknown
  :value32: Custom Formats, ☑ None

.. gui::    Radarr Profiles (SD)
  :path:    Settings --> Profiles --> SD
  :value0:  Name, SD
  :value1:  Language, English
  :value2:  Preferred Tags,
  :value3:  Cutoff, Bluray-480p
  :value4:  Custom Format Cutoff, {NONE}
  :value5:  Qualities,
  :value6:  ›, ☑ Bluray-576p
  :value7:  ›, ☑ Bluray-480p
  :value8:  ›, ☑ WEBDL-480p
  :value9:  ›, ☑ DVD
  :value10: ›, ☑ SDTV
  :value11: ›, ☑ DVDSCR
  :value12: ›, ☑ REGIONAL
  :value13: ›, ☑ TELECINE
  :value14: ›, ☑ TELESYNC
  :value15: ›, ☑ CAM
  :value16: ›, ☑ WORKPRINT
  :value17: Custom Formats, ☑ None

.. gui::   Radarr Profiles (HD-720p)
  :path:   Settings --> Profiles --> HD-720p
  :value0: Name, HD-720p
  :value1: Language, English
  :value2: Preferred Tags,
  :value3: Cutoff, Bluray-720p
  :value4: Custom Format Cutoff, {NONE}
  :value5: Qualities,
  :value6: ›, ☑ Bluray-720p
  :value7: ›, ☑ WEBDL-720p
  :value8: ›, ☑ HDTV-720p
  :value9: Custom Formats, ☑ None

.. gui::   Radarr Profiles (HD-1080p)
  :path:   Settings --> Profiles --> HD-1080p
  :value0: Name, HD-1080p
  :value1: Language, English
  :value2: Preferred Tags,
  :value3: Cutoff, Bluray-480p
  :value4: Custom Format Cutoff, {NONE}
  :value5: Qualities,
  :value6: ›, ☑ Remux-1080p
  :value7: ›, ☑ Bluray-1080p
  :value8: ›, ☑ WEBDL-1080p
  :value9: ›, ☑ HDTV-1080p
  :value10: Custom Formats, ☑ None

.. gui::   Radarr Profiles (Ultra-HD)
  :path:   Settings --> Profiles --> Ultra-HD
  :value0: Name, Ultra-HD
  :value1: Language, English
  :value2: Preferred Tags,
  :value3: Cutoff, Remux-2160p
  :value4: Custom Format Cutoff, {NONE}
  :value5: Qualities,
  :value6: ›, ☑ Remux-2160p
  :value7: ›, ☑ Bluray-2160p
  :value8: ›, ☑ WEBDL-2160p
  :value9: ›, ☑ HDTV-2160p
  :value10: Custom Formats, ☑ None

.. gui::    Radarr Profiles (HD - 720p/1080p)
  :path:    Settings --> Profiles --> HD - 720p/1080p
  :value0:  Name, HD - 720p/1080p
  :value1:  Language, English
  :value2:  Preferred Tags,
  :value3:  Cutoff, Bluray-720p
  :value4:  Custom Format Cutoff, {NONE}
  :value5:  Qualities,
  :value6:  ›, ☑ Remux-2160p
  :value7:  ›, ☑ Remux-1080p
  :value8:  ›, ☑ Bluray-1080p
  :value9:  ›, ☑ WEBDL-1080p
  :value10: ›, ☑ HDTV-1080p
  :value11: ›, ☑ Bluray-720p
  :value12: ›, ☑ WEBDL-720p
  :value13: ›, ☑ HDTV-720p
  :value14: Custom Formats, ☑ None

.. gui::   Radarr Delay Profiles
  :path:   Settings --> Profiles --> Delay Profiles --> +
  :value0:      Protocol, Usenet
  :value1:  Usenet Delay, 60 Minutes
  :value2: Torrent Delay, No Delay
  :value3:          Tags, {NONE}

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
  :value2: Maximum Size, 0
  :value3: Prefer Special Indexer Flags, {NO}
  :value4: RSS Sync Interval, 0
  :value5: Whiteliste Subtitle Tags,
  :value6: Allow Hardcoded Subs, {NO}
  :value7: Parser Leniency, Strict

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

  Certificate validation needs to be disabled for local addresses as let's
  encrypt certs presented using a non-routable IP will fail full-chain
  validation, which is the `default validation method`_ as of 2020-11-01.

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

.. _default validation method: https://old.reddit.com/r/radarr/comments/k3pifj/connection_to_sabnzbd_broken_after_update/
