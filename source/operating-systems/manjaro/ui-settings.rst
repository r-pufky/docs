.. _manajaro-kde-ui-settings:

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

Global Theme
************
.. gui:: General
  :nav:    ⌘ --> system settings
  :path:   appearance --> global theme
  :value0: ☑, arc dark
  :update: 2021-12-20

.. gui:: Application Style
  :nav:    ⌘ --> system settings
  :path:   appearance --> global theme --> application style
  :value0:                                       ☑, breeze
  :value1: › configure gnome/gtk application style, arc dark
  :update: 2021-12-20

.. gui:: Plasma Style
  :nav:    ⌘ --> system settings
  :path:   appearance --> global theme --> plasma style
  :value0: ☑, arc dark
  :update: 2021-12-20

.. gui:: Colors
  :nav:    ⌘ --> system settings
  :path:   appearance --> global theme --> colors
  :value0: ☑, arc dark
  :update: 2021-12-20

.. gui:: Theme
  :nav:    ⌘ --> system settings
  :path:   appearance --> global theme --> window decorations --> theme
  :value0: ☑, arc dark
  :update: 2021-12-20

.. gui:: Titlebar Buttons
  :nav:    ⌘ --> system settings
  :path:   appearance --> global theme --> window decorations
           titlebar buttons
  :value0: {DELETE}, on all desktops
  :value1: {DELETE}, more actions for this window
  :value2:        ☑, shade (right side - left of minimize)
  :value3:        ☑, keep below other windows (leftmost)
  :value4:        ☑, keep above other windows (right of keep below)
  :update: 2021-12-20

.. gui:: Fonts
  :nav:    ⌘ --> system settings
  :path:   appearance --> global theme --> fonts
  :value0: fixed width, SFMono Nerd Font 11pt regular
  :update: 2021-12-20

.. gui:: Icons
  :nav:    ⌘ --> system settings
  :path:   appearance --> global theme --> fonts
  :value0: ☑, papirus-dark
  :update: 2021-12-20

.. gui:: Cursors
  :nav:    ⌘ --> system settings
  :path:   appearance --> global theme --> cursors
  :value0: ☑, breeze
  :update: 2021-12-20

.. gui:: Launch Feedback
  :nav:    ⌘ --> system settings
  :path:   appearance --> global theme --> launch feedback
  :value0:               cursor, no feedback
  :value1:         task manager, check enable animation
  :value2: stop animation after, 5 seconds
  :update: 2021-12-20

.. gui:: Splash Screen
  :nav:    ⌘ --> system settings
  :path:   appearance --> global theme --> splash screen
  :value0: ☑, QuarksSplashDarker (Install from UI)
  :update: 2021-12-20

