.. _steam-older-game-versions:

Steam Older Game Versions
#########################
All games on steam are versioned and stored in a repository; this provides a
mechanism to install an old version for a game.

#. Find your game on `the Steam DB <https://steamdb.info/>`_.
#. Locate the manifests for all versions of a game by navigating to a specific
   game version manifest:

   :cmdmenu:`Game --> APPID --> Packages --> SUBID --> Depots --> Depot ID --> Manifests`

   `example manifest list <https://steamdb.info/depot/335819/manifests/>`_.
#. Determine the ``MANIFESTID`` to use.
   `example manifest <https://steamdb.info/depot/335819/history/?changeid=M:6929390125920150286>`_.
#. Open the Steam console from browser: `steam://nav/console <steam://nav/console>`_.
   Steam Client Bootstrapper should launch.
#. Download the old version:
   
   .. code-block:: bash
     :caption: download_depot <AppID> <DepotID> <ManifestID>

     download_depot 239140 335819 23871677621866113

   * ``AppID`` is found on the main game listing.
   * ``DepotID`` & ``ManifestID`` found on the manifest listing.
   * On completion the location of the download will be shown.

#. Data will be downloaded but not installed. It is typically located:

   ``Steam\steamapps\content\app_{APPID}\depot_{DEPOTID}``

#. Copy the original game files that will be overwritten to another location or
   back them up.
#. Copy the old version files into the game directory.
#. Disable the Internet connection before starting the game; as steam will
   typically force-update on launch. After launched, the Internet connection
   can be restored.

.. rubric:: References

#. `Download older versions of Steam game <https://steamcommunity.com/sharedfiles/filedetails/?id=889624474>`_
