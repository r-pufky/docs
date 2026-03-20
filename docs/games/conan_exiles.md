# Conan Exiles

!!! example "Migrated to ansible collection"
    Use [r_pufky.games.conan_exiles][a].

!!! tip
    * If connecting on local network, use the private IP of the server, not the
      public IP address.
    * **/home/steam/conan_exiles/ConanSandbox/Saved** contains server state
      information.


## Configuration

* [Engine.ini][k] - Service settings.
* [Game.ini][l] - Runtime service settings.
* [ServerSettings.ini][m] - Gameplay settings.

### [Isle of Siptah][b]
Set the default map to enable 'Isle of Siptah' expansion. Extra configuration
options are enabled in **ServerSettings.ini**.

!!! abstract "Engine.ini"
    0644 {USER}:{USER}

    ``` ini
    ; Enabling this map enables extra settings in ServerSettings.ini.
    [/Script/EngineSettings.GameMapsSettings]
    ServerDefaultMap=/Game/DLC_EXT/DLC_Siptah/Maps/DLC_Isle_of_Siptah
    ```

!!! abstract "ServerSettings.ini"
    0644 {USER}:{USER}

    ``` ini
    ; Isle of Siptah expanded options.
    StormEnabled=True
    ElderThingsEnabled=True
    ElderThingsIdleLifespan=30.000000
    SiegeElderThingsEnabled=False
    StormCooldown=105.000000
    StormAccumulationTime=1.000000
    StormDuration=15.000000
    StormDissipationTime=1.000000
    StormEnduranceDrainMultiplier=0.000000
    ElderThingSpawnRate=1.000000
    StormTimeWeekdayStart='0000'
    StormTimeWeekdayEnd=2359
    StormTimeWeekendStart='0000'
    StormTimeWeekendEnd=2359
    StormMinimumOnlinePlayers=0
    StormBuildingAllowed=True
    StormMapBlocker=True
    EnableBuildingDestructionCapsules=False
    ServerTransferEnabled=False
    ; These are feature ID's to blacklist, format: ("ID", "ID", "ID")
    FeatsBlacklist=''
    CanDamagePlayerOwnedStructuresPeriod=120
    ElderThingSiegeDamageMultiplier=1.000000
    MinimumBuildingSizeToBeSieged=41
    AmbientElderThingRespawnRate=1.000000
    SiegeElderThingRespawnRate=1.000000
    StormBuildingDamageRateMultiplier=1.000000
    MaxAmbientElderThings=700
    MaxSiegeElderThings=5
    MaxAmbushElderThings=200
    ElderThingSiegeBuildingSizeMultiplier=1.000000
    StormBuildingDamageEnabled=False
    SiegeElderThingMapMarkers=False
    MinimumStormDamageBuildingPieces=0
    StormBuildingDamageMultiplier=1.000000
    VaultRefreshTime=10
    VaultRefreshDeviation=2
    SurgeDeviationMin=60
    SurgeDeviationMax=60
    SurgeSacrificeRequirementMultiplier=1.000000
    SurgeDespawnTimer=90
    AltarModuleActiveTimeMultiplier=1.000000
    RandomSurgesCountMin=6
    RandomSurgesCountMax=10
    DecoupleSurgeFromStorm=False
    DecoupledSurgeCooldown=5
    ```

### Recommended Mods
Quality of life recommended mods for PVE.

* [Pythagoras: Expanded Building][c]
* [ExtendedCartography][d]
* [PRN_NPCEquipmentLoot][e]
* [Configurable Elevators][f]
* [Pickup+][g]
* [Navigator][h]
* [Map-Marker][i]


## Reference[^1]

[^1]: https://www.conanexiles.com/dedicated-servers

[a]: https://galaxy.ansible.com/ui/repo/published/r_pufky/game/docs
[b]: https://forums.funcom.com/t/hosting-a-dedicated-server-for-isle-of-siptah/136857/4
[c]: https://steamcommunity.com/sharedfiles/filedetails/?id=2723987721
[d]: https://steamcommunity.com/sharedfiles/filedetails/?id=1641464108
[e]: https://steamcommunity.com/sharedfiles/filedetails/?id=1401061998
[f]: https://steamcommunity.com/sharedfiles/filedetails/?id=1716717492
[g]: https://steamcommunity.com/sharedfiles/filedetails/?id=864199675
[h]: https://steamcommunity.com/sharedfiles/filedetails/?id=2869834350
[i]: https://steamcommunity.com/sharedfiles/filedetails/?id=2859016366

[k]: https://conanexiles.fandom.com/wiki/Dedicated_Server_Setup:_Linux_and_Wine#Engine.ini
[l]: https://conanexiles.fandom.com/wiki/Dedicated_Server_Setup:_Linux_and_Wine#Game.ini
[m]: https://conanexiles.fandom.com/wiki/Dedicated_Server_Setup:_Linux_and_Wine#ServerSettings.ini
