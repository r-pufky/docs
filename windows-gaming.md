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
5. [Moving User Profile Locations to Alternate Location](#moving-user-profile-locations-to-alternate-location)
6. [Removing pre-installed Windows packages](#removing-pre-installed-windows-packages)
7. [Format ReFS on using a single drive](#format-refs-on-using-a-single-drive)
8. [Addressing 100% disk usage issues](#addressing-100-disk-usage-issues)
9. [Hiding local desktop for Chrome Remote Desktop](#hiding-local-desktop-for-chrome-remote-desktop)
10. [Fixing non-working Windows store apps / 'trial expired' apps](#fixing-non-working-windows-store-apps-trial-expired-apps)
11. [Enable Bitlocker on USB drives over RDP](#enable-bitlocker-on-usb-drives-over-rdp)
11. [Fix Windows Applications not appearing in start menu searches](#fix-windows-applications-not-appearing-in-start-menu-searches)

Creating a UEFI USB Boot Disk
-----------------------------
Using the [windows Media Creation Tool][10] will create a USB boot disk, however
this will be using MBR. This specific setup will create a UEFI USB boot disk.
* Download full windows 10 ISO image with [Windows Media Creation Tool][10]
  * Create installation media for a different PC
  * Select correct options (typically, english, windows 10 pro, 64-bit)
  * Select save location for the ISO file
* Create bootable media with [Rufus][11]
  * GPT partition scheme for UEFI
  * NTFS
  * Other options are OK for defaults
  * Once image is applied, dump decompressed Windows 10 drivers to USB drive
    as well

Installing Windows 10 Without Live Account
------------------------------------------
* Delete all existing partitions
* Skip / check later all attempts to enter product key
* Create a **local account** (on sign in with microsoft account)
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
* [Connected User Experiences and Telemetry][16]
* [Diagnostic Tracking Services][16]
* Razer Game Scanner

### Set reasonable Privacy Settings
```start > settings > privacy```
* Disable [all options on all 13 pages][20]. Re-enable to taste.
* Disable ad-tracking, go here: https://choice.microsoft.com/en-gb/opt-out

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

### [Disable Cortana][21]
```start > Cortana & Search Settings```
* Disable all options
* Clear all data

```win + r > gpedit.msc```
> Key: Computer Configuration > Administrative Templates > Windows Components > Search

> **Policy**: Allow Cortana = Disabled

### Disable [OneDrive from storing files][30]
```win + r > gpedit.msc```
> Key: Computer Configuration > Administrative Templates > Windows Components > OneDrive

> **Policy**: Prevent the usage of OneDrive for file storage = Enabled

### Disable OneDrive scheduled update task
This will sometimes randomly re-enable OneDrive when it is updated.

```start > Task Scheduler > Task Scheduler Library```

> Key: OneDrive Standalone Update Task v2 = Disabled

### Disable [suggested apps in Windows][31]
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

### [Disable automatic resource exhaustion resolution][22]
By default, windows will automatically force close applications when memory starts to
fill up. Prevent Windows from being dumb.

```win + r > gpedit.msc```
> Key: Computer Configuration > Administrative Templates > System > Troubleshooting and Diagnostics > Windows Resource Exhaustion Detection and Resolution

> **Policy**: Configure Scenario Execution Level = Disabled

### [Disable Windows Defender Service][24]
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

* [Windows Defender notification icon][35] = Disabled

### [Disable silent windows store app installs][12] (regedit as admin)
> Key: HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager

> **DWORD**: SilentInstalledAppsEnabled = 0

> Key: HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager\SuggestedApps\*

> **DWORD**: (all suggested apps) = 0

### [Remove OneDrive from Windows Explorer][13] (regedit as admin)
> Key: HKEY_CLASSES_ROOT\\CLSID\\{018D5C66-4533-4307-9B53-224DE2ED1FE6}

> **DWORD**: System.IsPinnedToNameSpaceTree = 0

### [Disable quick access pane in Windows Explorer][14] (regedit as admin)
* Set [explorer to use **this pc**][17] instead of quick access, or this will break
* ```Explorer > file > folder options > Open File Explorer To = This PC```

> Key: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer

> New **DWORD**: HubMode = 1

### [Remove services from being listed in Task Manager][27] (regedit as admin)
> Key: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run

> Key: HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run
* Delete values after disabling

### [Remove win+g key prompt when starting game][28] (regedit as admin)
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

### [Disable Ads in Windows Explorer from Sync Providers][29] (windows explorer)
Sync providers for windows explorer can now show Ads. Disable it.

```win + e > view > options > view```
* Uncheck show sync provider notifications

### [Disable hibernation for Windows 10 sleep resume problems][34] (cmd as admin)
If your system doesn't seem to be resuming from sleep properly (e.g. power is on, but keyboard/mouse won't resume it), disable hibernation. This does affect power consumption and probably shouldn't be used on laptops.

```cmd
powercfg /h off
```

Reboot machine to apply policy

### Cleanup default profiles, set as non-admin user
* Create a new account, set to admin
* Remove admin access from your primary account

[Setting Execution Policy][8]
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


Moving User Profile Locations to Alternate Location
---------------------------------------------------
Relocate certain portions of your user profile to alternate location, to make reinstallation easier, as
well as keep music and media folders on separate drives.

```
win + e > Select location > Right Click > Properties > Location Tab > Move ...
```
* Select new (or existing) location to relocate
* Move existing files into the new location
* Apply


Removing pre-installed [Windows packages][6]
--------------------------------------------
Certain packages (and windows store applications) cannot be removed with
[programs & applications][7]. This removes those applications using Windows
built-in package manager.
* _Remove-AppxProvisionedPackage_ will remove packages for newly provisioned
  accounts
* _Remove-AppxPackage_ removes for the current user
* _Get-AppxPackage -AllUsers_ will return results for all users on system

### Remove packages with [remove-crapware.ps1](windows-scripts/remove-crapware.ps1) (powershell as admin)
```powershell
remove-crapware.ps1
```

Format ReFS on using a [single drive][1]
----------------------------------------
ReFS allows for integrated file checksums, duplication and error recovery,
however by default it requires two disks. This will allow you to use this
filesystem on a single disk.

### Edit Windows Registry (regedit as admin)
> Key: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control

> New **Key**: MiniNT

> New **DWORD**: AllowRefsFormatOverNonmirrorVolume = 1

* Reboot

### Setup disk for ReFS (powershell as admin)
```powershell
diskpart
list disk
select disk [#]
clean
create partition primary
format fs=refs quick
```

### Mount disk and format with integrity enabled
```win + x > computer management > disk utilities```
* Mount ReFS partition to a drive letter
* Reformat drive with [integrity enabled][2]

```powershell
format X: /fs:refs /i:enabled /q
```

### Verifiy ReFS with Integrity is working (powershell as admin)
* Write a temporary file the drive and use this to lookup on the filesystem.

```powershell
Get-Item X:\<file> | Get-FileIntegrity
```
* Enabled and Enforced should be set to True


Addressing 100% Disk Usage Issues
---------------------------------
Generally speaking, 100% disk usage issues usually means there's a Filesystem check happening, or another service
is hammering the disk. These will address this but may break functionality of your system.

### Disable Services
Disable by ```right-click > stop``` and ```right-click > properties > disable```

```win + r > services.msc```
* [Windows Search][15]
* [Superfetch][15] ([causes 100% CPU usage][25], [system & compressed memory service][26])

### [Disable prefetch and superfetch][32] (regedit as admin)
This addresses 100% disk usage during idle in windows 10, even if you've already disabled the superfetching service.
> Key: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management\PrefetchParameters

> **DWORD**: EnablePrefetcher = 0

> New **DWORD**: EnableSuperfetcher = 0

### [Disable ReFS scheduled tasks][33]
By default ReFS will schedule integrity checks (as well as automatic integrity checks after windows crashes),
which cause 100% disk usage on system PID 4. Disabling these prevents these from automatically being scheduled
but you can still manually run them.

```start > Task Scheduler > Task Scheduler Library > Microsoft > Windows > Data Integrity Scan```

> Key: Data Integrity Scan = Disabled

> Key: Data Integrity Scan for Crash Recovery = Disabled


[Hiding local desktop for Chrome Remote Desktop][36]
----------------------------------------------------
By default Chrome Remote Desktop will always show locally what is happening when you remotely connect. This
disables this feature and presents a login screen instead, allowing you to work privately remotely. CRD will
open a connection, then locally connect to remote desktop to hide your current session.

### Edit Windows Registry (regedit as admin)
> Key: HKEY_LOCAL_MACHINE\Software\Policies\Google\Chrome\RemoteAccessHostRequireCurtain

> New **DWORD**: RemoteAccessHostRequireCurtain = 1

> Key: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp

> **DWORD**: SecurityLayer = 1

```start > Control Panel > System and Security > System > Remote Settings > Remote```
* Check 'Allow remote connections to this computer'
* Uncheck 'Allow connections only from computers runing Remote Desktop with Network Level Authentication'

### [Block inbound RDP connections with Windows Firewall][37]
```start > Control Panel > System and Security > Windows Firewall > Advanced settings > Inbound Rules```

**Rule**: Remote Desktop - Shadow (TCP-in) = Block

**Rule**: Remote Desktop - User Mode (TCP-in) = Block

**Rule**: Remote Desktop - User Mode (UDP-in) = Block

[Fixing non-working Windows store apps / 'trial expired' apps][38]
------------------------------------------------------------------
Default windows 10 applications may stop working if you remove dependent apps from the system; as such, apps
like xbox controller config will never load, or calculator will prompt you with trial expired. This resets your
system to the default app installation state for windows 10.

### Powershell (as admin)
```powershell
Get-AppXPackage -AllUsers | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}
```


[Enable Bitlocker on USB drives over RDP][39]
---------------------------------------------
By default, bitlocker does not allow encryption to be enabled on USB devices over RDP connections -- this happens
because RDP treats USB drives as mapped network drives and not external drives. This enables direct drive access
for RDP connections. This is probably unsafe.

```win + r > gpedit.msc```
> Key: Computer Configuration > Administrative Templates > System > Removable Storage Access

> **Policy**: All Removable Storage: Allow direct access in remote sessions = Enabled


[Fix Windows Applications not appearing in start menu searches][40]
-------------------------------------------------------------------
Background Tasks need to be enabled for the application index to be updated when new programs are installed. By
disabling all background tasks (global toggle) this index is never updated, and therefore apps will stop appearing
in start menu searches. You can still disable all apps in the background, however the service still needs to be
enabled.

```start > Settings > Background Apps```

> Key: Let apps run in the background = Enabled


[1]: http://winaero.com/blog/how-to-format-any-drive-in-windows-8-1-with-refs/
[2]: http://blog.architecting.it/2012/07/10/windows-server-2012-windows-server-8-resilient-file-system/w8-refs-2/
[3]: https://github.com/r-pufky/docs/blob/master/force-upgrade-to-10.cmd
[6]: https://thomas.vanhoutte.be/miniblog/delete-windows-10-apps/
[7]: http://www.makeuseof.com/tag/3-clever-powershell-functions-upgrading-windows-10/
[8]: http://stackoverflow.com/questions/4037939/powershell-says-execution-of-scripts-is-disabled-on-this-system
[10]: http://windows.microsoft.com/en-us/windows-10/media-creation-tool-install
[11]: https://rufus.akeo.ie/
[12]: https://youtu.be/wgKJMsJ-6XU?t=4m47s
[13]: https://www.tekrevue.com/tip/remove-onedrive-file-explorer-sidebar-windows-10/
[14]: http://www.winhelponline.com/blog/remove-quick-access-other-shell-folders-file-explorer/#quickaccess_v1607
[15]: http://superuser.com/questions/1016152/100-ssd-activity-0-r-w-speed-system-hang-issue
[16]: http://www.forbes.com/sites/gordonkelly/2015/11/24/windows-10-automatic-spying-begins-again/#5f0b888d2d97
[17]: https://www.maketecheasier.com/remove-quick-access-file-explorer/
[20]: http://bgr.com/2015/07/31/windows-10-upgrade-spying-how-to-opt-out/
[21]: http://www.howtogeek.com/265027/how-to-disable-cortana-in-windows-10/
[22]: https://www.autoitscript.com/forum/topic/177749-stopping-windows-10-from-auto-closing-programs-to-free-up-ram/
[23]: http://www.outsidethebox.ms/why-windows-8-defragments-your-ssd-and-how-you-can-avoid-this/#_Toc352763197
[24]: https://www.tenforums.com/tutorials/5918-windows-defender-turn-off-windows-10-a.html
[25]: https://answers.microsoft.com/en-us/windows/forum/windows_10-performance/system-and-compressed-memory-service-high-cpu/421c32bd-e65b-4339-9473-db775e50096a?page=21
[26]: https://usefulpcguide.com/18428/system-and-compressed-memory-high-cpu/
[27]: https://www.tenforums.com/tutorials/2944-startup-items-add-delete-enable-disable-windows-10-a.html
[28]: https://www.tenforums.com/tutorials/8637-game-bar-turn-off-windows-10-a.html
[29]: https://www.extremetech.com/computing/245553-microsoft-now-puts-ads-windows-file-explorer
[30]: https://support.office.com/en-us/article/Turn-off-or-uninstall-OneDrive-f32a17ce-3336-40fe-9c38-6efb09f944b0
[31]: https://www.howtogeek.com/259946/how-to-get-rid-of-suggested-apps-in-windows-10/
[32]: http://www.thewindowsclub.com/disable-superfetch-prefetch-ssd
[33]: http://bakins-bits.com/wordpress/?p=195
[34]: https://www.tenforums.com/general-support/5265-turn-off-wake-up-problems.html
[35]: https://www.howtogeek.com/264796/how-to-remove-the-windows-defender-icon-from-your-notification-area/
[36]: https://support.google.com/chrome/a/answer/2799701?hl=en&vid=0-243350879834-1495198101821
[37]: https://superuser.com/questions/723832/windows-firewall-blocks-remote-desktop-with-custom-port
[38]: https://community.spiceworks.com/how_to/122006-windows-10-your-trial-period-for-this-app-has-expired-visit-the-windows-store-to-purchase-the-full-app-problem
[39]: https://superuser.com/questions/962125/bitlocker-refuses-to-enable-via-rdp-on-data-drive-but-ok-on-the-os-drive
[40]: https://superuser.com/questions/947392/windows-10-search-cant-find-any-applications-even-calculator
