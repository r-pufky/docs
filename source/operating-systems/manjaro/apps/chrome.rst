.. _manjaro-kde-plasma-apps-chrome:

Chrome
######
Chromium sync/login not will bo enabled after march 15th due to API going
private. Run from AUR source. Recommended to use automated GUI or CLI methods
as OS update check will detect new versions.

GUI
***
:cmdmenu:`⌘ --> add/remove software --> search --> AUR --> google-chrome`

Automated Build
***************
Only required if the GUI is not used.

.. code-block:: bash
  :caption: Install build dependencies and Chrome via AUR

  pacman -S --needed base-devel git
  pamac search Google Chrome
  pamac build google-chrome

.. note::
  If prompted use default(**all**) package installs for devel.

Manual git Build
****************
Build from AUR source manually. Not required.

.. code-block:: bash
  :caption: Install with manual build from AUR

  git clone https://aur.archlinux.org/google-chrome.git
  cd google-chrome
  makepkg -si

This must be updated manually.

.. code-block:: bash

  git pull
  makepkg -si

Disable Background services
***************************
Chrome background services will cause "failed to restore properly" messages on
startup.

:cmdmenu:`chrome://settings/system`

* ☐ continue running background apps when google chrome is closed

Use System GTK Themes
*********************
Apply the current system GTK theme set in UI and Themes. Requires restart.

:cmdmenu:`chrome://settings/appearance`

* theme: GTK+
* ☐ use system title bar and borders
