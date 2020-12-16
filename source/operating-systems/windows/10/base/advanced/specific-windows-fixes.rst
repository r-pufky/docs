.. _w10-specific-windows-fixes:

Specific Windows Fixes
######################
All changes listed below are for very specific use cases, and should not be
applied by default or without thought.

.. danger::
  These can seriously break your shit if you blindly execute these. Default
  recommendation here is **not** apply these.

Execution Policy: **Unrestricted** (see: :ref:`setting-execution-policy`).

Reset Password
**************
Windows 10 has a `habit of locking out after updates`_. `Reset your password
from safe mode`_.

Be sure to hold ``shift`` until the troubleshooting options appear.
:cmdmenu:`Login Screen --> shift (hold) + Restart --> Troubleshoot --> Advanced options --> Startup Settings --> Restart -> Enable Safe Mode with Command Prompt`

.. code-block:: powershell
  :caption: Find the correct user and set password.

  net user
  net user {USER} {PASS}

Moving User Profile Locations to Alternate Location
***************************************************
Relocate certain portions of your user profile to alternate location, to make
reinstallation easier, as well as keep music and media folders on separate
drives.

:cmdmenu:`⌘ + e --> select location --> RMB --> properties --> location tab --> move`

   * Select new (or existing) location to relocate.
   * Move existing files into the new location.
   * Apply.

Format ReFS on using a single driv
***********************************
ReFS allows for integrated file checksums, duplication, and error recovery;
however by default it requires two disks. This will allow you to use this
filesystem on a single disk with `integrity enabled`_ which is not possible by
default.

Recently `ReFS create moved to Windows 10 Workstation`_, effectively removing
the ability to create ReFS containers in Windows 10 Pro, but they can still be
read.

.. wregedit:: REFS single drive regedit
  :key_title: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\MiniNT
  :names:     AllowRefsFormatOverNonmirrorVolume
  :types:     DWORD
  :data:      1
  :admin:
  :no_section:
  :no_caption:

    Reboot to enable changes.

