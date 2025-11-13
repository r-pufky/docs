# Windows

!!! warning "Registry & GPO Tweaks Removed"
    [See 2022-10.19.0][a] for Registry and GPO settings before they were
    removed.

!!! success "[WinUtil][c]"
    Goto utility for [non-AD][b] Windows machines. All major standard tweaks
    may be done with this utility.

    ``` powershell
    # Run as administrator.
    irm "https://christitus.com/win" | iex
    ```

!!! tip
    See [run commands for launching all settings windows from run command][t].


## [Setting Execution Policy][d]
Powershell scripts require unrestricted execution policy to be set to execute.
By default this is [**disabled**][e] and is the **correct choice**. Once you've
executed scripts, you **must** manually reset this to restricted or you leave
yourself open to bad things. This persists across sessions.

Check and set unrestricted policy.
``` powershell
# Run as administrator.
Get-ExecutionPolicy
Set-ExecutionPolicy -ExecutionPolicy unrestricted -Force
```

Set restricted policy.
``` powershell
# Run as administrator.
Set-ExecutionPolicy -ExecutionPolicy restricted -force
```

### Set Execution Policy Via Script
Commands entered directly into powershell are executed. Scripts may be run
without setting execution policy by launching a sub-shell with ExecutionPolicy
bypassed.

Execute script without setting ExecutionPolicy.
``` powershell
PowerShell.exe -ExecutionPolicy Bypass -File {SCRIPT}.ps1
```


## ISO Downloads
Microsoft provides ISO images of Windows for users to install, which require a
separate activation key.

* [Windows 11][f].
* [Windows 10][g].

Execute the downloaded binary:

1. Create installation media for a different PC.
2. Select correct options (typically, english, Pro / Multi, 64-bit).
3. Select save location for the ISO file.

!!! tip "Try Linux"
    Modern linux distributions have greatly increased useability and game
    support in recent years. Instead of dealing with the Ad and privacy
    nightmare that is [non-AD][h] connected Windows machines, any modern
    distribution will meet your needs.

    Recommend [Manjaro (Arch stable)][i] or [Mint (Debian testing)][j].

### Create UEFI USB Boot Disk
Using the Windows Media Creation Tool will create a USB boot disk, however
this will be using MBR. This specific setup will create a UEFI USB boot disk:

1. [Download and run Ventoy][k].
2. Copy [ISO](#iso-downloads) downloaded to root of USB disk.
3. Reboot and select ISO to boot into.

## Install
Use [USB Boot Disk][l].

### Local Account Install
Connected Microsoft accounts associate [TPM keys][m], [Bitlocker keys][n],
MS account, as well as user data together leading to a privacy nightmare.
Additionally MS has recently pushed for
[automatically uploading user data via OneDrive][o] without asking and setting
[default locations for Word documents to MS servers][p].

!!! warning
    Always install using a local account. If you want an MS account associated
    later you can always make that link yourself.

[Windows 11][q] (1)
{ .annotate }

1. Windows versions <26120 use **OOBE/BYPASSNRO** [local account bypass][q].

Continue through install until **Sign in** appears.

1. **Shift+F10** will open a terminal.
2. **start ms-cxh:local**
3. Create local user with opened dialog window.

!!! danger "Use 11 or Linux"
    Windows 10 is being [actively exploited][r] with 0-days post update support
    drop. Do **not** use unless isolated.

[Windows 10 Home][s]

1. Unplug and disable **all** network connections.
2. Continue through install until **Let's connect you to a network**.
3. Select **I don't have internet**.
4. Select **Continue with limited setup**.

[Windows 10 Pro][s]

1. Continue through install until **How would you like to set up?**.
2. Select **Set up for personal use**.
3. Select **Offline account**.
4. Create a **local account**.

!!! tip
    Install [Process Explorer][u] and [Secure Delete][v] for detailed process
    tracking, debugging, and secure delete.

[a]: https://github.com/r-pufky/docs/tree/2022-10-19.0
[b]: ../../glossary/os.md#ad
[c]: https://github.com/ChrisTitusTech/winutil
[d]: https://blog.netspi.com/15-ways-to-bypass-the-powershell-execution-policy/
[e]: https://stackoverflow.com/questions/4037939/powershell-says-execution-of-scripts-is-disabled-on-this-system
[f]: https://www.microsoft.com/en-us/software-download/windows11
[g]: https://www.microsoft.com/en-us/software-download/windows10
[h]: ../../glossary/os.md#ad
[i]: https://manjaro.org
[j]: https://https://linuxmint.com
[k]: https://www.ventoy.net
[l]: #create-uefi-usb-boot-disk
[m]: https://www.youtube.com/watch?v=t1eX_vvAlUc
[n]: https://account.microsoft.com/devices/recoverykey
[o]: https://learn.microsoft.com/en-us/answers/questions/4166769/how-to-stop-one-drive-from-auto-uploading
[p]: https://learn.microsoft.com/en-us/answers/questions/5300029/stop-office-365-on-desktop-defaulting-to-one-drive
[q]: https://www.tomshardware.com/how-to/install-windows-11-without-microsoft-account
[r]: https://www.darkreading.com/vulnerabilities-threats/microsoft-october-patch-update
[s]: https://www.pcmag.com/how-to/how-to-set-up-microsoft-windows-with-local-account
[t]: https://ss64.com/nt/run.html
[u]: https://docs.microsoft.com/en-us/sysinternals/downloads/process-explorer
[v]: https://docs.microsoft.com/en-us/sysinternals/downloads/sdelete
