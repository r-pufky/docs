# [Maintainerr][a]
Maintainerr makes managing your media easy. No longer will you have to worry
about your precious hard drive space being taken up by media, that isn't even
being watched.

## Overview
Maintainerr configuration is non-intuitive.

!!! danger "Default user state is Plex owner"
    Plex owner account state is generally used for **per-user** item status
    (e.g. isWatched) etc. When using new matches, always confirm with a Plex
    owner user and a standard user with known values for specific media to
    ensure the rule is matching appropriately.

    In most cases it probably is not.

!!! warning "Watched status"
    Plex treats **marked as watched** and **viewed** (fully view by a user) as
    two separate states. See [remove on user viewed](#remove-on-user-viewed)
    for an example that appropriately handles this.

### [Rules][c]
Evaluate media on server based on parameters set. If a media item matches a
rule, it is added to a collection.

Define constraints around items placed in a collection. Items are operated on
in bulk at the scale of the item placed (e.g. episodes will be per-episode,
season is per-season, series is per-series).

!!! warning "Changing the item type will remove all items from the collection"

### [Collections][d]
A collection container will be auto-generated when a rule is initially created.
Items in this collection will be deleted (or whatever action is specified by
the rule). Collections are visible to all Plex users on the collections tab.

!!! warning "Changing rule item type will remove all items from the collection"

## Examples

### Remove on user viewed
Cleanup reality shows (All shows that match 'The Real Housewives', 'Love
Island', 'Below Deck') that are only watched once by a single user. An episode
will be marked for deletion after it has at least one full view and is marked
watched by Plex owner. Deletion occurs every 30 days.

Remove monitored status from Sonarr and delete matched episode.

!!! warning "Only enable Sonarr/Plex actions after validation"
    Run the rule and check the auto-populated collection to ensure the correct
    episodes appear before enabling deletion!

!!! example "Rules ➔ New Rule ➔ General"
    * Name: **Maintenance: Shows**
    * Description: **Cleanup shows watched by only one person**
    * Library: **TV Shows**
    * Media Type: **Episodes**
    * Sonarr Server: **{SONARR}**
    * Sonarr Action: **Unmonitor and delete episode**  # 'Do nothing' for testing.
    * Take action after days: **30**

!!! example "Rules ➔ New Rule ➔ Options"
    * Active: ✔  # Disable to run tests.
    * Show on Plex library recommended: ✘
    * Show on Plex home: ✘
    * Enable Overlays: ✘
    * Use Rules: ✔
    * Custom Collection: ✘
    * Notifications: ✘
    * Keep logs for months: **6**
    * Sort title: **{DEFAULT}**
    * Collection items sort: **Default**
    * Rule handler schedule override: ✘
    * Custom Collection Poster: ✘

!!! example "Rules ➔ New Rule ➔ Rules"
    * Rule 1:
        * First Value: **Sonarr - Series title**
        * Action: **Contains (Exact list match)**
        * Second Value: **Text**
        * Custom Value: **["The Real Housewives", "Love Island", "Below Deck"]**  # JSON list.
    * Rule 2:
        * First Value: **Plex - Total views**
        * Action: **Bigger**
        * Second Value: **Number**
        * Custom Value: **0**
    * Rule 3:
        * Operator: **AND**
        * First Value: **Plex - Is Watched**
        * Action: **Equals**
        * Second Value: **Boolean**
        * Custom Value: **True**

[a]: https://maintainerr.info/
[b]: https://docs.maintainerr.info/
[c]: https://docs.maintainerr.info/rules/
[d]: https://docs.maintainerr.info/collections/
