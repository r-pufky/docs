.. _manjaro-pacman:

Pacman
######
Package Management utility for arch distros.

`Reference <https://wiki.archlinux.org/title/pacman>`__

.. code-block:: bash

  sudo pacman -Syu {PACKAGE}        # update database (and install package if specified, preferred)
  sudo pacman -Syyu                 # Force update data even if already 'up to date'
  sudo pacman -Syuu                 # enable downgrades
  sudo pacman -Ss {SEARCH}          # search for a package
  sudo pacman -Si {PACKAGE}         # show informatio on package
  sudo pacman -S {PACKAGE} ... {PACKAGE} # install packages
  sudo pacman -R {PACKAGE}         # remove package only
  sudo pacman -Rs {PACKAGE}        # remove package and all dependencies not used by other packages
  sudo pacman -Rns {PACKAGE}       # remove package and all dependencies not used by other packages, do not save config files
  sudo pacman -Qdtq                # remove packages with no dependencies (leftover from other packages)
  sudo pacman -Qi {PACKAGE}        # show information for install package
  sudo pacman -Ql                  # list all currently installed packages
