.. _windows-10-remove-startup-items:

`Remove Startup Items`_
#######################
Force remove items from Task Manager Startup list that cannot be removed in the
GUI; such as Microsoft OneDrive which will leave a setup startup service on
removal.

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