# Troubleshooting


## GIT Push immediate fails for GPG SSH Connections
GPG agent must be defined in **SSH_AUTH_SOCK** for keys to be detected on push.

!!! danger "GIT push fail, GPG key not authorized"

``` bash
# Launch from a terminal with keys already setup.
ssh-add -L
code  # vscodium, vscode
```

## [Repository does not automatically open all submodules][a]
Default submodule load limit is low.

!!! danger ""
    repository has XX submodules which won't be opened automatically. You can still open each one individually by opening a file within.

!!! example "ctrl + , ➔ User ➔ Extensions ➔ Git"
    * Detect Submodules: ✔
    * Detect Submodules Limit: **50**
    * Repository Scan Max Dept: **-1**


## [Unlock Login Keyring Always Prompted][b]
KDE Wallet is used to securely store GitHub credentials.

May be prompted on every open if KDE Wallet is not enabled.

!!! example "⌘ ➔ System Settings ➔ Security & Privacy ➔ KDE Wallet"
    * Enable the KDE Wallet Subsystem: ✔
    * Use KDE Wallet for the Secret Service interface: ✔

[a]: https://stackoverflow.com/questions/60917209/disable-vs-code-warning-submodules-which-wont-be-opened-automatically/61178091
[b]: https://github.com/microsoft/vscode/issues/104319
