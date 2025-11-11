# Troubleshooting

## Increase Failed auth Lockout Attempts
Manjaro will lockout a user for 10 minutes on 3 failed password attempts over
15 minutes.

!!! danger "Error"
    Expressed as sudo not working with valid password or unable to login to the
    system.

**/etc/security/faillock.conf** (1)
{ .annotate }

1. 0644 root:root
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

## Fonts look fuzzy
Fonts may not support subpixel hints or it may be disabled.

Copy custom fonts to system.
``` bash
# Requires reboot if not manually loaded in Font Manager.
cp {FONTS} /usr/share/fonts
systemsettings kcm_fontinst  # Font Manager in GUI.
```

Tweak font display for LCD's if display is still not clean.

**/etc/fonts/local.conf** (1)
{ .annotate }

1. 0644 root:root
    ``` bash
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

**~/.Xresources** (1)
{ .annotate }

1. 0644 {USER}:{USER}
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

Reference:

* https://wiki.manjaro.org/index.php/Improve_Font_Rendering

## Caps lock as Control
Override caps lock for keyboards that do not remap caps lock key.

**/etc/default/keyboard** (1)
{ .annotate }

1. 0644 root:root
    ``` bash
    XKBOPTIONS="ctrl:nocaps"
    ```

For current session.
``` bash
localectl set-x11-keymap us pc105 ,query ctrl:nocaps
```

Reboot to apply.

## Windows Opening on Wrong Monitor
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

Reference:

* https://old.reddit.com/r/kde/comments/gx8dch/programs_always_open_on_wrong_monitor/

## Manjaro Updates Consistently Fail
Last update was more than six months ago and keys are expired.

**/etc/pacman.conf** (1)
{ .annotate }

1. 0644 root:root
``` bash
# Only for expired PGP keys -- DANGEROUS - always revert after updates.
# SigLevel = Required DatabaseOptional
SigLevel = Optional TrustAll
```

``` bash
pamac update
```

Reference:

* https://gitlab.archlinux.org/archlinux/archlinux-keyring/-/issues/286
* https://old.reddit.com/r/ManjaroLinux/comments/1lr0sdz/having_trouble_updating_with_pacman_corrupted/
