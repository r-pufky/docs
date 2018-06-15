Youtube Extractor
-----------------
Download and extract data from youtube videos.

1. [Installing Utilities](#installing-utilities)
1. [Snippets](#snippets)
1. [References](#references)

Installing Utilities
--------------------
```bash
curl http://yt-dl.org/latest/youtube-dl -o /usr/local/bin/youtube-dl
chmod +x /usr/local/bin/youtube-dl
apt install lame libav-tools
```

Snippets
--------
### Extract 320kbps Audio From Video
```bash
youtube-dl <url> --extract-audio --audio-format mp3 --audio-quality 320K --keep-video --add-metadata
```

### List all formats for a video
```bash
youtube-dl <url> -F
```

### Download only the 1080p vidoe/audio stream from a video
```bash
youtube-dl <url> 'bestvideo[height<=1080]+bestaudio/best[height<=1080]'
```

### Download a playlist
```bash
youtube-dl https://youtube.com/playlist?list=<LID> --yes-playlist
```

### Convert webm to mkv
```bash
ffmpeg -i your_input_filename.webm -qscale 0 your_outfile_name.mkv
```

References
----------
[youtube-dl Source download (latest)][1]

[youtube-dl github repo][2]

[Using youtube-dl][3]

[Using youtube-dl with LAME][4]

[Convert webm format][5]

[1]: http://yt-dl.org/latest/
[2]: http://rg3.github.io/youtube-dl/download.html
[3]: http://linuxaria.com/recensioni/how-to-download-youtube-video-or-audio-tracks-from-the-linux-terminal
[4]: http://www.linuxjournal.com/content/grabbing-your-music-youtube-do-it-your-way
[5]: https://askubuntu.com/questions/323944/convert-webm-to-other-formats
