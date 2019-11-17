.. _youtube-extractor:

Youtube Extractor
#################
Download and extract data from youtube videos.

.. code-block:: bash
  :caption: Install Utilities.

  curl http://yt-dl.org/latest/youtube-dl -o /usr/local/bin/youtube-dl
  chmod +x /usr/local/bin/youtube-dl
  apt install lame libav-tools

Snippets
********

.. code-block:: bash
  :caption: Extract 320kbps Audio From Video.

  youtube-dl <url> --extract-audio --audio-format mp3 --audio-quality 320K --keep-video --add-metadata

.. code-block:: bash
  :caption: List all formats for a video.

  youtube-dl <url> -F

.. code-block:: bash
  :caption: Download only the 1080p video/audio stream from a video.

  youtube-dl <url> 'bestvideo[height<=1080]+bestaudio/best[height<=1080]'

.. code-block:: bash
  :caption: Download a playlist.

  youtube-dl https://youtube.com/playlist?list=<LID> --yes-playlist

.. code-block:: bash
  :caption: Track Downloaded Videos for Archiving.

  youtube-dl --download-archive <FILE>

.. note::
  Download only videos not listed in file and adds any downloaded videos to
  the given file.

.. rubric:: References

#. `youtube-dl Source download (latest) <http://yt-dl.org/latest/>`_
#. `youtube-dl github repo <http://rg3.github.io/youtube-dl/download.html>`_
#. `Using youtube-dl <http://linuxaria.com/recensioni/how-to-download-youtube-video-or-audio-tracks-from-the-linux-terminal>`_
#. `Using youtube-dl with LAME <http://www.linuxjournal.com/content/grabbing-your-music-youtube-do-it-your-way>`_
#. `Convert webm format <https://askubuntu.com/questions/323944/convert-webm-to-other-formats>`_
