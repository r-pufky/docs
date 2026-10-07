# Betterbird
Betterbird is better than Thunderbird in three ways: It contains new features
exclusive to Betterbird, it contains bug fixes exclusive to Betterbird and it
contains fixes that Thunderbird may ship at a later stage.

=== "CachyOS"
    Install via AUR helper.

    ``` bash
    pacman -S betterbird
    ```

=== "Windows"
    [Download][a] and install.

## Config

!!! example "⚙ ➔ Betterbird Settings"
    * General:
        * Disk Space:
            * Compact all folders when it will save over 500MB in total: ✔
                * Ask every time before compacting: ✔
    * Indexing:
        * Enable global search and indexer: ✘
    * Privacy & Security:
        * Mail Content:
            * Allow remote content in messages: ✘
        * Web Content:
            * Tell websites not to sell or share my data: ✔

!!! example "⚙ ➔ Account Settings"
    * {IMAP_ACCOUNT}
        * Synchronization & Storage:
            * Disk Space:
                * Synchronize all messages locally regardless of age: ✔
            * Rentention Policy:
                * Don't delete any messages: ✔
                * Always keep starred messages: ✔

### [Cardbook][b]
Contact management with vcard v3.0, v4.0 support.

!!! tip "v4.0 vcard supported"
    Create a new address book and explicitly set v4.0 format support.

!!! example "⚙ ➔ Add-ons and Themes ➔ Cardbook ➔ ⚙"
    * General:
        * Unique source for contacts: ✔
    * Display Tabs:
        * Lists: ✔
        * Technical: ✔
        * vCard: ✔
        * Public Keys: ✔
    * Show on Map with: **Google Maps**
    * Show name as: **Display Name**
    * Miscellaneous:
        * Show the number of contacts: ✔
        * Warn me when I attempt to drag contacts: ✔
        * Double-click on a contact edits it instead of emails it: ✔

!!! example "Address Book ➔ RMB ➔ Edit Address Book ➔ Miscellaneous"
    * Display Name Formula: **(({{1}} )({{2}} |{{6}} )({{4}} |{{3}} )({{5}} |)|{{7}})**
    * Apply to All Address Books
    * **Validate**

    Existing display names must be refreshed. This prefers names in the format:
    real > nick > family > other; organization name if nothing else present.

### [Remove Duplicate Messages][c]

!!! example "⚙ ➔ Add-ons and Themes ➔ Remove Duplicate Messages ➔ ⚙"
    * General Settings:
        * Review search results before deletion: ✔
        * Default action for duplicate messages: ✔
    * Message Comparison:
        * Message ID: ✔
        * Size (Headers & Body): ✔

[a]: https://www.betterbird.eu/downloads/
[b]: https://addons.thunderbird.net/de/thunderbird/addon/Cardbook/
[c]: https://addons.thunderbird.net/en-US/thunderbird/addon/removedupes/
