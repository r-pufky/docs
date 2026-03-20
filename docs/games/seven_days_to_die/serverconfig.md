# [serverconfig.xml][a]
Server instance configuration.

!!! tip "Additional Options In-game"
    There are several game settings that you cannot change when starting a new
    game. You can use [console commands][b] to change some of them.

    ``` bash
	  setgamepref BedrollDeadZoneSize 30
    ```

## Server Representation

### ServerName
Server name.

  Variable    | Type | Default
 -------------|------|---------
  ServerName  | str  | My Game Host


### ServerDescription
Server description.

  Variable          | Type | Default
 -------------------|------|---------
  ServerDescription | str  | A 7 Days to Die server

### ServerWebsiteURL
Server URL link.

  Variable         | Type | Default
 ------------------|------|---------
  ServerWebsiteURL | str  | ''

### ServerPassword
Server password.

  Variable       | Type | Default
 ----------------|------|---------
  ServerPassword | str  | ''

### ServerLoginConfirmationText
Login confirmation text.

If set the user will see the message during joining the server and has to
confirm it before continuing. For more complex changes to this window you can
change the 'serverjoinrulesdialog' window in UI.

  Variable                    | Type | Default
 -----------------------------|------|---------
  ServerLoginConfirmationText | str  | ''

### Region
Server region.

  Variable | Type | Default  | Values
 ----------|------|----------|--------
  Region   | str  | veryfast | **NorthAmericaEast**
           |      |          | **NorthAmericaWest**
           |      |          | **CentralAmerica**
           |      |          | **SouthAmerica**
           |      |          | **Europe**
           |      |          | **Russia**
           |      |          | **Asia**
           |      |          | **MiddleEast**
           |      |          | **Africa**
           |      |          | **Oceania**

### Language
Server player base primary language (in english).

  Variable | Type | Default
 ----------|------|---------
  Language | str  | English

## Networking

### ServerPort
Server port.

  Variable   | Type | Default
 ------------|------|---------
  ServerPort | int  | 26900

### ServerVisibility
Server visibility.

!!! note "Friends Only"
    As you are never friend of a dedicated server, setting this will only work
    when the first player connects manually by IP.

  Variable         | Type | Default | Values
 ------------------|------|---------|--------
  ServerVisibility | int  | 2       | **2**: Public.
                   |      |         | **1**: Friends only.
                   |      |         | **0**: Not listed.

### ServerDisabledNetworkProtocols
Disabled networking protocols.

  Variable         | Type | Default | Values
 ------------------|------|---------|--------
  ServerDisabledNetworkProtocols | str  | SteamNetworking | **SteamNetworking**: Steam library indirect service connections. Disable when no NAT router between your users and server or when port-forwarding is set up correctly.
                                 |      |                 | **LiteNetLib**: Built-in UDP Networking. Only disable for temporary troubleshooting as it will greatly degrade server optimization.

### ServerMaxWorldTransferSpeedKiBs
Maximum speed world is transferred on first connect (KiB/s). Only when the
client does not have the world yet.

  Variable                        | Type | Default | Values
 ---------------------------------|------|---------|--------
  ServerMaxWorldTransferSpeedKiBs | int  | 512     | **0**: Disable.
                                  |      |         | **1300**: Limit is about 1300 KiB/s (10Mbps), even if higher value.

## Slots

### ServerMaxPlayerCount
Maximum Concurrent Players.

  Variable             | Type | Default
 ----------------------|------|---------
  ServerMaxPlayerCount | int  | **8**: Greater than 20 players may cause data save issues.

### ServerReservedSlots
Player count reserved slots. Out of MaxPlayerCount this many slots can only be
used by players with a specific permission level.

  Variable            | Type | Default
 ---------------------|------|---------
  ServerReservedSlots | int  | **0**: Greater than 20 players may cause data save issues.

### ServerReservedSlotsPermission
Required permission level to use reserved slots above.

  Variable                      | Type | Default
 -------------------------------|------|---------
  ServerReservedSlotsPermission | int  | 100

### ServerAdminSlots
This many admins can still join even if the server has reached MaxPlayerCount.

  Variable         | Type | Default
 ------------------|------|---------
  ServerAdminSlots | int  | 0

