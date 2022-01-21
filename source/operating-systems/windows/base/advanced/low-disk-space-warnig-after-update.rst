.. _wbase-specific-windows-fixes-low-disk-space-warnig-after-update:

Low Disk Space Warning After Update
###################################
After updating to Windows 10 1803, a consistent low disk space warning appears.
This happens as the upgrade now sets the OEM partition (~450MB) to be mounted
on boot. This drive is almost entirely full (~400MB) and triggers a low disk
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

`Reference <https://www.thewindowsclub.com/faq-low-disk-space-notification-or-warning-in-windows-7-how-to-disable-etc>`__
