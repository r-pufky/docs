.. _windows-10-disable-restore-points:

Disable Restore Points
######################
All system changes trigger a backup of affect files before changes are applied;
this creeate a drastic performance hit.

.. ggui:: Disable restore points for each drive
  :key_title: ⌘ + r -->
              systempropertiesprotection -->
              Protection Settings -->
              {DRIVE} -->
              Configure
  :option:    ☑,
              Max Usage,
              Delete all restore points for this drive
  :setting:   Disable system protection,
              0,
              Delete
  :no_section:
  :no_launch:

    .. note::
      Be sure to set this for each drive explicitly.

.. code-block:: powershell
  :caption: `Disable restore points`_ powershell (as admin)

  Get-PSDrive -PSProvider FileSystem | ForEach-Object -Process {Disable-ComputerRestore -Drive $_.Root -ErrorAction SilentlyContinue}
  vssadmin delete shadows /all /Quiet

    .. note::
      This will disable system restore on all mounted Filesystems.

.. wtschedule:: Disable schedule task for System Restore.
  :key_title:   Microsoft --> Windows --> SystemRestore --> SR --> RMB --> Disable
  :option:      Name,
                Description
  :setting:     SR,
                This task creates regular system protection points.
  :no_section:
  :no_caption:

:term:`Registry`
****************
.. wregedit:: Disable system restore via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows NT\SystemRestore
  :names:     DisableConfig
  :types:     DWORD
  :data:      1
  :no_section:

.. wregedit:: Disable system restore via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows NT\SystemRestore
  :names:     DisableSR
  :types:     DWORD
  :data:      1
  :no_section:
  :no_launch:

.. wregedit:: Disable system restore via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SystemRestore
  :names:     DisableConfig
  :types:     DWORD
  :data:      1
  :no_section:
  :no_launch:

.. wregedit:: Disable system restore via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SystemRestore
  :names:     DisableSR
  :types:     DWORD
  :data:      1
  :no_section:
  :no_launch:

:term:`Registry`
****************
.. wgpolicy:: Disable system restore via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              System -->
              System Restore -->
              Turn off System Restore
  :option:    ☑
  :setting:   Enabled
  :no_section:

.. wgpolicy:: Disable system restore configuration via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              System -->
              System Restore -->
              Turn off Configuration
  :option:    ☑
  :setting:   Enabled
  :no_section:

.. rubric:: References

#. `Disable System Restore <https://www.sevenforums.com/tutorials/81500-system-restore-enable-disable.html>`_

.. _Disable restore points: https://github.com/adolfintel/Windows10-Privacy#system-restore