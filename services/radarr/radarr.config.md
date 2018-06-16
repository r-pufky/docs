Radarr Basic Config
-------------------
An example of how to setup radarr.

Settings
--------
Be sure to toggle `advanced settings` to on; toggle back and forth to set both.

### Media Management

#### Movie Naming
 * Rename Episodes: yes
 * Replace Illegal Characters: yes
 * Colon Replacement Format: delete
 * Standard Movie Format: {Movie TitleThe} ({Release Year}){ - Edition Tags}
 * Movie Folder Format: {Movie TitleThe} ({Release Year})
 * Include Quality: no
 * Replace Spaces: no
 * Separator: Space

#### Folders
 * Create empty movie folders: no
 * Automatically Rename Folders: yes
 * Movie Paths Default to Static: yes

#### Importing
 * Skip Free Space Check: no
 * Use Hardlinks Instead of Copy: no
 * Import Extra Files: no

#### File Management
 * Ignore Delete Movies: no
 * Download Propers: yes
 * Analyse Video Files: yes
 * Change File Date: no
 * Recycling Bin: /data/downloads/media-trashed

#### Permissions
 * Set Permissions: yes
 * File chmod mask: 2660
 * Folder chmod mask: 2770
 * chown User: radarr <OR DOCKER UID>
 * chown Group: media <OR DOCKER GID>

### Profiles
 * Any:
   * Language: English
   * Cutoff: Bluray-480p
   * Qualities: BR-DISK, Remux-2160p, Bluray-2160p, WEBDL-2160p, HDTV-2160p,
                Remux-1080p, Bluray-1080p, WEBDL-1080p, HDTV-1080p, Bluray-720p,
                WEBDL-720p, HDTV-720p, Bluray-576p, Bluray-480p, WEBDL-480p,
                DVD-R, DVD, SDTV, DVDSCR, REGIONAL, TELECINE, TELESYNC, CAM,
                WORKPRINT
 * SD:
   * Language: English
   * Cutoff: Bluray-480p
   * Qualities: Bluray-576p, Bluray-480p, WEBDL-480p, DVD, SDTV, DVDSCR,
                REGIONAL, TELECINE, TELESYNC, CAM, WORKPRINT
 * HD-720p:
   * Language: English
   * Cutoff: HDTV-720p
   * Qualities: Bluray-720p, WEBDL-720p, HDTV-720p
 * HD-1080p:
   * Language: English
   * Cutoff: HDTV-1080p
   * Qualities: Remux-1080p, Bluray-1080p, WEBDL-1080p, HDTV-1080p
 * Ultra-HD:
   * Language: English
   * Cutoff: Remux-2160p
   * Qualities: Remux-2160p, Bluray-2160p, WEBDL-2160p, HDTV-2160p
 * HD - 720p/1080p:
   * Language: English
   * Cutoff: Bluray-720p
   * Qualities: Remux-1080p, Bluray-1080p, WEBDL-1080p, HDTV-1080p, Bluray-720p,
                WEBDL-720p, HDTV-720p

#### Delay Profiles
 * Prefer Usenet
 * Usenet Delay: 60 minutes
 * Torrent Delay: 0 minutes

### Quality

|Quality       | Title        | Size Limit (30m/60m)      |
|--------------|--------------|---------------------------|
| Unknown      | Unknown      | 0B 0B 8.79GB 13.67GB      |
| WORKPRINT    | WORKPRINT    | 0B 0B 8.79GB 13.67GB      |
| CAM          | CAM          | 0B 0B 8.79GB 13.67GB      |
| TELESYNC     | TELESYNC     | 0B 0B 8.79GB 13.67GB      |
| TELECINE     | TELECINE     | 0B 0B 8.79GB 13.67GB      |
| REGIONAL     | REGIONAL     | 0B 0B 8.79GB 13.67GB      |
| DVDSCR       | DVDSCR       | 0B 0B 8.79GB 13.67GB      |
| SDTV         | SDTV         | 0B 0B 8.79GB 13.67GB      |
| DVD          | DVD          | 0B 0B 8.79GB 13.67GB      |
| DVD-R        | DVD-R        | 0B 0B 8.79GB 13.67GB      |
| WEBDL-480p   | WEBDL-480p   | 0B 0B 8.79GB 13.67GB      |
| Bluray-480p  | Bluray-480p  | 0B 0B 8.79GB 13.67GB      |
| Bluray-576p  | Bluray-576p  | 0B 0B 8.79GB 13.67GB      |
| HDTV-720p    | HDTV-720p    | 0B 0B 8.79GB 13.67GB      |
| WEBDL-720p   | WEBDL-720p   | 0B 0B 8.79GB 13.67GB      |
| Bluray-720p  | Bluray-720p  | 0B 0B 8.79GB 13.67GB      |
| HDTV-1080p   | HDTV-1080p   | 0B 0B 8.79GB 13.67GB      |
| WEBDL-1080p  | WEBDL-1080p  | 0B 0B 8.79GB 13.67GB      |
| Bluray-1080p | Bluray-1080p | 0B 0B Unlimited Unlimited |
| Remux-1080p  | Remux-1080p  | 0B 0B Unlimited Unlimited |
| HDTV-2160p   | HDTV-2160p   | 0B 0B Unlimited Unlimited |
| WEBDL-2160p  | WEBDL-2160p  | 0B 0B Unlimited Unlimited |
| Bluray-2160p | Bluray-2160p | 0B 0B Unlimited Unlimited |
| Remux-2160p  | Remux-2160p  | 0B 0B Unlimited Unlimited |
| BR-DISK      | BR-DISK      | 0B 0B Unlimited Unlimited |
| Raw-HD       | Raw-HD       | 0B 0B Unlimited Unlimited |

### Indexers
 * Name: <YOUR_INDEXER_NAME>
 * Enable RSS Sync: yes
 * Enable Search: yes
 * URL: <INDEXER_API_URI>
 * API Key: <YOUR_API_KEY>
 * Categories: 2000,2010,2020,2030,2035,2040,2045,2050,2060
 * Remove year from search string: no
 * Search by Title: no

#### Options
 * Minimum Age: 0
 * Retention: 0
 * Maximum Size: 0
 * Prefer Special Indexer Flags: no
 * RSS Sync Interval: 240
 * Whitelisted Subtitle Tags: <empty>
 * Allow Hardcoded Subs: no
 * Parser Leniency: Strict

#### Availability Options
 * Availability Delay: 0

### Download Clients
 * Name: nzbget
 * Enable: yes
 * Host: <YOUR_NZBGET_IP>
 * Port: <YOUR_NZBGET_PORT>
 * Username: <API_USERNAME>
 * Password: <API_PASSWORD>
 * Category: movies
 * Recent Priority: normal
 * Older Priority: normal
 * Use SSL: yes
 * Add Paused: no

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
 * Username: <YOUR_PLEX_EMAIL>
 * Password: <YOUR_PLEX_PASSWORD>
 * Update Library: no
 * Use SSL: yes

### General

#### Start-Up
 * Bind Address: *
 * Port Number: 7878
 * Enable SSL: no
 * Open browser on start: no

#### Security
 * Authentication: none
 * API Key: <GENERATE_API_KEY>

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

#### Movies
 * Page Size: 250
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
