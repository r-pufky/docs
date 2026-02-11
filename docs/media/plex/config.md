# Configuration
Plex does not consistently apply casing to XML settings and are frequently
mis-spelled or inconsistently spelled. Order does not matter (Plex initially
only stores non-default values until it is set once, then the setting is always
stored, last changed setting last).

Options here reflect file analysis.

!!! abstract "Preferences.xml"
    0755 {USER}:{USER}

    ``` xml
    <!-- An empty preferences file will be auto-populated on service start. -->
    <!-- All preferences are stored in the Preferences element. -->
    <?xml version="1.0" encoding="utf-8"?>
    <Preferences />
    ```

## General

### FriendlyName
Server Friendly name.

  Variable    | Type | Default
 -------------|------|---------
 FriendlyName | str  | ''

### sendCrashReports
Send crash reports to Plex?

  Variable        | Type | Default
 -----------------|------|---------
 sendCrashReports | bool | false

### PushNotificationsEnabled
Enable Push Notifications? Allow this server to send push notifications to
mobile devices. Push notifications are delivered using Plex services. They're
associated with your account, and some of them may contain information about
the contents of your library.

  Variable                | Type | Default
 -------------------------|------|---------
 PushNotificationsEnabled | bool | false

### logDebug
Enable Plex Media Server debug logging? Debug logging enables additional detail
in the log files and is helpful in diagnosing problems.

  Variable | Type | Default
 ----------|------|---------
 logDebug  | bool | false

### LogVerbose
Enable Plex Media Server verbose logging? Verbose logging is only useful to
debug specific issues and should only be enabled if requested by support staff.

  Variable  | Type | Default
 -----------|------|---------
 LogVerbose | bool | false

### ButlerUpdateChannel
Server update channel. Does not circumvent entitlement (PlexPass) early
previews.

  Variable           | Type | Default | Values
 --------------------|------|---------|--------
 ButlerUpdateChannel | int  | 0       | **0**: Stable (public).
                     |      |         | **8**: Beta.

## [Remote Access][a]

### PublishServerOnPlexOnlineKey
Enable Remote Access? Publishing a server on Plex Online makes it automatically
available on your client devices without any configuration of your router.

  Variable                    | Type | Default
 -----------------------------|------|---------
 PublishServerOnPlexOnlineKey | bool | false

### ManualPortMappingMode
Enable manual port specification? You may need to enable this to establish a
direct connection from outside your network. You may also need to configure
your router.

  Variable             | Type | Default
 ----------------------|------|---------
 ManualPortMappingMode | bool | false

### AuthenticationMethod
Manul Port to Use.

  Variable            | Type | Default
 ---------------------|------|---------
 AuthenticationMethod | int  | 32400

### AuthenticationRequired
Internet upload speed (Kbps). Overall upload limit for all streams. WebUI uses
Mbps and should be converted accordingly.

  Variable             | Type | Default
 ----------------------|------|---------
AuthenticationRequired | int  | 0

### WanPerStreamMaxUploadRate
Limit remote stream bitrate (Kbps). Set the maximum bitrate of a single remote
stream from this server.

  Variable                 | Type | Default
 --------------------------|------|---------
 WanPerStreamMaxUploadRate | int  | 0 (Original - no limit).

## Library

### FSEventLibraryUpdatesEnabled
Scan my library automatically? Your library will be updated automatically when
changes to library folders are detected. Uses iNotify and will not work on
network mounted filesystems.

  Variable                    | Type | Default
 -----------------------------|------|---------
 FSEventLibraryUpdatesEnabled | bool | false

### FSEventLibraryPartialScanEnabled
Run a partial scan when changes are detected? When changes to library folders
are detected, only scan the folder that changed. Uses iNotify and will not work
on network mounted filesystems.

  Variable                        | Type | Default
 ---------------------------------|------|---------
 FSEventLibraryPartialScanEnabled | bool | false

### watchMusicSections
Include music libraries in automatic updates? Linux systems limit the maximum
number of watched directories; this may cause problems with large music
libraries. Uses iNotify and will not work on network mounted filesystems.

  Variable          | Type | Default
 -------------------|------|---------
 watchMusicSections | bool | false

### ScheduledLibraryUpdatesEnabled
Enable Scan my library periodically? Enable this option for network mounted
filesystems.

  Variable                      | Type | Default
 -------------------------------|------|---------
 ScheduledLibraryUpdatesEnabled | bool | false

### ScheduledLibraryUpdateInterval
Library scan interval (seconds).

  Variable                      | Type | Default
 -------------------------------|------|---------
 ScheduledLibraryUpdateInterval | int  | 86400

### autoEmptyTrash
Empty trash automatically after every scan?

  Variable      | Type | Default
 ---------------|------|---------
 autoEmptyTrash | bool | true

### allowMediaDeletion
Allow media deletion? The owner of the server will be allowed to delete media
files from disk.

  Variable          | Type | Default
 -------------------|------|---------
 allowMediaDeletion | bool | true

### OnDeckWindow
Weeks to consider for Continue Watching. Media that has not been watched in
this many weeks will not appear in Continue Watching.

  Variable    | Type | Default
 -------------|------|---------
 OnDeckWindow | int  | 16
### OnDeckLimit
Maximum number of Continue Watching items which will appear. Limits the number
of shows which will appear Continue Watching. Setting it too high can affect
performance.

  Variable   | Type | Default
 ------------|------|---------
 OnDeckLimit | int  | 40