### ServerAdminSlotsPermission
Required permission level to use the admin slots above.

  Variable                   | Type | Default
 ----------------------------|------|---------
  ServerAdminSlotsPermission | int  | 0

## Admin Interfaces

### WebDashboardEnabled
Enable web dashboard?

  Variable            | Type | Default
 ---------------------|------|---------
  WebDashboardEnabled | bool | false

### WebDashboardPort
Web dashboard port.

  Variable         | Type | Default
 ------------------|------|---------
  WebDashboardPort | int  | 8080

### WebDashboardUrl
External URL to web dashboard if not the public IP of the server (e.g. behind
a reverse proxy). Full URL required 'https://domainOfReverseProxy.tld:1234/'.

  Variable        | Type | Default
 -----------------|------|---------
  WebDashboardUrl | str  | ''

### EnableMapRendering
Enable map rendering? Render map to tile images while exploring it. Used by web
dashboard to display a view of the map.

  Variable           | Type | Default
 --------------------|------|---------
  EnableMapRendering | bool | false

## TelnetEnabled
Enable telnet server?

  Variable      | Type | Default
 ---------------|------|---------
  TelnetEnabled | bool | true

## TelnetPort
Telnet server port.

  Variable   | Type | Default
 ------------|------|---------
  TelnetPort | int  | 8081

## TelnetPassword
Telnet server password. If no password is set the server will only listen on
the local loopback interface.

  Variable       | Type | Default
 ----------------|------|---------
  TelnetPassword | str  | ''

## TelnetFailedLoginLimit
Failed telnet login attempts before blocking client.

  Variable               | Type | Default
 ------------------------|------|---------
  TelnetFailedLoginLimit | int  | 10

## TelnetFailedLoginsBlocktime
Failed telnet login block time (seconds).

  Variable                    | Type | Default
 -----------------------------|------|---------
  TelnetFailedLoginsBlocktime | int  | 10

## TerminalWindowEnabled
Show terminal window for log output/command input (windows only)?

  Variable              | Type | Default
 -----------------------|------|---------
  TerminalWindowEnabled | bool | true

## Folder & File Locations

### AdminFileName
Server admin file name. Path relative to UserDataFolder/Saves.

  Variable      | Type | Default
 ---------------|------|---------
  AdminFileName | str  | serveradmin.xml

### UserDataFolder
Use this to override where the server stores all user data, including RWG
generated worlds and saves.

  Variable       | Type | Default
 ----------------|------|---------
  UserDataFolder | str  | N/A: Use an absolute path.

## Other Technical Settings

### ServerAllowCrossplay
Enable crossplay. Crossplay servers will only be found in searches and joinable
if sanctions are not ignored, and have a default or lower player slot count.

  Variable             | Type | Default
 ----------------------|------|---------
  ServerAllowCrossplay | bool | false

### EACEnabled
Enable Easy Anti-cheat?

  Variable   | Type | Default
 ------------|------|---------
  EACEnabled | bool | true

### IgnoreEOSSanctions
Ignore EOS (Epic Online Services) sanctions when allowing players to join?

  Variable           | Type | Default
 --------------------|------|---------
  IgnoreEOSSanctions | bool | false

### HideCommandExecutionLog
Hide command execution logging.

  Variable                | Type | Default | Values
 -------------------------|------|---------|--------
  HideCommandExecutionLog | int  | 0       | **0**: Show everything.
                          |      |         | **1**: Hide from Telnet/control_panel.
                          |      |         | **2**: 1 + hide from remote game clients.
                          |      |         | **3**: Hide everything.

### MaxUncoveredMapChunksPerPlayer
Number of chunks that can be uncovered on in game map by each player.

Resulting max map file size limit per player is (x * 512 Bytes), uncovered area
is (x * 256 m²). Default 131072 means max 32 km² can be uncovered at any time.

  Variable                       | Type | Default
 --------------------------------|------|---------
  MaxUncoveredMapChunksPerPlayer | int  | **131072**: (32 km²).

### PersistentPlayerProfiles
Enable persistent player profiles?

  Variable                 | Type | Default | Values
 --------------------------|------|---------|--------
  PersistentPlayerProfiles | bool | false   | **False**: Disabled - player can join with any selected profile.
                           |      |         | **True**: Enabled - player joins with last profile they joined with.

