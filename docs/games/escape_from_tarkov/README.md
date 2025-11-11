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

* [Net Framework 4.7.2](https://dotnet.microsoft.com/download/dotnet-framework/thank-you/net472-developer-pack-offline-installer)
* [.NET Runtime 6](https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/runtime-desktop-6.0.4-windows-x64-installer)

Reference:

* https://hub.sp-tarkov.com/files/file/6-spt-aki/

#### Automatic Installation
This is a user supported tool which automatically applies all patches required.
Preferred.

1. Download the installer:
   https://hub.sp-tarkov.com/files/file/601-spt-aki-installer/#overview
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
2. Download the downgrade patcher for the specific version you have installed.
   This will downgrade the SPT install to the currently supported SPT version.
   https://hub.sp-tarkov.com/files/file/142-aki-patcher/#versions
3. Extract patcher files to **c:\Battlestate Games\SPT**.
4. Run patcher and ignore virus warnings (triggered as these are re-writing
    signed binaries).
5. Download the [SPT installer](https://hub.sp-tarkov.com/files/file/601-spt-aki-installer/#overview),
    extract to **c:\Battlestate Games\SPT**
6. Run installer (ignore virus warnings (triggered as these are re-writing
    signed binaries.)

    https://hub.sp-tarkov.com/files/file/6-spt-aki/

Reference:

* https://dev.sp-tarkov.com/waffle.lord/Patcher

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

Reference:

* https://www.sp-tarkov.com/#download
* https://www.sp-tarkov.com/#features
* https://hub.sp-tarkov.com/files/file/6-spt-aki/
* https://dev.sp-tarkov.com/SPT-AKI

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
