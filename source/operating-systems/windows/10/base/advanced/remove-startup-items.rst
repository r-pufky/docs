.. _w10-remove-startup-items:

`Remove Startup Items`_
#######################
Force remove items from Task Manager Startup list that cannot be removed in the
GUI; such as Microsoft OneDrive which will leave a setup startup service on
removal.

.. dropdown:: Force remove startup items
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in
  :open:

  Delete entries that should not appear (or can't be removed from startup by
  other means).

  .. regedit:: Force remove startup items
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
               Explorer\StartupApproved\Run
    :value0:   {ANY}, {BINARY}, {DELETE}
    :ref:      https://www.tenforums.com/tutorials/2944-add-delete-enable-disable-startup-items-windows-10-a.html
    :update:   2021-02-19
    :generic:
    :open:

  .. regedit:: Force remove startup items
    :path:     HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\
               Explorer\StartupApproved\Run
    :value0:   {ANY}, {BINARY}, {DELETE}
    :ref:      https://www.tenforums.com/tutorials/2944-add-delete-enable-disable-startup-items-windows-10-a.html
    :update:   2021-02-19
    :generic:
    :open:
