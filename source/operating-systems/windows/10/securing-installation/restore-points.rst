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

  Disable-ComputerRestore -Drive "C:\"
  vssadmin delete shadows /all /Quiet

.. wtschedule:: Disable schedule task for System Restore.
  :key_title:   Microsoft --> Windows --> System Restore --> SR --> RMB --> Disable
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

.. _Disable restore points: https://github.com/adolfintel/Windows10-Privacy#system-restore