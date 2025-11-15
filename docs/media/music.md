# Music Processing
Basic music processing rules for importing music.

## Album Artwork

1. Find larger than **500x500** and resize to **500x500**.

    !!! tip
        Ensure **DPI >= 72**; **1600x1600** should be around 1.5 megs.

2. **Use Template Image** if no image found, replacing text as needed.
3. If no large image or template exists (and template doesn’t make sense), take
   largest small picture, and up sample it:

    !!! tip
        Change DPI to something large like **500**.

4. Trim / rotate picture as needed for clean edges; touch up if needed.
5. Auto level the picture for sharper image:

    !!! example "⌘ + shift + l"

6. Save image as **png**, uncompressed / interweaved: **band - album.png**

## Track Formatting

### Subtitles to albums
``` text
[album]: [subtitle]
[album] - [subtitle]: [subtitle]
Live Trax Volume XX: YYYY-MM-DD [Venue] City, state
```

### Multiple songs in a single track
``` text
# No segway
[song 1] / [song 2]

# Segway
[song 1] > [song 2]
```

### Mixes, Remixes
``` bash
[song title] ([style if applicable] Remix)
```

### Featured Artists
``` bash
[song title] (Featuring [artist name 1][, artist name 2] …)
```

### Remixed, Featured in same song
``` bash
[song title] [remix] [featured artists]
```

!!! note
    Mixes, Remixes, Featured Artists formatting is now handled in **Set
    Featured Artist and Remixes** script.

## [Music Genres][b]

### House
* Beat every 4/4.
* Distinct drum/beat every measure.
* Example: turn me on @ **1:18**.

### Dubstep
* Heavy Bass.
* Drum Patterns.
* Clipped Samples (jarring / repeating).
* Electronic bass.
* Sample: Holy Ghost @ **1:35**.

## Music Purge

### Album Artist (A-Z)
* Most videos are purged unless unique (i.e. Nirvana MTV, etc); normal music
  videos are almost always purged.
* Experience albums (albums that are continuous) should be marked as such in the
  tags (**gapless**) and not have a song deleted even if it is below 4 stars.
* Music with no rating is skipped.
* Skipped: **Alanis Morissette**
* Stopped: **Ani Defranco**

[b]: http://www.reddit.com/r/Music/comments/1v70di/can_someone_eli5_the_different_types_of_edm/
