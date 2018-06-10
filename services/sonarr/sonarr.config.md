Sonarr Basic Config
-------------------
An example of how to setup sonarr.

Settings
--------
Be sure to toggle `advanced settings` to on; toggle back and forth to set both.

### Media Management

#### Episode Naming
 * Rename Episodes: yes
 * Replace Illegal Characters: yes
 * Standard Episode Format: {Series Title} - S{season:00}E{episode:00} - {Episode Title}
 * Daily Episode Format: {Series Title} - {Air-Date} - {Episode Title}
 * Anime Episode Format: {Series Title} - S{season:00}E{episode:00} - {Episode Title}
 * Series Folder Format: {Series Title}
 * Include Series Title: yes
 * Include Episode Title: yes
 * Inlucde Quality: no
 * Replace Series: no
 * Separator: Dash
 * Numbering Style: S01E05
 * Season Folder Format: Season {season:00}
 * Multi-Episode Style: Prefixed Range
 * Single Episode Example: The Series Title (2010) - S01E01 - Episode Title (1)
 * Multi-Episode Example: The Series Title (2010) - S01E01-E03 - Episode Title
 * Daily-Episode Example: The Series Title (2010) - 2013-10-30 - Episode Title (1)
 * Anime Episode Example: The Series Title (2010) - S01E01 - Episode Title (1)
 * Anime Multi-Episode Example: The Series Title (2010) - S01E01-E03 - Episode Title
 * Series Folder Example: The Series Title (2010)
 * Season Folder Example: Season 01

#### Folders
 * Create empty series folders: no
 * Delete empty folers: no

#### Importing
 * Skip Free Space Check: no
 * Use Hardlink instead of Copy: no
 * Import Extra Files: no

#### File Management
 * Ignore Deleted Episodes: no
 * Download Propers: yes
 * Analyze video files: yes
 * Change File Date: None
 * Recycling Bin: /data/downloads/sonarr-recycle

#### Permissions
 * Set Permissions: yes
 * File chmod mask: 2660
 * Folder chmod mask: 2770
 * chown User: sonarr
 * chown Group: media

### Profiles
 * Any:
   * Language: English
   * Cutoff: SDTV
   * Qualities: WEBDL-480p, DVD, Bluray-1080p, WEBDL-1080p, HDTV-1080p,
                Bluray-720p, WEBDL-720p, HDTV-720p, SDTV
 * SD:
   * Language: English
   * Cutoff: SDTV
   * Qualities: WEBDL-480p, DVD, SDTV
 * HD-720p:
   * Language: English
   * Cutoff: HDTV-720p
   * Qualities: Bluray-720p, WEBDL-720p, HDTV-720p
 * HD-1080p:
   * Language: English
   * Cutoff: HDTV-1080p
   * Qualities: Bluray-1080p, WEBDL-1080p, HDTV-1080p
 * HD-ALL:
   * Language: English
   * Cutoff: HDTV-720p
   * Qualities: Bluray-1080p, WEBDL-1080p, HDTV-1080p, Bluray-720p, WEBDL-720p,
                HDTV-720p

#### Delay Profiles
 * Prefer Usenet
 * Usenet Delay: 60 minutes
 * Torrent Delay: 0 minutes

### Quality

|Quality       | Title        | Size Limit (30m/60m)      |
|--------------|--------------|---------------------------|
| Unknown      | Unknown      | 0B 0B 2.93GB 5.86GB       |
| SDTV         | SDTV         | 0B 0B 2.93GB 5.86GB       |
| WEBDL-480p   | WEBDL-480p   | 0B 0B 2.93GB 5.86GB       |
| DVD          | DVD          | 0B 0B 2.93GB 5.86GB       |
| HDTV-720p    | HDTV-720p    | 0B 0B 2.93GB 5.86GB       |
| HDTV-1080p   | HDTV-1080p   | 0B 0B 2.93GB 5.86GB       |
| Raw-HD       | Raw-HD       | 0B 0B Unlimited Unlimited |
| WEBDL-720p   | WEBDL-720p   | 0B 0B 2.93GB 5.86GB       |
| Bluray-720p  | Bluray-720p  | 0B 0B 2.93GB 5.86GB       |
| WEBDL-1080p  | WEBDL-1080p  | 0B 0B 2.93GB 5.86GB       |
| Bluray-1080p | Bluray-1080p | 0B 0B 2.93GB 5.86GB       |
| HDTV-2160p   | HDTV-2160p   | 0B 0B Unlimited Unlimited |
| WEBDL-2160p  | WEBDL-2160p  | 0B 0B Unlimited Unlimited |
| Bluray-2160p | Bluray-2160p | 0B 0B Unlimited Unlimited |

### Indexers
 * Name: <YOUR INDEXER NAME>
 * Enable RSS Sync: yes
 * Enable Search: yes
 * URL: <INDEXER API URI>
 * API Path: /api
 * API Key: <YOUR API KEY>
 * Categories: 5030,5040

#### Options
 * Minimum Age: 0
 * Retention: 0
 * Maximum Size: 0
 * RSS Sync Interval: 15

#### Restrictions
 * Must not contain: megusta

### Download Client
 * Name: nzbget
 * Enable: yes
 * Host: <YOUR NZBGET IP>
 * Port: <YOUR NZBGET PORT>
 * Username: <API_USERNAME>
 * Password: <API_PASSWORD>
 * Category: tv
 * Recent Priority: normal
 * Older Priority: normal
 * Add Paused: no
 * Use SSL: yes

#### Completed Download Handling
 * Enable: yes
 * Remove: yes

#### Failed Download Handling
 * Redownload: no

#### Drone Factory Options
 * Drone Factory Interval: 0

### Connect
 * Name: Plex Server
 * On Grab: no
 * On Download: yes
 * On Upgrade: yes
 * On Rename: yes
 * Host: <PLEX IP>
 * Port: 32400
 * Username: <YOUR PLEX EMAIL>
 * Password: <YOUR PLEX PASSWORD>
 * Update Library: yes
 * Use SSL: yes

### General

#### Start-Up
 * Bind Address: *
 * Port Number: 8989
 * Enable SSL: no
 * Open browser on start: no

#### Security
 * Authentication: none
 * API Key: <GENERATE API KEY>

#### Proxy Settings
 * Use Proxy: no

#### Logging
 * Log Level: info

#### Analytics
 * Enable: no

#### Updates
 * Branch: master
 * Automatic: on
 * Mechanism: Built-in

### UI

#### Calendar
 * First Day of Week: Sunday
 * Week Column Header: Tue 3/25

#### Dates
 * Short Date Format: YYYY-MM-DD
 * Long Date Format: Tuesdat, March 25, 2014
 * Time Format: 17:00/17:30
 * Show Relative Dates: no

#### Style
 * Enable Color-Impaired mode: no
