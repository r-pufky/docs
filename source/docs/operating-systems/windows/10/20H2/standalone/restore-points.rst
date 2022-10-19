.. _w10-20h2-standalone-restore-points:

Restore Points
##############
All system changes trigger a backup of affect files before changes are applied;
this creeate a drastic performance hit. Disable restore points.

.. dropdown:: Disable restore points for each drive
  :color: primary
  :icon: browser
  :animate: fade-in
  :class-container: sd-shadow-sm

  .. gui::    Disable restore points for each drive
    :path:    ⌘ + r -->
              systempropertiesprotection -->
              Protection Settings -->
              {DRIVE} -->
              Configure
    :value0:  ☑, Disable system protection
    :value1:  Max Usage, 0
    :value2:  Delete all restore points for this drive, {DELETE}
    :update:  2021-02-19
    :generic:
    :open:

    Be sure to set this for each drive explicitly.

  .. dropdown:: Powershell
    :icon: terminal
    :animate: fade-in
    :open:

    .. code-block:: powershell
      :caption: Disable restore points powershell (as admin)

      Get-PSDrive -PSProvider FileSystem | ForEach-Object -Process {Disable-ComputerRestore -Drive $_.Root -ErrorAction SilentlyContinue}
      vssadmin delete shadows /all /Quiet

  `Reference <https://github.com/adolfintel/Windows10-Privacy#system-restore>`__

.. dropdown:: Disable system restore
  :color: primary
  :icon: note
  :animate: fade-in
  :class-container: sd-shadow-sm

  .. gpo::    Disable system restore
    :path:    Computer Configuration -->
              Administrative Templates -->
              System -->
              System Restore -->
              Turn off System Restore
    :value0:  ☑, {ENABLED}
    :ref:     https://www.tenforums.com/tutorials/99782-enable-disable-system-restore-windows.html
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable system restore
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows NT\
               SystemRestore
    :value0:   DisableSR, {DWORD}, 1
    :ref:      https://www.tenforums.com/tutorials/99782-enable-disable-system-restore-windows.html
    :update:   2021-02-19
    :generic:
    :open:

  .. regedit:: Disable system restore
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\
               CurrentVersion\SystemRestore
    :value0:   DisableSR, {DWORD}, 1
    :ref:      https://www.tenforums.com/tutorials/99782-enable-disable-system-restore-windows.html
    :update:   2021-02-19
    :generic:
    :open:

  .. gui::    Disable system restore scheduled tasks
    :label:   Task Scheduler
    :nav:     ⌘ --> Task Scheduler --> Task Scheduler Library
    :path:    Microsoft --> Windows --> SystemRestore --> SR -->
              {RMB} --> Disable
    :value0:  Name, SR
    :value1:  Description, This task creates regular system protection points.
    :update:  2021-02-19
    :generic:
    :open:

.. dropdown:: Disable system restore configuration
  :color: primary
  :icon: note
  :animate: fade-in
  :class-container: sd-shadow-sm

  .. note::
    Windows updates can re-enable restore points even though this is disabled.

  .. gpo::    Disable system restore configuration
    :path:    Computer Configuration -->
              Administrative Templates -->
              System -->
              System Restore -->
              Turn off Configuration
    :value0:  ☑, {ENABLED}
    :ref:     https://www.tenforums.com/tutorials/99782-enable-disable-system-restore-windows.html
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable system restore configuration
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows NT\
               SystemRestore
    :value0:   DisableConfig, {DWORD}, 1
    :ref:      https://www.tenforums.com/tutorials/99782-enable-disable-system-restore-windows.html
    :update:   2021-02-19
    :generic:
    :open:

  .. regedit:: Disable system restore configuration
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\
               CurrentVersion\SystemRestore
    :value0:   DisableConfig, {DWORD}, 1
    :ref:      https://www.tenforums.com/tutorials/99782-enable-disable-system-restore-windows.html
    :update:   2021-02-19
    :generic:
    :open:
