# Steam

!!! example "Migrated to ansible collection"
    Use [r_pufky.game][a].


## Install Old Game Version
All games on steam are versioned and stored in a repository - this provides a
mechanism to install an old version for a game.

1. Find your game on [the Steam DB][b].
2. Locate the manifests for all versions of a game by navigating to a specific
    game version manifest:

    !!! example "Game ➔ APPID ➔ Packages ➔ SUBID ➔ Depots ➔ Depot ID ➔ Manifests"

    Example [manifest list][c].

3. Determine the **MANIFESTID** to use.

    Example [manifest][d].

4. Open the Steam console from browser:
    [steam://nav/console][e]. Steam Client Boot strapper should launch.
5. Download old version:

    ``` bash
    # download_depot <AppID> <DepotID> <ManifestID>
    download_depot 239140 335819 23871677621866113
    ```

    * **AppID** is found on the main game listing.
    * **DepotID** & **ManifestID** found on the manifest listing.
    * On completion the location of the download will be shown.
    * Downloaded to **Steam\steamapps\content\app_{APPID}\depot_{DEPOTID}**

7. Copy the original game files that will be overwritten to another location or
   back them up.
8. Copy the old version files into the game directory.
9. Disable the Internet connection before starting the game. Steam will
   typically force-update on launch. After launching the Internet connection
   can be restored.


## References[^1]

[^1]: https://steamcommunity.com/sharedfiles/filedetails/?id=889624474

[a]: https://galaxy.ansible.com/ui/repo/published/r_pufky/game/docs
[b]: https://steamdb.info
[c]: https://steamdb.info/depot/335819/manifests
[d]: https://steamdb.info/depot/335819/history/?changeid=M:6929390125920150286
[e]: steam://nav/console




