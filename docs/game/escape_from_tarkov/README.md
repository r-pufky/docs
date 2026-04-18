# Escape from Tarkov

## FIKA Server
FIKA is a locally hosted multiplayer serve for Escape from Tarkov.

!!! tip
    See [FIKA Server](server.md) to setup a dedicated server. This assumes a
    server is already configured.

### Windows
Install EFT and disable automatic updates. Note the installed version.

!!! example "EFT Launcher ➔ Profile ➔ Settings ➔ Updates: ✘"
    Updates are disabled to ensure mod always works.

Install mod dependencies:

* [Net Framework 4.7.2][a].
* [.NET Runtime 6][b].

#### Automatic Installation
This is a user supported tool which automatically applies all patches required.
Preferred.

1. [Download the installer][c].
2. Create an empty folder for SPT to be installed to and extract installer to
    this location. Prefer same drive and root folder as EFT.

    Suggest: **c:\Battlestate Games\SPT**

3. Run installer.

#### Manual Installation
!!! tip
    Only do this if you know what you are doing. This requires knowing what
    version of EFT you are running, then manually downgrading to the latest
    SPT-AKI supported version and applying the SPT-AKI patches.

1. Copy **c:\Battlestate Games\EFT** to **c:\Battlestate Games\SPT**.
2. [Download the downgrade patcher][d] for the specific version you have
   installed. This will downgrade the SPT install to the currently supported
   SPT version.
3. Extract patcher files to **c:\Battlestate Games\SPT**.
4. Run patcher and ignore virus warnings (triggered as these are re-writing
    signed binaries).
5. Download the [SPT installer][e] and extract to **c:\Battlestate Games\SPT**.
6. [Run installer][f] (ignore virus warnings - these rewrite signed binaries).

#### [Install FIKA Mod][g]

1. Extract inlcuded `Fika.Release.*.zip` to `c:/tarkov-coop-fika`
2. `Fika.Core.dll` should be in `c:/tarkov-coop-fika/BepInEx/plugins`

!!! abstract "c:/tarkov-coop-fika/BepInEx/config/com.bepis.bepinex.configurationmanager.cfg"
    0644 {USER}:{USER}

    ``` bash
    # There are two locations to set.
    Show config manager = F11
    Show config manager = F11
    ```

3. Copy settings to SPT: **user** ➔ **c:/tarkov-coop-fika/user**
4. Setup Steam Shortcut
    * steam ➔ games ➔ add non-steam game to library
    * Target: `c:/tarkov-coop-fika/SPT.Launcher.exe`
    * Icon (click it): select `EscapeFromTarkov.exe`
    * Name: 'Escape from Tarkov (Coop)'
    * Start In: `c:/tarkov-coop-fika`
    * Enable steam overlay while in game
    * controller ➔ disable steam input
    * controller ➔ use desktop configruation in launcher
5. Launch 'Escape from Tarkov (Coop)'
    Ignore 'copy game settings' dialogs and any errors on inital launch (these
    are because the default server is not running).

    * settings ➔ Developer Mode ➔ Enable
    * settings ➔ URL➔ `http://{IP}:6969`
    * settings ➔ On Game Start ➔ Close Launcher
    * settings ➔ SPT Game Path ➔ `c:/tarkov-coop-fika`
    * click `➔` to launch

    Your previous account (if migrated) will be available with no password.

    On first run, YOU MUST WAIT 30 SECONDS FOR THE TOS ACCEPTANCE OR GAME WILL
    EXIT.
6. Set FIKA Options
    Press **F11** During game to pull up mod overlay; click on **FIKA Core** to
    expand mod options. Note: The UI is confusing. The verbiage next to the
    checkbox represents the current state, **NOT** what ticking it does.

    * Show Feed: Enabled (checked)
    * Auto Extract: Enabled (checked)
    * Show Extract Message: Enabled (checked)
    * Extract Key: F8
    * Ping System: Enabled (checked)
    * Ping Button: {SET}
    * Free Camera Button: F9
    * Show Player Name Plates: Enabled (checked)
    * Show Player Faction Icon: Disabled (unchecked)
    * Hide Name Plate In Optic: Enabled (checked)
    * Dynamic AI: Enabled (checked)
    * Dynamic AI Range: 150.0m (double check if sniping and AI not moving)
    * Culling System: Enabled (checked)
    * Culling Range: 30m
    * Enforced Spawn Limits: Disabled (unchecked)

