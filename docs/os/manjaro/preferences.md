# Preferences
These are personal configuration preferences.

## Install Arc and Papirus themes
``` bash
# Choose arc-icon-theme for recommended features.
pamac install papirus-icon-theme arc-gtk-theme
wget -qO- https://raw.githubusercontent.com/PapirusDevelopmentTeam/arc-kde/master/install.sh | env uninstall=true sh
wget -qO- https://raw.githubusercontent.com/PapirusDevelopmentTeam/arc-kde/master/install.sh | sh
sudo find /usr/share/{plasma,aurorae,color-schemes,konsole,konversation,Kvantum,plasma,wallpapers,yakuake} -type d -exec chmod o+rx {} \;
sudo find /usr/share/{plasma,aurorae,color-schemes,konsole,konversation,Kvantum,plasma,wallpapers,yakuake} -type f -exec chmod o+r {} \;
```

!!! note
    **Login** required. KDE will not display themes correctly until logging off
    and logging back in.

Reference:

* https://github.com/PapirusDevelopmentTeam/arc-kde/issues/140

## System Settings

### Global Theme

??? example "⌘ ➔ System Settings ➔ Appearance & Style"
    * Colors & Themes:
        * Global Theme:
            * Colors:  **Arc Dark**
            * Night Light: **Always off**
            * Application Style: **Breeze**
                * GNOME/GTK Application Style: **Breeze**
            * Plasma Style: **Arc Dark**
            * Window Decorations: **Arc Dark**
                * Titlebar Buttons (from left to right)
                    * Keep above other windows: **Leftmost**
                    * Keep below other windows: **Left**
                    * Context help: **Right**
                    * Shade: **Right**
                    * Minimize: **Right**
                    * Maximize: **Right**
                    * Close: **Rightmost**
            * Icons: **Papirus-Dark**
            * Cursors: **Breeze**
                * Configure Launch Feedback
                    * Cursor feedback: **None**
                    * Task Manager feedback: ✔
                    * Stop animations after: **5 seconds**
            * System Sound: **Ocean**
                * Enable Notification Sounds: ✘
            * Splash Screen: **Manjaro Splash 2.0**  (Use *Get New ...*)
            * Login Screen: **Breath**
            * Boot Splash Screen: **manjaro-mac-style**  (Use *Get New ...*)
        * Login Screen (SDDM)
            * Breath: ✔
            * Background: **/usr/share/wallpapers/SafeLanding/contents/images/*.jpg**

                !!! note
                    **Apply plasma settings** after setting background and any
                    other theme UI settings. This will apply the current UI
                    settings (arc dark) to the Breeze login screen; this should
                    match the **lockscreen**.
    * Text & Fonts:
        * Anti-Aliasing: ✔

??? example "⌘ ➔ System Settings ➔ Workspace"
    * General Behavior:
        * Display informational tooltips on mouse hover: ✔
        * Display visual feedback for status changes: ✔
        * Scrolling: **Prefer smooth scrolling**
        * Clicking files or folders: **Selects them**
        * Clicking in scrollbar track: **Scrolls to the clicked location**
        * Middle-click: **Pastes selected text**
        * Touch Mode: **Automatically enable as needed**
    * File Search:
        * File Indexing: ✘
    * Plasma Search:
        * All: ✘
        * Applications: ✔
        * System Settings: ✔
        * Calculator: ✔
        * Date and Time: ✔
        * Dictionary: ✔
        * Help Runner: ✔
        * Special Characters: ✔
        * Spell Checker: ✔
        * Terminate Applications: ✔
        * Unit Converter: ✔

??? example "⌘ ➔ System Settings ➔ Apps & Windows"
    * Default Applications:
        * Web browser: **Firefox**
        * Email client: **Firefox**
        * Image viewer: **Gwenview**
        * Music player: **Elisa**
        * Video player: **VLX media player**
        * Text editor: **VSCodium**
        * PDF Viewer: **Okular**
        * File manager: **Dolphin**
        * Terminal Emulator: **alacritty**
        * Archive manager: **Ark**
    * Window Management:
        * Window Behavior:
            * Focus:
                * Window activation policy: **Focus follows mouse**
                * Delay focus by: **300ms**
                * Focus stealing prevention: **None**
                * Raising window: **Click raises active window**
                * Multiscreen behavior: **Separate screen focus**
            * Titlebar Actions:
                * Double-click: **Maximize**
                * Mouse wheel: **Change opacity**
                * Maximize window by double clicking its frame: ✔
                * Maximize button action (left click): **Maximize**
                * Maximize button action (Middle click): **Vertically Maximize**
                * Maximize button action (Right click): **Horizontally Maximize**
            * Advanced:
                * Window placement: **Centered**
        * Task Switcher
            * Show selected window: ✔
            * Compact: ✔
        * Desktop Effects:
            * Accessibility:
                * All: ✘
                * Zoom: ✔
            * Appearance:
                * All: ✘
                * Blur: ✔
                * Desaturate Unresponsive Applications: ✔
                * Fading Popups: ✔
                * Full Screen: ✔
                * Highlight Screen Edges and hot Corners: ✔
                * Login: ✔
                * Logout: ✔
                * Maximize: ✔
                * Sliding Popups: ✔
            * Focus:
                * All: ✘
                * Dialog Parent: ✔
                * Dim Screen for Administrator Mode: ✔
            * Peek at Desktop Animation:  **Window Aperture**
            * Tools:
                * All: ✘
            * Virtual Desktop Switching Animation: **Slide**
            * Window Management: **Overview**
            * Window Open/Close Animation: **Fade**
        * Virtual Desktops:
            * Delete all extra desktops.
    * Notifications:
        * Do Not Distrub Mode: ✔ **when screens are mirrored **
        * Do Not Distrub Mode: ✔ **During screen sharing**
        * Critical Notifications: ✔ **Show in Do Not Disturb mode**
        * Normal Notifications: ✘
        * Low priority notifications: ✔ **Show popup**
        * Low priority notifications: ✘ **Show in history**
        * Location: ✔ **Near notification icon**
        * Hide: **5 seconds**
        * Application progress: ✔ **show in notifications**
        * Application progress: ✔ **Keep popup open during progress**
        * Application progress: ✔ **Show in task manager**
        * System Notifications:
            * All: ✘
            * Notification: ✔ **show a message in a pop-up**
        * Application Notifications:
            * All: ✘ (Re-enable to taste)

??? example "⌘ ➔ System Settings ➔ Input & Output"
    * Mouse & Touchpad ➔ Screen Edges
        * Upper left: **Lock Screen**
        * Upper Right: **Present Windows - All Desktops**
        * Trigger quarter tiling in: **outer 25%**
        * Switch on desktop edge: **Disabled**
        * Activation delay: **75ms**
        * Reactivation delay: **350ms**
        * Corner Barrier: ✔
        * Edge Barrier: **None**
    * Keyboard ➔ Shortcuts
        * KWin:
            * Make window fullscreen: **alt+return**
            * Maximize Window: **Meta_PgUp**
            * Minimize Window: **Meta_PgDown**
        * Krunner:
            * Launch: **Alt+Space, Search, Alt+F2**
        * plasmashell:
            * Activate Application Launcher Widget: **Meta+Space**
    * Accessibility:
        * System Bell:
            * Audible Bell: ✘
            * Visual Bell: ✘
        * Keyboard filters:
            * Slow keys: ✘
            * Bounce keys: ✘

??? example "⌘ ➔ System Settings ➔ Security & Privacy"
    * Screen Locking:
        * Lock screen automatically: **5 minutes**
        * Lock after waking from sleep: ✔
        * Delay before password required: **Require password immediately**
        * Keyboard shortcut: **Meta+L**
    * Recent Files:
        * Keep history: **For 1 month**
        * Remember opened documents: **Only for specific applications**
        * Exclude applications not on the list: ✔
    * User Feedback: **Disabled**

??? example "⌘ ➔ System Settings ➔ System ➔ Autostart"
    * Delete all.

## Taskbar

??? example "Clock ➔ MMB ➔ Configure Digital Clock"
    * Show date: ✔ **Awlays below**
    * Show seconds: **Only in tooltip**
    * Show time zone: **Only when different from local time zone**
    * Display timezone as: **Code*
    * Time display: **24 hour**
    * Date format: **ISO date**
    * Text display: **Automatic**

??? example "System Tray ➔ MMB ➔ Configure System Tray"
    * General:
        * Scale with Panel height: ✔
    * Entries:
        * Always show all entries: ✔
        * All: **Disabled**
        * Audio Volume: **Shown when relevant**
        * Bluetooth: **Shown when relevant**
        * Disks & Devices: **Shown when relevant**
        * Notifications: **Enable for file copy progress to be shown**

??? example "Taskbar ➔ MMB ➔ Show Panel Configuration"
    * Style: **Disable floating**

??? example "Remove Unused Tray Apps"
    * Show desktop
    * News
        * Autostart: ✘
        * Error notifications: ✘
    * Key lock status
    * Manjaro settings manager
        * Check unsupported kernels: ✘
        * Check missing language packs: ✘
        * Manually quit.

## Applications

!!! example "⌘ ➔ add/remove software ➔ ⋮ ➔ preferences ➔ third party"
    * Enable AUR support: ✔
    * Check for updates: ✔
    * Check for development packages updates: ✔

``` bash
pamac install alacritty git git-lfs vim tmux meld steam
#  extra/bind
pamac install signal-desktop discord
```

Remove extra software to taste
``` bash
pamac remove skanlit  # Flatbed scanning.
pamac remove hplip  # HP printer libraries.
pamac remove k3b  # CD burner.
pamac remove qbittorrent  # Torrents.
pamac thunderbird thunderbird-i18n-en-us  # Thick email client.
pamac remove yakuake  # Dropdown terminal.
pamac remove openconnect  # Cisco VPNs.
pamac remove networkmanager-openconnect  # Cisco VPNs.
```

[Install Chrome](../../app/chrome.md#manjaro).

[Install VSCodium](../../app/vscodium.md#manjaro).

## Remove MSN (Manjaro Settings Notifier)
Remove if you are an advanced user.

Comment out all contents:

**/etc/xdg/autostart/msm_kde_notifier.desktop**

**/etc/xdg/autostart/pamac-tray-plasma.desktop**

**/etc/xdg/autostart/org.fcitx.Fcitx5.desktop**

Optionally set immutable to prevent upgrades reverting changes.
``` bash
chattr +i /etc/xdg/autostart/{msm_kde_notifier.desktop,pamac-tray-plasma.desktop,org.fcitx.Fcitx5.desktop}
```

Reboot to apply changes

Reference:

* https://forum.manjaro.org/t/msm-notifier-access-error-when-saving-your-notification-settings/64671
* https://forum.manjaro.org/t/how-to-disable-discovernotifier-without-uninstalling-discover/65449
