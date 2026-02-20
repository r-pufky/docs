# Preferences
These are personal configuration preferences.


## Install [Arc and Papirus themes][a]
Arc-KDE is arc-dark for Plasma 6.

!!! warning "Re-login required after installation"
    Installation requires **re-login**. KDE will not display themes correctly
    until logging off and logging back in.

``` bash
# Choose arc-icon-theme for recommended features.
pacman -S ---needed papirus-icon-theme
# Uninstall with 'env uninstall=true sh'.
wget -qO- https://raw.githubusercontent.com/PapirusDevelopmentTeam/arc-kde/master/install.sh | sh
# Correct potential permission problems with UMASK (see reference).
sudo find /usr/share/{plasma,aurorae,color-schemes,konsole,konversation,Kvantum,plasma,wallpapers,yakuake} -type d -exec chmod o+rx {} \;
sudo find /usr/share/{plasma,aurorae,color-schemes,konsole,konversation,Kvantum,plasma,wallpapers,yakuake} -type f -exec chmod o+r {} \;
```


## Input & Output

!!! example "⌘ ➔ System Settings ➔ Input & Output"

### Mouse & Touchpad

!!! example "Mouse & Touchpad"
    * Mouse:
        * Device: **Select Mouse** (each mouse must be configured)
        * Pointer speed: **5**
        * Enable pointer acceleration: ✘
    * Touchpad:
        * Disable while typing: ✔
        * Pointer speed: **5**
        * Enable pointer acceleration: ✘
        * Scroll by moving two fingers anywhere: ✔
        * Scroll by natural scrolling direction: ✘
        * Right-click by pressing anywhere with two fingers: ✔
        * Tap to click: ✔
        * Allow dragging after tapping: ✔
        * Allow briefly lifting finger during tap-and-drag: ✔
        * Two-finger tap right-click (three finger for middle): ✔


### Keyboard

!!! example "Keyboard"
    * Shortcuts:
        * Plasma Workspace:
            * Activate Application Launcher: **Alt+F1, Meta**
            * Activate Application Launcher Widget: **Meta+Space**
        * Window Management:
            * Make window fullscreen: **Meta+Return**
            * Maximize Window: **Meta+PgUp**
            * Minimize Window: **Meta+PgDown**
        * Krunner:
            * Launch: **Alt+Space, Search, Alt+F2**

### Sound
Disable any unused device and name devices for sanity. Headset should be
enabled for all channels to allow for splitting recording and playback devices.

!!! example "Sound"
    * Rename Devices: Update to understandable names
    * Playback Devices:
        * HDMI: **off** (any HDMI output is generally unused)
        * Headset:
            * Profile: **Game Output + Chat Output + Chat Input**
    * Recording Devices: Mute all that are not used.
    * Notification Sounds: ✘

### Display & Monitor

!!! example "Display & Monitor"
    * Display Configuration:
        * Identify & arrange to taste
        * Refresh rate: **max**
        * Color profile: **Built-in**
        * Color accuracy: **Prefer color accuracy**
        * Control hardware brightness with DDC/CI: ✔
        * Enable EDR (Extended Dynamic Range): ✔
    * Night Light: **Always off**
    * Screen Edges:
        * Upper left: **Lock Screen**
        * Upper Right: **Present Windows - All Desktops**
        * Maximize windows dragged to top edge: ✔
        * Tile windows dragged to left or right edge: ✔
        * Trigger quarter tiling in: **outer 25%**
        * Switch on desktop edge: **Disabled**
        * Activation delay: **75ms**
        * Reactivation delay: **350ms**
        * Corner Barrier: ✔
        * Edge Barrier: **None**

### Accessibility

!!! example "Accessibility"
    * System Bell:
        * Audible Bell: ✘
        * Visual Bell: ✘
    * Modifier Keys:
        * Sticky keys: ✘
    * Keyboard filters:
        * Slow keys: ✘
        * Bounce keys: ✘
    * Activation Shortcuts:
        * Ring the system bell: ✘
    * Shake Pointer:
        * Shake pointer to find it: ✘


