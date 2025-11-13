# PlayOn
Steaming service recorder.

!!! tip
    Port **57331** is only used if you use PlayOn to stream recordings /
    provide a media library; by default this can be safely disabled.


## Setup
[Minimum requirements][a].

!!! note
    Any option not listed is left on default setting.

1. Install [PlayOn Desktop][b] but do not launch immediately.
2. Launch and skip through helper setup screens.

!!! example "PlayOn ➔ ⚙"
    * Video Performance"
        * Quality: **HD**
        * Allow resumable playback: ✔
        * Advanced options:
            * H.264 Recording Profile: **High**
    * System Check:
        * Notify Automatically: ✔
    * Channels:
        * Disable all channels not used.
        * Login to used channels.


## Convert PlayOn Recording to MKV Containers
``` bash
#!/bin/bash
#
# Converts playon videos to mkv format, preserving encoding and stripping metadata.
# For multiple: find -type f -exec ~/bin/playon-to-mkv netflix|amazon|playon|custom {}
#

# playon-to-mkv [netflix|amazon|playon] file
# playon-to-mkv custom pre-trim post-trim file

# Playon adds a 4 second pre-roll video with account/IP address, strip this.
# Playon adds a 5 second post-roll video with account/IP address, strip this.
# Playon adds metadata pertaining to account for video, strip this.
PLAYON_PRE=4
PLAYON_POST=5

# Netflix adds a 6.5 second netflix video, strip this.
# Netflix can inject a blank screen at the end, but it is not consistent.
NETFLIX_PRE=6
NETFLIX_POST=0

# Amazon adds a 1.5 second post-roll video for series, strip this.
AMAZON_PRE=0
AMAZON_POST=1.5

echo 'Calculating distances ...'
FILE="$2"
case "$1" in
  "netflix")
    echo 'Processing NETFLIX'
    PRE=$(awk '{print $1+$2}' <<< "${PLAYON_PRE} ${NETFLIX_PRE}")
    POST=$(awk '{print $1+$2}' <<< "${PLAYON_POST} ${NETFLIX_POST}")
    ;;
  "amazon")
    echo 'Processing AMAZON'
    PRE=$(awk '{print $1+$2}' <<< "${PLAYON_PRE} ${AMAZON_PRE}")
    POST=$(awk '{print $1+$2}' <<< "${PLAYON_POST} ${AMAZON_POST}")
    ;;
  "custom")
    echo 'Processing CUSTOM'
    PRE=$2
    POST=$3
    FILE="$4"
    ;;
  *)
    echo 'Prcessing PLAYON'
    PRE=${PLAYON_PRE}
    POST=${PLAYON_POST}
    ;;
esac
filename=$(basename "${FILE}")
dir=$(dirname "${FILE}")
extension="${filename##*.}"
basename="${filename%.*}"

ORIGINAL_LENGTH=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "${FILE}" | cut -d\. -f1)
TRIM_LENGTH=$(awk '{print $1-$2-$3}' <<< "${ORIGINAL_LENGTH} ${PRE} ${POST}")
echo -e "Distances: \nLength: ${ORIGINAL_LENGTH}\nPre Offset: ${PRE}\nPost Offset: ${POST}\nTrim: ${TRIM_LENGTH}"

echo 'Stripping metadata and trimming ...'
ffmpeg -i "${FILE}" -ss ${PRE} -acodec copy -vcodec copy -map_metadata -1 -t ${TRIM_LENGTH} "${dir}/${basename}.stripped.${extension}"
echo 'Packing into mkv ...'
mkvmerge -o "$-{basename}.mkv" "${basename}.stripped.${extension}"
echo 'Setting media permssions ...'
chown ${USER}:${USER} "${basename}.mkv"
chmod 0640 "${basename}.mkv"
```


## References[^1][^2][^3]

[^1]: https://www.playon.tv/support/minreqs
[^2]: https://www.playon.tv/user-guide/intro
[^3]: https://forums.webosnation.com/webos-apps-games/297294-port-forwarding-playon.html

[a]: https://www.playon.tv/support/minreqs
[b]: https://www.playon.tv/getplayon
