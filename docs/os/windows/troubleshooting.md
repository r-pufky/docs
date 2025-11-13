# Troubleshooting


## Applications Not Appearing in Start Menu Searches
Background Tasks need to be enabled for the application index to be updated when
new programs are installed.

!!! example "⌘ + r ➔ ms-settings:privacy-backgroundapps"
    Let apps run in the background: ✔

By [disabling all background tasks (global toggle)][a] this index is never
updated, and therefore apps will stop appearing in start menu searches. You can
still disable all apps in the background, however the service still needs to be
enabled.


## [NTFS File Ownership Access Denied][b]
[Default well known SIDs][c] were removed from file permissions and replaced
with a specific user SID that no longer exists.

Replace old SID with current system SID. (1)
{ .annotate }

1. Alternatively take ownership and copy files to a NTFS partition with proper
   SID's set.

``` powershell
# Run as administrator.
setacl.exe -on c:\ -ot file -actn trustee -trst "n1:S-old-501;n2:S-new-501;ta:repltrst" -rec cont
```

Affected NTFS partition should be nuked and re-formatted.


## Undeletable System Volumes
System Volume information copied from another system which no longer exists.

Take ownership and grant full privileges for everyone to remove the directory.
``` powershell
# Run as administrator.
takeown /f ".\System Volume Information" /a /r /d y
icacls ".\System Volume Information" /t /c /grant administrators:F System:F everyone:F
rd ".\System Volume Information"
```

## Application or game refuses to start [(Hyper-V Virtualization detected)][d]
Some applications and games detect Hyper-V virtualization and refuse to start.

Disable Hyper-V on Windows boot instead of through the BIOS. This removes the
hypervisor kernel modules which prevents this from happening without needing to
turn it off.
``` powershell
# run as administrator.
bcdedit --% /copy {current} /d "No Hyper-V"

bcdedit --%  /set {GUID} hypervisorlaunchtype off
```

Restart holding **shift** to show boot options. Select **No Hyper-V**.


## Locked out after [Update (Password Reset)][g]
Updates may cause users to be locked out after rebooting.

No Alternative Account.

1. Download [Hiren BootCD ISO][e].
2. Create [Bootable USB Disk][f].

    !!! example "Utilities ➔ Security ➔ Passwords ➔ Lazesoft Password Security"

    !!! note
        Accounts may only be reset and unlocked (no password); passwords cannot be
        set in this tool without a license. Resetting the account will also clear
        saved tokens, such as chrome auto login.

Alternative Account [(no admin required).][h]

1. Reboot and hold **shift** until the troubleshooting options appear.

    !!! example "Login Screen ➔ shift (hold) + Restart"

    !!! example "Troubleshoot ➔ Advanced options ➔ Startup Settings ➔ Restart ➔ Enable Safe Mode with Command Prompt"

2. Find the correct user and set password.

    ``` powershell
    net user
    net user {USER} {PASS}
    ```


## [UTC Realtime Clock][i]
Only required if dual booting requires Windows 10.

Set BIOS clock to UTC and update windows to interpret the Realtime Clock (RTC)
using the UTC timezone. Disable NTP updates and let **other** operation system
handle clock updates.

!!! example "Set RTC to UTC"
    `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\TimeZoneInformation`

    Key: **RealTimeIsUniversal**

    Type: **DWORD**

    Value: **1**

!!! example "Disable NTP sync"
    `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\W32Time\TimeProviders\NtpClient`

    Key: **Enabled**

    Type: **DWORD**

    Value: **0**


## Realtek A-Volute (Nahimic)
Realtek has added A-Volute(Nahimic) services to the install package. These
generally automatically take over speaker and microphone settings to improve
'quality'. They are also added automatically via Microsoft auto updates based
on hardware detection, as well as through Dolby Atmos installation.

Disabling does **not** affect either realtek or dolby installs.

Nahimic behaves very much like a virus, automatically reinstalling itself and
running two processes to ensure it is always loaded; providing no value to the
end user.

### [Disabling][j]
If the realtek device is not being used, **disable it** in the BIOS. This will
prevent Microsoft from re-installing the software every time windows update
runs.

