Lidarr Basic Config
-------------------
An example of how to setup lidarr.

Settings
--------
Be sure to toggle `advanced settings` to on; toggle back and forth to set both.

### Media Management

#### Track Naming
 * Rename Tracks: yes
 * Replace Illegal Characters: yes
 * Standard Track Format: {track:00} - {Track Title}
 * Artist Folder Format: {Artist Name}
 * Album Folder Format: {Album Title}

#### Folders
 * Create empty artist folders: no
 * Delete empty folders: no

#### Importing
 * Skip Free Space Check: no
 * Use Hardlinks Instead of Copy: no
 * Import Extra Files: no

#### File Management
 * Ignore Delete Tracks: no
 * Download Propers: yes
 * Analyse Audio Files: yes
 * Change File Date: no
 * Recycling Bin: /data/downloads/media-trashed

#### Permissions
 * Set Permissions: yes
 * File chmod mask: 2660
 * Folder chmod mask: 2770
 * chown User: lidarr <OR DOCKER UID>
 * chown Group: media <OR DOCKER GID>

### Profiles
 * Any:
   * Cutoff: Unknown
   * Qualities: WAV, FLAC 24bit, FLAC, ALAC, OGG Vorbis Q10, AAC-320,
                OGG Vorbis Q9, MP3-320, AAC-VBR, MP3-VBR-V0, AAC-256,
                OGG Vorbis Q8, MP3-256, MP3-VBR-V2, OGG Vorbis Q7, MP3-224, WMA,
                AAC-192, OGG Vorbis Q6, MP3-192, MP3-160, OGG Vorbis Q5,
                MP3-128, MP3-112, MP3-96, MP3-80, MP3-64, MP3-56, MP3-48,
                MP3-40, MP3-32, MP3-24, MP3-16, MP3-8, Unknown
 * Lossless:
   * Cutoff: Lossless
   * Qualities: FLAC 24bit, FLAC, ALAC
 * Standard:
   * Cutoff: Low Quality Lossy
   * Qualities: OGG Vorbis Q10, AAC-320, OGG Vorbis Q9, MP3-320, AAC-VBR,
                MP3-VBR-V0, AAC-256, OGG Vorbis Q8, MP3-256, MP3-VBR-V2,
                OGG Vorbis Q7, MP3-224, WMA, AAC-192, OGG Vorbis Q6, MP3-192

#### Language Profiles
 * English

#### Metadata Profiles
 * Standard
   * Primary Type: Album
   * Secondary Type: Studio
   * Release Statuses: Official

#### Delay Profiles
 * Prefer Usenet
 * Usenet Delay: 60 minutes
 * Torrent Delay: 0 minutes

### Quality

