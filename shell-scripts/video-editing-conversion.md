Video Editing / Conversion
--------------------------
Shell scripts and utilites for editing/converting videos.

1. [Installing Utilities](#installing-utilities)
1. [Snippets](#snippets)
1. [References](#references)

Installing Utilities
--------------------
Tools used for these commands.

```bash
apt install mencoder ffmpeg mkvtoolnix imagemagick avconv libavcodec-extra-53 libav-tools
```

Snippets
--------
### Splitting MKV Files into Smaller MKV’s Based on Timestamps
```bash
mkvmerge -o out.file --split timecodes:00:42:06.000,01:22:20.000 in.file
```

### Cut and Direct Copy Video to New File
```bash
mencoder [-ss 00:00:00] -endpos 00:15:00 -oac copy -ovc copy in.file -o out.file
ffmpeg -i input.wmv -ss 00:00:00.000 -t 00:15:00.000 -acodec copy -vcodec copy output.wmv
```

### [Strip metadata][1] (metadata that is not required)
```bash
Ffmpeg -map_metadata -1
```

### Generate Copies at One Second Intervals (For Bad Encodes)
```bash
for x in `seq -w 5 15`;do mencoder -oac copy -ovc copy -ss 11:${x} -endpos 14:00 in.file -o out-${x}.file;done
```

### Merge Video Files into a Single File
```bash
mencoder -oac copy -ovc copy [-noskip] [hr-edl-seek] in1.file in2.file inX.file -o out.file
```

### Insert a Video into a MKV Container (No Video Conversion -- Preferred)
```bash
mkvmerge -o out.mkv in.file
```

### Insert and Convert a Video into a MKV Container (Re-encodes Video Than Insert)
```bash
mencoder in.file -o out.mkv -of lavf -oac copy -ovc lavc
```

### Insert and Convert Videos in a Directory to MKV Containers
```bash
find . -name "*.flv" -exec mencoder {} -o {}.mkv -of lavf -oac copy -ovc lavc \;
```

### Convert Entire Directory to MKV Containers
```bash
for x in `ls -1`;do mkvmerge -o ${x}.mkv ${x}; done
```

### Convert Animated GIF to AVI/MPG
```bash
convert image.gif output%05d.png
convert -delay 12 -quality 100 output*png final_movie.mpg
ffmpeg -r 9 -i output%05d.png final_movie.avi
```

### Combine multiple video parts into one video
```bash
mkvmerge -o out.mkv 1.file + 2.file + 3.file + 4.file + 5.file
```

### Rip MP3 Audio from FLV File
```bash
avconv -i <input.flv> output.mp3
```

### Convert FLV to MKV Container
```bash
ffmpeg -i <input.flv> -vcodec copy -acodec copy out.mkv
```

References
----------
[mencoder online manual][2]

[mencoder selecting codecs][3]

[mencoder for merging video files][4]

[mencoder for video editing][5]

[mencoder how to trim and split][6]

ffmpeg for slicing video files [one][7] [two][8]

[Convert static images to video files][9]

Convert animated GIF’s to video files [one][10] [two][11] [three][12]

[Splitting MKV’s into smaller MKV’s][13]

[Combining multiple videos parts into one file][14]

[1]: https://stackoverflow.com/questions/11474532/how-to-change-metadata-with-ffmpeg-avconv-without-creating-a-new-file
[2]: http://www.mplayerhq.hu/DOCS/HTML/en/mencoder.html
[3]: http://www.mplayerhq.hu/DOCS/HTML/en/menc-feat-selecting-codec.html
[4]: http://www.linuxquestions.org/questions/linux-general-1/how-to-merge-2-avi-together-424988/
[5]: http://bro1.centras.info/mencoder_editing.html
[6]: http://www.misterhowto.com/index.php?category=Computers&subcategory=Video&article=trim_or_split_with_mencoder
[7]: http://www.joeldare.com/wiki/video:cut_video_with_ffmpeg
[8]: http://www.mydigitallife.info/convert-flash-video-flv-files-to-mpg-or-avi-and-other-media-formats/
[9]: http://jupiter.ethz.ch/~pjt/makingMovies.html
[10]: http://stackoverflow.com/questions/3212821/animated-gif-to-avi-on-linux
[11]: http://www.catswhocode.com/blog/19-ffmpeg-commands-for-all-needs
[12]: http://www.imagemagick.org/discourse-server/viewtopic.php?f=1&t=14743&view=next
[13]: http://www.bunkus.org/videotools/mkvtoolnix/doc/mkvmerge.html
[14]: https://askubuntu.com/questions/637074/merging-multiple-more-than-two-videos-on-ubuntu