Startup & Shutdown
******************
.. gui:: Login Screen
  :nav:    ⌘ --> system settings --> startup and shutdown
  :path:   login screen (sddm)
  :value0:            ☑, Chili for Plasma (Install from UI)
  :value1: › background, ``/usr/share/wallpapers/SafeLanding/contents/images/*.jpg``
  :update: 2021-12-20

.. gui:: Autostart
  :nav:    ⌘ --> system settings --> startup and shutdown
  :path:   autostart
  :value0: {DELETE}, all
  :update: 2021-12-20

Langauge Packs
**************
.. gui:: Language Packs
  :nav:    ⌘ --> system settings
  :path:   language packs
  :value0: {ADD}, all language packs
  :update: 2021-12-20
  :open:

Workspace Behavior
******************
.. gui:: General Behavior
  :nav:    ⌘ --> system settings --> workspace behavior
  :path:   general behavior
  :value0: clicking in scrollbar track: scrolls to clicked location
  :update: 2021-12-20

.. gui:: Desktop Effects
  :nav:     ⌘ --> system settings --> workspace behavior
  :path:    desktop effects
  :value0:                         accessibility,  
  :value1:                                   › ☑, zoom (configured automatically with 150% scaling)
  :value2:                            appearance,  
  :value3:                                   › ☑, blur
  :value4:                                   › ☑, destaturate unresponsive applications
  :value5:                                   › ☑, fading popups
  :value6:                                   › ☑, fall apart
  :value7:                                   › ☑, full screen
  :value8:                                   › ☑, login
  :value9:                                   › ☑, logout
  :value10:                                  › ☑, maximize
  :value11:                                  › ☑, morphing popups
  :value12:                                  › ☑, screen edge
  :value13:                                  › ☑, sliding popups
  :value14:                                  › ☑, translucency
  :value15:                                  › ☑, squash
  :value16:                                focus,  
  :value17:                                  › ☑, dialog parent
  :value18:                                  › ☑, dim screen for administrative mode
  :value19:               show desktop animation,  
  :value20:                                  › ☑, eye on screen
  :value21:  virtual desktop switching animation,  
  :value22:                                  › ☑, slide
  :value23:                    window management,  
  :value24:                                  › ☑, desktop grid
  :value25:                                  › ☑, present windows
  :value26:          window open/close animation,  
  :value27:                                  › ☑, glide
  :update: 2021-12-20

.. gui:: Screen Edges
  :nav:    ⌘ --> system settings --> workspace behavior
  :path:   screen edges
  :value0:             {UPPPER LEFT}, lock screen
  :value1:             {UPPER RIGHT}, present windows - all desktops
  :value2:                         ☑, windows dragged to top edge
  :value3:                         ☑, windows dragged to left or right edge
  :value4: trigger quarter tiling in, outer 25%
  :value5:    switch on desktop edge, {OFF}
  :value6:          activation delay, 500ms
  :value7:        reactivation delay, 1000ms
  :update: 2021-12-20

.. gui:: Screen Locking
  :nav:    ⌘ --> system settings --> workspace behavior
  :path:   screen locking
  :value0:            ☑ lock screen automatically, 5mins
  :value1:                                    › ☑, after waking from sleep
  :value2: allow unlocking without a password for, 0 seconds
  :value3:                      keyboard shortcut, ⌘ + L
  :value4:                             appearance,  
  :value5:                                    › ☑, clock
  :value6:                                    › ☐, media controls
  :value7:                                › image, safe landing (same as login screen)
  :update: 2021-12-20

.. gui:: Virtual Desktops
  :nav:    ⌘ --> system settings --> workspace behavior
  :path:   virtual desktops
  :value0: {DELETE}, all
  :update: 2021-12-20

.. gui:: Activities
  :nav:    ⌘ --> system settings --> workspace behavior
  :path:   activities --> privacy
  :value0:              keep history, 1 month
  :value1: remember opened documents, only for specific applications
  :value2:                         ›, sublime
  :value3:                         ☑, blacklist applications not in the list
  :update: 2021-12-20

  The minimum time is one month; clear current data.

Windows Management
******************
.. gui:: Window Behavior
  :nav:    ⌘ --> system settings --> windows management
  :path:   window behavior
  :value0:                       focus,  
  :value1:  › window activation policy, focus follows mouse
  :value2:            › delay focus by, 300ms
  :value3: › focus stealing prevention, low
  :value4:                         › ☑, click raises active window
  :update: 2021-12-20

.. gui:: Task Switcher
  :nav:    ⌘ --> system settings --> windows management
  :path:   task switcher
  :value0: main,  
  :value1: › ☑, show selected window
  :value2: › ☑, thumbnail grid
  :update: 2021-12-20

Shortcuts
*********
.. gui:: KWin
  :nav:    ⌘ --> system settings --> shortcuts
  :path:   system services --> kwin
  :value0: make window fullscreen, alt+return
  :update: 2021-12-20

.. gui:: KRunner
  :nav:    ⌘ --> system settings --> shortcuts
  :path:   applications --> krunner
  :value0: krunner,  
  :value1:    › ☐, alt + f2
  :value2:    › ☑, search
  :value3:    › ☑, alt + space
  :update: 2021-12-20

.. gui:: Activity Switching
  :nav:    ⌘ --> system settings --> shortcuts
  :path:   system services --> activity switching
  :value0: activate application launcher widget,  
  :value1: {DELETE}, alt + f1
  :value2:    {ADD}, ⌘ + space
  :update: 2021-12-20

  This will enable meta only key and meta+space key for app launcher.

Search
******
.. gui:: File Search
  :nav:    ⌘ --> system settings --> search
  :path:   file search
  :value0: ☐, enable file search
  :update: 2021-12-20

.. gui:: KRunner
  :nav:    ⌘ --> system settings --> search
  :path:   krunner
  :value0: ☐, bookmarks
  :value1: ☐, browser history
  :value2: ☐, browser tabs
  :value3: ☐, kate sessions
  :value4: ☐, konsole proflies
  :value5: ☐, web search keywords
  :update: 2021-12-20

  Krunner must be enabled for start searches

.. gui:: Web Search Keywods
  :nav:    ⌘ --> system settings --> search
  :path:   web search keywords
  :value0: ☐, enable web search keywords
  :update: 2021-12-20

.. _manajaro-kde-ui-settings-personalization:

Personalization
***************
.. gui:: Notifications
  :nav:    ⌘ --> system settings --> personalization
  :path:   notifications
  :value0:        do not disturb mode, ☐ enable when screens are minimized
  :value1:     critical notifications, ☑ show in do not disturb mode
  :value2:       normal notifications, ☐ show over full screen windows
  :value3: low priority notifications, ☑ show popup
  :value4:                      popup, ☑ show near notification icon
  :value5:                 hide after, 5secs
  :value6:       application progress,  
  :value7:                        › ☐, show in task manager  (enable if GUI copy progress not showing)
  :value8:                        › ☐, show in notifications (enable if GUI copy progress not showing)
  :value9:                        › ☑, keep popup open during progress
  :value10:      notifications badges, ☑ show in task manager
  :update: 2021-12-20

.. gui:: Accessibility
  :nav:    ⌘ --> system settings --> personalization
  :path:   accessibility
  :value0:             bell,  
  :value1:              › ☐, audible bell
  :value2:              › ☐, visible bell
  :value3:    modifier keys,  
  :value4:              › ☐, sticky keys
  :value5: keyboard filters,  
  :value6:              › ☐, slow keys
  :value7:    screen reader,  
  :value8:              › ☐, enable screen reader
  :update: 2021-12-20

.. gui:: Default Applications
  :nav:    ⌘ --> system settings --> personalization
  :path:   applications --> default applications
  :value0:      email client, google chrome
  :value1: terminal emulator, alacritty
  :update: 2021-12-20

KDE Wallet
**********
.. gui:: Wallet Preferences
  :nav:    ⌘ --> system settings --> kde wallet
  :path:   wallet preferences
  :value0: ☐, enable the kde wallet subsystem
  :update: 2021-12-20

.. gui:: Access Control
  :nav:    ⌘ --> system settings --> kde wallet
  :path:   access control
  :value0: ☑, prompt when an application accesses a wallet
  :update: 2021-12-20

User Feedback
*************
.. gui:: User Feedback
  :nav:    ⌘ --> system settings
  :path:   user feedback
  :value0: {DISABLE},  
  :update: 2021-12-20

Input Devices
*************
.. gui:: Touchpad
  :nav:     ⌘ --> system settings --> hardware --> input devices
  :path:    touchpad
  :value0:                     ☑, device enabled
  :value1:                     ☑, disable when typing
  :value2:                     ☐, left handed mode
  :value3:                     ☐, press left and right buttons for middle click
  :value4:                  0.00, pointer accleration
  :value5:  acceleration profile, ☑ adaptive
  :value6:                     ☑, tap to click
  :value7:                     ☑, tap and drag
  :value8:                     ☐, tap and drag lock
  :value9:      two finger click, ☑ right click (three-finger tap to middle click)
  :value10:            scrolling, ☑ two fingers
  :value11:                    ☐, invert scroll direction
  :value12:                    ☐, disable horizontal scrolling
  :value13:          right-click, ☑ press bottom-right corner
  :value14:         middle-click, ☑ press bottom-middle
  :update: 2021-12-20

Night Color
***********
.. gui:: Night Color
  :nav:    ⌘ --> system settings --> hardware --> display and monitor
  :path:   night color
  :value0: ☐, activate night color
  :update: 2021-12-20

Taskbar Clock
*************
.. gui:: Night Color
  :nav:    taskbar clock --> {RMB} --> configure digital clock
  :path:   appearance
  :value0:                    ☐, activate night color
  :value1:          information, ☑ show date (adaptive location)
  :value2:       show time zone, ☑ only when different from local time zone
  :value3: display time zone as, code
  :value4:         time display, 24-hour
  :value5:          date format, iso date
  :update: 2021-12-20

System Tray
***********
.. gui:: General
  :nav:    system tray --> {RMB} --> configure system tray
  :path:   general
  :value0: ☑, scale with panel height
  :update: 2021-12-20

.. gui:: Entries
  :nav:     system tray --> {RMB} --> configure system tray
  :path:    entries
  :value0:                        ☑, always show all entries
  :value1:       application status,  
  :value2:                › default, always shown
  :value3:           › media player, show when relevant
  :value4:          › notifications, show when relevant (required for GUI file copy progress)
  :value5:         hardware control,  
  :value6:                › default, show when relevant
  :value7:  › display configuration, {DISABLED}
  :value8:               › touchpad, {DISABLED}
  :value9:        › key lock status, {DISABLED}
  :value10:       › keyboard layout, {DISABLED}
  :value11:           › kde connect, {DISABLED}
  :value12:         system services,  
  :value13:             › clipboard, {DISABLED}
  :value14:            › disk quota, {DISABLED}
  :value15:   › night color control, {DISABLED}
  :value16: c         miscellaneous,  
  :value17:          › kate session, {DISABLED}
  :value18:        › weather report, {DISABLED}
  :update: 2021-12-20

  File copy progress also requires notifications settings to be enabled. See
  :ref:`manajaro-kde-ui-settings-personalization`.

.. gui:: Remove Show Desktop
  :nav:    system tray --> {RMB}
  :path:   enter edit mode
  :value0: {DELETE}, show desktop
  :update: 2021-12-20

.. gui:: Remove News
  :nav:    system tray --> news
  :path:   settings
  :value0: ☐, autostart
  :value1: ☐, show error notifications
  :update: 2021-12-20

  Manually quit News.

.. gui:: Remove Show Desktop
  :nav:    system tray --> manjaro settings manager
  :path:   options
  :value0: ☐, check unsupported kernels
  :value1: ☐, check new kernels
  :value2: ☐, check missing language packs
  :update: 2021-12-20

  Manually quit Manajero Settings Manager.

.. gui:: Remove Key Lock Status
  :nav:    system tray
  :path:   key lock status
  :value0: {DELETE}
  :update: 2021-12-20

.. gui:: Remove Shortcuts
  :nav:    system tray
  :path:   shortcuts
  :value0: {DELETE}
  :update: 2021-12-20

Rename Terminals
****************
.. gui:: Make Alacritty Default 'Terminal'
  :nav:    ⌘ --> alacritty
  :path:   edit
  :value0:     general,  
  :value1:        name, terminal
  :value2: application,  
  :value3:        name, terminal
  :value4: description, terminal
  :update: 2021-12-20

.. gui:: Rename Konsole to 'konsole' (from terminal)
  :nav:    ⌘ --> konsole
  :path:   edit
  :value0: application,  
  :value4: description, konsole
  :update: 2021-12-20
