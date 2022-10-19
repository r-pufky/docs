.. _w10-21h2-standalone-paging:

Paging
######
Systems with more than **8GB** memory should disable paging. This may need to be
re-enabled if certain programs rely on the paging file existing.

.. dropdown:: Give priority to foreground applications
  :color: primary
  :icon: shield-lock
  :animate: fade-in
  :class-container: sd-shadow-sm

  .. gui::    Give priority to foreground applications
    :path:    ⌘ + r -->
              systempropertiesadvanced -->
              Performance -->
              Settings -->
              Advanced -->
              Processor scheduling
    :value0:  ☑, Programs
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable paging files on all drives via Registry
    :path:     HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\
               PriorityControl
    :value0:   Win32PrioritySeparation, {DWORD}, 2
    :update:   2021-02-19
    :generic:
    :open:

    ``2`` is the value used for the GUI setting. ``26`` is the highest
    foreground priority. ``18`` prefers background services.

.. dropdown:: Disable paging files for all drives
  :color: primary
  :icon: shield-lock
  :animate: fade-in
  :class-container: sd-shadow-sm

  .. gui::    Disable paging files for all drives
    :path:    ⌘ + r -->
              systempropertiesadvanced -->
              Performance -->
              Settings -->
              Advanced -->
              Virtual memory -->
              Change...
    :value0:  ☑, No paging file
    :update:  2021-02-19
    :generic:
    :open:

    Be sure to set this for each drive explicitly.

  .. regedit:: Disable paging files on all drives
    :path:     HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\
               Session Manager\Memory Management
    :value0:   PagingFiles, {SZ}, {EMPTY}
    :ref:      https://petri.com/pagefile_optimization
    :update:   2021-02-19
    :generic:
    :open:

.. regedit:: Disable swapfile for windows components
  :path:     HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\
             Session Manager\Memory Management
  :value0:   SwapfileControl, {DWORD}, 0
  :ref:      https://www.windowscentral.com/what-swapfilesys-and-do-i-need-it-my-windows-10-pc,
             https://github.com/Disassembler0/Win10-Initial-Setup-Script/issues/190
  :update:   2021-02-19