### OnDeckIncludePremieres
Include season premieres in Continue Watching? New season premieres will always
appear no matter how many weeks have passed since watching.

  Variable              | Type | Default
 -----------------------|------|---------
 OnDeckIncludePremieres | bool | true

### LibraryVideoPlayedThreshold
Video played threshold. Set the progress percentage for video playback at which
point the video will be marked as played.

  Variable                   | Type | Default
 ----------------------------|------|---------
 LibraryVideoPlayedThreshold | int  | 95

### LibraryVideoPlayedAtBehaviour
Video play completion behavior. Decide whether to use end credits markers to
determine the played state of video items. LibraryVideoPlayedThreshold used
when markers are not available.

  Variable                     | Type | Default | Values
 ------------------------------|------|---------|--------
 LibraryVideoPlayedAtBehaviour | int  | 3       | **0**: At selected threshold percentage.
                               |      |         | **1**: At final credits marker position.
                               |      |         | **2**: At first credits marker position.
                               |      |         | **3**: Earliest between threshold percent and first credits marker (default).

### SmartShuffleMusic
Enable smart shuffling on artists and smart music playlists? Smart shuffling
prefers highly rated, popular and less recently heard tracks.

  Variable         | Type | Default
 ------------------|------|---------
 SmartShuffleMusic | bool | true

### MusicSeparateAlbumTypes
Group albums by type? Group into LPs, EPs & Singles, Compilations, Live Albums,
Demos and Remixes.

  Variable               | Type | Default | Values
 ------------------------|------|---------|---------------------------
 MusicSeparateAlbumTypes | str  | enabled | **enabled**
                         |      |         | **disabled**

### iTunesSharingEnabled
Enable iTunes plugin (requires server restart)?

  Variable            | Type | Default
 ---------------------|------|---------
 iTunesSharingEnabled | bool | false

### iTunesLibraryXmlPath
iTunes library XML path (absolute path)?

  Variable            | Type | Default
 ---------------------|------|---------
 iTunesLibraryXmlPath | str  | ''

### ScannerLowPriority
Run scanner tasks at a lower priority?

  Variable          | Type | Default
 -------------------|------|---------
 ScannerLowPriority | bool | false

### MarkerSource
Marker source. Credits markers can be generated locally and/or retrieved via an
online database. Online markers may not always exist, if this preference is set
to **any** then any locally detected markers are submitted anonymously back to
the online database for future use.

  Variable    | Type | Default | Values
 -------------|------|---------|---------------------------------------------
 MarkerSource | str  | any     | **any**: Both, try online first (default).
              |      |         | **cloud**: Online only (no local detection).
              |      |         | **local**: Local detection only.

### GenerateBIFBehavior
Generate video preview thumbnails. Video preview thumbnails provide live
updates in Now Playing and while seeking on supported apps. Thumbnail
generation may take a long time, cause high CPU usage, and consume additional
disk space. You can turn off thumbnail generation for individual libraries in
the library's advanced settings.


  Variable          | Type | Default | Values
 -------------------|------|---------|--------
GenerateBIFBehavior | str  | never   | **never**: never.
                    |      |         | **scheduled**: as a scheduled task.
                    |      |         | **asap**: as a scheduled task and when media is added.

### GenerateIntroMarkerBehavior
Generate intro video markers. Detects show intros, exposing the **Skip Intro**
button in clients.

  Variable                   | Type | Default | Values
 ----------------------------|------|---------|--------
 GenerateIntroMarkerBehavior | str  | asap    | **never**: never.
                             |      |         | **scheduled**: as a scheduled task.
                             |      |         | **asap**: as a scheduled task and when media is added.

### GenerateCreditsMarkerBehavior
Generate credits video markers. Detects movie and episode end credits.

  Variable                     | Type | Default | Values
 ------------------------------|------|---------|--------
 GenerateCreditsMarkerBehavior | str  | asap    | **never**: never.
                               |      |         | **scheduled**: as a scheduled task.
                               |      |         | **asap**: as a scheduled task and when media is added.

### GenerateAdMarkerBehavior
Generate ad video markers. Detects movie and episode ads.

  Variable                | Type | Default   | Values
 -------------------------|------|-----------|--------
GenerateAdMarkerBehavior  | str  | scheduled | **never**: never.
                          |      |           | **scheduled**: as a scheduled task.
                          |      |           | **asap**: as a scheduled task and when media is added.

### GenerateVADBehavior
Generate voice activity data. Detects voice activity data for movies and
episodes. This is used to help synchronize subtitles to the audio track. This
detection can be toggled per library by editing the individual library and
navigating to the advanced section.

  Variable          | Type | Default   | Values
 -------------------|------|-----------|--------
GenerateVADBehavior | str  | scheduled | **never**: never.
                    |      |           | **scheduled**: as a scheduled task.
                    |      |           | **asap**: as a scheduled task and when media is added.

### GenerateChapterThumbBehavior
Generate chapter thumbnails. Chapter thumbnails provide images in the chapter
view on supported apps. They can take a long time to generate and consume
additional disk space.

  Variable                    | Type | Default   | Values
 -----------------------------|------|-----------|--------
 GenerateChapterThumbBehavior | str  | scheduled | **never**: never.
                              |      |           | **scheduled**: as a scheduled task.
                              |      |           | **asap**: as a scheduled task and when media is added.

