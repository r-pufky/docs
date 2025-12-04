# Troubleshooting


## Increase Failed auth Lockout Attempts
Manjaro will lockout a user for 10 minutes on 3 failed password attempts over
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


## Application Scaling
High DPI monitors require custom scaling settings.

!!! example "⌘ ➔ system settings ➔ display and monitor ➔ display configuration"
    * Global scale: **150%**
    * Legacy applications (X11): **Apply scaling themselves**


## [Fonts look fuzzy][a]
Fonts may not support subpixel hints or it may be disabled.

Copy custom fonts to system.
``` bash
# Requires reboot if not manually loaded in Font Manager.
cp {FONTS} /usr/share/fonts
systemsettings kcm_fontinst  # Font Manager in GUI.
```

Tweak font display for LCD's if display is still not clean.

!!! abstract "/etc/fonts/local.conf"
    0644 root:root

    ``` xml
    <?xml version="1.0"?>
    <!DOCTYPE fontconfig SYSTEM "fonts.dtd">
    <fontconfig>
      <match target="font">
        <edit name="autohint" mode="assign">
          <bool>false</bool>
        </edit>
        <edit name="hinting" mode="assign">
          <bool>true</bool>
        </edit>
        <edit name="antialias" mode="assign">
          <bool>true</bool>
        </edit>
        <edit mode="assign" name="hintstyle">
          <const>hintslight</const>
        </edit>
        <edit mode="assign" name="rgba">
          <const>rgb</const>
        </edit>
        <edit mode="assign" name="lcdfilter">
          <const>lcddefault</const>
        </edit>
      </match>
    </fontconfig>
    ```

!!! abstract "~/.Xresources"
    0644 {USER}:{USER}

    ``` bash
    Xft.antialias: 1
    Xft.hinting: 1
    Xft.autohint: 0
    Xft.rgba: rgb
    Xft.hintstyle: hintslight
    Xft.lcdfilter: lcddefault
    ```

Merge settings, link additional profiles, and update cache.
``` bash
xrdb -merge ~/.Xresources
ln -s /usr/share/fontconfig/conf.avail/10-sub-pixel-rgb.conf /etc/fonts/conf.d/
ln -s /usr/share/fontconfig/conf.avail/11-lcdfilter-default.conf /etc/fonts/conf.d/
fc-cache -f -v
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


## [Windows Opening on Wrong Monitor][b]
Some applications misbehave.

!!! example "System Settings ➔ Apps & Windows ➔ Window Management"
    * Window Behavior:
        * Advanced:
            * Window placement: **Centered**
    * Window Rules:
        * Add New:
            * Description: **Fix windows starting on wrong screen**
            * Window class (application): **Unimportant**
            * Match whole window class: **No**
            * Window types: **Normal Window**  # un-select all others.
            * Add Property:
                * Ignore requested geometry:
                    * Apply Initially: **Yes**


## [Manjaro Updates Consistently Fail][c]
Last update was more than six months ago and [keys are expired][d].

!!! abstract "/etc/pacman.conf"
    0644 root:root

    ``` bash
    # Only for expired PGP keys -- DANGEROUS - always revert after updates.
    # SigLevel = Required DatabaseOptional
    SigLevel = Optional TrustAll
    ```

``` bash
pamac update
```


## [Mouse Acceleration Seems Wonky][g]
Adaptive refresh seems to cause mouse acceleration issues in KDE Plasma Wayland.

!!! example "⌘ ➔ System Settings ➔ Input & Output"
    * Mouse & Touchpad (All devices)
        * Pointer Acceleration: **None**
    * Display & Monitor
        * Adaptive sync:  **Never**


## Recover from a Bad Upgrade with Encrypted Root Disk
Generally when Windows decides it's the boot manager and is wrong.

Boot from [USB Boot Disk](README.md#install).

Mount LUKS Volume
``` bash
ls -l /dev/{nvme,sd}*

# Mount LUKS encrypted partition.
crypt setup -v luksOpen /dev/{PARTITION} crypt_drive

# Mount and decrypt.
mount /dev/mapper/crypt_drive /mnt

# Switch to installed system root and update.
manjato-chroot /mnt
pacman-mirrors --fasttrack 5 && pacman -Syyu

# Update EFI boot manager.
efibootmgr -v
grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=manjaro --recheck
grub-mkconfig -o /boot/grub/grub.cfg
mkinitcpio -P
pacman -S linux
efibootmgr -v
```


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

[a]: https://wiki.manjaro.org/index.php/Improve_Font_Rendering
[b]: https://old.reddit.com/r/kde/comments/gx8dch/programs_always_open_on_wrong_monitor
[c]: https://gitlab.archlinux.org/archlinux/archlinux-keyring/-/issues/286
[d]: https://old.reddit.com/r/ManjaroLinux/comments/1lr0sdz/having_trouble_updating_with_pacman_corrupted
[e]: https://old.reddit.com/r/ManjaroLinux/comments/fzog8g/get_a_list_of_packages_you_installed_yourself
[f]: https://www.baeldung.com/linux/list-packages-by-install-date
[g]: https://discuss.kde.org/t/weird-mouse-anomalies-after-update-to-kde-plasma-6-1/17414