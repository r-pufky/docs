# Elden Ring


## Linux Install
!!! tip
    You can just install directly from steam if you haven't downloaded the game
    already, or don't mind downloading again.

``` bash
# Copy from windows partition to linux
cp -av /mnt/win/Program Files (x86)/Steam/steamapps/common/ELDEN RING \
  ~/.steam/steam/steamapps/common/ELDEN RING
```

From steam install Elden Ring - it should validate files instead and download
**Proton**.


## Install Seemless Co-Op
Download [Seemless Coop][a] and extract to Elden Ring location (Steam ➔ Elden
Ring ➔ RMB ➔ Manage ➔ Browse Local Files).

Modify settings to taste.

!!! abstract "Game/SeamlessCoop/ersc_settings.ini"
    0644 {USER}:{USER}

    ``` ini
    [GAMEPLAY]

    ; Invaders are other players that will join your world uninvited and try to
    ; kill you and your party.  0=FALSE  1=TRUE
    allow_invaders = 0

    ; Debuffs (Rot Essence) will be acquired when you die, and will only be
    ; cured when you sit at a bonfire.  0=FALSE  1=TRUE
    death_debuffs = 0

    ; Spirit summons can aid you in multiplayer.  0=FALSE  1=TRUE
    allow_summons = 1

    ; 0 = Normal | 1 = None | 2 = Display player ping | 3 = Display player soul
    ; level | 4 = Display player death count | 5 = Soul level AND ping
    overhead_player_display = 4

    ; Whether to skip the intro logos when booting the game. 0 = FALSE 1 = TRUE
    skip_splash_screens = 1

    ; Game volume before initial save load. 0 = MUTE 10 = MAX
    default_boot_master_volume = 2

    [SCALING]

    ; Amount of enemy health (%) per player for each enemy. (Default: 35 = 35%
    ; more enemy health per player)
    enemy_health_scaling = 35

    ; Amount of enemy damage (%) per player for each enemy. (Default: 0 = 0%
    ; more enemy damage per player)
    enemy_damage_scaling = 0

    ; Amount of enemy posture absorption (%) per player for each enemy.
    ; (Default: 15 = 15% more per player)
    enemy_posture_scaling = 15

    ; Amount of boss health (%) per player for bosses. (Default: 100 = 100%
    ; more boss health per player)
    boss_health_scaling = 100

    ; Amount of enemy damage (%) per player for bosses. (Default: 0 = 0% more
    ; enemy damage towards players, per player)
    boss_damage_scaling = 0

    ; Amount of boss posture absorption (%) per player for bosses. (Default:
    ; 20 = 20% more boss posture per player)
    boss_posture_scaling = 20

    [PASSWORD]

    ; Session password
    cooppassword = {SESSION_PASSED}

    [SAVE]

    ;Your save file extension (in the vanilla game this is .sl2). Use any
    ; alphanumeric characters (limit = 120)
    save_file_extension = co2

    [LANGUAGE]

    ;Leave this blank unless you want to load a custom locale file. The mod
    ; will default to your game language.
    mod_language_override = (docs)
    ```

### Create Co-Op Shortcut
!!! tip
    Existing Elden Ring library covers are located at:
    **~/.steam/steam/appcache/librarycache/1245620/**

!!! example "Steam → Games → Add a non-steam game"
    * Executable: **~/.steam/steam/steamapps/common/ELDEN RING/Game/ersc_launcher.exe**
    * shortcut: **ELDEN RING (coop)**
    * compatibility:
        * Force use of specific steam play compatibility tool: **Proton (hotfix)**
    * Controller: **Setup your controller device**
    * Customization:
        * Cover: **Library_600x900.jpg**
        * Background: **Library_hero.jpg**
        * Logo: **logo.png**
        * Wide cover: **header.jpg**
        * Custom sort name: **ELDEN RING (coop)**

Launch new game shortcut, accept TOS, and quit (saves not loaded yet).

### Transfer Window Saves
Copy profile information from Windows and place in both Steam and Proton
directories.

``` bash
# Copy to Steam Profile.
cp -av /mnt/win/Users/{USER}/AppData/Roaming/EldenRing/ \
  ~/.local/share/Steam/steamapps/compatdata/1245620/pfx/drive_c/users/steamuser/AppData/Roaming/EldenRing/{STEAMID64}/

# Copy to Proton Profile.
cp -av /mnt/win/Users/{USER}/AppData/Roaming/EldenRing/ \
  ~/.local/share/Steam/steamapps/compatdata/{VERY_LARGE_NUMBER}/pfx/drive_c/users/steamuser/AppData/Roaming/EldenRing/{STEAMID64}
```

!!! info
    The new app id will be very large and mirror ELDEN RING app data.

Relaunch custom game with coop saves.

[a]: https://github.com/LukeYui/EldenRingSeamlessCoopRelease/releases
