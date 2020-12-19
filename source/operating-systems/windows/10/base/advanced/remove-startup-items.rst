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

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    Delete entries that should not appear (or can't be removed from startup by
    other means).

    .. wregedit:: Force remove startup items
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
                  Explorer\StartupApproved\Run
      :names:     {ANY}
      :types:     BINARY
      :data:      {DELETE}
      :no_section:
      :no_caption:

    .. wregedit:: Force remove startup items
      :key_title: HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\
                  Explorer\StartupApproved\Run
      :names:     {ANY}
      :types:     REG_BINARY
      :data:      {DELETE}
      :admin:
      :no_section:
      :no_caption:
      :no_launch:

.. _Disable Startup Items:  https://www.tenforums.com/tutorials/2944-add-delete-enable-disable-startup-items-windows-10-a.html
