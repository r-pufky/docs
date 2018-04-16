Windows Issues
--------------
All changes listed below are for very specific use cases, and should not be applied by default or
without thought. These can seriously break your shit if you blindly execute these.

My default recommendation here is not apply these.

Addresses common issues encountered with Windows 10.

Windows 10 pro

Execution Policy: **Unrestricted** (See: [Setting Execution Policy](windows-gaming.md#setting-execution-policy))

1. [Moving User Profile Locations to Alternate Location](#moving-user-profile-locations-to-alternate-location)
2. [Format ReFS on using a single drive](#format-refs-on-using-a-single-drive)
3. [Addressing 100% disk usage issues](#addressing-100-disk-usage-issues)
4. [Hiding local desktop for Chrome Remote Desktop](#hiding-local-desktop-for-chrome-remote-desktop)
5. [Fixing non-working Windows store apps / 'trial expired' apps](#fixing-non-working-windows-store-apps-trial-expired-apps)
6. [Enable Bitlocker on USB drives over RDP](#enable-bitlocker-on-usb-drives-over-rdp)
7. [Fix Windows Applications not appearing in start menu searches](#fix-windows-applications-not-appearing-in-start-menu-searches)
8. [Disable hibernation for Windows 10 sleep resume problems](#disable-hibernation-for-windows-10-sleep-resume-problems)
9. [Enabling SSH Access](#enabling-ssh-access)
10. [NTFS File Ownership Access Denied](#ntfs-file-ownership-access-denied)


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
* Reformat drive with [integrity enabled][1]

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

### [Disable prefetch and superfetch][2] (regedit as admin)
This addresses 100% disk usage during idle in windows 10, even if you've already disabled the superfetching service.
> Key: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management\PrefetchParameters

> **DWORD**: EnablePrefetcher = 0

> New **DWORD**: EnableSuperfetcher = 0

### [Disable ReFS scheduled tasks][3]
By default ReFS will schedule integrity checks (as well as automatic integrity checks after windows crashes),
which cause 100% disk usage on system PID 4. Disabling these prevents these from automatically being scheduled
but you can still manually run them.

```start > Task Scheduler > Task Scheduler Library > Microsoft > Windows > Data Integrity Scan```

> Key: Data Integrity Scan = Disabled

> Key: Data Integrity Scan for Crash Recovery = Disabled


[Hiding local desktop for Chrome Remote Desktop][5]
----------------------------------------------------
By default Chrome Remote Desktop will always show locally what is happening when you remotely connect. This
disables this feature and presents a login screen instead, allowing you to work privately remotely. CRD will
open a connection, then locally connect to remote desktop to hide your current session.

### Installing CRD (Chrome Remote Desktop)
* Sign in to Chrome
* Disable all sync'ing with account (if wanted)
* Install the [Chrome Remote Desktop Extension][13]
* Launch the installer

```share (green button) > accept and install > Run MSI installer```

* On Authorize screen click ```continue```

```CRD > My Computers > Enable remote connections```
* Create a PIN for connection
* Uncheck Improve CRD

### Edit Windows Registry (regedit as admin)
> Key: HKEY_LOCAL_MACHINE\Software\Policies\Google\Chrome

> New **DWORD**: RemoteAccessHostRequireCurtain = 1

> Key: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp

> **DWORD**: SecurityLayer = 1

```start > Control Panel > System and Security > System > Remote Settings > Remote```
* Check 'Allow remote connections to this computer'
* Uncheck 'Allow connections only from computers runing Remote Desktop with Network Level Authentication'

### [Block inbound RDP connections with Windows Firewall][6]
```start > Control Panel > System and Security > Windows Firewall > Advanced settings > Inbound Rules```

**Rule**: Remote Desktop - Shadow (TCP-in) = Block

**Rule**: Remote Desktop - User Mode (TCP-in) = Block

**Rule**: Remote Desktop - User Mode (UDP-in) = Block


[Fixing non-working Windows store apps / 'trial expired' apps][7]
------------------------------------------------------------------
Default windows 10 applications may stop working if you remove dependent apps from the system; as such, apps
like xbox controller config will never load, or calculator will prompt you with trial expired. This resets your
system to the default app installation state for windows 10.

### Powershell (as admin)
```powershell
Get-AppXPackage -AllUsers | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}
```


[Enable Bitlocker on USB drives over RDP][8]
---------------------------------------------
By default, bitlocker does not allow encryption to be enabled on USB devices over RDP connections -- this happens
because RDP treats USB drives as mapped network drives and not external drives. This enables direct drive access
for RDP connections. This is probably unsafe.

```win + r > gpedit.msc```
> Key: Computer Configuration > Administrative Templates > System > Removable Storage Access

> **Policy**: All Removable Storage: Allow direct access in remote sessions = Enabled


[Fix Windows Applications not appearing in start menu searches][9]
-------------------------------------------------------------------
Background Tasks need to be enabled for the application index to be updated when new programs are installed. By
disabling all background tasks (global toggle) this index is never updated, and therefore apps will stop appearing
in start menu searches. You can still disable all apps in the background, however the service still needs to be
enabled.

```start > Settings > Background Apps```

> Key: Let apps run in the background = Enabled


[Disable hibernation for Windows 10 sleep resume problems][4] (cmd as admin)
-----------------------------------------------------------------------------
If your system doesn't seem to be resuming from sleep properly (e.g. power is on, but keyboard/mouse won't resume it), disable hibernation. This does affect power consumption and probably shouldn't be used on laptops.

```cmd
powercfg /h off
```

[Enabling SSH Access][10]
-------------------------
Windows 10 has a beta which allows for SSHd and SSH-agent use to access the windows system. This covers the manual
installation process, there is also a beta you may install via optional features.

* [Download][11] and extract the latest binaries to ```c:\Program Files\```
* Install the SSHd service, generate host keys, lock down files and allow inbound SSH connections

### Powershell (as admin)
```powershell
cd c:\Program Files\OpenSSH
powershell.exe -ExecutionPolicy Bypass -File install-sshd.ps1
./ssh-keygen.exe -A
powershell.exe -ExecutionPolicy Bypass -File ./FixHostFilePermissions.ps1
New-NetFirewallRule -Protocol TCP -LocalPort 22 -Direction Inbound -Action Allow -DisplayName SSH
```

### Enable SSHD Service and set for Automatic Startup
```win + r > services.msc```
* SSHD

### Setting up publickey authentication

* Create ```c:\Users\<username>\.ssh```
* Grant SSHD service read permissions

```powershell
icacls C:\users\<username>\.ssh /grant "NT Service\sshd:R" /T
```

NTFS File Ownership Access Denied[14]
-------------------------------------
When reinstalling windows, or moving a drive to another system, sometimes the NTFS file system will deny access to files you own. This is generally because the default [well-known SID's][15] were removed from the file permissions, and replaced with a specific user SID that no longer exists. You can fix this by replacing the old SID with the new SID:

```powershell
setacl.exe -on C:\ 
           -ot file 
           -actn trustee -trst "n1:S-old-501;n2:S-new-501;ta:repltrst" 
           -rec cont
```

Additionally, the drive should really be nuked and re-formatted [using well-known SID's][15] which will remove this issue.

[1]: http://blog.architecting.it/2012/07/10/windows-server-2012-windows-server-8-resilient-file-system/w8-refs-2/
[2]: http://www.thewindowsclub.com/disable-superfetch-prefetch-ssd
[3]: http://bakins-bits.com/wordpress/?p=195
[4]: https://www.tenforums.com/general-support/5265-turn-off-wake-up-problems.html
[5]: https://support.google.com/chrome/a/answer/2799701?hl=en&vid=0-243350879834-1495198101821
[6]: https://superuser.com/questions/723832/windows-firewall-blocks-remote-desktop-with-custom-port
[7]: https://community.spiceworks.com/how_to/122006-windows-10-your-trial-period-for-this-app-has-expired-visit-the-windows-store-to-purchase-the-full-app-problem
[8]: https://superuser.com/questions/962125/bitlocker-refuses-to-enable-via-rdp-on-data-drive-but-ok-on-the-os-drive
[9]: https://superuser.com/questions/947392/windows-10-search-cant-find-any-applications-even-calculator
[10]: https://winscp.net/eng/docs/guide_windows_openssh_server
[11]: https://github.com/PowerShell/Win32-OpenSSH/releases
[12]: https://support.microsoft.com/en-us/help/4056892/windows-10-update-kb4056892
[13]: https://chrome.google.com/webstore/detail/chrome-remote-desktop/gbchcmhmhahfdphkhkmpfmihenigjmpp
[14]: https://superuser.com/questions/439675/how-to-bind-old-users-sid-to-new-user-to-remain-ntfs-file-ownership-and-permiss
[15]: http://support.microsoft.com/kb/243330