# BlueBubbles
Opensource iMessages.

## Setup
[VM's may be used](https://docs.bluebubbles.app/server/advanced/macos-virtualization/running-a-macos-vm/enabling-imessage-in-a-vm)
but are fragile and complicated. It is better to use actual hardware to prevent
flagging your Apple account.

Install [Chrome](https://www.google.com/chrome).

Install [BlueBubbles](https://bluebubbles.app/downloads/server).

## Installation Notes
Follow the [instructions on the site](https://bluebubbles.app/install/) and
[Disable SIP](https://docs.bluebubbles.app/private-api/installation).

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

**/etc/ssh/sshd_config** (1)
{ .annotate }

1. 0644 root:root
``` bash
# Setup authorized_keys before disabling passwords.
PasswordAuthentication no

# This option appears only in new versions of macOS
KbdInteractiveAuthentication no

# This option appears only in old versions of macOS
ChallengeResponseAuthentication no
```
