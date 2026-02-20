# Troubleshooting


## Increase Failed auth Lockout Attempts
CachyOS will lockout a user for 10 minutes on 3 failed password attempts over
15 minutes.

!!! danger ""
    Expressed as sudo not working with valid password or unable to login to the
    system.

!!! abstract "/etc/security/faillock.conf"
    0644 root:root

    ``` bash
    deny = 5
    fail_interval = 300
    unlock_time = 600
    ```

## Caps lock as Control
Override caps lock for keyboards that do not remap caps lock key.

!!! abstract "/etc/default/keyboard"
    0644 root:root

    ``` bash
    XKBOPTIONS="ctrl:nocaps"
    ```

For current session.
``` bash
localectl set-x11-keymap us pc105 ,query ctrl:nocaps
```

Reboot to apply.


## [Mouse Acceleration Seems Wonky][g]
Adaptive refresh seems to cause mouse acceleration issues in KDE Plasma Wayland.

!!! example "⌘ ➔ System Settings ➔ Input & Output"
    * Mouse & Touchpad (All devices)
        * Pointer Acceleration: **None**
    * Display & Monitor
        * Adaptive sync:  **Never**


## [List of User Installed Packages][e]
Only explicitly installed by user (no dependencies).

``` bash
pacman -Qqe | grep -v "$(awk '{print $1}' /desktopfs-pkgs.txt)"
```

Reference:


## [List of Package by Install Date][f]

``` bash
pacman -Syu expac
expac --timefmt='%Y-%m-%d %T' '%l\t%n' | sort -n
```

[e]: https://old.reddit.com/r/ManjaroLinux/comments/fzog8g/get_a_list_of_packages_you_installed_yourself
[f]: https://www.baeldung.com/linux/list-packages-by-install-date
[g]: https://discuss.kde.org/t/weird-mouse-anomalies-after-update-to-kde-plasma-6-1/17414