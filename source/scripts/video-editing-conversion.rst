.. _video-editing-conversion:

Video Editing / Conversion
##########################
Shell scripts and utilites for editing/converting videos.

.. code-block:: bash
  :caption: Installing Utilities

  apt install mencoder ffmpeg mkvtoolnix imagemagick avconv libavcodec-extra-53 libav-tools

Snippets
********

.. code-block:: bash
  :caption: Splitting MKV Files into Smaller MKV’s Based on Timestamps

  mkvmerge -o out.file --split timecodes:00:42:06.000,01:22:20.000 in.file

.. code-block:: bash
  :caption: Cut and Direct Copy Video to New File

  mencoder [-ss 00:00:00] -endpos 00:15:00 -oac copy -ovc copy in.file -o out.file
  ffmpeg -i input.wmv -ss 00:00:00.000 -t 00:15:00.000 -acodec copy -vcodec copy output.wmv

.. code-block:: bash
  :caption: `Strip metadata`_ (metadata that is not required)

  Ffmpeg -map_metadata -1

.. code-block:: bash
  :caption: Generate Copies at One Second Intervals (For Bad Encodes)

  for x in `seq -w 5 15`;do mencoder -oac copy -ovc copy -ss 11:${x} -endpos 14:00 in.file -o out-${x}.file;done

.. code-block:: bash
  :caption: Merge Video Files into a Single File

  mencoder -oac copy -ovc copy [-noskip] [hr-edl-seek] in1.file in2.file inX.file -o out.file

.. code-block:: bash
  :caption: Insert a Video into a MKV Container (No Video Conversion -- Preferred)

  mkvmerge -o out.mkv in.file

.. code-block:: bash
  :caption: Insert and Convert a Video into a MKV Container (Re-encodes Video Than Insert)

  mencoder in.file -o out.mkv -of lavf -oac copy -ovc lavc

.. code-block:: bash
  :caption: Insert and Convert Videos in a Directory to MKV Containers

  find . -name "*.flv" -exec mencoder {} -o {}.mkv -of lavf -oac copy -ovc lavc \;

.. code-block:: bash
  :caption: Convert Entire Directory to MKV Containers

  find . -type f -exec mkvmerge -o {}.mkv {} \;

.. code-block:: bash
  :caption: Convert Animated GIF to AVI/MPG

  convert image.gif output%05d.png
  convert -delay 12 -quality 100 output*png final_movie.mpg
  ffmpeg -r 9 -i output%05d.png final_movie.avi

.. code-block:: bash
  :caption: Combine multiple video parts into one video

  mkvmerge -o out.mkv 1.file + 2.file + 3.file + 4.file + 5.file

.. code-block:: bash
  :caption: Rip MP3 Audio from FLV File

  avconv -i <input.flv> output.mp3

.. code-block:: bash
  :caption: Convert FLV to MKV Container

  ffmpeg -i <input.flv> -vcodec copy -acodec copy out.mkv

.. code-block:: bash
  :caption: Convert webm to mkv

  ffmpeg -i your_input_filename.webm -qscale 0 your_outfile_name.mkv

Download M3U8 Playlist
**********************
For videos that are sitched together in short increments, usually TS (video
stream).

Turn on developer tools (Chrome):
* :cmdmenu:` ... --> More Tools --> Developer Tools`.
* Load Video URL.
* :cmdmenu:`Developer Tools --> Network --> All`.
* Filter by ``m3u8``.
* Determine stream URL to use.
* :cmdmenu:`RMB --> Copy --> Copy link address`.

.. code-block:: bash
  :caption: Use ffmpeg to download and stitch stream together

  ffmpeg -i https://<URI>.m3u8 -c:v copy -c:a copy -f mpegts output.ts

.. rubric:: References

#. `mencoder online manual <http://www.mplayerhq.hu/DOCS/HTML/en/mencoder.html>`_
#. `mencoder selecting codecs <http://www.mplayerhq.hu/DOCS/HTML/en/menc-feat-selecting-codec.html>`_
#. `mencoder for merging video files <http://www.linuxquestions.org/questions/linux-general-1/how-to-merge-2-avi-together-424988/>`_
#. `mencoder for video editing <http://bro1.centras.info/mencoder_editing.html>`_
#. `mencoder how to trim and split <http://www.misterhowto.com/index.php?category=Computers&subcategory=Video&article=trim_or_split_with_mencoder>`_
#. `ffmpeg for slicing video files (1) <http://www.joeldare.com/wiki/video:cut_video_with_ffmpeg>`_
#. `ffmpeg for slicing video files (2) <http://www.mydigitallife.info/convert-flash-video-flv-files-to-mpg-or-avi-and-other-media-formats/>`_
#. `Convert static images to video files <http://jupiter.ethz.ch/~pjt/makingMovies.html>`_
#. `Convert animated GIF’s to video files (1) <http://stackoverflow.com/questions/3212821/animated-gif-to-avi-on-linux>`_
#. `Convert animated GIF’s to video files (1) <http://www.catswhocode.com/blog/19-ffmpeg-commands-for-all-needs>`_
#. `Convert animated GIF’s to video files (1) <http://www.imagemagick.org/discourse-server/viewtopic.php?f=1&t=14743&view=next>`_
#. `Splitting MKV’s into smaller MKV’s <http://www.bunkus.org/videotools/mkvtoolnix/doc/mkvmerge.html>`_
#. `Combining multiple videos parts into one file <https://askubuntu.com/questions/637074/merging-multiple-more-than-two-videos-on-ubuntu>`_

.. _Strip metadata: https://stackoverflow.com/questions/11474532/how-to-change-metadata-with-ffmpeg-avconv-without-creating-a-new-file