### LoudnessAnalysisBehavior
Analyze audio tracks for loudness. Loudness analysis allows various features,
such as loudness leveling and smart transitions. It can take a long time to
complete when analyzing many tracks, and cause high CPU usage.

  Variable                | Type | Default   | Values
 -------------------------|------|-----------|--------
 LoudnessAnalysisBehavior | str  | scheduled | **never**: never.
                          |      |           | **scheduled**: as a scheduled task.
                          |      |           | **asap**: as a scheduled task and when media is added.

### MusicAnalysisBehavior
Analyze audio tracks for sonic features. Sonic analysis allows various
features, such as track radio. It can take a long time to complete when
analyzing many tracks, and cause high CPU usage.

  Variable             | Type | Default   | Values
 ----------------------|------|-----------|--------
 MusicAnalysisBehavior | str  | scheduled | **never**: never.
                       |      |           | **scheduled**: as a scheduled task.
                       |      |           | **asap**: as a scheduled task and when media is added.

### LocationVisibility
Location visibility. Server owners may wish to restrict who can see location
names for items which contain geolocation metadata. By default only the server
owner will have visibility of these.

  Variable          | Type | Default | Values
 -------------------|------|---------|--------
 LocationVisibility | int  | 1       | **1**: Admin only.
                    |      |         | **2**: Everyone.

### DatabaseCacheSize
Database Cache Size (MB). Set the size of the main database cache size in MB.
Increasing size increases exposure for DB data loss if a crash happens before
updates are written to disk.

  Variable         | Type | Default
 ------------------|------|---------
 DatabaseCacheSize | int  | 40

## Network

### IPNetworkType
Client network. Network to advertise to clients.

  Variable     | Type | Default   | Values
 --------------|------|-----------|--------
 IPNetworkType | str  | dualstack | **v4only**: Advertise only IPv4.
               |      |           | **v6only**: Advertise only IPv6.
               |      |           | **dualstack**: Advertise on both IPv4/6 networks.

### secureConnections
Use Secure connections? When enabled, some unencrypted connections (originating
from the Media Server computer) will still be allowed and apps that don't
support secure connections will not be able to connect at all.

  Variable         | Type | Default | Values
 ------------------|------|---------|--------
 secureConnections | bool | false   | **True**: Required.
                   |      |         | **False**: Preferred (default).

### customCertificatePath
Custom certificate location. Absolute path to a PKCS #12 file containing a
certificate and private key to enable TLS support on a custom domain.

  Variable             | Type | Default
 ----------------------|------|---------
 customCertificatePath | str  | ''

### customCertificateKey
Custom certificate encryption key.

  Variable            | Type | Default
 ---------------------|------|---------
 customCertificateKey | str  | ''

### customCertificateDomain
Custom certificate domain. Domain name to be published to plex.tv using your
mapped port; must match a name from the custom certificate file.

  Variable               | Type | Default
 ------------------------|------|---------
 customCertificateDomain | str  | ''

### PreferredNetworkInterface
Preferred network interface. The network interface local clients will use to
connect.

 Variable                  | Type | Default | Values
 --------------------------|------|---------|--------
 PreferredNetworkInterface | str  | ''      | **''**: Any network connection.
                           |      |         | **{ADAPTER}**: Use specified location interface (e.g. enp4s0, etc).

### DisableTLSv1_0
Use Strict TLS configuration? Disables legacy weak ciphers, increases DH group
size, and switches to ECDSA certificates when renewing. May prevent older
clients from connecting.

  Variable      | Type | Default
 ---------------|------|---------
 DisableTLSv1_0 | bool | false

### GdmEnabled
Enable local network discovery (GDM)? This enables the media server to discover
other servers and players on the local network.

  Variable  | Type | Default
 -----------|------|---------
 GdmEnabled | bool | true

### WanPerUserStreamCount
Remote streams allowed per user. Maximum number of simultaneous streams each
user is allowed when not on the local network.

 Variable              | Type | Default | Values
 ----------------------|------|---------|--------
 WanPerUserStreamCount | int  | 0       | **0**: Unlimited connections.
                       |      |         | **1-20**: Max number of connections.

### LanNetworksBandwidth
LAN networks bandwidth enforcement. Comma separated list of IP addresses or
IP/netmask entries for networks that will be considered to be on the local
network when enforcing bandwidth restrictions. If set, all other IP addresses
will be considered to be on the external network and will be subject to
external network bandwidth restrictions. If left blank, only the server's
subnet is considered to be on the local network.

 Variable             | Type | Default | Values
 ---------------------|------|---------|--------
 LanNetworksBandwidth | str  | ''      | **{CIDR}**: CIDR notation.
                      |      |         | **{IP}**: IPv4 or IPv6.

### MinutesAllowedPaused
Terminate Sessions Paused for Longer Than X (minutes). Terminate any sessions
which have been paused for longer than specified amount of time in minutes.
Audio-only sessions and live sessions are excluded.

 Variable             | Type | Default | Values
 ---------------------|------|---------|--------
 MinutesAllowedPaused | int  | 0       | **0**: No limit.

### TreatWanIpAsLocal
Treat WAN IP as LAN bandwidth? Treat incoming requests from this network's WAN
IP address as LAN requests in terms of bandwidth. This often occurs when DNS
rebinding protection is in place and clients on the LAN cannot contact the
server directly but instead have to go through the WAN IP address.

 Variable          | Type | Default
 ------------------|------|---------
 TreatWanIpAsLocal | bool | true

