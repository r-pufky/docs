# VSCodium (VSCode)
VSCodium is VSCode without telemetry; gnome-keyring is needed to store github
clearsync credentials. If prompted for keyring password use login password.
https://github.com/microsoft/vscode/issues/104319

=== "Manjaro"
    !!! example "⌘ ➔ Add/Remove Software ➔ Search ➔ AUR"
        * vscodium-bin
        * vscodium-bin-marketplace
        * vscodium-features

    Settings are located in: **~/.vscode-oss** and **~/.config/VSCodium**.

=== "Windows"
    ``` powershell
    winget install vscodium
    ```

## Window Style
!!! example "ctrl + , ➔ Window"
    * Title bar style: **native**
    * Dialog style: **native**

## Disable Copilot
!!! example "ctrl + , ➔ Features ➔ Chat ➔ Command Center: ✘"

## Allow No Verify Commits
!!! example "ctrl + , ➔ User ➔ Extensions ➔ Git ➔ Allow No Verify Commit: ✔"

## Enable Commit Signing
!!! example "ctrl + , ➔ User ➔ Extensions ➔ Git ➔ Enable Commit Signing: ✔"

Reference:

* https://dev.to/devmount/signed-git-commits-in-vs-code-36do

## Exclude Files in File Explorer
!!! example "ctrl + , ➔ User ➔ Explorer ➔ Auto Reveal Exclude"
    Add files with globbing to ignore.

Reference:

* https://stackoverflow.com/questions/30140112/how-to-hide-specified-files-directories-e-g-git-in-the-sidebar-vscode

## Terminal Profiles
Set default shell and profile preferences.

!!! example "ctrl+, ➔ Open Settings (JSON) (upper right)"

Set default shell profiles for each OS:
``` json
"terminal.integrated.defaultProfile.linux": "bash",
"terminal.integrated.defaultProfile.osx": "bash",
"terminal.integrated.defaultProfile.windows": "powershell",
```

Set profile customization:
``` json
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
```

Restart.

Reference:

* https://stackoverflow.com/questions/51820921/vscode-integrated-terminal-doesnt-load-bashrc-or-bash-profile
