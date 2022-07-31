.. _youtube-extractor:

Youtube Extractor
#################
Download and extract data from youtube videos.

.. code-block:: bash
  :caption: Install Utilities (linux).

  curl http://yt-dl.org/latest/youtube-dl -o /usr/local/bin/youtube-dl
  chmod +x /usr/local/bin/youtube-dl
  apt install lame libav-tools

Windows `requires manual installation of the binary and libav tools <https://stackoverflow.com/questions/30770155/ffprobe-or-avprobe-not-found-please-install-one>`_:

* `youtube-dl binary <http://ytdl-org.github.io/youtube-dl/download.html>`_
* `libav-tools <http://builds.libav.org/windows/release-gpl/>`

Copy all `.dll` and `.exe` from `libav-tools/win64/usr/bin` to the location of
`youtube-dl.exe`.

Snippets
********

.. code-block:: bash
  :caption: Extract 320kbps MP3 Audio From Video.

  youtube-dl --extract-audio --audio-format mp3 --audio-quality 320K --keep-video --add-metadata {URL}

.. code-block:: bash
  :caption: Extract FLAC Audio From Video.

  youtube-dl --extract-audio --audio-format flac --audio-quality 0 --add-metadata {URL}

.. code-block:: bash
  :caption: List all formats for a video and select the best ones.

  youtube-dl -F {URL}
  youtube-dl -f ###+### {URL}

.. code-block:: bash
  :caption: Download only the 1080p video/audio stream from a video.

  youtube-dl -f "bestvideo[height<=1080]+bestaudio/best[height<=1080]" {URL}

.. code-block:: bash
  :caption: Download a playlist.

  youtube-dl https://youtube.com/playlist?list={PLAYLIST ID} --yes-playlist

.. code-block:: bash
  :caption: Track Downloaded Videos for Archiving.

  youtube-dl --download-archive {FILE}

.. note::
  Download only videos not listed in file and adds any downloaded videos to
  the given file.

Azure Media Services
********************
These can be downloaded by forcing a `m3u8` stream and downloading. This works
for MS streaming vieos and other services using Azure Media Service backends.

#. :cmdmenu:`ctrl + shift + i --> network --> all`
#. Load the video/stream page
#. Locate the `manifest(format=...)` URI in Chrome Dev Tools
#. :cmdmenu:`RMB --> copy --> copy linke address`
#. Use with `youtube-dl`, changing manifest portion of the URI to
   `manifest(format=m3u8-aapl-v3)`

.. rubric:: References

#. `youtube-dl Source download (latest) <https://github.com/ytdl-org/youtube-dl/releases>`_
#. `youtube-dl github repo <https://rg3.github.io/youtube-dl/download.html>`_
#. `Using youtube-dl <http://linuxaria.com/recensioni/how-to-download-youtube-video-or-audio-tracks-from-the-linux-terminal>`_
#. `Using youtube-dl with LAME <https://www.linuxjournal.com/content/grabbing-your-music-youtube-do-it-your-way>`_
#. `Convert webm format <https://askubuntu.com/questions/323944/convert-webm-to-other-formats>`_
#. `Download any Azure Media Service <https://anduin.aiursoft.com/post/2020/5/15/download-any-azure-media-service-video-or-live-stream-with-ffmpeg>`_
