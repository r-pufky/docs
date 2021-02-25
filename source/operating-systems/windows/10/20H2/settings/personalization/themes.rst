.. _w10-20h2-settings-personalization-themes:

Themes
######
.. gpo::   Remove Recycle Bin from Desktop
  :path:   User Configuration -->
           Administrative Templates -->
           Desktop -->
           Remove Recycle Bin icon from desktop
  :value0: ☑, {ENABLED}
  :ref:    https://www.pelegit.co.il/remove-recycle-bin-using-group-policy/
  :update: 2021-02-19

  Recycle bin can still be accessed via
  :cmdmenu:`⌘ --> recycle bin --> recycle bin properties`

.. regedit:: Remove Recycle Bin from Desktop
  :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion
             Explorer\Desktop\NameSpace
  :value0:   {645FF040-5081-101B-9F08-00AA002F954E}, {DELETE}, {DELETE}
  :ref:      https://www.computerhope.com/issues/ch001276.htm
  :update:   2021-02-19

  This key should be deleted.