### RelayEnabled
Enable Relay? Relay allows connections to the server through a proxy relay when
the server is not accessible otherwise. Proxy relay is bandwidth limited.

 Variable     | Type | Default
 -------------|------|---------
 RelayEnabled | bool | true

### customConnections
Custom server access URLs. Comma separated list of URLs (http or https) which
are published up to plex.tv for server discovery.

 Variable          | Type | Default
 ------------------|------|---------
 customConnections | str  | ''

### allowedNetworks
Comma separated list of IP addresses and networks that are allowed without
auth. List of IP addresses or IP/netmask entries for networks that are allowed
to access Plex Media Server without logging in. When the server is signed out
and this value is set, only localhost and addresses on this list will be
allowed.

Any app connecting to the server this way without being signed in will be
treated as the admin/owner. That means access to all libraries as well as the
ability to change server settings. We strongly encourage using Plex apps that
allow signing in to accounts to ensure the highest security for your computer
and network.

 Variable        | Type | Default | Values
 ----------------|------|---------|--------
 allowedNetworks | str  | ''      | **{CIDR}**: CIDR notation.
                 |      |         | **{IP}**: IPv4 or IPv6.

### WebHooksEnabled
Use webhooks? Allow this server to send events to external services.

 Variable        | Type | Default
 ----------------|------|---------
 WebHooksEnabled | bool | true

## Transcoder

### TranscoderQuality
Transcoder quality. Quality profile used by the transcoder.

 Variable          | Type | Default | Values
 ------------------|------|---------|--------
 TranscoderQuality | int  | 0       | **0**: Automatic.
                   |      |         | **1**: Prefer higher speed encoding.
                   |      |         | **2**: Prefer higher quality encoding.
                   |      |         | **3**: Make my CPU hurt.

### TranscoderTempDirectory
Transcoder temporary directory.

 Variable                | Type | Default
 ------------------------|------|---------
 TranscoderTempDirectory | str  | /tmp

### DownloadsTempDirectory
Downloads temporary directory.

 Variable               | Type | Default
 -----------------------|------|---------
 DownloadsTempDirectory | str  | /tmp

### TranscoderThrottleBuffer
Transcoder default throttle buffer (seconds). Number of seconds to buffer
before throttling the transcoder. Playback will not start (even with direct
streaming) until buffer is full - if playback takes a long time to start,
reduce this value.

 Variable                 | Type | Default
 -------------------------|------|---------
 TranscoderThrottleBuffer | int  | 60

### TranscoderH264BackgroundPreset
Background transcoding x264 preset. The x264 preset value used for background
transcoding (Sync and Media Optimizer). Slower values will result in better
video quality and smaller file sizes, but will take significantly longer to
complete processing.

 Variable                       | Type | Default  | Values
 -------------------------------|------|----------|--------
 TranscoderH264BackgroundPreset | str  | veryfast | **ultrafast**
                                |      |          | **superfast**
                                |      |          | **veryfast**
                                |      |          | **faster**
                                |      |          | **fast**
                                |      |          | **medium**
                                |      |          | **slow**
                                |      |          | **slower**
                                |      |          | **veryslow**

### TranscoderToneMapping
Enable HDR tone mapping? Transcoded HDR content will appear highly dimmed and
desaturated with this disabled. Additional driver components may be needed to
support hardware transcoding with this feature enabled; see our support
articles for further details.