.. code-block:: powershell
  :caption: Setup disk for ReFS (powershell as admin).

  diskpart
  list disk
  select disk [#]
  clean
  create partition primary
  format fs=refs quick

:cmdmenu:`⌘ + x --> computer management --> disk utilities`

   * Mount ReFS partition to a drive letter.
   * Reformat drive with `integrity enabled`_.

.. code-block:: powershell
  :caption: Format Single Drive with Integrity Enabled & Verify with Test File
            (powershell as admin).

  format X: /fs:refs /i:enabled /q
  echo $null >> X:\test
  Get-Item X:\test | Get-FileIntegrity

.. note::
  Both Enabled and Enforced should be set to True.

.. rubric:: Disable ReFS Scheduled Tasks

By default ReFS will schedule integrity checks (as well as automatic integrity
checks after windows crashes), which cause 100% disk usage on system PID 4.
`Disabling ReFS Scheduled Tasks`_ prevents these from automatically being
scheduled, but can still be manually run.

.. wtschedule:: Disable REFS scheduled tasks task
  :key_title:   Microsoft --> Windows --> Data Integrity Scan
  :option:      Data Integrity Scan,
                Data Integrity Scan for Crash Recovery
  :setting:     Disabled,
                Disabled
  :no_section:
  :no_caption:

Addressing 100% Disk Usage Issues
*********************************
Generally speaking, 100% disk usage issues usually means there's a Filesystem
check happening, or another service is hammering the disk. These will address
this but may break functionality of your system.

These services either do user data tracking, or are a major performance hit for
SSD's. Disable by :cmdmenu:`RMB --> stop` and
:cmdmenu:`RMB --> properties --> disable`.

.. wservice:: Disable search service
  :key_title: Windows Search --> General
  :option:    Startup type,
              Service status
  :setting:   Disabled,
              Stopped
  :no_section:

    See `SSD activity issue`_.

.. wservice:: Disable superfetch service
  :key_title: Windows Search --> General
  :option:    Startup type,
              Service status
  :setting:   Disabled,
              Stopped
  :no_section:
  :no_launch:

    See `100% CPU usage issue`_ and `System & Compressed Memory Service issue`_.

`Disable Prefetch and Superfetch`_
**********************************
This addresses 100% disk usage during idle in windows 10, even if you've already
disabled the superfetching service.

.. wregedit:: Disable prefetch and superfetch regedit
  :key_title: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\
              Session Manager\Memory Management\PrefetchParameters
  :names:     EnablePrefetcher,
              EnableSuperfetcher
  :types:     DWORD,
              DWORD
  :data:      0,
              0
  :admin:
  :no_section:
  :no_caption:

.. _w10-hiding-local-desktop-crd:

`Hiding Local Desktop for Chrome Remote Desktop`_
*************************************************
By default Chrome Remote Desktop will always show locally what is happening when
you remotely connect. This disables this feature and presents a login screen
instead, allowing you to work privately remotely. CRD will open a connection,
then locally connect to remote desktop to hide your current session.

Installing CRD (Chrome Remote Desktop):

* Sign in to Chrome.
* Disable all sync'ing with account (if wanted).
* Install the `Remote Desktop Extension`_.
* Launch the installer.

:cmdmenu:`share (green button) --> accept and install --> run msi installer`

* On Authorize screen click :cmdmenu:`continue`

:cmdmenu:`CRD --> my computers --> enable remote connections`

* Create a PIN for connection.
* ☐ Improve CRD.

.. wregedit:: Enable remote access curtain for CRD regedit
  :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Google\Chrome
  :names:     RemoteAccessHostRequireCurtain
  :types:     DWORD
  :data:      1
  :admin:
  :no_section:
  :no_caption:

.. wregedit:: Enable RDP security regedit
  :key_title: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\
              Terminal Server\WinStations\RDP-Tcp
  :names:     SecurityLayer
  :types:     DWORD
  :data:      1
  :admin:
  :no_section:
  :no_caption:
  :no_launch:

:cmdmenu:`⌘ + r --> control --> System and Security --> System --> Remote Settings --> Remote`

* ☑ Allow remote connections to this computer.
* ☐ Allow connections only from computers running Remote Desktop with Network
  Level Authentication.

.. wfirewall:: Block inbound rdp connections firewall
  :key_title: Advanced Settings --> Inbound Rules
  :option:    Remote Desktop - Shadow (TCP-in),
              Remote Desktop - User Mode (TCP-in),
              Remote Desktop - User Mode (UDP-in)
  :setting:   Block,
              Block,
              Block
  :admin:
  :no_section:
  :no_caption:

    `See block inbound RDP connections with Windows Firewall`_.

`Fixing Broken Windows Store apps`_ / 'Trial Expired' Apps
**********************************************************
Default windows 10 applications may stop working if you remove dependent apps
from the system. Symptoms include apps like xbox controller config never
loading, or calculator prompting with trial expired. This resets the system to
the default app installation state for windows 10.

.. code-block:: powershell
  :caption: Reinstall default Windows applications (powershell as admin).

  Get-AppXPackage -AllUsers | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}

`Enable Bitlocker on USB drives over RDP`_
******************************************
By default, bitlocker does not allow encryption to be enabled on USB devices
over RDP connections -- this happens because RDP treats USB drives as mapped
network drives and not external drives. This enables direct drive access for RDP
connections. This is unsafe.

.. wgpolicy:: Enable bitlocker on usb drives over rdp policy
  :key_title: Computer Configuration -->
              Administrative Templates -->
              System -->
              Removable Storage Access
  :option:    All Removable Storage: Allow direct access in remote sessions
  :setting:   Enabled
  :no_section:
  :no_caption:

.. _w10-background-apps:

`Fix Windows Applications Not Appearing in Start Menu Searches`_
****************************************************************
Background Tasks need to be enabled for the application index to be updated when
new programs are installed. By disabling all background tasks (global toggle)
this index is never updated, and therefore apps will stop appearing in start
menu searches. You can still disable all apps in the background, however the
service still needs to be enabled.

