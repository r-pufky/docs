# Video Tools
Shell scripts and utilities for editing/converting videos.

``` bash
apt install mencoder ffmpeg mkvtoolnix imagemagick avconv libavcodec-extra-53 libav-tools
```


## Determine length in seconds of a given video file
``` bash
ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$1" | cut -d\. -f1
```


## Split MKV into Smaller MKV’s Based on Timestamps
``` bash
mkvmerge -o out.file --split timecodes:00:42:06.000,01:22:20.000 in.file
```


## Cut and Direct Copy Video to New File
``` bash
mencoder [-ss 00:00:00] -endpos 00:15:00 -oac copy -ovc copy in.file -o out.file
ffmpeg -i input.wmv -ss 00:00:00.000 -t 00:15:00.000 -acodec copy -vcodec copy output.wmv
```


## [Strip metadata][a]
``` bash
Ffmpeg -map_metadata -1  # Only metadata that is not required.
```


## Generate Copies at One Second Intervals (For Bad Encodes)
``` bash
for x in `seq -w 5 15`;do mencoder -oac copy -ovc copy -ss 11:${x} -endpos 14:00 in.file -o out-${x}.file;done
```


## Merge Video Files into a Single File
``` bash
mencoder -oac copy -ovc copy [-noskip] [hr-edl-seek] in1.file in2.file inX.file -o out.file
```


## Insert a Video into a MKV Container
``` bash
mkvmerge -o out.mkv in.file  # No Video Conversion -- Preferred.
```


## Insert and Convert a Video into a MKV Container
``` bash
# Re-encodes then inserts.
mencoder in.file -o out.mkv -of lavf -oac copy -ovc lavc
```


## Insert and Convert Videos in a Directory to MKV Containers
``` bash
find . -name "*.flv" -exec mencoder {} -o {}.mkv -of lavf -oac copy -ovc lavc \;
```


## Convert Entire Directory to MKV Containers
``` bash
find . -type f -exec mkvmerge -o {}.mkv {} \;
```


## Convert Animated GIF to AVI/MPG
``` bash
convert image.gif output%05d.png
convert -delay 12 -quality 100 output*png final_movie.mpg
ffmpeg -r 9 -i output%05d.png final_movie.avi
```


## Combine multiple video parts into one video
``` bash
mkvmerge -o out.mkv 1.file + 2.file + 3.file + 4.file + 5.file
```


## Rip MP3 Audio from FLV File
``` bash
avconv -i {FLV FILE} output.mp3
```


## Convert FLV to MKV Container
``` bash
ffmpeg -i {FLV FILE} -vcodec copy -acodec copy out.mkv
```


## Convert webm to mkv
``` bash
ffmpeg -i your_input_filename.webm -qscale 0 your_outfile_name.mkv
```


## Use ffmpeg to download and stitch stream together
``` bash
ffmpeg -i https://{URI}.m3u8 -c:v copy -c:a copy -f mpegts output.ts
```


## ffmpeg Convert [Minimizing Quality Loss][b]
Convert file stripping metadata and enabling skipping and scrubbing in video.

``` bash
ffmpeg -i example.mp4 -ss 00:00:10.000 -t 00:51:29.000 -crf 15 -movflags +faststart -pix_fmt yuv420p -map_metadata -1 out.mp4
```


## Download M3U8 Playlist
For videos that are stitched together in short increments, usually TS (video
stream).

Turn on developer tools (Chrome):

* ⋮ ➔ More Tools ➔ Developer Tools
* Load Video URL.
* Developer Tools ➔ Network ➔ All
* Filter by **m3u8**.
* Determine stream URL to use.
* RMB ➔ Copy ➔ Copy link address

## Reference[^1][^2][^3][^4][^5][^6][^7][^8][^9][^10][^11][^12][^13][^14][^15][^16]

[^1]: http://www.mplayerhq.hu/DOCS/HTML/en/mencoder.html
[^2]: http://www.mplayerhq.hu/DOCS/HTML/en/menc-feat-selecting-codec.html
[^3]: https://www.linuxquestions.org/questions/linux-general-1/how-to-merge-2-avi-together-424988/
[^4]: http://brovienas.tripod.com/mencoder_editing.html
[^5]: http://www.misterhowto.com/index.php?category=Computers&subcategory=Video&article=trim_or_split_with_mencoder
[^6]: https://www.joeldare.com/wiki/video:cut_video_with_ffmpeg
[^7]: https://techjourney.net/convert-flash-video-flv-files-to-mpg-or-avi-and-other-media-formats/
[^8]: http://jupiter.ethz.ch/~pjt/makingMovies.html
[^9]: https://stackoverflow.com/questions/3212821/animated-gif-to-avi-on-linux
[^10]: https://catswhocode.com/ffmpeg-commands/
[^11]: http://www.imagemagick.org/discourse-server/viewtopic.php?f=1&t=14743&view=next
[^12]: https://mkvtoolnix.download/doc/mkvmerge.html
[^13]: https://askubuntu.com/questions/637074/how-to-merge-multiple-more-than-two-videos-on-ubuntu
[^14]: https://askubuntu.com/questions/59383/extract-part-of-a-video-with-a-one-line-command
[^15]: https://superuser.com/questions/542989/getting-the-video-frame-number-in-vlc
[^16]: https://www.linuxuprising.com/2018/07/how-to-stream-netflix-videos-at-1080p.html

[a]: https://stackoverflow.com/questions/11474532/how-to-change-metadata-with-ffmpeg-avconv-without-creating-a-new-file
[b]: https://stackoverflow.com/questions/25569180/ffmpeg-convert-without-loss-quality