### MaxChunkAge
Number of in-game days which must pass since visiting a chunk before it will
reset to its original state if not revisited or protected (e.g. by a land
claim or bedroll being in close proximity).

  Variable    | Type | Default | Values
 -------------|------|---------|--------
  MaxChunkAge | int  | -1      | **-1**: Disable.
              |      |         | **#**: Number of in-game days.

### SaveDataLimit
Max disk space allowed for each save game (MB). Saved chunks may be forcibly
reset to their original states to free up space when this limit is reached.

  Variable      | Type | Default
 ---------------|------|---------
  SaveDataLimit | int  | **-1**: Disable (MB).

## GameWorld
World map to use.

  Variable | Type | Default   | Values
 ----------|------|-----------|--------
  Gameplay | str  | Navezgane | **RWG**: see WorldGenSeed and WorldGenSize options below.
           |      |           | **Navezgane**: Main world (default).
           |      |           | **Pregen06k01**: Pregenerated random map 1.
           |      |           | **Pregen06k02**: Pregenerated random map 2.
           |      |           | **Pregen08k01**: Pregenerated random map 3.
           |      |           | **Pregen08k02**: Pregenerated random map 4.

### WorldGenSeed
If RWG this is the seed for the generation of the new world. If a pre-generated
world resulting name already exists it will simply load it.

  Variable     | Type | Default
 --------------|------|---------
  WorldGenSeed | str  | MyGame

### WorldGenSize

  Variable     | Type | Default
 --------------|------|---------
  WorldGenSize | int  | **6144**: Officially supported sizes are between 6144 and 10240 and must be a multiple of 2048. Only used when GameWorld=RWG.

### GameName
Whatever you want the game name to be. Affects the save game name as well as
the seed used when placing decoration (trees etc.) in the world. It does not
control the generic layout of the world if creating an RWG world.

  Variable | Type | Default
 ----------|------|---------
  GameName | str  | **MyGame**: Allowed characters [A-Za-z0-9_-.].

### GameMode

  Variable | Type | Default
 ----------|------|---------
  GameMode | str  | GameModeSurvival


### GameDifficulty

  Variable       | Type | Default | Values
 ----------------|------|---------|--------
  GameDifficulty | int  | 1       | **0**: Scavenger.
                 |      |         | **1**: Adventurer (default).
                 |      |         | **2**: Nomad.
                 |      |         | **3**: Warrior.
                 |      |         | **4**: Survivalist.
                 |      |         | **5**: Insane.

### BlockDamagePlayer
How much damage do players to blocks (percentage in whole numbers).

  Variable          | Type | Default
 -------------------|------|---------
  BlockDamagePlayer | int  | 100

### BlockDamageAI
How much damage do AIs to blocks (percentage in whole numbers).

  Variable      | Type | Default
 ---------------|------|---------
  BlockDamageAI | int  | 100

### BlockDamageAIBM
How much damage do AIs during blood moons to blocks (percentage in whole
numbers).

  Variable        | Type | Default
 -----------------|------|---------
  BlockDamageAIBM | int  | 100

### XPMultiplier
XP gain multiplier (percentage in whole numbers).

  Variable     | Type | Default
 --------------|------|---------
  XPMultiplier | int  | 100

### PlayerSafeZoneLevel
If a player is less or equal this level he will create a safe zone (no enemies)
when spawned.

  Variable            | Type | Default
 ---------------------|------|---------
  PlayerSafeZoneLevel | int  | 5

### PlayerSafeZoneHours
Hours in world time this safe zone exists.

  Variable            | Type | Default
 ---------------------|------|---------
  PlayerSafeZoneHours | int  | 5

## Game Rules

### BuildCreate
Cheat mode.

  Variable    | Type | Default
 -------------|------|---------
  BuildCreate | bool | false

### DayNightLength
Real time minutes per in game day: 60 minutes.

  Variable       | Type | Default
 ----------------|------|---------
  DayNightLength | int  | 60

### DayLightLength
In game hours the sun shines per day: 18 hours day light per in game day.

  Variable       | Type | Default
 ----------------|------|---------
  DayLightLength | int  | 18