:cmdmenu:`⌘ + r --> ms-settings:privacy-backgroundapps`

   * Let apps run in the background: ☑

`Disable Hibernation for Windows 10 Sleep Resume Problems`_
***********************************************************
If your system doesn't seem to be resuming from sleep properly (e.g. power is
on, but keyboard/mouse won't resume it), disable hibernation. This does affect
power consumption and probably shouldn't be used on laptops.

.. code-block:: powershell
  :caption: Disable hibernation (powershell as admin).

  powercfg /h off

Enabling SSH Access
*******************
See :ref:`service-ssh-windows-setup` to enble SSHD on Windows.

`NTFS File Ownership Access Denied`_
************************************
When reinstalling windows, or moving a drive to another system, sometimes the
NTFS file system will deny access to files you own. This is generally because
the default `well known SIDs`_ were removed from the file permissions, and
replaced with a specific user SID that no longer exists (and now can no longer
be removed, prompting this perms error everytime you access it). You can fix
this by replacing the old SID with the new SID:

.. code-block:: powershell
  :caption: Replace old SID with current system SID (powershell as admin).

  setacl.exe -on c:\ -ot file -actn trustee -trst "n1:S-old-501;n2:S-new-501;ta:repltrst" -rec cont

Alternatively take ownership and copy files to a NTFS partition with proper
SID's set.

The affected NTFS partition should really be nuked and re-formatted using
`well known SIDs`_ which will remove this issue.

OEM Partition / `Low Disk Space Warning After 1803 Update`_
***********************************************************
After updating to Windows 10 1803, a consistent low disk space warning appears.
This happens as the upgrade now sets the OEM partition (~450MB) to be mounted on
boot. This drive is `almost entirely full`_ (~400MB) and triggers a low disk
warning.

.. code-block:: powershell
  :caption: Unmount OEM partition from drive (powershell as admin).

  mountvol {OEM PARTITION DRIVE}: /d

.. wregedit:: Disable disk space warning checks for partition regedit
  :key_title: HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\
              Policies\Explorer
  :names:     NoLowDiskSpaceChecks
  :types:     DWORD
  :data:      1
  :admin:
  :no_section:
  :no_caption:

`Application Using the Wrong Audio Output Device`_
**************************************************
Some applications will not respect the default output device in Windows 10 and
output to the wrong device. Output settings can be set for specific applications
via the settings menu.

:cmdmenu:`⌘ + r --> ms-settings:sound --> Advanced sound options --> App volume and device preferences`

   * Set preferred output for device (application must be running).

`Disable Caret Browsing Notifications`_
***************************************
Remove notification on F7 press for caret browsing. This is a holdover from
Internet Explorer.

.. wregedit:: Disable Caret Browsing Notifications via Registry
  :key_title: HKEY_CURRENT_USER\Software\Microsoft\Internet Explorer\CaretBrowsing
  :names:     Enabled
  :types:     DWORD
  :data:      0
  :no_section:

.. wgpolicy:: Disable Caret Browsing Notifications via GPO
  :key_title: User Configuration -->
              Administrative Templates -->
              Windows Components -->
              Internet Explorer -->
              Internet Control Panel -->
              Advanced Page -->
              Turn on Caret Browsing support
  :option:    ☑
  :setting:   Disabled
  :no_section:

Windows Bootloader Missing / Multiple OS
****************************************
Fix the UEFI bootloader if it is missing or has extra entries.

Restart in Diagnostics Mode:

:cmdmenu:`shift + restart --> troubleshooting --> command prompt`

.. note::
  :cmdmenu:`shift` can be held during normal boot to get to the same menu.

First remove any `extra EFI boot configuration data`_ from other operating
systems.

