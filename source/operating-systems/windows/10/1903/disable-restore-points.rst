.. _w10-1903-disable-restore-points:

Disable Restore Points
######################
All system changes trigger a backup of affect files before changes are applied;
this creeate a drastic performance hit.

.. dropdown:: Disable restore points for each drive
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: GUI
    :title: font-weight-bold
    :animate: fade-in
    :open:

    Be sure to set this for each drive explicitly.

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
      :no_caption:
      :no_launch:

  .. dropdown:: Powershell
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. code-block:: powershell
      :caption: `Disable restore points`_ powershell (as admin)

      Get-PSDrive -PSProvider FileSystem | ForEach-Object -Process {Disable-ComputerRestore -Drive $_.Root -ErrorAction SilentlyContinue}
      vssadmin delete shadows /all /Quiet

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
    :ref:     https://www.sevenforums.com/tutorials/81500-system-restore-enable-disable.html
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable system restore
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows NT\SystemRestore
    :value0:   DisableSR, {DWORD}, 1
    :ref:      https://www.sevenforums.com/tutorials/81500-system-restore-enable-disable.html
    :update:   2021-02-19
    :generic:
    :open:

  .. regedit:: Disable system restore
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SystemRestore
    :value0:   DisableSR, {DWORD}, 1
    :ref:      https://www.sevenforums.com/tutorials/81500-system-restore-enable-disable.html
    :update:   2021-02-19
    :generic:
    :open:

  .. dropdown:: Scheduled Tasks
    :title: font-weight-bold
    :animate: fade-in

    .. wtschedule:: Disable system restore scheduled tasks
      :key_title:   Microsoft --> Windows --> SystemRestore --> SR --> RMB --> Disable
      :option:      Name,
                    Description
      :setting:     SR,
                    This task creates regular system protection points.

.. _Disable restore points: https://github.com/adolfintel/Windows10-Privacy#system-restore

.. dropdown:: Disable system restore configuration
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. gpo::    Disable system restore configuration
    :path:    Computer Configuration -->
              Administrative Templates -->
              System -->
              System Restore -->
              Turn off Configuration
    :value0:  ☑, {ENABLED}
    :ref:     https://www.sevenforums.com/tutorials/81500-system-restore-enable-disable.html
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable system restore configuration
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows NT\SystemRestore
    :value0:   DisableConfig, {DWORD}, 1
    :ref:      https://www.sevenforums.com/tutorials/81500-system-restore-enable-disable.html
    :update:   2021-02-19
    :generic:
    :open:

  .. regedit:: Disable system restore configuration
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SystemRestore
    :value0:   DisableConfig, {DWORD}, 1
    :ref:      https://www.sevenforums.com/tutorials/81500-system-restore-enable-disable.html
    :update:   2021-02-19
    :generic:
    :open:
