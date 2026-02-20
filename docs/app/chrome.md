# Chrome

See [Auto Select Client Certificate][a] to auto select certificate for matched
sites.

=== "CachyOS"
    Install via AUR helper.

    ``` bash
    paru -S google-chrome
    ```

    !!! example "chrome://settings/appearance"
        * Use system title bar and borders: ✔

=== "Manjaro"
    Install via AUR helper.

    ``` bash
    pamac install google-chrome
    ```

    !!! example "chrome://settings/appearance"
        * Use system title bar and borders: ✔

=== "Windows"
    [Download][f] and install.

    [Disable Software Reporting][b]

    !!! example "Disable Chrome running software reporting tool"
        `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Google\Chrome`

        Key: **ChromeCleanupEnabled**

        Type: **DWORD**

        Values: **0**

    !!! example "Disable reporting results to Google"
        `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Google\Chrome`

        Key: **ChromeCleanupReportingEnabled**

        Type: **DWORD**

        Value: **0**


## Block location tracking

!!! example "chrome://settings/content/location"
    * Ask before accessing (Recommended): **Disabled**

!!! example "chrome://settings/content/notifications"
    * Ask before sending (Recommended): **Disabled**


## Disable Background Services
Chrome background services will cause "failed to restore properly" messages on
startup.

!!! example "chrome://settings/system"
    * Continue running background apps when google chrome is closed: ✘


## Chrome Remote Desktop

[Install CRD][c].

### [Hiding Local Desktop][d] for Chrome Remote Desktop (Windows)
By default Chrome Remote Desktop will always show locally what is happening
when you remotely connect. This disables this feature and presents a login
screen instead, allowing you to work privately remotely. CRD will open a
connection, then locally connect to remote desktop to hide your current
session.

!!! example "Enable remote access curtain for CRD"
    `HKEY_LOCAL_MACHINE\Software\Policies\Google\Chrome`

    Key: **RemoteAccessHostRequireCurtain**

    Type: **DWORD**

    Value: **1**

!!! example "Enable RDP security"
    `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp`

    Key: **SecurityLayer**

    Type: **DWORD**

    Value: **1**

!!! example "⌘ + r ➔ control ➔ System and Security ➔ System ➔ Remote Settings ➔ Remote"
    * Allow remote connections to this computer: ✔
    * Allow connections only from computers running Remote Desktop with
      NetworkLevel Authentication: ✘

!!! example "⌘ ➔ Control Panel ➔ System and Security ➔ [Windows Defender Firewall][e] ➔ Advanced Settings ➔ Inbound Rules"
    * Remote Desktop - Shadow (TCP-in): **Block**
    * Remote Desktop - User Mode (TCP-in): **Block**
    * Remote Desktop - User Mode (UDP-in): **Block**

[a]: ../service/nginx/manual/cert_based_authentication.md#auto-select-client-certificate
[b]: https://www.ghacks.net/2018/01/20/how-to-block-the-chrome-software-reporter-tool-software_reporter_tool-exe
[c]: https://remotedesktop.google.com
[d]: https://support.google.com/chrome/a/answer/2799701?hl=en&vid=0-243350879834-1495198101821
[e]: https://superuser.com/questions/723832/windows-firewall-blocks-remote-desktop-with-custom-port
[f]: https://www.google.com/chrome