### BiomeProgression
Enables biome hazards and loot stage caps to promote biome progression. Loot
stage caps are increased by completing biome challenges.

  Variable    | Type | Default
 -------------|------|---------
  BiomeProgression | bool | true

### StormFreq
Adjusts the frequency of storms.

  Variable  | Type | Default | Values
 -----------|------|---------|--------
  StormFreq | int  | 100     | **0**: disable.
            |      |         | **50**: 50%.
            |      |         | **100**: Normal.
            |      |         | **150**: 150%.
            |      |         | **200**: 200%.
            |      |         | **300**: 300%.
            |      |         | **400**: 400%.
            |      |         | **500**: 500%.

### DeathPenalty
Penalty after dying.

  Variable     | Type | Default | Values
 --------------|------|---------|--------
  DeathPenalty | int  | 1       | **0**: Nothing.
               |      |         | **1**: Default Classic XP Penalty.
               |      |         | **2**: Injured You keep most of your de-buffs. Food and Water is set to 50% on respawn.
               |      |         | **3**: Permanent Death: Your character is completely reset. You will respawn with a fresh start within the saved game.

### DropOnDeath
Drop items on death.

  Variable    | Type | Default | Values
 -------------|------|---------|--------
  DropOnDeath | int  | 1       | **0**: Nothing.
              |      |         | **1**: Everything.
              |      |         | **2**: Toolbelt only.
              |      |         | **3**: Backpack only.
              |      |         | **4**: Delete all.

### DropOnQuit
Drop items on quit.

  Variable   | Type | Default | Values
 ------------|------|---------|--------
  DropOnQuit | int  | 0       | **0**: Nothing.
             |      |         | **1**: Everything.
             |      |         | **2**: Toolbelt only.
             |      |         | **3**: Backpack only.

### BedrollDeadZoneSize
Size (box "radius", so a box with 2 times the given value for each side's
length) of bedroll dead zone, no zombies will spawn inside this area, and any
cleared sleeper volumes that touch a bedroll deadzone will not spawn after
they've been cleared.

  Variable            | Type | Default
 ---------------------|------|---------
  BedrollDeadZoneSize | int  | 15

### BedrollExpiryTime
Number of real world days a bedroll stays active after owner was last online.

  Variable          | Type | Default
 -------------------|------|---------
  BedrollExpiryTime | int  | 45

### AllowSpawnNearFriend
Can new players joining the server for the first time select to join near any
friend playing at the same time?

  Variable             | Type | Default | Values
 ----------------------|------|---------|--------
  AllowSpawnNearFriend | int  | 2       | **0**: Disabled.
                       |      |         | **1**: Always.
                       |      |         | **2**: Only near friends in forest biome.

### CameraRestrictionMode

  Variable              | Type | Default | Values
 -----------------------|------|---------|--------
  CameraRestrictionMode | int  | 0       | **0**: 1st/3rd person cameras.
                        |      |         | **1**: 1st person only.
                        |      |         | **2**: 3rd person only.

### JarRefund
The empty jar refund percentage after consuming an item.

  Variable  | Type | Default
 -----------|------|---------
  JarRefund | int  | 0

## Performance Related

### MaxSpawnedZombies
This setting covers the entire map. There can only be this many zombies on the
entire map at one time. Changing this setting has a huge impact on performance.

  Variable          | Type | Default
 -------------------|------|---------
  MaxSpawnedZombies | int  | 64

### MaxSpawnedAnimals
If your server has a large number of players you can increase this limit to add
more wildlife. Animals don't consume as much CPU as zombies.

!!! note "Does not cause more animals to spawn arbitrarily"
    The biome spawning system only spawns a certain number of animals in a
    given area, but if you have lots of players that are all spread out then
    you may be hitting the limit and can increase it.

  Variable          | Type | Default
 -------------------|------|---------
  MaxSpawnedAnimals | int  | 50

### ServerMaxAllowedViewDistance
Max view distance a client may request. High impact on memory usage and
performance.

  Variable                     | Type | Default
 ------------------------------|------|---------
  ServerMaxAllowedViewDistance | int  | **12**: (6-12).

### MaxQueuedMeshLayers
Maximum amount of Chunk mesh layers that can be enqueued during mesh
generation. Reducing this will improve memory usage but may increase Chunk
generation time.

  Variable            | Type | Default
 ---------------------|------|---------
  MaxQueuedMeshLayers | int  | 1000

