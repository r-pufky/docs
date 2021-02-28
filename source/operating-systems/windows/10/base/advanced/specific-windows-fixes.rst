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

.. regedit:: REFS single drive regedit
  :path:     HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\MiniNT
  :value0:   AllowRefsFormatOverNonmirrorVolume, {DWORD}, 1
  :update:   2021-02-19

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

.. gui::   Disable REFS scheduled tasks task
  :label:  Task Scheduler
  :nav:    ⌘ --> Task Scheduler --> Task Scheduler Library
  :path:   Microsoft --> Windows --> Data Integrity Scan
  :value0:                    Data Integrity Scan, {DISABLED}
  :value1: Data Integrity Scan for Crash Recovery, {DISABLED}
  :update: 2021-02-19

Addressing 100% Disk Usage Issues
*********************************
Generally speaking, 100% disk usage issues usually means there's a Filesystem
check happening, or another service is hammering the disk. These will address
this but may break functionality of your system.

These services either do user data tracking, or are a major performance hit for
SSD's. Disable by :cmdmenu:`RMB --> stop` and
:cmdmenu:`RMB --> properties --> disable`.

.. gui::   Disable search service
  :label:  Service
  :nav:    ⌘ --> services.msc
  :path:   Windows Search --> General
  :value0:   Service name, WService
  :value1:   Startup type, {DISABLED}
  :value2: Service status, {STOPPED}
  :ref:    https://superuser.com/questions/1016152/100-ssd-activity-0-r-w-speed-system-hang-issue
  :update: 2021-02-19

.. gui::   Disable superfetch service
  :label:  Service
  :nav:    ⌘ --> services.msc
  :path:   Superfetch --> General
  :value0:   Service name, SysMain
  :value1:   Startup type, {DISABLED}
  :value2: Service status, {STOPPED}
  :ref:    https://www.ghacks.net/2018/05/01/all-the-issues-of-windows-10-version-1803-you-may-run-into/,
           http://whatsabyte.com/windows/system-and-compressed-memory-high-cpu/
  :update: 2021-02-19

Disable Prefetch and Superfetch
*******************************
This addresses 100% disk usage during idle in windows 10, even if you've already
disabled the superfetching service.

.. regedit:: Disable prefetch and superfetch regedit
  :path:     HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\
             Session Manager\Memory Management\PrefetchParameters
  :value0:   EnablePrefetcher,   {DWORD}, 0
  :value1:   EnableSuperfetcher, {DWORD}, 0
  :ref:      https://www.thewindowsclub.com/disable-superfetch-prefetch-ssd
  :update:   2021-02-19

.. _w10-hiding-local-desktop-crd:

Hiding Local Desktop for Chrome Remote Desktop
**********************************************
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

.. regedit:: Enable remote access curtain for CRD regedit
  :path:     HKEY_LOCAL_MACHINE\Software\Policies\Google\Chrome
  :value0:   RemoteAccessHostRequireCurtain, {DWORD}, 1
  :ref:      https://support.google.com/chrome/a/answer/2799701?hl=en&vid=0-243350879834-1495198101821
  :update:   2021-02-19

.. regedit:: Enable RDP security regedit
  :path:     HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\
             Terminal Server\WinStations\RDP-Tcp
  :value0:   SecurityLayer, {DWORD}, 1
  :ref:      https://support.google.com/chrome/a/answer/2799701?hl=en&vid=0-243350879834-1495198101821
  :update:   2021-02-19

:cmdmenu:`⌘ + r --> control --> System and Security --> System --> Remote Settings --> Remote`

* ☑ Allow remote connections to this computer.
* ☐ Allow connections only from computers running Remote Desktop with Network
  Level Authentication.

.. gui::   Block inbound rdp connections firewall
  :label:  Firewall
  :nav:    ⌘ -->Control Panel --> System and Security --> Windows Defender Firewall
  :path:   Advanced Settings --> Inbound Rules
  :value0:    Remote Desktop - Shadow (TCP-in), {BLOCK}
  :value1: Remote Desktop - User Mode (TCP-in), {BLOCK}
  :value2: Remote Desktop - User Mode (UDP-in), {BLOCK}
  :ref:    https://superuser.com/questions/723832/windows-firewall-blocks-remote-desktop-with-custom-port
  :update: 2021-02-19

`Fixing Broken Windows Store apps`_ / 'Trial Expired' Apps
**********************************************************
Default windows 10 applications may stop working if you remove dependent apps
from the system. Symptoms include apps like xbox controller config never
loading, or calculator prompting with trial expired. This resets the system to
the default app installation state for windows 10.