[AMD iGPU's will pass encoding frames][b] back and forth between iGPU and CPU
drastically reducing performance. Recommend disabling for AMD iGPU.

 Variable              | Type | Default
 ----------------------|------|---------
 TranscoderToneMapping | bool | true

### TranscoderToneMappingAgorithm
Tonemapping Algorithm. Algorithm to use when performing HDR tone mapping.

!!! info
    XML var IS mis-spelled.

 Variable                      | Type | Default | Values
 ------------------------------|------|---------|--------
 TranscoderToneMappingAgorithm | str  | hable   | **linear**: Stretch entire reference gamut to a linear multiple of display.
                               |      |         | **gamma**: Fit a logarithmic transfer between the tone curves.
                               |      |         | **clip**: Hard-clip any out-of-range values. Use it for perfect color accuracy for in-range values, while distorting out-of-range values.
                               |      |         | **reinhard**: Preserve overall image brightness with a simple curve, using nonlinear contrast, which results in flattening details and degrading color accuracy.
                               |      |         | **hable**: Preserve both dark and bright details better than reinhard, at the cost of slightly darkening everything. Use it when detail preservation is more important than color and brightness accuracy.
                               |      |         | **mobius**: Smoothly map out-of-range values, while retaining contrast and colors for in-range material as much as possible. Use it when color accuracy is more important than detail preservation.

### TranscoderCanOnlyRemuxVideo
Disable video stream transcoding? Disable transcoding of the video stream in
transcoder operations. With this set, the transcoder may still transcode audio
as well as remux video.

 Variable                    | Type | Default
 ----------------------------|------|---------
 TranscoderCanOnlyRemuxVideo | bool | false

### HardwareAcceleratedCodecs
Use hardware acceleration when available? Plex Media Server will attempt to use
hardware-accelerated video codecs when encoding and decoding video. Hardware
acceleration can make transcoding faster and allow more simultaneous video
transcodes, but it can also reduce video quality and compatibility.

 Variable                  | Type | Default
 --------------------------|------|---------
 HardwareAcceleratedCodecs | bool | true

### HardwareAcceleratedEncoders
Use hardware-accelerated video encoding? If hardware acceleration is enabled,
this controls whether it's used for encoding, in addition to decoding.

 Variable                    | Type | Default
 ----------------------------|------|---------
 HardwareAcceleratedEncoders | bool | true

### TranscoderHEVCEncoding
Enable HEVC video Encoding (experimental)? Enable transcoding using the HEVC
codec if it is supported by the client.

 Variable               | Type | Default | Values
 -----------------------|------|---------|--------
 TranscoderHEVCEncoding | str  | always  | **never**: Never use HEVC video encoding.
                        |      |         | **hevc-sources**: Encode HEVC sources only.
                        |      |         | **always**: Always use HEVC video encoding.

### TranscoderHEVCOptimize
Enable HEVC Optimization (experimental)? If available, enable use of HEVC while
optimizing your media.

 Variable               | Type | Default
 -----------------------|------|---------
 TranscoderHEVCOptimize | bool | false

### HardwareDevicePath
Hardware transcoding device. The GPU or other hardware device that will be used
for transcoding. Path is automatically generated when device is set in WebUI.

 Variable           | Type | Default | Values
 -------------------|------|---------|--------
 HardwareDevicePath | str  | ''      | **''**: Auto device or auto-generated Plex value (default).
                    |      |         | **{PCI_ID}@{DEVICE_ID}**: Hardware address '10de:1eb1:10de:12a0@0000:42:00.0'.

### TranscodeCountLimit
Maximum simultaneous video transcodes. Limit the number of simultaneous video
transcode streams server can utilize.

 Variable            | Type | Default | Values
 --------------------|------|---------|--------
 TranscodeCountLimit | int  | 0       | **0**: Unlimited connections (default).
                     |      |         | **1-20**: Max number of connections.

### _CPU-TranscodeCountLimit
Maximum simultaneous CPU transcodes. Limit the number of simultaneous video
transcode streams your server can utilize on your CPU.

 Variable                 | Type | Default | Values
 -------------------------|------|---------|--------
 _CPU-TranscodeCountLimit | int  | 0       | **0**: Unlimited connections.
                          |      |         | **1-20**: Max number of connections.

### OptimizerTranscodeCountLimit
Maximum simultaneous background video transcodes. Limit the number of
simultaneous video transcode your server can utilize for the optimizer and
downloads.

 Variable                     | Type | Default | Values
 -----------------------------|------|---------|--------
 OptimizerTranscodeCountLimit | int  | 0       | **0**: Unlimited connections.
                              |      |         | **1-20**: Max number of connections.

## DLNA

### DlnaEnabled
Enable the DLNA server? This allows the server to stream media to DLNA (Digital
Living Network Alliance) devices.

 Variable    | Type | Default
 ------------|------|---------
 DlnaEnabled | bool | false

### DlnaClientPreferences
DLNA client preferences. These should generally not be altered.

 Variable              | Type | Default
 ----------------------|------|---------
 DlnaClientPreferences | str  | ''

### DlnaReportTimeline
DLNA server timeline reporting? Enable the DLNA server to report timelines for
video play activity.

 Variable           | Type | Default
 -------------------|------|---------
 DlnaReportTimeline | bool | true

### DlnaDefaultProtocolInfo
DLNA default protocol info. Protocol info string used in GetProtocolInfo
responses by the DLNA server. Comma separated list of protocols.

 Variable                | Type | Default
 ------------------------|------|---------
 DlnaDefaultProtocolInfo | str  | http-get:*:video/mpeg:*,http-get:*:video/mp4:*,http-get:*:video/vnd.dlna.mpeg-tts:*,http-get:*:video/avi:*,http-get:*:video/x-matroska:*,http-get:*:video/x-ms-wmv:*,http-get:*:video/wtv:*,http-get:*:audio/mpeg:*,http-get:*:audio/mp3:*,http-get:*:audio/mp4:*,http-get:*:audio/x-ms-wma*,http-get:*:audio/wav:*,http-get:*:audio/L16:*,http-get:*image/jpeg:*,http-get:*image/png:*,http-get:*image/gif:*,http-get:*image/tiff:*

### DlnaDeviceDiscoveryInterval
DLNA media renderer discovery interval (seconds). Number of seconds between
DLNA media renderer discovery requests.

 Variable                    | Type | Default
 ----------------------------|------|---------
 DlnaDeviceDiscoveryInterval | int  | 60

### DlnaAnnouncementLeaseTime
DLNA server announcement lease time (seconds). Duration in seconds of DLNA
Server SSDP announcement lease time.

 Variable                  | Type | Default
 --------------------------|------|---------
 DlnaAnnouncementLeaseTime | int  | 1800

### DlnaDescriptionIcons
DLNA server description icons. Icons offered by DLNA server when devices
request server description. Comma separated lists separated by semicolons.

 Variable             | Type | Default
 ---------------------|------|---------
 DlnaDescriptionIcons | str  | png,jpeg;260x260,120x120,48x48

## Scheduled Tasks

### ButlerStartHour
Time at which tasks start to run (24 hour clock). The time at which the server
starts running background maintenance tasks.

 Variable        | Type | Default | Values
 ----------------|------|---------|--------
 ButlerStartHour | int  | 2       | **0**: Midnight.

### ButlerEndHour
Time at which tasks stop running (24 hour clock). The time at which the
background maintenance tasks stop running.

 Variable      | Type | Default | Values
 --------------|------|---------|--------
 ButlerEndHour | int  | 5       | **0**: Midnight.

### ButlerTaskBackupDatabase
Backup database every three days?

 Variable                 | Type | Default
 -------------------------|------|---------
 ButlerTaskBackupDatabase | bool | true

### ButlerDatabaseBackupPath
Backup directory.

 Variable                 | Type | Default
 -------------------------|------|---------
 ButlerDatabaseBackupPath | str  | /var/lib/plex/Plex Media Server/Plug-in Support/Databases

### ButlerTaskOptimizeDatabase
Optimize database every week?

 Variable                   | Type | Default
 ---------------------------|------|---------
 ButlerTaskOptimizeDatabase | bool | true

### ButlerTaskCleanOldBundles
Remove old bundles every week?

 Variable                  | Type | Default
 --------------------------|------|---------
 ButlerTaskCleanOldBundles | bool | true

### ButlerTaskCleanOldCacheFiles
Remove old cache files every week?

 Variable                     | Type | Default
 -----------------------------|------|---------
 ButlerTaskCleanOldCacheFiles | bool | true

### ButlerTaskRefreshLocalMedia
Refresh local metadata every three days?

 Variable                    | Type | Default
 ----------------------------|------|---------
 ButlerTaskRefreshLocalMedia | bool | true

### ButlerTaskRefreshLibraries
Update all libraries during maintenance?

 Variable                   | Type | Default
 ---------------------------|------|---------
 ButlerTaskRefreshLibraries | bool | false

### ButlerTaskUpgradeMediaAnalysis
Upgrade media analysis during maintenance?

 Variable                       | Type | Default
 -------------------------------|------|---------
 ButlerTaskUpgradeMediaAnalysis | bool | true

### ButlerTaskRefreshPeriodicMetadata
Refresh library metadata periodically?

 Variable                          | Type | Default
 ----------------------------------|------|---------
 ButlerTaskRefreshPeriodicMetadata | bool | true

### ButlerTaskDeepMediaAnalysis
Perform extensive media analysis during maintenance?

 Variable                    | Type | Default
 ----------------------------|------|---------
 ButlerTaskDeepMediaAnalysis | bool | true

## Extras

### CinemaTrailersType
Choose Cinema Trailers from?

 Variable           | Type | Default | Values
 -------------------|------|---------|--------
 CinemaTrailersType | bool | true    | **False**: All movies.
                    |      |         | **True**: Only unwatched movies (default).

### CinemaTrailersFromLibrary
Include Cinema Trailers from movies in my library?

 Variable                  | Type | Default
 --------------------------|------|---------
 CinemaTrailersFromLibrary | bool | true

### CinemaTrailersFromTheater
Include Cinema Trailers from new and upcoming movies in theaters? PlexPass
entitlement only.

 Variable                  | Type | Default
 --------------------------|------|---------
 CinemaTrailersFromTheater | bool | false

### CinemaTrailersFromBluRay
Include Cinema Trailers from new and upcoming movies on Blu-ray? PlexPass
entitlement only.

 Variable                 | Type | Default
 -------------------------|------|---------
 CinemaTrailersFromBluRay | bool | false

### CinemaTrailersIncludeEnglish
Always include English language Cinema Trailers? For trailers of movies not in
my library.

 Variable                     | Type | Default
 -----------------------------|------|---------
 CinemaTrailersIncludeEnglish | bool | true

### CinemaTrailersPrerollID
Movie pre-roll videos. List of absolute paths to videos for pre-roll before
playing a movie.

 Variable                | Type | Default | Values
 ------------------------|------|---------|--------
 CinemaTrailersPrerollID | str  | ''      | Comma separated list will play **all** videos before movie.
                         |      |         | semi-colon separated list will play **one random** video before movie.

### GlobalMusicVideoPath
Global music videos path.

 Variable             | Type | Default
 ---------------------|------|---------
 GlobalMusicVideoPath | str  | ''

## Libraries

### MergedRecentlyAdded
Merge Recently Added items? Recently Added items from the same media type will
be combined together on Home for libraries Recommended to Home. Only content
from libraries pinned to the app sidebar will appear in Merged Recently Added
recommendations.

 Variable            | Type | Default
 --------------------|------|---------
 MergedRecentlyAdded | bool | false

## Live TV & DVR
If you have a tuner card, please help out by working with the author and
providing anonymous configuration information to codify options.

### DvrIncrementalEpgLoader
Enable incremental DVR electronic program guides loader? PlexPass entitlement
only.

 Variable                | Type | Default
 ------------------------|------|---------
 DvrIncrementalEpgLoader | bool | false

## Identifiers
Auto-generated Plex options to uniquely identifier a Plex server. Carry these
settings over to new installations to retain Plex server identification.

### MachineIdentifier

 Variable          | Type | Default
 ------------------|------|---------
 MachineIdentifier | str  | {AUTO}

### ProcessedMachineIdentifier

 Variable                   | Type | Default
 ---------------------------|------|---------
 ProcessedMachineIdentifier | str  | {AUTO}

### AnonymousMachineIdentifier

 Variable                   | Type | Default
 ---------------------------|------|---------
 AnonymousMachineIdentifier | str  | {AUTO}

## Stateful
Not user configurable.

Configuration options here are not found directly in the server UI. These are
generally updated/added automatically during Plex usage, but may be set after
initial Plex execution. These are kept to document variables in case future
releases migrate these to configurable values or migrated into the DB directly.

Changing these values have no effect.

### AcceptedEULA
Accept Plex EULA? Plex cannot be used without accepting the EULA.

 Variable     | Type | Default
 -------------|------|---------
 AcceptedEULA | bool | true

### CertificateUUID
Let's Encrypt certificate UUID. [Plex automatically creates][c] and distributes
certificates to support it's own HTTPS by default scheme. These are
automatically issued on first install.

Do **NOT** use your own Let's Encrypt material.

 Variable        | Type | Default | Values
 ----------------|------|---------|--------
 CertificateUUID | str  | ''      | **{UUIDv4}**: UUIDv4a, generated random data.

### CertificateVersion
Let's Encrypt [certificate version][c].

 Variable           | Type | Default | Values
 -------------------|------|---------|--------
 CertificateVersion | str  | 3       | **1**: TLSv1.1.
                    |      |         | **2**: TLSv1.2.
                    |      |         | **3**: TLSv1.3.

### collectUsageData
Collect usage data? Sends usage data to plex. This [has been deprecated][d] in
lieu of other mechanisms now, however this is kept in case any edge cases still
use this variable. This is no longer configurable in the WebUI.

 Variable         | Type | Default
 -----------------|------|---------
 collectUsageData | bool | true

### GlobalMusicVideoPathMigrated
Global music video paths migrated from legacy config? Old Plex installs tracked
music videos separately from other media; these are now integrated and tracked
in Plex DB. This should always be true unless OldestPreviousVersion=legacy.

 Variable                     | Type | Default | Values
 -----------------------------|------|---------|--------
 GlobalMusicVideoPathMigrated | bool | true    | **False**: Force Plex to migrate music video paths on next start.
                              |      |         | **True**: Paths already migrated or auto-generated Plex value (default).

### LanguageInCloud
Use plex cloud settings for language options? This overrides local settings in
the Language section. Now force enabled by plex.

 Variable        | Type | Default
 ----------------|------|---------
 LanguageInCloud | bool | true

### LastAutomaticMappedPort
Last port automatically mapped with PublishServerOnPlexOnlineKey.

 Variable                | Type | Default
 ------------------------|------|---------
 LastAutomaticMappedPort | int  | 0

### MetricsEpoch
Use year 2038+ safe epochs for timestamps? Old Plex installs used unix
timestamp epochs which will generate errors after 2038. This should always be
true unless plex_cfg_oldest_previous_version=legacy.

 Variable     | Type | Default | Values
 -------------|------|---------|--------
 MetricsEpoch | int  | 1       | **1**: Use 2038 safe epochs or auto-generated Plex value.
              |      |         | **0**: Use unix timestamp.

### OldestPreviousVersion
Oldest previously installed plex version. Version is set on initial Plex
installation.

 Variable              | Type | Default | Values
 ----------------------|------|---------|--------
 OldestPreviousVersion | str  | ''      | **''**: auto-generated Plex value.
                       |      |         | **legacy**: Legacy plex install (1st gen plex >10 years ago).
                       |      |         | **{VERSION}**: Last installed plex version (e.g. '1.28.2.6106-44a5bbd28').

### PubSubServer
Plex pubsub server IP.

 Variable     | Type | Default
 -------------|------|---------
 PubSubServer | str  | 184.105.148.115

### PubSubServerPing
Latest plex pubsub server ping.

 Variable         | Type | Default
 -----------------|------|---------
 PubSubServerPing | int  | 65

### PubSubServerRegion
Plex pubsub server region.

 Variable           | Type | Default
 -------------------|------|---------
 PubSubServerRegion | str  | sjc

## Service

### PlexOnlineUsername
Plex username.

 Variable           | Type | Default
 -------------------|------|---------
 PlexOnlineUsername | str  | ''

### PlexOnlineMail
Plex user email.

 Variable       | Type | Default
 ---------------|------|---------
 PlexOnlineMail | str  | ''

### PlexOnlineToken
Plex user access token.

A new plex install (or one requiring a new access token after revocation)
requires the initial manual setup process to be run locally. Use a SSH tunnel
to access the server-side configuration page.

``` bash
ssh -L 32400:localhost:32400 {plex_host}
```

Then connect to http://localhost:32400/web and run through the configuration
steps.

1. Select media libraries to use.
2. Sign-in on server: upper right ➔ sign-in.
3. Select server and claim: claim now ➔ claim server.
4. Update **plex_cfg_online_token** with new token in found in
   **plexmediaserver.xml** located in **plex_srv_application_support_dir**.

Enable Secure Server Connection

1. Ensure **32400** is forwarded from the router.
2. Enable [DNS Rebinding][e] on router.

 Variable        | Type | Default
 ----------------|------|---------
 PlexOnlineToken | str  | ''

### PlexOnlineHome
Use this server as user home (default) server?

 Variable       | Type | Default
 ---------------|------|---------
 PlexOnlineHome | bool | true

## Experimental Settings
[Additional settings][f] in Preferences.xml that are typically hidden from
users.

All options are not configured in Preferences unless explicitly set. Any option
that is promoted (e.g. added to the UI) are actively migrated to standardized
sections.

Only set these options when explicitly fixing an issue.

### AlbumSort
Album sort. A field:direction value for the default album sort. 'year',
'title', etc. PMS 1.4.1+ has UI setting per library/per artist.

 Variable  | Type | Default
 ----------|------|---------
 AlbumSort | str  | year:desc

### ArticleStrings
Article strings. A comma-separated list of words considered to be grammatical
articles, which are removed in sort titles.

 Variable       | Type | Default
 ---------------|------|---------
 ArticleStrings | str  | the, das, der, a, an, el, la

### BackgroundTranscodeLowPriority
Background transcode low priority. Makes background transcodes have a lower
priority than active streaming when enabled.

 Variable                       | Type | Default | Values
 -------------------------------|------|---------|--------
 BackgroundTranscodeLowPriority | str  | 1       | **1**: Enabled.
                                |      |         | **0**: Disabled.

### DlnaPlatinumLoggingLevel
DLNA platinum logging level. Sets level for the separate 'Neptune DLNA'.

 Variable                 | Type | Default | Values
 -------------------------|------|---------|--------
 DlnaPlatinumLoggingLevel | str  | OFF     | **OFF**: Disabled.
                          |      |         | **ON**: Enabled.

### enableLocalSecurity
Enable local security. Determines whether Plex Media Server must be
claimed/signed-in to access it.

 Variable            | Type | Default | Values
 --------------------|------|---------|--------
 enableLocalSecurity | int  | 1       | **1**: Enabled.
                     |      |         | **0**: Disabled.

### GenerateBIFFrameInterval
Generate BIF frame interval. For video preview thumbnails, sets how often (in
seconds) we create the thumbnail. This directly affects library scanning
performance and storage space. A more reasonable value if there are freezes
during scanning is the scrub interval for the player used (10-15).

 Variable                 | Type | Default
 -------------------------|------|---------
 GenerateBIFFrameInterval | int  | 2

### GenerateBIFKeyframesOnly
Generate BIF keyframes only. When generating video preview thumbnails for
playback, only look at keyframes in the video. Greatly speeds up processing and
reduces CPU usage.

 Variable                 | Type | Default | Values
 -------------------------|------|---------|--------
 GenerateBIFKeyframesOnly | int  | 1       | **1**: Enabled.
                          |      |         | **0**: Disabled.

### LocalAppDataPath
local appdata path. Set the location of of the Plex Media Server data directory
(Windows only).

 Variable         | Type | Default
 -----------------|------|---------
 LocalAppDataPath | str  | C:\Users\{USER}\AppData\Local\Plex Media Server

### LogMemoryUse
Log memory use. Set Plex Media Server to log memory use and the system total
used memory in Plex Media Server logs. A server restart is required for the
change to take effect. Not recommended for normal usage. Requires PMS v1.20.2
or newer. Not available for FreeBSD or NVIDIA SHIELD.

 Variable     | Type | Default
 -------------|------|---------
 LogMemoryUse | int  | **0**: Disabled.
              |      | **1**: Enabled.

### LogNumFiles
Log num files. Number of past log files to retain.

 Variable    | Type | Default
 ------------|------|---------
 LogNumFiles | int  | 5

### LongRunningJobThreads
Long running job threads. Sets how many threads can be used for long-running
jobs, such as Sonic Analysis (Default is half the total threads for the
processor).

 Variable              | Type | Default
 ----------------------|------|---------
 LongRunningJobThreads | int  | 4

### RadioDaysSinceLastPlayed
Radio days since last played. When playing a Radio or Smart Shuffle, Plex
prefers to include tracks that have not been played recently. This sets that
recent period (default is 2).

 Variable                 | Type | Default
 -------------------------|------|---------
 RadioDaysSinceLastPlayed | int  | 2

### RadioDirectoryLimit
Radio directory limit. Controls how many genre, style, or mood radios are
exposed, on clients that support those radio types.

 Variable            | Type | Default
 --------------------|------|---------
 RadioDirectoryLimit | int  | 50

### TranscoderDefaultDuration
Transcoder default duration. Duration in minutes to use when transcoding
something with an unknown duration (120 is the default if nothing set).

 Variable                  | Type | Default
 --------------------------|------|---------
 TranscoderDefaultDuration | int  | 120

### TranscoderH264OptionsOverride
Transcoder H264 options override. The x264 preset to use when transcoding.

 Variable                      | Type | Default
 ------------------------------|------|---------
 TranscoderH264OptionsOverride | str  | veryfast

### TranscoderLogLevel
Transcoder log level. The log level for the Plex transcoder itself.

 Variable           | Type | Default | Values
 -------------------|------|---------|--------
 TranscoderLogLevel | str  | error   | **error**
                    |      |         | **verbose**

### TranscoderPhotoFileSizeLimitMiB
Transcoder photo file size limit MiB. Maximum photo size to be tagged or
transcoded (in mebibytes).

 Variable                        | Type | Default
 --------------------------------|------|---------
 TranscoderPhotoFileSizeLimitMiB | int  | 100

[a]: https://support.plex.tv/articles/200931138-troubleshooting-remote-access
[b]: https://old.reddit.com/r/PleX/comments/1hbn73h/hw_transcoding_with_ryzen_igpu/
[c]: https://words.filippo.io/how-plex-is-doing-https-for-all-its-users/
[d]: https://www.plex.tv/about/privacy-legal/privacy-preferences-deprecated-june-2024/
[e]: https://support.plex.tv/articles/206225077-how-to-use-secure-server-connections
[f]: https://support.plex.tv/articles/201105343-advanced-hidden-server-settings
