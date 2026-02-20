# VSCodium (VSCode / Code)
VSCodium / Code is VSCode without telemetry.

=== "CachyOS"
    ``` bash
    pacman -S code  # Optimized VScodium (preferred).
    paru -S code-marketplace  # Auto patch MS Marketplace.
    pacman -S vscodium  # or use the git source release.
    ```

=== "Manjaro"
    !!! example "⌘ ➔ Add/Remove Software ➔ Search ➔ AUR"
        * vscodium-bin
        * vscodium-bin-marketplace
        * vscodium-features

=== "Windows"
    ``` powershell
    winget install vscodium
    ```

## Locations
Existing configurations can be dropped into respective location to transfer
settings.

=== "Code"
      Option                | Location
     ----------------------:|----------
                   Settings | **~/.vscode-oss**
                     Config | **~/.config/Code - OSS**
                      State | **~/.local/state/Code - OSS**
      product.json (system) | **/usr/lib/code/product.json**
        product.json (user) | **~/.config/Code - OSS/product.json**

    !!! warning "MS Marketplace configuration required"
        Code uses opensource marketplace which will result in existing
        extensions not detected on launch. [Switching to MS Marketplace][f]
        resolves issue (or installing the opensource equivalent).

    !!! abstract "/.config/Code - OSS/product.json"
        ``` json
        {
          "extensionsGallery": {
            "serviceUrl": "https://marketplace.visualstudio.com/_apis/public/gallery",
            "itemUrl": "https://marketplace.visualstudio.com/items",
            "cacheUrl": "https://vscode.blob.core.windows.net/gallery/index",
            "controlUrl": ""
          }
        }
        ```

=== "VSCodium"
      Option                | Location
     ----------------------:|----------
                   Settings | **~/.vscode-oss**
                     Config | **~/.config/VSCodium**
                      State | **~/.local/state/VSCodium**
      product.json (system) | **/usr/share/vscodium/resources/app/product.json**
        product.json (user) | **~/.config/VSCodium/product.json**


## Window Style
!!! example "ctrl + , ➔ Window"
    * Title bar style: **native**
    * Dialog style: **native**


## Disable Copilot

!!! example "ctrl + , ➔ Features ➔ Chat ➔ Command Center: ✘"

!!! example "ctrl + , ➔ Features ➔ Chat ➔ Disable AI Features: ✔"


## Allow No Verify Commits
!!! example "ctrl + , ➔ User ➔ Extensions ➔ Git ➔ Allow No Verify Commit: ✔"


## [Enable Commit Signing][a]
!!! example "ctrl + , ➔ User ➔ Extensions ➔ Git ➔ Enable Commit Signing: ✔"


## Use [VSCodium as Commit Editor][b]

!!! example "ctrl + , ➔ User ➔ Extensions ➔ Git"
    * Terminal Authentication: ✔
    * Use Editor As Commit Input: ✔


## Use [Terminal for Github Authentication][c]

!!! example "ctrl + , ➔ User ➔ Extensions ➔ Git ➔ Terminal Authentication: ✔"

!!! example "ctrl + , ➔ User ➔ Extensions ➔ GitHub ➔ Git Authentication: ✔"


## [Exclude Files in File Explorer][d]
!!! example "ctrl + , ➔ User ➔ Explorer ➔ Auto Reveal Exclude"
    Add files with globbing to ignore.


## [Terminal Profiles][e]
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

[a]: https://dev.to/devmount/signed-git-commits-in-vs-code-36do
[b]: https://code.visualstudio.com/docs/sourcecontrol/overview#:~:text=To%20cancel%20the%20commit%20operation,toggling%20the%20git.useEditorAsCommitInput%20setting.
[c]: https://stackoverflow.com/questions/62772525/vscode-how-to-ask-for-password-in-terminal-instead-of-pop-up-tab
[d]: https://stackoverflow.com/questions/30140112/how-to-hide-specified-files-directories-e-g-git-in-the-sidebar-vscode
[e]: https://stackoverflow.com/questions/51820921/vscode-integrated-terminal-doesnt-load-bashrc-or-bash-profile
[f]: https://gist.github.com/anxkhn/9ae7b2248999168b73f303dec5851460
