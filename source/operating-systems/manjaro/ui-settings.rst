.. _manajaro-kde-plasma-ui-settings:

UI Settings
###########
KDE requires a logout for the fonts to become active in the session or just
import the fonts manually in ``font management`` after setup.

Themes
******
.. code-block:: bash
  :caption: Install Arc and Papirus themes

  pacman -Syu papirus-icon-theme arc-gtk-theme
  wget -qO- https://raw.githubusercontent.com/PapirusDevelopmentTeam/arc-kde/master/install.sh | sh

Re-login.

:cmdmenu:`⌘ --> system settings --> appearance --> global theme`

* arc dark

:cmdmenu:`⌘ --> system settings --> appearance --> global theme --> application style`

* breeze
* configure gnome/gtk application style
  * arc-dark

:cmdmenu:`⌘ --> system settings --> appearance --> global theme --> plasma style`

* arc dark

:cmdmenu:`⌘ --> system settings --> appearance --> global theme --> colors`

* arc dark

:cmdmenu:`⌘ --> system settings --> appearance --> global theme --> window decorations --> theme`

* arc dark

:cmdmenu:`⌘ --> system settings --> appearance --> global theme --> window decorations --> titlebar buttons`

* Remove: on all desktops
* Remove: more actions for this window
* Add: shade (right side, left of minimize)
* Add: keep below other windows (leftmost)
* Add: keep above other windows (right of keep below)

:cmdmenu:`⌘ --> system settings --> appearance --> global theme --> fonts`

* fixed width: SFMono Nerd Font 11pt regular

:cmdmenu:`⌘ --> system settings --> appearance --> global theme --> icons`

* papirus-dark

:cmdmenu:`⌘ --> system settings --> appearance --> global theme --> cursors`

* breeze

:cmdmenu:`⌘ --> system settings --> appearance --> global theme --> launch feedback`

* cursor: no feedback
* task manager: check enable animation
* stop animation after: 5 seconds

:cmdmenu:`⌘ --> system settings --> appearance --> global theme --> splash screen`

* QuarksSplashDarker (install from UI)

:cmdmenu:`⌘ --> system settings --> sddm login screen (sddm) --> login screen`

