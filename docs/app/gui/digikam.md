# Digikam

=== "CachyOS"
    Install via AUR helper.

    ``` bash
    pacman -S digikam
    ```

=== "Debian"
    Use AppImage for latest versions.

    ``` bash
    mkdir ~/apps && cd ~/apps
    wget https://download.kde.org/stable/digikam/9.0.0/digiKam-9.0.0-Qt6-x86-64.appimage
    chmod +x digiKam-9.0.0-Qt6-x86-64.appimage

    # Restricted FUSE mounts (e.g. containers) must extract.
    digiKam-9.0.0-Qt6-x86-64.appimage --appimage-extract
    ./squashfs-root/AppRun
    ```

## Setup
Configure settings before using or let initial imports completely finish before
setting values.

### XMP Sidecars
Enable XMP sidecars to prevent future application lock-in.

!!! example "Settings ➔ Configure Digikam ➔ Metadata ➔ Sidecars"
    * Reading and Writing to Sidecars
        * Read from sidecar files: ✔
        * Write to sidecar files: ✔ Write to item and XMP Sidecar
        * Sidecar file names are compatible with commercial programs: ✘

    Enabling write will automatically enable read. Files **without** existing
    XMP sidecars will **NOT** have existing metadata overwritten. This is a
    poorly worded configuration option which explains only the read-only case.

    Enabling sidecar compatibility will only use the basename of the file which
    breaks any file with multiple extensions. Leaving this disabled will create
    a sidecar for each extension.


!!! example "Tools ➔ Maintenance ➔ Sync Metadata and Database"
    * All Albums: ✔
    * Sync Direction: **From Database to image metadata**

    Future imports and edits will automatically use metadata and XMP sidecars.

### Generate Fingerprints
Required for duplicate and similarity matching.

!!! example "Tools ➔ Maintenance ➔ Rebuild Fingerprints"
    * Scan for changed or non-changed items (faster): ✘

    After the initial processing run enabling scan will only re-processed
    modified files.

## Files
Use [Karl Voit's Naming System][a] for sane future and application proof
processing.

!!! success ""
    **YYYY-MM-DDTHH.MM.SS.SSS - {ORIGINAL NAME} -- {TAGS}.ext**

!!! warning "Always check empty album directories"
    Digikam will only display known formats. Any album (e.g. directory) that
    has unknown formats will not be displayed. Files moved to trash will appear
    in **{ALBUM ROOT}/.dtrash**.

    Check directories in terminal before removing album.

Additional Rules:

1. **0** fill unknown times, **01** fill unknown month/day:

    **2015-04-01T00.00.00.000**

2. Date Determination (from most precise to least precise):
    * metadata
    * relative context from other photos.
    * Retrieval date (e.g. downloaded files).
    * original directory.
    * original parent directory.

### Rename
Access renaming by highlighting files and pressing **F2** or using batch
processing.

#### Base Format (EXIF)
Use EXIF to generate base filename with typically most accurate data source.

``` css
[date:"yyyy-MM-ddTHH.mm.ss.zzz - "][file]{lower} -- [meta:Xmp.digiKam.TagsList]{lower}.[ext]{lower}
```

#### Static Date
Set static date not aligning to current metadata.

``` css
[file]{replace:"^.*? - ","2021-08-19T00.00.00.000 - ",r} -- [meta:Xmp.digiKam.TagsList]{lower}.[ext]{lower}
```

#### Generic

``` css
# [anytext][-_]YYYY[-_]MM[-_]DD[-_]HH[-_]MM[-_]SS[-_]SSS[-_](.*).ext
# Autopad MS with 000's even when not present, handle -,_,'' between separators.
[file]{replace:"^.*[-_](\d{4})[-_\s]?(\d{2})[-_\s]?(\d{2})[-_\s]?(\d{2})[-_\s]?(\d{2})[-_\s]?(\d{2})[-_\s]?(\d+)?.*","\1-\2-\3T\4.\5.\6.\7000",r}{replace:"\.(\d{3})\d*",".\1",r} - [file]{lower} -- [meta:Xmp.digiKam.TagsList]{lower}.[ext]{lower}
``` css

[a]: https://karl-voit.at/managing-digital-photographs
