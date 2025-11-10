# VSCodium (VSCode)
VSCodium is VSCode without telemetry; gnome-keyring is needed to store github
clearsync credentials. If prompted for keyring password use login password.
https://github.com/microsoft/vscode/issues/104319

### Terminal Profiles
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

## Manjaro

!!! example "⌘ ➔ Add/Remove Software ➔ Search ➔ AUR ➔ vscodium-bin"

Install all packages.

Reference:

* https://stackoverflow.com/questions/51820921/vscode-integrated-terminal-doesnt-load-bashrc-or-bash-profile