.. code-block::
  :caption: Remove extra EFI entries before rebuilding Boot Configuration Data
            for Windows.
  :emphasize-lines: 3-4, 10

  diskpart
  list disk
  sel disk 0
  sel vol 2
  assign letter=Z:
  exit
  cd Z:
  cd EFI
  dir
  rmdir -S ubuntu

.. note::
  Look for ~100MB FAT32 partition, this is the standard partition Windows uses
  for storing EFI data. Adjust highlighted lines as needed for specific case.
  ``ubuntu`` removed here. ``Boot`` and ``Microsoft`` should be left intact.

.. code-block::
  :caption: Fix MBR, scan for all OS's on drive and rebuild Boot Configuration
            Data for Windows.

  bootrec /fixmbr
  bootrec /scanos
  bootrec /rebuildbcd

Restart machine.

If there are extra menu options, you may also edit UEFI boot options in firmware
or use `EasyUEFI`_ to do it in windows directly.

Display Driver Has Been Restarted
*********************************
Windows Vista+ has a feature called `Timeout Detection and Recovery`_, which
detects if the GPU becomes unresponsive and restarts the driver. The GPU running
at 100% load can inadvertantly trip this reset the driver, causing applications
to crash. This can saftely be increased from the default *2 seconds* to a larger
value with the only negative impact being that an actual crashing driver will
take that much longer to be reset. A bump to *8 to 10* seconds is generally ok;
it is **not** recommended to disable TDR entirely.

.. wregedit:: Increase TDR delay to 8 seconds
  :key_title: HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\
              GraphicsDrivers
  :names:     TdrDelay
  :types:     DWORD
  :data:      8
  :admin:
  :no_section:
  :no_caption:

Show Password on Wifi Network
*****************************
.. code-block:: powershell
  :caption: Dump wifi configuration including password (powershell as admin).

  netsh wlan show profile WiFi-name key=clear

DRIVER_IRQL_NOT_LESS_OR_EQUAL (`Epfwwfp.sys`_)
**********************************************

:cmdmenu:`shift + Reset --> Troubleshoot --> Advanced options --> Start-up Settings --> Restart --> 4 (Safe Mode)`
:cmdmenu:`Troubleshoot --> Command Prompt`

.. code-block:: powershell
  :caption: Remove ESET driver and reboot.

  del /F /S /Q /A “c:\Windows\System32\drivers\epfwwfp.sys”

Offending program should be reinstalled.

`Uninstall Edge Browser`_
*************************
Heavily integrated into Windows 10. Will probably break stuff.

Download and build `install_wim_tweak`_.

.. literalinclude:: source/remove-edge.cmd
  :caption: Remove Edge browser and reboot.

:download:`remove-edge.cmd <source/remove-edge.cmd>`

`USB Devices Slow`_
*******************
In Windows 1809+ default USB removal policy changed to ``Quick removal`` for
additional safety instead of ``Better performance`` for additional speed; as a
result USB devices may appear slower than normal. This reverts to the old
behavior.

.. ggui:: Enable Better Performance for USB Devices
  :key_title: win + x -->
              Disk Management -->
              RMB {USB DEVICE} -->
              Properties -->
              Policies
  :option:    Removal policy,
              › ☑,
              Write-caching policy,
              › ☑
  :setting:   ,
              Better performance,
              ,
              Enable write caching on the device
  :no_section:
  :no_caption:
  :no_launch:

Disable `Windows Backup Schedule`_
**********************************
Removed since Windows 7 but added back into Windows 10.

.. code-block:: powershell
  :caption: powershell (as admin).

  sdclt.exe /DISABLEJOB

