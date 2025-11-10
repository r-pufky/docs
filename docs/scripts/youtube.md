# Youtube
Download and extract data from youtube videos. **yt-dlp** is an actively
maintained fork of the defunct **yt-dl**.

## Install

=== "Linux"
    ``` bash
    curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /usr/local/bin/yt-dlp
    chmod a+rx /usr/local/bin/yt-dlp

    yt-dlp --update
    ```

=== "Windows"
    ``` powershell
    # libav-tools may be required: Copy all dll/exe files from
    # libav-tools/win64/usr/bin to location of yt-dlp.exe.
    winget install yt-dlp
    ```

    Reference:

    * http://builds.libav.org/windows/release-gpl

## Extract 320kbps MP3 Audio From Video
``` bash
yt-dlp --extract-audio --audio-format mp3 --audio-quality 320K --keep-video --add-metadata {URL}
```

## Extract FLAC Audio From Video.
``` bash
yt-dlp --extract-audio --audio-format flac --audio-quality 0 --add-metadata {URL}
```

## List all formats for a video and select the best ones.
``` bash
yt-dlp -F {URL}
yt-dlp -f ###+### {URL}
```

## Download only the 1080p video/audio stream from a video.
``` bash
yt-dlp -f "bestvideo[height<=1080]+bestaudio/best[height<=1080]" {URL}
```

## Download a playlist.
``` bash
yt-dlp https://youtube.com/playlist?list={PLAYLIST ID} --yes-playlist
```

## Track Downloaded Videos for Archiving.
``` bash
# This downloads only videos not listed in file and adds any downloaded videos
# to the given file.
yt-dlp --download-archive {FILE}
```

## Azure Media Services
These can be downloaded by forcing a **m3u8** stream and downloading. This
works for MS streaming videos and other services using Azure Media Service
backends.

1. ctrl + shift + i u2794 network ➔ all
2. Load the video/stream page.
3. Locate the **manifest(format=...)** URI in Chrome Dev Tools.
4. RMB ➔ copy ➔ copy link address
5. Use with **yt-dlp** changing manifest portion of the URI to
   **manifest(format=m3u8-aapl-v3)**

## References

* https://github.com/ytdl-org/yt-dlp/releases
* https://rg3.github.io/yt-dlp/download.html
* http://linuxaria.com/recensioni/how-to-download-youtube-video-or-audio-tracks-from-the-linux-terminal
* https://www.linuxjournal.com/content/grabbing-your-music-youtube-do-it-your-way
* https://askubuntu.com/questions/323944/convert-webm-to-other-formats
* https://anduin.aiursoft.com/post/2020/5/15/download-any-azure-media-service-video-or-live-stream-with-ffmpeg
