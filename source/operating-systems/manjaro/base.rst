.. _manajaro-kde-plasma-base:

Manjaro KDE Plasma
##################
Use the standard KDE release: https://manjaro.org/downloads/official/kde/

Disable Secure boot.

Base Utilities
**************

.. code-block:: bash

  pacman -Syu vim alacritty

.. gui:: Enable fractional scaling for UI
  :nav:  ⌘ --> system settings
  :path: display and monitor --> display configuration
  :value0: global scale, 150%
  :value1: ☑, for any display arrangement

  Use for high DPI displays per preference.

Capslock as Control
*******************
Change capslock to left control.

.. code-block:: bash

  sudo localectl set-x11-keymap us pc105 ,query ctrl:nocaps

.. code-block:: bash
  :caption: **0644 root root** ``/etc/default/keyboard``

  XKBOPTIONS="ctrl:nocaps"

Reboot to apply.

Use Bash Shell
**************
Default shell is zsh. Update user accounts as needed.

.. code-block:: bash
  :caption: **0644 root root** ``/etc/passwd``

  {user}:...:/bin/bash

GnuPG and Yubikey
*****************
Setup using :ref:`gpg-manjaro` and relaunch shell.

Remove Nobody User
******************
:cmdmenu:`⌘ --> manjaro settings manager --> user accounts`

* remove user nobody