## Zombie Settings

### EnemySpawnMode
Enable/Disable enemy spawning.

  Variable       | Type | Default
 ----------------|------|---------
  EnemySpawnMode | bool | true

### EnemyDifficulty

  Variable        | Type | Default | Values
 -----------------|------|---------|--------
  EnemyDifficulty | int  | 0       | **0**: Normal.
                  |      |         |**1**: Feral.

### ZombieFeralSense

  Variable         | Type | Default | Values
 ------------------|------|---------|--------
  ZombieFeralSense | int  | 0       | **0**: Off.
                   |      |         | **1**: Day.
                   |      |         | **2**: Night.
                   |      |         | **3**: All.

### ZombieMove

  Variable   | Type | Default | Values
 ------------|------|---------|--------
  ZombieMove | int  | 0       | **0**: Walk.
             |      |         | **1**: Jog.
             |      |         | **2**: Run.
             |      |         | **3**: Sprint.
             |      |         | **4**: Nightmare.

### ZombieMoveNight

  Variable        | Type | Default | Values
 -----------------|------|---------|--------
  ZombieMoveNight | int  | 3       | **0**: Walk.
                  |      |         | **1**: Jog.
                  |      |         | **2**: Run.
                  |      |         | **3**: Sprint.
                  |      |         | **4**: Nightmare.

### ZombieFeralMove

  Variable        | Type | Default | Values
 -----------------|------|---------|--------
  ZombieFeralMove | int  | 3       | **0**: Walk.
                  |      |         | **1**: Jog.
                  |      |         | **2**: Run.
                  |      |         | **3**: Sprint.
                  |      |         | **4**: Nightmare.

### ZombieBMMove

  Variable     | Type | Default | Values
 --------------|------|---------|--------
  ZombieBMMove | int  | 3       | **0**: Walk.
               |      |         | **1**: Jog.
               |      |         | **2**: Run.
               |      |         | **3**: Sprint.
               |      |         | **4**: Nightmare.

### AISmellMode

  Variable    | Type | Default | Values
 -------------|------|---------|--------
  AISmellMode | int  | 0       | **0**: Walk.
              |      |         | **1**: Jog.
              |      |         | **2**: Run.
              |      |         | **3**: Sprint.
              |      |         | **4**: Nightmare.

### BloodMoonFrequency
What frequency (in days) should a blood moon take place.

  Variable           | Type | Default
 --------------------|------|---------
  BloodMoonFrequency | int  | **7**: In days (0 disables).

### BloodMoonRange
How many days can the actual blood moon day randomly deviate from the above
setting. Setting this to 0 makes blood moons happen exactly each Nth day as
specified in BloodMoonFrequency.

  Variable       | Type | Default
 ----------------|------|---------
  BloodMoonRange | int  | 0

### BloodMoonWarning
The Hour number that the red day number begins on a blood moon day. Setting
this to -1 makes the red never show.

  Variable         | Type | Default
 ------------------|------|---------
  BloodMoonWarning | int  | 8


### BloodMoonEnemyCount
This is the number of zombies that can be alive (spawned at the same time) at
any time PER PLAYER during a blood moon horde, however, MaxSpawnedZombies
overrides this number in multiplayer games. Also note that your game stage
sets the max number of zombies PER PARTY. Low game stage values can result in
lower number of zombies than the BloodMoonEnemyCount setting. Changing this
setting has a huge impact on performance.

  Variable            | Type | Default
 ---------------------|------|---------
  BloodMoonEnemyCount | int  | 8

## Loot

### LootAbundance
Ppercentage in whole numbers.

  Variable      | Type | Default
 ---------------|------|---------
  LootAbundance | int  | 100

### LootRespawnDays
Days in whole numbers.

  Variable      | Type | Default
 ---------------|------|---------
  LootRespawnDays | int  | 7

### AirDropFrequency
How often airdrop occur in game-hours.

  Variable         | Type | Default
 ------------------|------|---------
  AirDropFrequency | int  | **72**: (0 disables).

### AirDropMarker
Sets if a marker is added to map/compass for air drops.

  Variable      | Type | Default
 ---------------|------|---------
  AirDropMarker | bool | true

## Multiplayer