## Appearance & Style
Apply the base global theme to have a consistent starting point. Window menu is
setup in [Window Management](#window-management).

!!! example "⌘ ➔ System Settings ➔ Appearance & Style"

!!! example "Colors & Themes"
    * Global Theme: **Breeze Dark** (Apply appearance, desktop, window layout)
    * Colors:
        * Accent color: **Accent color from color scheme**
        * Scheme: **Arc Dark**
    * Application Style: **Breeze**
    * Plasma Style: **Arc Dark**
    * Window Decorations:
        * Decorations: **Arc Dark**
        * Style: **Theme default (Normal window borders)**
        * ⋮ ➔ Configure Titlebar Buttons (from left to right)
            * Keep above other windows: **Left**
            * Keep below other windows: **Left**
            * Context help: **Right**
            * Minimize: **Right**
            * Maximize: **Right**
            * Close: **Rightmost**
    * Icons: **Papirus-Dark**
    * Cursors: **Breeze Dark**
        * Configure Launch Feedback
            * Cursor feedback: **None**
            * Task Manager feedback: ✔
            * Stop animations after: **5 seconds**
    * System Sound: **Ocean**
        * Enable Notification Sounds: ✘
    * Splash Screen: **CachyOS Nord**
    * Boot Splash Screen: **cachyos-bootanimation**

!!! example "Wallpaper"
    * Set for all screens: ✔
    * Add: **/usr/share/wallpapers/Arc-Mountains/contents/images/8000x4500.png**
    * Wallpaper: **8000x4500.png**

!!! example "Text & Fonts"
    * Fonts
        * Anti-Aliasing: ✔

!!! example "Animations"
    * Global animation speed: **80%** (4 ticks left)
    * Window open/close: **None**
    * Window maximize: **None**
    * Window minimize: **None**
    * Window full screen: **None**
    * Peek at desktop: **Window Aperture**
    * Virtual desktop switching: **Slide**
    * Fading popups: ✔
    * Sliding popups: ✔
    * Login fade: ✔
    * Logout fade: ✔


## Apps & Windows

!!! example "⌘ ➔ System Settings ➔ Apps & Windows"

### Default Applications

!!! example "Default Applications"
    * Web browser: **Firefox**
    * Email client: **Firefox**
    * Image viewer: **Gwenview**
    * Music player: **mpv media player**
    * Video player: **mpv media player**
    * Text editor: **Code - OSS**
    * PDF Viewer: **Firefox**
    * File manager: **Dolphin**
    * Terminal Emulator: **alacritty**
    * Archive manager: **Ark**

### Notifications

!!! example "Notifications"
    * Do Not Disturb mode when screens are mirrored: ✔
    * Do Not Disturb mode during screen sharing: ✔
    * Do Not Disturb mode while a fullscreen application is focused: ✔
    * Critical Notifications show in Do Not Disturb mode: ✔
    * Low priority notifications show popup: ✔
    * Low priority notifications show in history: ✘
    * Popups location near notification icon: ✔
    * Popups hide after: **5 seconds**
    * Popups show timeout indicator: ✘
    * Application progress show in notifications: ✔
    * Application progress keep popup open during progress: ✔
    * Notification badges show in task manager: ✔
    * System Notifications:
        * All: ✘
        * Notification:
            * Show a message in a pop-up: ✔
    * Application Notifications:
        * All: ✘ (Re-enable to taste)
        * Authentication System: **defaults**
        * Bluetooth: **defaults**
        * Device Notifier: **defaults**
        * KDE Wallet: **defaults**
        * Network Management: **defaults**

### Window Management

!!! example "Window Management"
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
        * Thumbnail Grid: ✔
    * Desktop Effects:
        * Accessibility:
            * All: ✘
        * Appearance:
            * All: ✘
            * Blur: ✔
            * Desaturate Unresponsive Applications: ✔
            * Highlight Screen Edges and hot Corners: ✔
        * Focus:
            * All: ✘
            * Dialog Parent: ✔
            * Dim Screen for Administrator Mode: ✔
        * Window Management:
            * All: ✘
            * Overview: ✔
        * Peek at Desktop Animation:  **Window Aperture**
    * Virtual Desktops:
        * Virtual Desktop Switching Animation: **Slide**
        * Delete all extra desktops.


## Workspace

!!! example "⌘ ➔ System Settings ➔ Workspace"

### General Behavior

!!! example "General Behavior"
    * Allow Plasma to show panel and widget tooltips: ✔
    * Allow Plasma to show OSD popups for status changes: ✔
    * Clicking in scrollbar track: **Scrolls to the clicked location**
    * Prefer smooth scrolling: ✔
    * Clicking files or folders: **Selects them**
    * Middle-click: **Pastes selected text**
    * When dragging file or folders: **Always ask what to do**
    * Touch Mode: **Automatically enable as needed**

### Search

!!! example "Search"
    * File Search:
        * Data to index: **Nothing (disable indexing entirely)**
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
    * Configure KRunner:
        * Position on screen: **Center**
        * Activation: **Activate when pressing any key on the desktop**
        * History: **Disabled**


## Security & Privacy

!!! example "⌘ ➔ System Settings ➔ Security & Privacy"

### Login Screen

!!! note
    **Apply plasma settings** after setting background and any other theme UI
    settings. This will apply the current UI settings to the login screen; this
    should match the **lockscreen**.

!!! example "Login Screen"
    * Automatically log in: ✘
    * Default user: **{USER}**
    * Default session: **Last logged-in session**
    * Configure Appearance:
        * Show clock: **Always**
        * Add: **/usr/share/wallpapers/Arc-Mountains/contents/images/8000x4500.png**

### Screen Locking

!!! example "Screen Locking"
    * Lock screen automatically: **5 minutes**
    * Lock after waking from sleep: ✔
    * Delay before password required: **Require password immediately**
    * Keyboard shortcut: **Meta+L**
    * Appearance:
        * Show clock: **Always**
        * Media controls: ✘
        * Add: **/usr/share/wallpapers/Arc-Mountains/contents/images/8000x4500.png**
    * Images: **8000x4500.png**

### KDE Wallet

!!! example "KDE Wallet"
    * Enable the KDE Wallet Subsystem: ✔
    * Close wallet when last application stops using it: ✔
    * Close wallet when screensaver starts: ✔
    * Close wallet when unused for: **10 minutes**
    * Use KDE Wallet for the Secret Service interface: ✔

### Recent Files

!!! example "Recent Files"
    * Keep history: **For 1 month**
    * Remember opened documents: **Only for specific applications**
    * Exclude applications not on the list: ✔ (remove all applications)

### User Feedback

!!! example "User Feedback"
    * Plasma: **Disabled**


## System

!!! example "⌘ ➔ System Settings ➔ System"

### Power Management
USB devices tend not to re-appear after suspending sessions. This applies
mainly to Desktops. Laptops should leave power management enabled.

!!! example "Power Management"
    * Suspend session when inactive: **Do nothing**
    * When power button pressed: **Show logout screen**
    * Switch to power profile: **Leave unchanged**
    * When inactive run after: **5 minutes**

### Autostart

!!! example "Autostart"
    * Delete all.

### Session

!!! example "Session"
    * Ask for confirmation on shutdown, restart, and logout: ✔
    * On login launch apps that were open: **Start with an empty session**


## Taskbar

### Digital Clock

!!! example "Clock ➔ RMB ➔ Configure Digital Clock"
    * Show date: ✔ **Always below**
    * Show seconds: **Only in tooltip**
    * Show time zone: **Only when different from local time zone**
    * Display timezone as: **Code**
    * Time display: **24 hour**
    * Date format: **ISO date**
    * Text display: **Automatic**

### System Tray
Target below up arrow for menu or near the bottom edge under icons.

!!! example "System Tray ➔ RMB ➔ Configure System Tray"
    * General:
        * Scale with Panel height: ✔
    * Entries:
        * All: **Disabled**
        * Audio Volume: **Show when relevant**
        * Bluetooth: **Show when relevant**
        * Disks & Devices: **Show when relevant**
        * Networks: **Show when relevant**
        * Power & Battery: **Always show**
        * Clipboard: **Show when relevant**
            * Clipboard history: ✘
            * History size: **1**
            * Keep the selection and clipboard the same: ✔
            * Text selection: **only when explicitly copied**
            * Non-text selection: **never save in history**
        * Media Player: **Show when relevant**
        * Notifications: **Show when relevant** (for file copy progress)
        * Always show all entries: ✔ (enable after setting above entries)

### Taskbar

!!! example "Taskbar ➔ RMB ➔ Show Panel Configuration"
    * Style: **Disable floating**
    * Panel Height: **32**
    * Peek at Desktop: **Remove**


## Packages

``` bash
pacman -S --needed alacritty git git-lfs vim tmux meld ncdu htop
pacman -S --needed signal-desktop steam mumble
# MPV with remove API (hotkey control)
pacman -S --needed mpv mpv-mpris
```

[Install Chrome](../../app/chrome.md).

[Install VSCodium](../../app/vscodium/README.md).

[a]: https://github.com/PapirusDevelopmentTeam

## Reference[^1]

[^1]: https://github.com/PapirusDevelopmentTeam/arc-kde/issues/140
