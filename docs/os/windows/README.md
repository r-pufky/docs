# Windows

!!! warning "Registry & GPO Tweaks Removed"
    [See 2022-10.19.0](https://github.com/r-pufky/docs/tree/2022-10-19.0) for
    Registry and GPO settings before they were removed.

!!! success "WinUtil"
    Goto utility for [non-AD](../../glossary/os.md#ad) Windows machines. All
    major standard tweaks may be done with this utility.

    ``` powershell
    # Run as administrator.
    irm "https://christitus.com/win" | iex
    ```

    https://github.com/ChrisTitusTech/winutil

## Setting Execution Policy
Powershell scripts require unrestricted execution policy to be set to execute.
By default this is **disabled** and is the **correct choice**. Once you've
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

Reference:

* https://blog.netspi.com/15-ways-to-bypass-the-powershell-execution-policy/
* https://stackoverflow.com/questions/4037939/powershell-says-execution-of-scripts-is-disabled-on-this-system

## ISO Downloads
Microsoft provides ISO images of Windows for users to install, which require a
separate activation key.

* [Windows 11](https://www.microsoft.com/en-us/software-download/windows11)
* [Windows 10](https://www.microsoft.com/en-us/software-download/windows10)

Execute the downloaded binary:

1. Create installation media for a different PC.
2. Select correct options (typically, english, Pro / Multi, 64-bit).
3. Select save location for the ISO file.

!!! tip "Try Linux"
    Modern linux distributions have greatly increased useability and game
    support in recent years. Instead of dealing with the Ad and privacy
    nightmare that is [non-AD](../../glossary/os.md#ad) connected Windows
    machines, any modern distribution will meet your needs.

    Recommend [Manjaro (Arch stable)](https://manjaro.org) or [Mint (Debian
    testing)](https://https://linuxmint.com).

### Create UEFI USB Boot Disk
Using the Windows Media Creation Tool will create a USB boot disk, however
this will be using MBR. This specific setup will create a UEFI USB boot disk:

1. [Download and run Ventoy](https://www.ventoy.net).
2. Copy [ISO](#iso-downloads) downloaded to root of USB disk.
3. Reboot and select ISO to boot into.

## Install
Use [USB Boot Disk](#create-uefi-usb-boot-disk).

### Local Account Install
Connected Microsoft accounts associate [TPM
keys](https://www.youtube.com/watch?v=t1eX_vvAlUc), [Bitlocker
keys](https://account.microsoft.com/devices/recoverykey), MS account, as well
as user data together leading to a privacy nightmare. Additionally MS has
recently pushed for [automatically uploading user data via
OneDrive](https://learn.microsoft.com/en-us/answers/questions/4166769/how-to-stop-one-drive-from-auto-uploading)
without asking and setting [default locations for Word documents to MS
servers](https://learn.microsoft.com/en-us/answers/questions/5300029/stop-office-365-on-desktop-defaulting-to-one-drive).

!!! warning
    Always install using a local account. If you want an MS account associated
    later you can always make that link yourself.

[Windows 11](https://www.tomshardware.com/how-to/install-windows-11-without-microsoft-account) (1)
{ .annotate }

1. Windows versions <26120 use the **OOBE/BYPASSNRO** local account bypass. See
   link.

Continue through install until **Sign in** appears.

1. **Shift+F10** will open a terminal.
2. **start ms-cxh:local**
3. Create local user with opened dialog window.

!!! danger "Use 11 or Linux"
    Windows 10 is being [actively exploited](https://www.darkreading.com/vulnerabilities-threats/microsoft-october-patch-update)
    with 0-days post update support drop. Do **not** use unless isolated.

[Windows 10 Home](https://www.pcmag.com/how-to/how-to-set-up-microsoft-windows-with-local-account#)

1. Unplug and disable **all** network connections.
2. Continue through install until **Let's connect you to a network**.
3. Select **I don't have internet**.
4. Select **Continue with limited setup**.

[Windows 10 Pro](https://www.pcmag.com/how-to/how-to-set-up-microsoft-windows-with-local-account#)

1. Continue through install until **How would you like to set up?**.
2. Select **Set up for personal use**.
3. Select **Offline account**.
4. Create a **local account**.


TODO

 https://ss64.com/nt/run.html
 .. _Process Explorer: https://docs.microsoft.com/en-us/sysinternals/downloads/process-explorer