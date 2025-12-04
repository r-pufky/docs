# Manjaro

[Manjaro KDE][a].

!!! warning "[Disable Secure Boot][b]"
    Secure boot requires manual configuration and is not recommended.


## Install
Use [USB Boot Disk][c].

1. Boot with Proprietary drivers.
2. Click on **Install Manjaro Linux** on Desktop.
    * Language: **American English**.
    * Region: **America**.
    * Zone: **Los Angeles**.
    * Keyboard: **English (US) / Default**.
    * Disk: **Erase Disk / No Swap / EXT4**.
      * Encryption: ✔
    * User:
      * Login: **Username**.
      * Computer: **Hostname**.
      * Log in automatically without asking for password: ✘
      * Use the same password for the administrator account: ✘
      * Administrator account: **leave password empty** (disables logins).
    * Office Suite: **None / LibreOffice**.
3. Select **Wayland** at bottom left of login screen.

    !!! info "Avoid X11"
        Modern linux distributions have great support for Wayland applications
        and allow for better gaming experiences given the change in MVC model
        from network server to local machine.

        This can always be switched at the login screen.

4. Manjaro users default to ZSH shell. Set desired shell.

    ``` bash
    chsh {USER} -s /bin/bash
    ```

5. Disable root logins

    ``` bash
    passwd --lock root
    ```

6. [Secure SSH][d].


## Configure Updates

!!! note
    Prefer **pamac** when executing commands excluding update configuration.

    [**pacman**][e] is the Arch package manager and [**pamac**][f] is the
    Manjaro package manager using pacman libraries.

``` bash
# Top 20 fastest servers.
pacman-mirrors --fasttrack 10 && pacman -Syyu

# Or update based on Country.
pacman-mirrors --country United_States && pacman -Syyu
```

!!! example "⌘ ➔ add/remove software ➔ ⋮ ➔ preferences"
    * General:
        * Check for updates: ✔
        * Update check frequency: **every day**
        * Automatically download updates: ✔
        * Hide tray icon when no updates: ✔
        * Use mirrors from: **United_States**
    * Advanced:
        * Check available disk space: ✔
        * Remove un-required dependencies: ✔
    * Third Party:
        * Enable AUR support: ✔
        * Keep built packages: ✔
        * Check for updates: ✔
        * Check for development package updates: ✔


## Optional Packages
``` bash
pamac install iptable-nft  # More performant IPTable drop-in.

# Steam client
pamac install steam  # Do not install steam-native-runtime unless issues.

# Remove Manjaro branding / default homepage for browsers.
pacman -R manjaro-browser-settings
```


## Windows Dual-boot
Dual booting requires Windows 10 to use [UTC instead of RTC][h].

Set RTC (realtime clock) to UTC and use NTP with timezone.
``` bash
timedatectl set-local-rtc 0
sudo ln -sf /usr/share/zoneinfo/America/Los_Angeles /etc/localtime
systemctl enable --now systemd-timesyncd
```

!!! example "⌘ ➔ manjaro settings manager ➔ Time and Date"
    * Set time and date automatically: ✔
    * Hardware clock in local time: ✘

[a]: https://manjaro.org/downloads/official/kde
[b]: https://wiki.archlinux.org/title/Unified_Extensible_Firmware_Interface/Secure_Boot#Implementing_Secure_Boot
[c]: ../windows/README.md#create-uefi-usb-boot-disk
[d]: ../../service/ssh/sshd/linux.md
[e]: https://wiki.archlinux.org/title/Pacman
[f]: https://wiki.manjaro.org/index.php/Pamac
[h]: ../windows/troubleshooting.md#utc-realtime-clock
