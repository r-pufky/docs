.. _manjaro-kde-apps-vscodium:

VSCodium (VSCode)
#################
VSCodium is VSCode without telemetry; gnome-keyring is needed to store github
clearsync credentials. If prompted for keyring password use login password.
https://github.com/microsoft/vscode/issues/104319

.. code-block:: bash

  pacman -Syu go gnome-keyring

.. gui:: Enable AUR Repository
  :nav:    ⌘ --> add/remove software
  :path:   ⋮ --> preferences --> third party
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

Be sure to disable private syncing of local cached copies:

#. Open ``~/.config/VSCodium/User/syncLocalSettings.json``
#. Add/Update ``ignoreUploadFolders``:

    .. code-block:: json

      "ignoreUploadFolders": [
        "workspaceStorage",
        "History",
        "globalStorage",
        "node_modules"
      ],

#. Force update settings gist: :cmdmenu:`shift+alt+u`
#. Verify extra files are **not** listed on the code tab of the gist. If so,
   check out the gist, remove from revision history, and force upload the gist
   again.

`Reference <https://github.com/shanalikhan/code-settings-sync/issues/1341sync>`__
`Reference <https://github.com/shanalikhan/code-settings-sync/pull/1357/files>`__

Terminal Profiles
*****************
Set default shell and profile preferences.

#. :cmdmenu:`ctrl+,`
#. View JSON listing (upper right, ``~/.config/VSCodium/User/settings.json``)
#. Set default shell profiles for each OS:

    .. code-block:: json

      "terminal.integrated.defaultProfile.linux": "bash",
      "terminal.integrated.defaultProfile.osx": "bash",
      "terminal.integrated.defaultProfile.windows": "powershell",

#. Set profile customization:

    .. code-block:: json

      "terminal.integrated.profiles.linux": {
        "bash": {
          "path": "bash",
          "args": ["-l"],
          "icon": "terminal-bash"
        },
        "tmux": {
          "path": "tmux",
          "icon": "terminal-tmux"
        },
      },
      "terminal.integrated.profiles.osx": {
        "bash": {
          "path": "bash",
          "args": ["-l"],
          "icon": "terminal-bash"
        },
        "tmux": {
          "path": "tmux",
          "icon": "terminal-tmux"
        },
      },
      "terminal.integrated.profiles.windows": {
        "PowerShell": {
          "source": "PowerShell",
          "icon": "terminal-powershell"
        },
        "Command Prompt": {
          "path": [
            "${env:windir}\\Sysnative\\cmd.exe",
            "${env:windir}\\System32\\cmd.exe"
          ],
          "args": [],
          "icon": "terminal-cmd"
        },
        "Git Bash": {
          "source": "Git Bash"
        }
      },

#. Restart machine for changes to apply.

`Reference <https://stackoverflow.com/questions/51820921/vscode-integrated-terminal-doesnt-load-bashrc-or-bash-profile>`__