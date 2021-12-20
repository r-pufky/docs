.. _manajaro-kde-mirrors-and-updates:

Use Latest Mirrors & Updates
############################
Set update preferences; use whatever country is closest to you. Be sure to
refresh country list first.

.. gui:: General
  :nav:    ⌘ --> add/remove software
  :path:   ⋮ --> preferences --> general
  :value0:                      ☑, check for updates
  :value1: update check frequency, every day
  :value2:                      ☑, automatically download updates
  :value3:                      ☑, hide tray icon when no updates
  :value4:       use mirrors from, United_States
  :update: 2021-12-15
  :open:

.. gui:: Advanced
  :nav:    ⌘ --> add/remove software
  :path:   ⋮ --> preferences --> advanced
  :value0: ☑, check available disk space
  :value1: ☑, remove unrequried dependencies
  :update: 2021-12-15
  :open:

.. gui:: Third Party
  :nav:    ⌘ --> add/remove software
  :path:   ⋮ --> preferences --> third party
  :value0: ☑, enable AUR support
  :value1: ☑, keep built packages
  :value2: ☑, check for updates
  :value3: ☑, check for development package updates
  :update: 2021-12-15
  :open:

.. code-block:: bash
  :caption: Set fastest mirrors for package installations

  sudo pacman-mirrors --fasttrack && sudo pacman -Syyu