### PartySharedKillRange
The distance you must be within to receive party shared kill XP and quest party
kill objective credit.

  Variable             | Type | Default
 ----------------------|------|---------
  PartySharedKillRange | int  | 100

### PlayerKillingMode
Player Killing Settings.

  Variable          | Type | Default | Values
 -------------------|------|---------|--------
  PlayerKillingMode | int  | 3       | **0**: No Killing.
                    |      |         | **1**: Kill Allies Only.
                    |      |         | **2**: Kill Strangers Only.
                    |      |         | **3**: Kill Everyone.

## Land Claim Options

### LandClaimCount
Maximum allowed land claims per player.

  Variable       | Type | Default
 ----------------|------|---------
  LandClaimCount | int  | 5

### LandClaimSize
Size in blocks that is protected by a keystone.

  Variable      | Type | Default
 ---------------|------|---------
  LandClaimSize | int  | 41

### LandClaimDeadZone
Keystones must be this many blocks apart (unless you are friends with the other
player).

  Variable          | Type | Default
 -------------------|------|---------
  LandClaimDeadZone | int  | 30

### LandClaimExpiryTime
The number of real world days a player can be offline before their claims
expire and are no longer protected.

  Variable            | Type | Default
 ---------------------|------|---------
  LandClaimExpiryTime | int  | 7

### LandClaimDecayMode
Controls how offline players land claims decay.

  Variable           | Type | Default | Values
 --------------------|------|---------|--------
  LandClaimDecayMode | int  | 0       | **0**: Slow (Linear).
                     |      |         | **1**: Fast (Exponential).
                     |      |         | **2**: None (Full protection until claim is expired).

### LandClaimOnlineDurabilityModifier
How much protected claim area block hardness is increased when a player is
online.

  Variable                          | Type | Default
 -----------------------------------|------|---------
  LandClaimOnlineDurabilityModifier | int  | **4**: Multipler (0 disables).

### LandClaimOfflineDurabilityModifier
How much protected claim area block hardness is increased when a player is
offline.

  Variable                           | Type | Default
 ------------------------------------|------|---------
  LandClaimOfflineDurabilityModifier | int  | **4**: Multipler (0 disables).

### LandClaimOfflineDelay
The number of minutes after a player logs out that the land claim area hardness
transitions from online to offline.

  Variable              | Type | Default
 -----------------------|------|---------
  LandClaimOfflineDelay | int  | 0

### DynamicMeshEnabled
Is Dynamic Mesh system enabled?

  Variable           | Type  | Default
 --------------------|-------|---------
  DynamicMeshEnabled | bool  | true

### DynamicMeshLandClaimOnly
Is Dynamic Mesh system only active in player LCB areas?

  Variable                 | Type  | Default
 --------------------------|-------|---------
  DynamicMeshLandClaimOnly | bool  | true

### DynamicMeshLandClaimBuffer
Dynamic Mesh LCB chunk radius.

  Variable                   | Type | Default
 ----------------------------|------|---------
  DynamicMeshLandClaimBuffer | int  | 3

### DynamicMeshMaxItemCache
How many items can be processed concurrently, higher values use more RAM.

  Variable                | Type | Default
 -------------------------|------|---------
  DynamicMeshMaxItemCache | int  | 3

### TwitchServerPermission
Required permission level to use twitch integration on the server.

  Variable               | Type | Default
 ------------------------|------|---------
  TwitchServerPermission | int  | 90

### TwitchBloodMoonAllowed
If the server allows twitch actions during a blood moon. This could cause
server lag with extra zombies being spawned during blood moon.

  Variable               | Type  | Default
 ------------------------|-------|---------
  TwitchBloodMoonAllowed | bool  | false

### QuestProgressionDailyLimit
Limits the number of quests that contribute to quest tier progression a player
can complete each day. Quests after the limit can still be completed for
rewards.

  Variable                   | Type | Default
 ----------------------------|------|---------
  QuestProgressionDailyLimit | int  | 4

## Reference[^1]

[^1]: https://developer.valvesoftware.com/wiki/7_Days_to_Die_Dedicated_Server


[a]: https://7daystodie.fandom.com/wiki/Server:_serverconfig.xml
[b]: https://7daystodie.fandom.com/wiki/Command_Console