.. _integrity enabled: https://docs.microsoft.com/en-us/windows-server/storage/refs/integrity-streams
.. _ReFS create moved to Windows 10 Workstation: https://arstechnica.com/gadgets/2017/08/microsoft-to-remove-full-refs-support-from-windows-10-pro-push-workstation-sku/
.. _SSD activity issue: https://superuser.com/questions/1016152/100-ssd-activity-0-r-w-speed-system-hang-issue
.. _100% CPU usage issue: https://www.ghacks.net/2018/05/01/all-the-issues-of-windows-10-version-1803-you-may-run-into/
.. _System & Compressed Memory Service issue: http://whatsabyte.com/windows/system-and-compressed-memory-high-cpu/
.. _Disable Prefetch and Superfetch: https://www.thewindowsclub.com/disable-superfetch-prefetch-ssd
.. _Disabling ReFS Scheduled Tasks: http://bakins-bits.com/wordpress/?p=195
.. _Hiding Local Desktop for Chrome Remote Desktop: https://support.google.com/chrome/a/answer/2799701?hl=en&vid=0-243350879834-1495198101821
.. _Remote Desktop Extension: https://remotedesktop.google.com/access
.. _See block inbound RDP connections with Windows Firewall:  https://superuser.com/questions/723832/windows-firewall-blocks-remote-desktop-with-custom-port
.. _Fixing Broken Windows Store apps: https://community.spiceworks.com/how_to/122006-windows-10-your-trial-period-for-this-app-has-expired-visit-the-windows-store-to-purchase-the-full-app-problem
.. _Enable Bitlocker on USB drives over RDP: https://superuser.com/questions/962125/bitlocker-refuses-to-enable-via-rdp-on-data-drive-but-ok-on-the-os-drive
.. _Fix Windows Applications Not Appearing in Start Menu Searches: https://superuser.com/questions/947392/windows-10-search-cant-find-any-applications-even-calculator
.. _Disable Hibernation for Windows 10 Sleep Resume Problems: https://www.tenforums.com/general-support/5265-turn-off-wake-up-problems.html
.. _NTFS File Ownership Access Denied: https://superuser.com/questions/439675/how-to-bind-old-users-sid-to-new-user-to-remain-ntfs-file-ownership-and-permiss
.. _well known SIDs: https://docs.microsoft.com/en-us/troubleshoot/windows-server/identity/security-identifiers-in-windows
.. _Low Disk Space Warning After 1803 Update: https://answers.microsoft.com/en-us/insider/forum/insider_wintp-insider_install-insiderplat_pc/new-oem-partition-appears-in-file-explorer-after/29a0a95c-fe51-41a5-a345-72773c437b39
.. _almost entirely full: https://www.thewindowsclub.com/faq-low-disk-space-notification-or-warning-in-windows-7-how-to-disable-etc
.. _Application Using the Wrong Audio Output Device: https://www.intowindows.com/set-different-audio-output-devices-for-different-programs-in-windows-10/
.. _EasyUEFI: https://www.easyuefi.com/index-us.html
.. _Timeout Detection and Recovery: https://www.pugetsystems.com/labs/hpc/Working-around-TDR-in-Windows-for-a-better-GPU-computing-experience-777/
.. _extra EFI boot configuration data: https://linuxbsdos.com/2015/09/05/how-to-delete-grub-files-from-a-boot-efi-partition-in-windows-10/
.. _Epfwwfp.sys: https://ugetfix.com/ask/how-to-fix-driver_irql_not_less_or_equal-epfwwfp-sys-error-on-windows/
.. _Uninstall Edge Browser: https://www.intowindows.com/how-to-uninstall-remove-edge-browser-from-windows-10/
.. _install_wim_tweak: https://github.com/shiitake/win6x_registry_tweak
.. _USB Devices Slow: https://docs.microsoft.com/en-us/windows/client-management/change-default-removal-policy-external-storage-media
.. _Windows Backup Schedule: https://www.tenforums.com/tutorials/75591-turn-off-schedule-windows-backup-windows-10-a.html
.. _Disable Caret Browsing Notifications: https://www.thewindowsclub.com/enable-caret-browsing-internet-explorer
.. _habit of locking out after updates: https://www.passfab.com/windows-tips/windows-10-password-incorrect-after-update.html
.. _Reset your password from safe mode: https://www.wimware.com/how-to/reset-windows-10-password-command-prompt.html