.. code-block:: powershell
  :caption: Reinstall default Windows applications (powershell as admin).

  Get-AppXPackage -AllUsers | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}

Enable Bitlocker on USB drives over RDP
***************************************
By default, bitlocker does not allow encryption to be enabled on USB devices
over RDP connections -- this happens because RDP treats USB drives as mapped
network drives and not external drives. This enables direct drive access for RDP
connections. This is unsafe.

.. gpo::   Enable bitlocker on usb drives over rdp policy
  :path:   Computer Configuration -->
           Administrative Templates -->
           System -->
           Removable Storage Access
  :value0: All Removable Storage: Allow direct access in remote sessions, Enabled
  :ref:    https://superuser.com/questions/962125/bitlocker-refuses-to-enable-via-rdp-on-data-drive-but-ok-on-the-os-drive
  :update: 2021-02-19

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

OEM Partition / Low Disk Space Warning After 1803 Update
********************************************************
After updating to Windows 10 1803, a consistent low disk space warning appears.
This happens as the upgrade now sets the OEM partition (~450MB) to be mounted on
boot. This drive is `almost entirely full`_ (~400MB) and triggers a low disk
warning.

.. code-block:: powershell
  :caption: Unmount OEM partition from drive (powershell as admin).

  mountvol {OEM PARTITION DRIVE}: /d

.. regedit:: Disable disk space warning checks for partition
  :path:     HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\
             Policies\Explorer
  :value0:   NoLowDiskSpaceChecks, {DWORD}, 1
  :ref:      https://answers.microsoft.com/en-us/insider/forum/insider_wintp-insider_install-insiderplat_pc/new-oem-partition-appears-in-file-explorer-after/29a0a95c-fe51-41a5-a345-72773c437b39
  :update:   2021-02-19

`Application Using the Wrong Audio Output Device`_
**************************************************
Some applications will not respect the default output device in Windows 10 and
output to the wrong device. Output settings can be set for specific applications
via the settings menu.

:cmdmenu:`⌘ + r --> ms-settings:sound --> Advanced sound options --> App volume and device preferences`

   * Set preferred output for device (application must be running).

Disable Caret Browsing Notifications
************************************
Remove notification on F7 press for caret browsing. This is a holdover from
Internet Explorer.

.. regedit:: Disable Caret Browsing Notifications
  :path:     HKEY_CURRENT_USER\Software\Microsoft\Internet Explorer\CaretBrowsing
  :value0:   Enabled, {DWORD}, 0
  :ref:      https://www.thewindowsclub.com/enable-caret-browsing-internet-explorer
  :update:   2021-02-19

.. gpo::   Disable Caret Browsing Notifications
  :path:   User Configuration -->
           Administrative Templates -->
           Windows Components -->
           Internet Explorer -->
           Internet Control Panel -->
           Advanced Page -->
           Turn on Caret Browsing support
  :value0: ☑, {DISABLED}
  :ref:    https://www.thewindowsclub.com/enable-caret-browsing-internet-explorer
  :update: 2021-02-19

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
Windows Vista+ has a feature called Timeout Detection and Recovery, which
detects if the GPU becomes unresponsive and restarts the driver. The GPU running
at 100% load can inadvertantly trip this reset the driver, causing applications
to crash. This can saftely be increased from the default *2 seconds* to a larger
value with the only negative impact being that an actual crashing driver will
take that much longer to be reset. A bump to *8 to 10* seconds is generally ok;
it is **not** recommended to disable TDR entirely.

.. regedit:: Increase TDR delay to 8 seconds
  :path:     HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\GraphicsDrivers
  :value0:   TdrDelay, {DWORD}, 8
  :ref:      https://www.pugetsystems.com/labs/hpc/Working-around-TDR-in-Windows-for-a-better-GPU-computing-experience-777/
  :update:   2021-02-19

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

USB Devices Slow
****************
In Windows 1809+ default USB removal policy changed to ``Quick removal`` for
additional safety instead of ``Better performance`` for additional speed; as a
result USB devices may appear slower than normal. This reverts to the old
behavior.

.. gui::   Enable Better Performance for USB Devices
  :path:   ⌘ + x -->
           Disk Management -->
           RMB {USB DEVICE} -->
           Properties -->
           Policies
  :value0: Removal policy,
  :value1: › ☑, Better performance
  :value2: Write-caching policy,
  :value3: › ☑, Enable write caching on the device
  :ref:    https://docs.microsoft.com/en-us/windows/client-management/change-default-removal-policy-external-storage-media
  :update: 2021-02-19

