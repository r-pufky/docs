# VSCodium (VSCode)
VSCodium is VSCode without telemetry.

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

## Use VSCodium as Commit Editor

!!! example "ctrl + , ➔ User ➔ Extensions ➔ Git"
    * Terminal Authentication: ✔
    * Use Editor As Commit Input: ✔

Reference:

* https://code.visualstudio.com/docs/sourcecontrol/overview#:~:text=To%20cancel%20the%20commit%20operation,toggling%20the%20git.useEditorAsCommitInput%20setting.


## Use Terminal for Github Authentication

!!! example "ctrl + , ➔ User ➔ Extensions ➔ Git ➔ Terminal Authentication: ✔"

!!! example "ctrl + , ➔ User ➔ Extensions ➔ GitHub ➔ Git Authentication: ✔"

Reference:

* https://stackoverflow.com/questions/62772525/vscode-how-to-ask-for-password-in-terminal-instead-of-pop-up-tab


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

## Suggested Extensions

* Ansible
* Better Align
* Code Runner
* Code Spell Checker
* ES7+ React/Redux/React-Native snippets
* Even Better TOML
* Git Blame
* GitHub Markdown Preview
* Go
* Go Coverage Viewer
* Go Doc
* Go Extension Pack
* Go Test Explorer
* Gremlins tracker for Visual Studio Code
* isort
* jinja
* Markdown Checkboxes
* Markdown Emoji
* Markdown Footnotes
* Markdown Preview Github Styling
* Markdown Preview Mermaid Support
* Markdown Table Formatter
* Markdown yaml Preamble
* NGINX Configuration Language Support
* PascalCase/camelCase to snake_case
* Paste JSON as Code
* Pylance
* Pylint
* Python
* Python Debugger
* Python Environments
* REG
* reStructuredText Syntax Highlighting
* Rewrap
* Scientific Terms - Code Spell Checker
* Sort lines
* Trailing Spaces
* vscode-go-syntax
* vscode-proto3
* YAML
* YAML to JSON
