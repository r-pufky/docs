.. _manjaro-kde-plasma-apps-vscodium:

VSCodium (VSCode)
#################
VSCodium is VSCode without telemetry; gnome-keyring is needed to store github
clearsync credentials. If prompted for keyring password use login password.
https://github.com/microsoft/vscode/issues/104319

.. code-block:: bash

  pacman -Syu go gnome-keyring

.. gui:: Enable AUR Repository
  :nav:    ⌘ --> add/remove software
  :path:   ... --> preferences --> third party
  :value0: ☑, enable AUR support
  :value1: ☑, check for updates
  :value2: ☑, check for development packages updates
  :update: 2021-12-15
  :open:

:cmdmenu:`start --> add/remove software --> search --> AUR`

* vscodium-bin
* vscodium-bin-features
* vscodium-bin-marketplace

Sync Settings
*************
VSCodium settings are sync'ed via the ``settings sync`` extension and pulled
from a private github gist.

A personal access token is required: https://github.com/settings/tokens with
``user:email`` permissions.

#. Install ``settings sync`` in extensions
#. Add github settings gist
#. :cmdmenu:`turn on sync settings`

  * Select all settings
  * Use github personal access token

#. :cmdmenu:`shift+alt+d` will install all extensions and settings