|Quality         | Title          | Size Limit (30m/60m)      | Kbps Min | Kbps Max |
|----------------|----------------|---------------------------|----------|----------|
| Unknown        | Unknown        | 0B 0B 51.3MB 115.4MB      | 0        | 350      |
| MP3-8          | MP3-8| 0B 0B   | 1.5MB 3.3MB               | 0        | 10       |
| MP3-16         | MP3-16         | 0B 0B 2.9MB 6.6MB         | 0        | 20       |
| MP3-24         | MP3-24         | 0B 0B 4.4MB 9.9MB         | 0        | 30       |
| MP3-32         | MP3-32         | 0B 0B 5.9MB 13.2MB        | 0        | 40       |
| MP3-40         | MP3-40         | 0B 0B 6.6MB 14.8MB        | 0        | 45       |
| MP3-48         | MP3-48         | 0B 0B 8.1MB 18.1MB        | 0        | 55       |
| MP3-56         | MP3-56         | 0B 0B 9.5MB 21.4MB        | 0        | 65       |
| MP3-64         | MP3-64         | 0B 0B 11MB 24.7MB         | 0        | 75       |
| MP3-80         | MP3-80         | 0B 0B 13.9MB 31.3MB       | 0        | 95       |
| MP3-96         | MP3-96         | 0B 0B 16.1MB 36.3MB       | 0        | 110      |
| MP3-112        | MP3-112        | 0B 0B 18.3MB 41.2MB       | 0        | 125      |
| MP3-128        | MP3-128        | 0B 0B 20.5MB 46.1MB       | 0        | 140      |
| OGG Vorbis Q5  | OGG Vorbis Q5  | 0B 0B 25.6MB 57.7MB       | 0        | 175      |
| MP3-160        | MP3-160        | 0B 0B 25.6MB 57.7MB       | 0        | 175      |
| MP3-192        | MP3-192        | 0B 0B 30.8MB 69.2MB       | 0        | 210      |
| OGG Vorbis Q6  | OGG Vorbis Q6  | 0B 0B 30.8MB 69.2MB       | 0        | 210      |
| AAC-192        | AAC-192        | 0B 0B 30.8MB 69.2MB       | 0        | 210      |
| WMA            | WMA            | 0B 0B 51.3MB 115.4MB      | 0        | 350      |
| MP3-224        | MP3-224        | 0B 0B 35.9MB 80.7MB       | 0        | 245      |
| OGG Vorbis Q7  | OGG Vorbis Q7  | 0B 0B 35.9MB 80.7MB       | 0        | 245      |
| MP3-VBR-V2     | MP3-VBR-V2     | 0B 0B 41MB 92.3MB         | 0        | 280      |
| MP3-256        | MP3-256        | 0B 0B 41MB 92.3MB         | 0        | 280      |
| OGG Vorbis Q8  | OGG Vorbis Q8  | 0B 0B 41MB 92.3MB         | 0        | 280      |
| AAC-256        | AAC-256        | 0B 0B 41MB 92.3MB         | 0        | 280      |
| MP3-VBR-V0     | MP3-VBR-V0     | 0B 0B 51.3MB 115.4MB      | 0        | 350      |
| AAC-VBR        | AAC-VBR        | 0B 0B 51.3MB 115.4MB      | 0        | 350      |
| MP3-320        | MP3-320        | 0B 0B 51.3MB 115.4MB      | 0        | 350      |
| OGG Vorbis Q9  | OGG Vorbis Q9  | 0B 0B 51.3MB 115.4MB      | 0        | 350      |
| AAC-320        | AAC-320        | 0B 0B 51.3MB 115.4MB      | 0        | 350      |
| OGG Vorbis Q10 | OGG Vorbis Q10 | 0B 0B 80.6MB 181.3MB      | 0        | 550      |
| ALAC           | ALAC           | 0B 0B Unlimited Unlimited | 0        | 1500     |
| FLAC           | FLAC           | 0B 0B Unlimited Unlimited | 0        | 1500     |
| FLAC 24bit     | FLAC 24bit     | 0B 0B Unlimited Unlimited | 0        | 1500     |
| WAV            | WAV            | 0B 0B Unlimited Unlimited | 0        | 1500     |

### Indexers
 * Name: <YOUR_INDEXER_NAME>
 * Enable RSS Sync: yes
 * Enable Search: yes
 * URL: <INDEXER_API_URI>
 * APT Path: /api
 * API Key: <YOUR_API_KEY>
 * Categories: 3000,3010,3020,3030,3040
 * Remove year from search string: no
 * Search by Title: no

#### Options
 * Minimum Age: 0
 * Retention: 0
 * Minimum Size: 0
 * Prefer Special Indexer Flags: no
 * RSS Sync Interval: 0
 * Whitelisted Subtitle Tags: <empty>
 * Allow Hardcoded Subs: no
 * Parser Leniency: Strict

### Download Clients
 * Name: nzbget
 * Enable: yes
 * Host: <YOUR_NZBGET_IP>
 * Port: <YOUR_NZBGET_PORT>
 * Username: <API_USERNAME>
 * Password: <API_PASSWORD>
 * Category: music
 * Recent Priority: normal
 * Older Priority: normal
 * Add Paused: no
 * Use SSL: yes

#### Completed Download Handling
 * Enable: yes
 * Remove: yes

#### Failed Download Handling
 * Redownload: no
 * Remove: no

### General

#### Host
 * Bind Address: *
 * Port Number: 8686
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

#### Backups
 * Folder: Backups
 * Interval: 7
 * Retention: 28

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
