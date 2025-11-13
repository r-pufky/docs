# Kindle
Find [compatible models][a].

!!! danger
    Delete any stray **.bin** or **update.bin.tmp.partial** that appear on the
    root of the Kindle during the process. These are kindle updates
    downloading.

!!! danger
    Kindle **must have** less than **90MB** (ideally around 50MB) free to
    prevent updates.

    Connect the Kindle to the computer and use [Kindle Filler Disk][b] to fill
    up the Kindle. Nested directories are fine and these can be removed after
    patching.


## [Adbreak][c]
Uses [CVE-2012-3748][d] to jailbreak recent Kindle updates.

1. Download [Adblock][e].
2. Enable Advertisements (Temporarily)

    !!! example "amazon.com ➔ Account ✋ ➔ Devices ➔ Preferences ➔ Country/Region Settings"
        * Set: **US**
        * Email: **{VALID_EMAIL}**
        * Phone: **{VALID_PHONE}**
        * Address: **{VALID_ADDRESS}**

    !!! example "amazon.com ➔ Account ➔ Payments ➔ Settings ➔ Your Purchase Preferences"
        Set default credit card and billing address matching region above.

    !!! example "amazon.com ➔ Account ✋ ➔ Kindle ➔ Details ➔ Special Offers: ✔"

    Leave kindle on and connected to the internet. Restarting may help to pull
    advertisements. They will show up on the lock screen.

3. Enable airplane mode.
4. Verify ads are listed:

    !!! example "Kindle ➔ ⋮ ➔ View All Ads"

5. Connect Kindle and copy **.assets** to local computer.
6. Extract **Ablock** into **.assets** folder.

7. Execute Adblock

    === "Linux"
        ``` bash
        Run find . -name 'details.html' -exec cp adbreak.html {} \;
        ```

    === "Windows"
        ``` powershell
        replace.bat
        ```

8. Copy modified **.assets** to Kindle and overwrite.
9. Disconnect Kindle and view an ad:

    !!! example "Kindle ➔ ⋮ ➔ View All Ads ➔ Any Ad"
        A terminal should appear while executing jailbreak. **Application
        errors** are OK.

        There will be multiple windows that open - ignore them.

    !!! success "Bang!"
        This message will appear when the jailbreak succeeds.
10. **Enable** airplane mode.


## [Hotfix][f]

1. **Enable** airplane mode.
2. Download [hotfix][g].
3. Connect kindle and extract **Update_hotfix_universal.bin** to the root of
   the Kindle.
4. Unplug Kindle and Update

    !!! example "Kindle ➔ ⋮ ➔ Update your Kindle"
        Airplane mode **must** be on.

5. Hotfix will install a 'book' labeled **Run Hotfix**. Open (execute) it.

    !!! warning
        This **must** be run after every Kindle update to ensure jailbreak
        persistence.


## [Install KUAL and MRPI][h]
Kindle Unified Application Launcher (KUAL) and MobileRead Package Installer
(MRPI) are used to run homebrew on Kindle.

Download [KUAL][i].

Download [MRPI][j].

1. Connect Kindle.
2. Extract MRPI and copy **mrpackages** and **extensions** to the root of the
   Kindle.
3. Extract KUAL and rename

    !!! warning
        Rename to **Update_KUALBooklet_HDRepack_install.bin**

        Install appears to work but does not succeed without renaming the file.

4. Copy renamed KUAL package to **Kindle/mrpackages/**
5. Unplug Kindle.
6. Execute MRPI

    !!! example "Kindle ➔ Search ➔ ;log mrpi"
        Enter ';log mrpi' in the search bar to execute command injection and
        launch MRPI setup. There will be multiple windows that open - ignore
        them.

        'Success. :)' will appear when complete.

        KUAL should appear as a book on your Kindle once rebooted.


## [Disable OTA Updates][k]
Install mod that disables updates.

Download [renametobin][l]

1. Connect Kindle.
2. Create **Kindle/update.bin.tmp.partial** folder.
3. Extract and copy **renametobin** folder to **Kindle/extensions**.
4. Unplug Kindle.
5. Extract RenameToBin

    !!! example "Kindle ➔ KUAL ➔ Rename OTA Binaries ➔ Rename"
        Kindle will automatically reboot.

        Selecting 'Restore' will re-enable OTA updates.


## [KOReader][m]
Opensource ebook reader that supports a massive amount of formats.

Download [koreader-kindlehf-*.zip][n].

1. Connect Kindle.
2. Extract and copy **extensions** and **koreader** to root of Kindle. Merge or
   replace any files.
3. Unplug Kindle.
4. Launch KOReader

    !!! example "Kindle ➔ KUAL ➔ KOReader"

!!! tip
    See https://koreader.rocks/user_guide for a helpful user guide.


## [KindleForge][o]
Opensource Kindle App Store. Allows for easy installation of packages without
manually connecting to a computer each time.

Download [KindleForge][o].

1. Connect Kindle.
2. Extract **KindleForge** and **.sh script** to **Kindle/documents**.
3. Unplug Kindle.


## Disable Ads
Remove Ads and tracking information after jailbreak.

!!! example "amazon.com ➔ Account ✋ ➔ Kindle ➔ Details ➔ Special Offers: ✘"


## Reference[^1][^2][^3][^4][^5][^6]

[^1]: https://kindlemodding.org/jailbreaking
[^2]: https://github.com/koreader/koreader
[^3]: https://github.com/iiroak/Kindle-Filler-Disk
[^4]: https://www.mobileread.com/forums/showthread.php?t=225030
[^5]: https://scriptlets.notmarek.com/
[^6]: https://open-slum.org

[a]: https://kindlemodding.org/kindle-models.html
[b]: https://github.com/iiroak/Kindle-Filler-Disk/tree/main/MTP
[c]: https://kindlemodding.org/jailbreaking/AdBreak
[d]: https://scarybeastsecurity.blogspot.com/2017/05/ode-to-use-after-free-one-vulnerable.html
[e]: https://github.com/htimesnine/AdBreak/releases/download/v1.0.1/adbreak.zip)
[f]: https://kindlemodding.org/jailbreaking/post-jailbreak/setting-up-a-hotfix
[g]: https://github.com/KindleModding/Hotfix/releases/latest/download/Update_hotfix_universal.bin
[h]: https://kindlemodding.org/jailbreaking/post-jailbreak/installing-kual-mrpi
[i]: https://kindlemodding.org/jailbreaking/post-jailbreak/installing-kual-mrpi/Update_KUALBooklet_HDRepack.bin
[j]: https://fw.notmarek.com/khf/kual-mrinstaller-khf.tar.xz
[k]: https://kindlemodding.org/jailbreaking/post-jailbreak/disable-ota
[l]: https://kindlemodding.org/jailbreaking/post-jailbreak/renameotabin.zip
[m]: https://kindlemodding.org/jailbreaking/post-jailbreak/koreader.html
[n]: https://github.com/koreader/koreader/releases
[o]: https://kindlemodshelf.me/kindleforge.html
[p]: https://github.com/KindleTweaks/KindleForge/releases
