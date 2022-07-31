.. _wbase-specific-windows-fixes-refx-on-windows-pro:

ReFS on Windows Pro
###################
Recently ReFS create moved to Windows 10 Workstation, effectively removing the
ability to create ReFS containers in Windows 10 Pro, but they can still be
read. Virtual disks with ReFS formatting can be created and exported for use in
10 Pro machines.

Empty ReFS formatted disk images below, ensure disk is **updated** and
**optimized** in storage spaces before use. bitlocker can be used.

* ReFS 1TB single virtual disk with integrity enabled: :download:`refsi.zip (784k)<source/refsi.zip>`
* ReFS 1TB mirrored virutal disk: :download:`refsi-mirrored.zip (1.8M)<source/refs-mirrored.zip>`

`Reference <https://arstechnica.com/gadgets/2017/08/microsoft-to-remove-full-refs-support-from-windows-10-pro-push-workstation-sku/>`__

Format ReFS on using a single drive
***********************************
ReFS allows for integrated file checksums, duplication, and error recovery;
however by default it requires two disks. This will allow you to use this
filesystem on a single disk with integrity enabled which is not possible by
default.

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
   * Reformat drive with integrity enabled.

.. code-block:: powershell
  :caption: Format Single Drive with Integrity Enabled & Verify with Test File
            (powershell as admin).

  format X: /fs:refs /i:enable /q
  echo $null >> X:\test
  Get-Item X:\test | Get-FileIntegrity

.. note::
  Both Enabled and Enforced should be set to True.

.. rubric:: Disable ReFS Scheduled Tasks

By default ReFS will schedule integrity checks (as well as automatic integrity
checks after windows crashes), which cause 100% disk usage on system PID 4.
Disabling ReFS Scheduled Tasks prevents these from automatically being
scheduled, but can still be manually run.

.. gui::   Disable REFS scheduled tasks task
  :label:  Task Scheduler
  :nav:    ⌘ --> Task Scheduler --> Task Scheduler Library
  :path:   Microsoft --> Windows --> Data Integrity Scan
  :value0:                    Data Integrity Scan, {DISABLED}
  :value1: Data Integrity Scan for Crash Recovery, {DISABLED}
  :update: 2021-02-19

`Reference <https://docs.microsoft.com/en-us/windows-server/storage/refs/integrity-streams>`__

`Reference <http://bakins-bits.com/wordpress/?p=195>`__

Addressing 100% Disk Usage Issues
*********************************
Generally speaking, 100% disk usage issues usually means there's a Filesystem
check happening, or another service is hammering the disk. These will address
this but may break functionality of your system.

These services either do user data tracking, or are a major performance hit for
SSD's. Disable by :cmdmenu:`{RMB} --> stop` and
:cmdmenu:`{RMB} --> properties --> disable`.

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
