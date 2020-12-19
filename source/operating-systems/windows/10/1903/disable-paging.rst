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

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    ``2`` is the value used for the GUI setting. ``26`` is the highest
    foreground priority. ``18`` prefers background services.

    .. wregedit:: Disable paging files on all drives via Registry
      :key_title: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\
                  PriorityControl
      :names:     Win32PrioritySeparation
      :types:     DWORD
      :data:      2
      :no_section:
      :no_caption:

.. dropdown:: Disable paging files for all drives
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: GUI
    :title: font-weight-bold
    :animate: fade-in

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

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Disable paging files on all drives
      :key_title: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\
                  Session Manager\Memory Management
      :names:     PagingFiles
      :types:     MULTI_SZ
      :data:      {EMPTY}
      :no_section:
      :no_caption:

.. dropdown:: Disable swapfile for windows components
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Disable swapfile for windows components via Registry
      :key_title: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\
                  Session Manager\Memory Management
      :names:     SwapfileControl
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

.. rubric:: References

#. `Windows pagefile Optimization <https://petri.com/pagefile_optimization>`_
#. `Windows disabling swapfile <https://www.windowscentral.com/what-swapfilesys-and-do-i-need-it-my-windows-10-pc>`_
#. `Windows swapfile explanation <https://github.com/Disassembler0/Win10-Initial-Setup-Script/issues/190>`_
