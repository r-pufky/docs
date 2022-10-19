.. _wbase-remove-startup-items:

Remove Startup Items
####################
Force remove items from Task Manager Startup list that cannot be removed in the
GUI; such as Microsoft OneDrive which will leave a setup startup service on
removal.

.. dropdown:: Force remove startup items
  :color: primary
  :icon: stack
  :animate: fade-in
  :class-container: sd-shadow-sm
  :open:

  Delete entries that should not appear (or can't be removed from startup by
  other means). All locations must be checked.

  .. regedit:: Force remove local machine startupapproved startup items
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
               Explorer\StartupApproved\Run
    :value0:   {ANY}, {BINARY}, {DELETE}
    :ref:      https://www.tenforums.com/tutorials/2944-add-delete-enable-disable-startup-items-windows-10-a.html
    :update:   2021-02-19

  .. regedit:: Force remove user startupapproved startup items
    :path:     HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\
               Explorer\StartupApproved\Run
    :value0:   {ANY}, {BINARY}, {DELETE}
    :ref:      https://www.tenforums.com/tutorials/2944-add-delete-enable-disable-startup-items-windows-10-a.html
    :update:   2021-02-19

  .. regedit:: Force remove user currentversion run
    :path:     HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
    :value0:   {ANY}, {BINARY}, {DELETE}
    :ref:      https://www.winhelponline.com/blog/task-manager-startup-tab-entries-remove-invalid/
    :update:   2022-01-09

  .. regedit:: Force remove local machine currentversion run
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
    :value0:   {ANY}, {BINARY}, {DELETE}
    :ref:      https://www.winhelponline.com/blog/task-manager-startup-tab-entries-remove-invalid/
    :update:   2022-01-09

  .. regedit:: Force remove user wow6432node currentversion run
    :path:     HKEY_CURRENT_USER\SOFTWARE\WOW6432Node\Microsoft\Windows\
               CurrentVersion\Run
    :value0:   {ANY}, {BINARY}, {DELETE}
    :ref:      https://www.winhelponline.com/blog/task-manager-startup-tab-entries-remove-invalid/
    :update:   2022-01-09

  .. regedit:: Force remove local machine wow6432node currentversion run
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\Windows\
               CurrentVersion\Run
    :value0:   {ANY}, {BINARY}, {DELETE}
    :ref:      https://www.winhelponline.com/blog/task-manager-startup-tab-entries-remove-invalid/
    :update:   2022-01-09

  .. regedit:: Force remove local machine currentversion startup approved
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
               Explorer\StartupApproved\Run32
    :value0:   {ANY}, {BINARY}, {DELETE}
    :ref:      https://www.winhelponline.com/blog/task-manager-startup-tab-entries-remove-invalid/
    :update:   2022-01-09
