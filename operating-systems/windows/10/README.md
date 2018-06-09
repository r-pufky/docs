Windows Setup
-------------
Standard Windows setup used for gaming. Removes known tracking.

Windows 10 pro

Execution Policy: **Unrestricted** (See: [Setting Execution Policy](#setting-execution-policy))

Assumes Admin Rights

1. [Setting Execution Policy](#setting-execution-policy)
2. [Creating a UEFI USB Boot disk](#creating-a-uefi-usb-boot-disk)
3. [Installing Windows 10 Without Live Account](#installing-windows-10-without-live-account)
4. [Securing Windows Installation](#securing-windows-installation)
5. [Removing pre-installed Windows packages](#removing-pre-installed-windows-packages)


[PC Hardware Troubleshooting](../troubleshooting-pc-hardware.md)

[Addition Windows 10 Issue Fixes](windows-issues.md)


[Setting Execution Policy][3]
-----------------------------
Powershell scripts require unrestricted execution policy to be set to
execute. By default this is **disabled** and is the **correct choice**.
Once you've executed scripts, you **must** manually reset this to restricted
or you leave yourself open to bad things. This persists across sessions.

### Check and set unrestricted policy (powershell as admin)
```powershell
get-executionpolicy
set-executionpolicy unrestricted
Y
```

### Set restricted policy (powershell as admin)
```powershell
set-executionpolicy restricted
Y
```


Creating a UEFI USB Boot Disk
-----------------------------
Using the [windows Media Creation Tool][4] will create a USB boot disk, however
this will be using MBR. This specific setup will create a UEFI USB boot disk.
* Download full windows 10 ISO image with [Windows Media Creation Tool][4]
  * Create installation media for a different PC
  * Select correct options (typically, english, windows 10 pro, 64-bit)
  * Select save location for the ISO file
* Create bootable media with [Rufus][5]
  * GPT partition scheme for UEFI
  * NTFS
  * Other options are OK for defaults
  * Once image is applied, dump decompressed Windows 10 drivers to USB drive
    as well

Installing Windows 10 Without Live Account
------------------------------------------
* Delete all existing partitions
* Skip / check later all attempts to enter product key
* Select **use a personal account** (non-organizational)
* Create a **local account** (lower left on the create account screen)
  * Create new account
  * Sign-in *without* a microsoft account

Securing Windows Installation
-----------------------------
A reboot is required once these changes are made. If you are a home user, see 
links for registry edits instead of using group policy.

### Disable Services
These services either do user data tracking, or are a major performance hit for
SSD's. Disable by ```right-click > stop``` and ```right-click > properties > disable```

```win + r > services.msc```
* [Connected User Experiences and Telemetry][9]
* [Diagnostic Tracking Services][9]
* Razer Game Scanner

### Set reasonable Privacy Settings
```start > settings > privacy```
* Disable [all options on all 13 pages][11]. Re-enable to taste.
* Disable ad-tracking, go here: https://choice.microsoft.com/en-gb/opt-out
* Background Apps: Leave background service enable, but disable all apps. This will prevent
  [searching from the start menu from breaking](#fix-windows-applications-not-appearing-in-start-menu-searches).
* Microphone: Leave enabled, but disable all apps. This will allow mumble to use the microphone. [1803 update breaks microphone][25]

### Disable Wi-Fi Sharing
```start > settings > change network settings > manage wifi settings```
* Uncheck all boxes for sharing

### Remove unused optional Windows features
```start > settings > optional features```
* English (united states) retail demo content (remove)
* Neutral retail demo content (cortana demo) (remove)
* News hub (remove)
* Microsoft Quick Assist (remove)
* Contact Support (remove)

### [Disable Cortana][12]
```start > Cortana & Search Settings```
* Disable all options
* Clear all data

```win + r > gpedit.msc```
> Key: Computer Configuration > Administrative Templates > Windows Components > Search

> **Policy**: Allow Cortana = Disabled

### Disable [OneDrive from storing files][18]
```win + r > gpedit.msc```
> Key: Computer Configuration > Administrative Templates > Windows Components > OneDrive

> **Policy**: Prevent the usage of OneDrive for file storage = Enabled

### Disable OneDrive scheduled update task
This will sometimes randomly re-enable OneDrive when it is updated.

```start > Task Scheduler > Task Scheduler Library```

> Key: OneDrive Standalone Update Task v2 = Disabled

### Disable [suggested apps in Windows][19]
```win + r > gpedit.msc```
> Key: Computer Configuration > Administrative Templates > Windows Components > Cloud Content

> **Policy**: Turn off Microsoft consumer experiences = Enabled

> **Policy**: Do not show Windows tips = Enabled

### Disable paging, restore points, automatic driver updates
```start > view advanced system settings > advanced > performance```
* Disable all paging on all drives

```start > view advanced system settings > system protection```
* Disable protection for all drives

```start > view advanced system settings > hardware > device installation settings```
* No (Disable)

### [Disable automatic resource exhaustion resolution][13]
By default, windows will automatically force close applications when memory starts to
fill up. Prevent Windows from being dumb.

```win + r > gpedit.msc```
> Key: Computer Configuration > Administrative Templates > System > Troubleshooting and Diagnostics > Windows Resource Exhaustion Detection and Resolution

> **Policy**: Configure Scenario Execution Level = Disabled

### [Disable Windows Defender Service][14]
Don't turn this off unless you know what you are doing. You should first disable all of the options for windows defender before
disabling the service, as cloud-based protection will cause 100% disk usage (in settings).

```win + r > gpedit.msc```
> Key: Computer Configuration > Administrative Templates > Windows Components > Windows Defender Antivirus

> **Policy**: Turn off Windows Defender = Enabled

> Key: Computer Configuration > Administrative Templates > Windows Components > Windows Defender Antivirus > Real-time Protection

> **Policy**: Turn off real-time protection = Enabled

> Key: Computer Configuration > Administrative Templates > Windows Components > Windows Defender Antivirus > Client Interface

> **Policy**: Suppress all notifications = Enabled

> Key: Computer Configuration > Administrative Templates > Windows Components > Windows Defender Antivirus > Reporting

> **Policy**: Turn off enhanced notifications = Enabled

```win + r > taskmgr > More details > Startup```

* [Windows Defender notification icon][20] = Disabled

### [Disable silent windows store app installs][6] (regedit as admin)
> Key: HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager

> **DWORD**: SilentInstalledAppsEnabled = 0

> Key: HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager\SuggestedApps\*

> **DWORD**: (all suggested apps) = 0

### [Disable Windows Store App Installs][21]

```start > Store```
> Click User Icon (or ... if signed in) > Settings

> Update apps automatically = Disabled

> Show products on tile = Disabled



### [Remove OneDrive from Windows Explorer][7] (regedit as admin)
> Key: HKEY_CLASSES_ROOT\\CLSID\\{018D5C66-4533-4307-9B53-224DE2ED1FE6}

> **DWORD**: System.IsPinnedToNameSpaceTree = 0

### [Disable quick access pane in Windows Explorer][8] (regedit as admin)
* Set [explorer to use **this pc**][10] instead of quick access, or this will break
* ```Explorer > file > folder options > Open File Explorer To = This PC```

> Key: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer

> New **DWORD**: HubMode = 1

### [Remove services from being listed in Task Manager][15] (regedit as admin)
> Key: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run

> Key: HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run
* Delete values after disabling

### [Remove win+g key prompt when starting game][16] (regedit as admin)
This happens because of the xbox app on Windows 10. Removing the app will fix this.
(see [Removing pre-installed Windows Packages](#removing-pre-installed-windows-packages))
> Key: HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\GameDVR

> **DWORD**: AppCaptureEnabled = 0


> Key: HKEY_CURRENT_USER\System\GameConfigStore

> **DWORD**: GameDVR_Enabled = 0

### Disable Microsoft Game Broadcasting Suite
Nearly every program on windows now wants to record your games and broadcast them. This disables the built-in
windows game broadcasting and recording software.

```win + r > gpedit.msc```
> Key: Computer Configuration > Administrative Templates > Windows Components > Windows Game Recording and Broadcasting

> **Policy**: Enables or disables Windows Game Recording and Broadcasting = Disabled

### [Disable Ads in Windows Explorer from Sync Providers][17] (windows explorer)
Sync providers for windows explorer can now show Ads. Disable it.

```win + e > view > options > view```
* Uncheck show sync provider notifications

### [Enable patching for meltdown and spectre][22]
Windows 10 will not automatically patch for meltdown and spectre due to anti-virus software
causing BSOD's. If you are running anti-virus software ensure you are not affected by
checking [this list][23] then adding the [following key](scripts/enable-meltdown-spectre-update.reg)
to the registry:

> Key: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\QualityCompat

> **DWORD**: cadca5fe-87d3-4b96-b7fb-a231484277cc = 0

Force check for new updates and ensure it's applied using [InSpectre][24]


Reboot machine to apply policy

Removing pre-installed [Windows packages][1]
--------------------------------------------
Certain packages (and windows store applications) cannot be removed with
[programs & applications][2]. This removes those applications using Windows
built-in package manager.
* _Remove-AppxProvisionedPackage_ will remove packages for newly provisioned
  accounts
* _Remove-AppxPackage_ removes for the current user
* _Get-AppxPackage -AllUsers_ will return results for all users on system

### Remove packages with [remove-crapware.ps1](scripts/remove-crapware.ps1) (powershell as admin)
```powershell
remove-crapware.ps1
```

Manually removing applications may be faster, since these applications are updated with each
major update to windows 10.

```start > Add or remove programs > Apps & features```


[1]: https://thomas.vanhoutte.be/miniblog/delete-windows-10-apps/
[2]: http://www.makeuseof.com/tag/3-clever-powershell-functions-upgrading-windows-10/
[3]: http://stackoverflow.com/questions/4037939/powershell-says-execution-of-scripts-is-disabled-on-this-system
[4]: http://windows.microsoft.com/en-us/windows-10/media-creation-tool-install
[5]: https://rufus.akeo.ie/
[6]: https://youtu.be/wgKJMsJ-6XU?t=4m47s
[7]: https://www.tekrevue.com/tip/remove-onedrive-file-explorer-sidebar-windows-10/
[8]: http://www.winhelponline.com/blog/remove-quick-access-other-shell-folders-file-explorer/#quickaccess_v1607
[9]: http://www.forbes.com/sites/gordonkelly/2015/11/24/windows-10-automatic-spying-begins-again/#5f0b888d2d97
[10]: https://www.maketecheasier.com/remove-quick-access-file-explorer/
[11]: http://bgr.com/2015/07/31/windows-10-upgrade-spying-how-to-opt-out/
[12]: http://www.howtogeek.com/265027/how-to-disable-cortana-in-windows-10/
[13]: https://www.autoitscript.com/forum/topic/177749-stopping-windows-10-from-auto-closing-programs-to-free-up-ram/
[14]: https://www.tenforums.com/tutorials/5918-windows-defender-turn-off-windows-10-a.html
[15]: https://www.tenforums.com/tutorials/2944-startup-items-add-delete-enable-disable-windows-10-a.html
[16]: https://www.tenforums.com/tutorials/8637-game-bar-turn-off-windows-10-a.html
[17]: https://www.extremetech.com/computing/245553-microsoft-now-puts-ads-windows-file-explorer
[18]: https://support.office.com/en-us/article/Turn-off-or-uninstall-OneDrive-f32a17ce-3336-40fe-9c38-6efb09f944b0
[19]: https://www.howtogeek.com/259946/how-to-get-rid-of-suggested-apps-in-windows-10/
[20]: https://www.howtogeek.com/264796/how-to-remove-the-windows-defender-icon-from-your-notification-area/
[21]: https://www.easeus.com/computer-instruction/stop-windows-10-installing-apps.html
[22]: https://support.microsoft.com/en-us/help/4056892/windows-10-update-kb4056892
[23]: https://docs.google.com/spreadsheets/d/184wcDt9I9TUNFFbsAVLpzAtckQxYiuirADzf3cL42FQ/htmlview?usp=sharing&sle=true
[24]: https://www.grc.com/inspectre.htm
[25]: https://www.ghacks.net/2018/05/01/all-the-issues-of-windows-10-version-1803-you-may-run-into/