Disable `Windows Backup Schedule`_
**********************************
Removed since Windows 7 but added back into Windows 10.

.. code-block:: powershell
  :caption: powershell (as admin).

  sdclt.exe /DISABLEJOB

`Debug DNS Issues`_
*******************
Windows 10 aggressively caches DNS with a DNS caching service and can sometimes
lead to invalid results. First flush resolver caches and test.

.. code-block:: powershell
  :caption: powershell

  ipconfig /flushdns
  Clear-DnsClientCache

If that does not work, disabling the DNS caching service can be used. **Cannot**
be disabled via ``services.msc``.

.. regedit:: Disable DNS caching service
  :path:     HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\Dnscache
  :value0:   Start, {DWORD}, 4
  :update:   2021-02-19

After resolving, re-enable the caching service and **Reboot**.

.. regedit:: Enable DNS caching service
  :path:     HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\Dnscache
  :value0:   Start, {DWORD}, 2
  :update:   2021-02-19

`Disable Hyper-V Per Boot`_
***************************
Some applications and games detect Hyper-V virtualization and refuse to start.
Disable Hyper-V on Windows boot instead of through the BIOS. This removes the
hypervisor kernel modules which prevents this from happening without needing to
turn it off.

.. code-block:: powershell
  :caption: powershell (as admin).

  bcdedit --% /copy {current} /d "No Hyper-V"

  bcdedit --%  /set {GUID} hypervisorlaunchtype off

Restart holding :cmdmenu:`shift` to show boot options. Select ``No Hyper-V``.

.. _integrity enabled: https://docs.microsoft.com/en-us/windows-server/storage/refs/integrity-streams
.. _ReFS create moved to Windows 10 Workstation: https://arstechnica.com/gadgets/2017/08/microsoft-to-remove-full-refs-support-from-windows-10-pro-push-workstation-sku/
.. _Disabling ReFS Scheduled Tasks: http://bakins-bits.com/wordpress/?p=195
.. _Remote Desktop Extension: https://remotedesktop.google.com/access
.. _Fixing Broken Windows Store apps: https://community.spiceworks.com/how_to/122006-windows-10-your-trial-period-for-this-app-has-expired-visit-the-windows-store-to-purchase-the-full-app-problem
.. _Fix Windows Applications Not Appearing in Start Menu Searches: https://superuser.com/questions/947392/windows-10-search-cant-find-any-applications-even-calculator
.. _Disable Hibernation for Windows 10 Sleep Resume Problems: https://www.tenforums.com/general-support/5265-turn-off-wake-up-problems.html
.. _NTFS File Ownership Access Denied: https://superuser.com/questions/439675/how-to-bind-old-users-sid-to-new-user-to-remain-ntfs-file-ownership-and-permiss
.. _well known SIDs: https://docs.microsoft.com/en-us/troubleshoot/windows-server/identity/security-identifiers-in-windows
.. _almost entirely full: https://www.thewindowsclub.com/faq-low-disk-space-notification-or-warning-in-windows-7-how-to-disable-etc
.. _Application Using the Wrong Audio Output Device: https://www.intowindows.com/set-different-audio-output-devices-for-different-programs-in-windows-10/
.. _EasyUEFI: https://www.easyuefi.com/index-us.html
.. _extra EFI boot configuration data: https://linuxbsdos.com/2015/09/05/how-to-delete-grub-files-from-a-boot-efi-partition-in-windows-10/
.. _Epfwwfp.sys: https://ugetfix.com/ask/how-to-fix-driver_irql_not_less_or_equal-epfwwfp-sys-error-on-windows/
.. _Uninstall Edge Browser: https://www.intowindows.com/how-to-uninstall-remove-edge-browser-from-windows-10/
.. _install_wim_tweak: https://github.com/shiitake/win6x_registry_tweak
.. _Windows Backup Schedule: https://www.tenforums.com/tutorials/75591-turn-off-schedule-windows-backup-windows-10-a.html
.. _habit of locking out after updates: https://www.passfab.com/windows-tips/windows-10-password-incorrect-after-update.html
.. _Reset your password from safe mode: https://www.wimware.com/how-to/reset-windows-10-password-command-prompt.html
.. _Disable Hyper-V Per Boot: https://www.hanselman.com/blog/switch-easily-between-virtualbox-and-hyperv-with-a-bcdedit-boot-entry-in-windows-81
.. _Debug DNS Issues: https://wintechlab.com/enable-disable-dns-client-service/
