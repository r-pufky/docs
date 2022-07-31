.. _video-editing-conversion:

Video Editing / Conversion
##########################
Shell scripts and utilites for editing/converting videos.

.. code-block:: bash
  :caption: Installing Utilities.

  apt install mencoder ffmpeg mkvtoolnix imagemagick avconv libavcodec-extra-53 libav-tools

Snippets
********

Splitting MKV Files into Smaller MKV’s Based on Timestamps
==========================================================
.. code-block:: bash

  mkvmerge -o out.file --split timecodes:00:42:06.000,01:22:20.000 in.file

Cut and Direct Copy Video to New File
=====================================
.. code-block:: bash

  mencoder [-ss 00:00:00] -endpos 00:15:00 -oac copy -ovc copy in.file -o out.file
  ffmpeg -i input.wmv -ss 00:00:00.000 -t 00:15:00.000 -acodec copy -vcodec copy output.wmv

`Strip metadata`_ (metadata that is not required)
=================================================
.. code-block:: bash

  Ffmpeg -map_metadata -1

Generate Copies at One Second Intervals (For Bad Encodes)
=========================================================
.. code-block:: bash

  for x in `seq -w 5 15`;do mencoder -oac copy -ovc copy -ss 11:${x} -endpos 14:00 in.file -o out-${x}.file;done

Merge Video Files into a Single File
====================================
.. code-block:: bash

  mencoder -oac copy -ovc copy [-noskip] [hr-edl-seek] in1.file in2.file inX.file -o out.file

Insert a Video into a MKV Container (No Video Conversion -- Preferred)
======================================================================
.. code-block:: bash

  mkvmerge -o out.mkv in.file

Insert and Convert a Video into a MKV Container (Re-encodes Video Than Insert)
==============================================================================
.. code-block:: bash

  mencoder in.file -o out.mkv -of lavf -oac copy -ovc lavc

Insert and Convert Videos in a Directory to MKV Containers
==========================================================
.. code-block:: bash

  find . -name "*.flv" -exec mencoder {} -o {}.mkv -of lavf -oac copy -ovc lavc \;

Convert Entire Directory to MKV Containers
==========================================
.. code-block:: bash

  find . -type f -exec mkvmerge -o {}.mkv {} \;

Convert Animated GIF to AVI/MPG
===============================
.. code-block:: bash

  convert image.gif output%05d.png
  convert -delay 12 -quality 100 output*png final_movie.mpg
  ffmpeg -r 9 -i output%05d.png final_movie.avi

Combine multiple video parts into one video
===========================================
.. code-block:: bash

  mkvmerge -o out.mkv 1.file + 2.file + 3.file + 4.file + 5.file

Rip MP3 Audio from FLV File
===========================
.. code-block:: bash

  avconv -i {FLV FILE} output.mp3

Convert FLV to MKV Container
============================
.. code-block:: bash

  ffmpeg -i {FLV FILE} -vcodec copy -acodec copy out.mkv

Convert webm to mkv
===================
.. code-block:: bash

  ffmpeg -i your_input_filename.webm -qscale 0 your_outfile_name.mkv

Use ffmpeg to download and stitch stream together
=================================================
.. code-block:: bash
  :caption: Use ffmpeg to download and stitch stream together.

  ffmpeg -i https://{URI}.m3u8 -c:v copy -c:a copy -f mpegts output.ts

ffmpeg Convert `Minimizing Quality Loss`_
=========================================
Convert file stripping metadata and enabling skipping and scrubbing in video.

.. code-block:: bash

   ffmpeg -i example.mp4 -ss 00:00:10.000 -t 00:51:29.000 -crf 15 -movflags +faststart -pix_fmt yuv420p -map_metadata -1 out.mp4

Download M3U8 Playlist
**********************
For videos that are sitched together in short increments, usually TS (video
stream).

Turn on developer tools (Chrome):

* :cmdmenu:`⋮ --> More Tools --> Developer Tools`
* Load Video URL.
* :cmdmenu:`Developer Tools --> Network --> All`
* Filter by ``m3u8``.
* Determine stream URL to use.
* :cmdmenu:`{RMB} --> Copy --> Copy link address`

.. rubric:: References

#. `mencoder online manual <http://www.mplayerhq.hu/DOCS/HTML/en/mencoder.html>`_
#. `mencoder selecting codecs <http://www.mplayerhq.hu/DOCS/HTML/en/menc-feat-selecting-codec.html>`_
#. `mencoder for merging video files <https://www.linuxquestions.org/questions/linux-general-1/how-to-merge-2-avi-together-424988/>`_
#. `mencoder for video editing <http://brovienas.tripod.com/mencoder_editing.html>`_
#. `mencoder how to trim and split <http://www.misterhowto.com/index.php?category=Computers&subcategory=Video&article=trim_or_split_with_mencoder>`_
#. `ffmpeg for slicing video files (1) <https://www.joeldare.com/wiki/video:cut_video_with_ffmpeg>`_
#. `ffmpeg for slicing video files (2) <https://techjourney.net/convert-flash-video-flv-files-to-mpg-or-avi-and-other-media-formats/>`_
#. `Convert static images to video files <http://jupiter.ethz.ch/~pjt/makingMovies.html>`_
#. `Convert animated GIF’s to video files (1) <https://stackoverflow.com/questions/3212821/animated-gif-to-avi-on-linux>`_
#. `Convert animated GIF’s to video files (2) <https://catswhocode.com/ffmpeg-commands/>`_
#. `Convert animated GIF’s to video files (3) <http://www.imagemagick.org/discourse-server/viewtopic.php?f=1&t=14743&view=next>`_
#. `Splitting MKV’s into smaller MKV’s <https://mkvtoolnix.download/doc/mkvmerge.html>`_
#. `Combining multiple videos parts into one file <https://askubuntu.com/questions/637074/how-to-merge-multiple-more-than-two-videos-on-ubuntu>`_
#. `Extract part of video <https://askubuntu.com/questions/59383/extract-part-of-a-video-with-a-one-line-command>`_
#. `Get frame number in VLC <https://superuser.com/questions/542989/getting-the-video-frame-number-in-vlc>`_
#. `Stream Netflix videos at 1080p in Linux <https://www.linuxuprising.com/2018/07/how-to-stream-netflix-videos-at-1080p.html>`_

.. _Strip metadata: https://stackoverflow.com/questions/11474532/how-to-change-metadata-with-ffmpeg-avconv-without-creating-a-new-file
.. _Minimizing Quality Loss: https://stackoverflow.com/questions/25569180/ffmpeg-convert-without-loss-quality
