.. _w10-1903-disable-paging:

Disable Paging
##############
Systems with more than **8GB** memory should disable paging. This may need to be
re-enabled if certain programs rely on the paging file existing.

.. dropdown:: Give priority to foreground applications
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: GUI
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. ggui:: Give priority to foreground applications
      :key_title: ⌘ + r -->
                  systempropertiesadvanced -->
                  Performance -->
                  Settings -->
                  Advanced -->
                  Processor scheduling
      :option:    ☑
      :setting:   Programs
      :no_section:
      :no_caption:
      :no_launch:

  .. regedit:: Disable paging files on all drives via Registry
    :path:     HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\
               PriorityControl
    :value0:   Win32PrioritySeparation, {DWORD}, 2
    :ref:      https://petri.com/pagefile_optimization
    :update:   2021-02-19
    :generic:
    :open:

    ``2`` is the value used for the GUI setting. ``26`` is the highest
    foreground priority. ``18`` prefers background services.

.. dropdown:: Disable paging files for all drives
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: GUI
    :title: font-weight-bold
    :animate: fade-in
    :open:

    Be sure to set this for each drive explicitly.

    .. ggui:: Disable paging files for all drives
      :key_title: ⌘ + r -->
                  systempropertiesadvanced -->
                  Performance -->
                  Settings -->
                  Advanced -->
                  Virtual memory -->
                  Change...
      :option:    ☑
      :setting:   No paging file
      :no_section:
      :no_caption:
      :no_launch:

  .. regedit:: Disable paging files on all drives
    :path:     HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\
               Session Manager\Memory Management
    :value0:   PagingFiles, {MULTI_SZ}, {EMTPY}
    :ref:      https://petri.com/pagefile_optimization
    :update:   2021-02-19
    :generic:
    :open:

.. regedit:: Disable swapfile for windows components via Registry
  :path:     HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\
             Session Manager\Memory Management
  :value0:   SwapfileControl, {DWORD}, 0
  :ref:      https://www.windowscentral.com/what-swapfilesys-and-do-i-need-it-my-windows-10-pc,
             https://github.com/Disassembler0/Win10-Initial-Setup-Script/issues/190
  :update:   2021-02-19