* Chili for Plasma (install from UI)
* background: ``/usr/share/wallpapers/SafeLanding/contents/images/*.jpg``

Langauge Packs
**************
:cmdmenu:`⌘ --> system settings --> language packs`

* Install all

Workspace Behavior
******************
:cmdmenu:`⌘ --> system settings --> workspace behavior`

:cmdmenu:`general behavior`

* clicking in scrollbar track: scrolls to clicked location

:cmdmenu:`dekstop effects`

* accessibility

  * zoom (configured automatically with 150% scaling)

* appearance

  * blur
  * destaturate unresponsive applications
  * fading popups
  * fall apart
  * full screen
  * login
  * logout
  * maximize
  * morphing popups
  * screen edge
  * sliding popups
  * translucency
  * squash

* focus

  * dialog parent
  * dim screen for administrative mode

* show desktop animation

  * eye on screen

* virtual desktop switchin animation

  * slide

* window management

  * desktop grid
  * present windows

* window open/close animation

  * glide

:cmdmenu:`screen edges`

* Upper left: lock screen
* Upper right: present windows - all desktops

:cmdmenu:`screen locking`

* ☑ lock screen automatically: 5mins
* ☑ after waking from sleep
* allow unlocking without a password for: 0 seconds
* keyboard shortcut: super + L
* appearance

  * ☑ clock
  * ☐ media controls
  * image: safe landing (same as login screen)

:cmdmenu:`virtual desktops`

* Remove additional desktops

:cmdmenu:`activities > privacy`

* keep history: 1 month (minimum time, clear current)
* remember opened documents: only for specific applications

  * sublime
  * ☑ blacklist applications not in the list

Startup & Shutdown
******************
:cmdmenu:`⌘ --> system settings --> startup and shutdown --> autostart`

* remove all

Windows Management
******************
:cmdmenu:`⌘ --> system settings --> windows management`

:cmdmenu:`window behavior`

* focus

  * window activation policy: focus follows mouse
  * delay focus by: 300ms
  * focus stealing prevention: low
  * raising windows: ☑ click raises active window

:cmdmenu:`task switcher`

* main

  * ☑ show selected window
  * ☑ thumbnail grid

Shortcuts
*********
:cmdmenu:`⌘ --> system settings --> shortcuts`

:cmdmenu:`shortcuts --> system services --> kwin`

* make window fullscreen: alt+return

:cmdmenu:`shortcuts --> applications --> krunner`

* krunner

  * ☐ alt+f2
  * ☑ search
  * ☑ alt+space

:cmdmenu:`shortcuts --> system services --> plasma`

* activate application launcher widget (activity switching)

  * delete: alt+f1
  * add: meta+space

.. note::
  This will enable meta only key and meta+space key for app launcher.

Search
******
:cmdmenu:`⌘ --> system settings --> search`

:cmdmenu:`file search`

* ☐ enable file search

:cmdmenu:`krunner`

* ☐ bookmarks
* ☐ browser history
* ☐ browser tabs
* ☐ kate sessions
* ☐ konsole proflies
* ☐ web search keywords

.. note::
  Krunner must be enabled for start searches

:cmdmenu:`web search keywords`

* ☐ enable web search keywords

Personalization
***************
:cmdmenu:`⌘ --> system settings --> personalization`

:cmdmenu:`notifications`

* do not disturb mode: ☐ enable when screens are minimized
* critical notifications: ☑ show in do not disturb mode
* normal notifications: ☐ show over full screen windows
* low priority notifications: ☑ show popup
* popup: ☑ show near notification icon
* hide after: 5secs
* application progress

  * ☐ show in task manager  (enable if GUI copy progress not showing)
  * ☐ show in notifications (enable if GUI copy progress not showing)
  * ☑ keep popup open during progress

* notifications badges: ☑ show in task manager

:cmdmenu:`accessibility`

* bell

  * ☐ audible bell
  * ☐ visible bell

* modifier keys

  * ☐ sticky keys

* keyboard filters

  * ☐ slow keys

* screen reader

  * ☐ enable screen reader

:cmdmenu:`applications --> default applications`

* email client: google chrome
* terminal emulator: alacritty

KDE Wallet
**********
:cmdmenu:`⌘ --> system settings --> kde wallet`

* wallet preferences

  * ☐ enable the kde wallet subsystem

* access control

  * ☑ prompt when an application accesses a wallet

User Feedback
*************
:cmdmenu:`⌘ --> system settings --> user feedback`

* disable

Input Devices
*************
:cmdmenu:`⌘ --> system settings --> hardware --> input devices --> touchpad`

* general

  * ☑ device enabled
  * ☑ disable when typing
  * ☐ left handed mode
  * ☐ press left and right buttons for middle click
  * 0.00: pointer accleration
  * acceleration profile: ☑ adaptive
  * ☑ tap to click
  * ☑ tap and drag
  * ☐ tap and drag lock
  * two finger click: ☑ right click (three-finger tap to middle click)
  * scrolling: ☑ two fingers
  * ☐ invert scroll direction
  * ☐ disable horizontal scrolling
  * right-click: ☑ press bottom-right corner
  * middle-click: ☑ press bottom-middle

Night Color
***********
:cmdmenu:`⌘ --> system settings --> hardware --> display and monitor --> night color`

* ☐ activate night color

Taskbar Clock
*************
:cmdmenu:`clock (lower right) --> settings --> appearance`

* information: ☑ show date (adaptive location)
* show time zone: ☑ only when different from local time zone
* display time zone as: code
* time display: 24-hour
* date format: iso date

System Tray
***********
:cmdmenu:`system tray --> settings --> general` or
:cmdmenu:`system tray --> RMB --> enter edit mode`

* panel icon size: ☑ scale with panel height

:cmdmenu:`system tray --> settings --> entries`

* ☑ always show all entries
* application status

  * default: always shown
  * media player: show when relevant
  * notifications: show when relevant (required for GUI file copy progress; unless disable in notifications settings)

* hardware control

  * default: show when relevant
  * display configuration: disabled
  * touchpad: disabled
  * key lock status: disabled
  * keyboard layout: disabled
  * kde connect: disabled

* system services

  * clipboard: disabled
  * disk quota: disabled
  * night color control: disabled

* miscellaneous

  * kate session: disabled
  * weather report: disabled

:cmdmenu:`system tray --> RMB --> enter edit mode`

* delete: show desktop

:cmdmenu:`system tray --> news --> settings`

* ☐ autostart
* ☐ show error notifications
* quit

:cmdmenu:`system tray --> manjaro settings manager --> options`

* ☐ check unsupported kernels
* ☐ check new kernels
* ☐ check missing language packs
* quit

:cmdmenu:`system tray --> key lock status`

* remove

:cmdmenu:`system tray --> shorcuts`

* remove all

Rename Terminals
****************
:cmdmenu:`⌘ --> alacritty --> edit`

* general

  * name: terminal

* application

  * name: terminal
  * description: terminal

:cmdmenu:`⌘ --> konsole --> edit`

* application

  * description: konsole
