# [Ludusavi][a]
Multi-platform, Multi-OS game save manager. Replacement for
[Gamesave Manager][b].

To convert existing Gamesave Manager saves use
[GSM-to-Ludusavi-converter][d].

=== "CachyOS"
    ``` bash
    paru -S ludusavi-bin
    ```

=== "Manjaro"
    ``` bash
    pamac install ludusavi-bin
    ```

=== "Windows"
    ``` powershell
    winget install -e --id mtkennerly.ludusavi
    winget upgrade -e --id mtkennerly.ludusavi
    ```

=== "OSX"
    [Download from releases page][c]


## Configuration

!!! example "Backup"
    * Back up to: **{PATH}**

!!! example "Other"
    * Theme: **Dark**
    * Check for updates automatically: ✔
    * Scan:
        * Backup format: **Zip**
        * Backup compression: **Zstd**
        * Backup level: **22** (see [compression levels](#compression-levels))
        * Skip backup when data would be removed, not added or updated: ✔
    * Manifest:
        * https://raw.githubusercontent.com/mtkennerly/ludusavi-manifest/master/data/manifest.yaml
        * https://raw.githubusercontent.com/BloodShed-Oni/ludusavi-extra-manifests/main/BS_ex-manifest.yaml
        * https://raw.githubusercontent.com/BloodShed-Oni/ludusavi-extra-manifests/main/BS_software-manifest.yaml

## Manifests
Manifests support additional games and game related software.

* https://raw.githubusercontent.com/hblamo/ludusavi-emudeck-manifest/main/manifest.yml
* https://github.com/hvmzx/ludusavi-manifests

## Compression Levels
Zstd offers highest compression with consistent decompression speeds; however
compression is slow. Level must be set accordingly to specific CPU to set an
ideal backup time.

!!! info "Backups are archives, spend the time to maximally compress."

  Level | MB/s (per core) | MB/S Effective | 1GB data (8 cores)
 -------|-----------------|----------------|--------------------
  22    | 2-3             | 3.5MB/s        | 286s
  15    | 4-11            | 25MB/s         | 40s
  10    | 30-100          | 200MB/s        | 5s (gzip equivalent)


[a]: https://github.com/mtkennerly/ludusavi
[b]: https://www.gamesave-manager.com
[c]: https://github.com/mtkennerly/ludusavi/releases
[d]: https://github.com/jose-l-martins/GSM-to-Ludusavi-converter