Disable Nahimic Virtual Devices
!!! example "⌘ + x ➔ Device Manager ➔ Software components ➔ A-Volute Nh3 Audio Effects Component ➔ Disable"
!!! example "⌘ + x ➔ Device Manager ➔ Sound, video and game controllers"
    * Nahimic Mirroring Device: ✘
    * Sonic Studio Virtual Mixer: ✘

Disable [Nahimic Services][k]
!!! example "⌘ ➔ services.msc ➔ Nahimic service ➔ General ➔ Disabled"
    Stop service.

Prevent [Nahimic Executables from Starting][l]
!!! example "User Configuration ➔ Administrative Templates ➔ System ➔ Don't run specified Windows applications"
    * Enabled: ✔
    * List of disallowed applications
        * c:\Windows\System32\NahimicService.exe
        * c:\Windows\System32\NahimicSvc64.exe
        * c:\Windows\SysWOW64\NahimicSvc32.exe
        * c:\Windows\System32\NhNotifSys.exe
        * c:\Users\{USER}\AppData\Local\NhNotifSys\NhNotifSys.exe
        * c:\Users\{USER}\AppData\Local\NhNotifSys\sonicstudio\NhNotifSys.exe

Disable Nahimic Scheduled Tasks (tasks may not exist)
!!! example "⌘ ➔ Task Scheduler ➔ Task Scheduler Library"
    * NahimicSvc32Run: ✘
    * NahimicSvc64Run: ✘
    * NahimicTask32: ✘
    * NahimicTask64: ✘

Delete files that have been placed in
**C:\Users\{USER}\AppData\Local\NhNotifSys**.


## EA Updater (or other apps) showing in search results

!!! example "⌘ + i ➔ Privacy & Security ➔ Searching Windows"
    * Classic: ✔
    * Exclude **all** drives


## [Disable USB Selective Suspend][m]
Prevents external drives from being disconnected while in use.

!!! example "⌘ + x ➔ Device Manager ➔ Universal Serial Bus controllers"
    * Right click on each USB Root Hub:
        * Power Management:
            * Allow the computer to turn off this device to save power: ✘

!!! example "⌘ + i ➔ System ➔ Power & Battery"
    Verify current power plan isn't set to aggressively manage USB power.


## [Prevent Disk Check on Every Boot][n]
Dual booting systems encounter this.

!!! example "Disable hybrid boot"
    `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Power`

    Key: **HiberbootEnabled**

    Type: **DWORD**

    Value: **0**


## [Astro A40's Not Consistently Working][o]
Windows 11 requires DAC to be directly connected to a motherboard USB port and
not a hub.

[a]: https://superuser.com/questions/947392/windows-10-search-cant-find-any-applications-even-calculator
[b]: https://superuser.com/questions/439675/how-to-bind-old-users-sid-to-new-user-to-remain-ntfs-file-ownership-and-permiss
[c]: https://docs.microsoft.com/en-us/troubleshoot/windows-server/identity/security-identifiers-in-windows
[d]: https://www.hanselman.com/blog/switch-easily-between-virtualbox-and-hyperv-with-a-bcdedit-boot-entry-in-windows-81
[e]: https://www.hirensbootcd.org/download
[f]: README.md#create-uefi-usb-boot-disk
[g]: https://www.passfab.com/windows-tips/windows-10-password-incorrect-after-update.html
[h]: https://www.wimware.com/how-to/reset-windows-10-password-command-prompt.html
[i]: https://forum.manjaro.org/t/root-tip-get-your-time-timezone-right-using-manjaro-windows-dual-boot/1167
[j]: https://old.reddit.com/r/MSI_Gaming/comments/ilys2o/nahimic_is_literal_malware_no_matter_how_you/
[k]: https://old.reddit.com/r/Amd/comments/koh9ca/turning_offdisabling_my_rgb_g_skill_trident_z_neo/
[l]: https://appuals.com/how-to-remove-windows-defender-icon-on-windows-10/
[m]: https://forum.sienci.com/t/usb-selective-suspend-in-windows-11/10345
[n]: https://www.prime-expert.com/articles/b26/stop-disk-check-from-running-on-every-boot
[o]: https://old.reddit.com/r/AstroGaming/comments/1h9t8mp/windows_11_a40s_combined_output_channel_audio_fix/