You are ready to play.

#### Launching Game
Must be launched in the following order to run properly.

1. Launch the server (Server.exe if manually patched):
    **c:\Battlestate Games\SPT\Aki.Server.exe**
2. Launch the client (Launcher.exe if manually patched):
    **c:\Battlestate Games\SPT\Aki.Client.exe**
1. Create account with entitlements:
    * Launcher ➔ Make a new account
      * Select whatever entitlements you wish (starting items).
    * Launcher ➔ Start game

## Creating Host Server
Certain game options will be enforce server side. Host server actually hosts
the game using game assets. This is the client with the most powerful machine.

* pick raid map to play
* pick the same SLOT number (1 or 2)
* player with the strongest machine should HOST the raid
* **COOP** mode and **Practice Mode** will be force enabled with FIKA
* after insurance click **host raid**
  * Pick number of players; game will NOT start until everyone has joined
* start

## Moving Install Location
Registry keys must be updated to point to new binary locations.

1. Find EFT Uninstall registry keys (regedit)

!!! example "⌘ ➔ regedit ➔ Computer"

    ``` regedit
    Computer\HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\{B0FDA062-7581-4D67-B085-C4E7C358037F}_is1
    ```

2. Upload binary locations for each key (do not change additional options)

    * DisplayIcon
    * Inno Setup: App Path
    * InstallLocation
    * QuietUninstallString
    * UninstallString

3. Update BsgLauncher Paths

    ``` regedit
    %appdata%/Roaming/Battlestate Games/BsgLauncher/settings
    ```

## Upgrading SPT Minor Releases
Minor releases only require in-place replace of existing SPT files.

1. Download the specified version from `versions.md`
2. Backup replaced files (prepend with date `YYYY-MM-DD.{FILE}`)

    * BepInEx
    * SPT_Data
    * SPT.Server.exe
    * SPT.Launcher.exe
    * doorstop_config.ini
    * winhttp.dll

3. Extract archive into `c:/tarkov-coop-fika`
4. Update plugin configuration files

   `c:/tarkov-coop-fika/BepInEx/config`

## Settings
Game settings that balance colors and rendering quality.

!!! example "EFT ➔ ⚙ ➔ Graphics"
    * Object LOD quality: **2.5**
    * Overall visibility: **1500**
    * Anti-aliasing: **TAA High**
    * Resampling: **1x off**
    * Nvidia DLSS: **Off**
    * HBAO: **Off**
    * SSR: **Off**
    * Antistropic Filtering: **Off**
    * Nvidia Reflex Low Latency: **On and boost**
    * Sharpness: **0.4**
    * High quality color: ✘
    * Z-Blur: ✘
    * Chromatic Aberrations: ✘
    * Noise: ✘
    * Gress Shadows: ✘
    * Mip Streaming: ✘
    * Flash Indicator: ✘

!!! example "Nvidia Control Panel ➔ Display ➔ Adjust desktop color settings"
    * Apply color enhancements:
        * Color channel: **All channels**
        * Brightness: **+60%**
        * Contrast: **+75%**
        * Gamma: **+1.40**
        * Digital vibrance: **+80%**
        * Hue: **0**

## Reference[^1][^2][^3][^4][^5]
[^1]: https://github.com/sp-tarkov/patcher
[^2]: https://www.sp-tarkov.com/#download
[^3]: https://www.sp-tarkov.com/#features
[^4]: https://hub.sp-tarkov.com/files/file/6-spt-aki
[^5]: https://dev.sp-tarkov.com/SPT-AKI

[a]: https://dotnet.microsoft.com/download/dotnet-framework/thank-you/net472-developer-pack-offline-installer
[b]: https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/runtime-desktop-6.0.4-windows-x64-installer
[c]: https://hub.sp-tarkov.com/files/file/601-spt-aki-installer/#overview
[d]: https://hub.sp-tarkov.com/files/file/142-aki-patcher/#versions
[e]: https://hub.sp-tarkov.com/files/file/601-spt-aki-installer/#overview
[f]: https://hub.sp-tarkov.com/files/file/6-spt-aki/
[g]: https://github.com/project-fika/Fika-Plugin/releases/latest