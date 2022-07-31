.. _w10-21h2-standalone-restore-points:

Restore Points
##############
All system changes trigger a backup of affect files before changes are applied;
this creeate a drastic performance hit. Disable restore points.

.. dropdown:: Disable restore points for each drive
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

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
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. code-block:: powershell
      :caption: Disable restore points powershell (as admin)

      Get-PSDrive -PSProvider FileSystem | ForEach-Object -Process {Disable-ComputerRestore -Drive $_.Root -ErrorAction SilentlyContinue}
      vssadmin delete shadows /all /Quiet

  `Reference <https://github.com/adolfintel/Windows10-Privacy#system-restore>`__

.. dropdown:: Disable system restore
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

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
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. note::
    Windows updates can re-enable restore points, leave enabled to disable if
    needed after update.

  .. gpo::    Enable system restore configuration
    :path:    Computer Configuration -->
              Administrative Templates -->
              System -->
              System Restore -->
              Turn off Configuration
    :value0:  ☑, {DISABLED}
    :ref:     https://www.tenforums.com/tutorials/99782-enable-disable-system-restore-windows.html
    :update:  2021-02-19
    :generic:
    :open:
