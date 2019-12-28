.. _windows-10-disable-startup-services:

`Remove Startup Items`_
#######################
Remove startup items that are unused from the Task Manager Startup list. For
items such as Microsoft OneDrive, which won't disappear when removed.

:term:`Registry`
****************
.. wregedit:: Remove startup items for system via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
              Explorer\StartupApproved\Run
  :names:     {ANY}
  :types:     BINARY
  :data:      {DELETE}
  :no_section:

    .. note::
      Delete entries that should not appear (or can't be removed from startup by
      other means). This applies to the entire **system**.

.. wregedit:: Remove startup items for user via Registry
  :key_title: HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\
              Explorer\StartupApproved\Run
  :names:     {ANY}
  :types:     REG_BINARY
  :data:      {DELETE}
  :admin:
  :no_section:
  :no_caption:
  :no_launch:

    .. note::
      Delete entries that should not appear (or can't be removed from startup by
      other means). This applies to the current **user**.

.. _Disable Startup Items:  https://www.tenforums.com/tutorials/2944-add-delete-enable-disable-startup-items-windows-10-a.html