# BlueBubbles
Opensource iMessages.

## Setup
[VM's may be used][a] but are fragile and complicated. It is better to use
actual hardware to prevent flagging your Apple account.

Install [Chrome][b].

Install [BlueBubbles][c].

## Installation Notes
Follow the [instructions on the site][d] and [Disable SIP][e].

!!! example "BlueBubbles ➔ Settings"
    * Connection Settings:
        * Messages Private API: ✔
        * FaceTime Private API: ✔
        * FaceTime Calling: ✔
    * Features:
        * Open FindMy App on Startup: ✔
        * Keep MacOS Awake: ✔
        * Auto Start Method: Launch Agent
        * Start Minimized: ✔
        * Show Dock Badge: ✔
        * Hide Dock Icon: ✔
    * Update Settings:
        * Check for Updates on Startup: ✔
        * Use OLED Black Dark Mode: ✔

!!! example "⌘ ➔ System Settings ➔ Users & Groups"
    * Automatically log in as: **{USER}**

### Enable SSH
!!! example "⌘ ➔ System Settings ➔ Sharing ➔ Remote Login"
    * Remote Login: ✔
        * Allow full disk access for remote users: ✔
        * Allow access for: **{USER}**

??? abstract "/etc/ssh/sshd_config"
    0644 root:root

    ``` bash
    # Setup authorized_keys before disabling passwords.
    PasswordAuthentication no

    # This option appears only in new versions of macOS
    KbdInteractiveAuthentication no

    # This option appears only in old versions of macOS
    ChallengeResponseAuthentication no
    ```

[a]: https://docs.bluebubbles.app/server/advanced/macos-virtualization/running-a-macos-vm/enabling-imessage-in-a-vm
[b]: https://www.google.com/chrome
[c]: https://bluebubbles.app/downloads/server
[d]: https://bluebubbles.app/install/
[e]: https://docs.bluebubbles.app/private-api/installation
