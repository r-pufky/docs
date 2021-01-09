.. _w10-20h2-themes:

Themes
######

.. dropdown:: Remove Recycle Bin from Desktop
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Recycle bin can still be accessed via
  :cmdmenu:`⌘ --> recycle bin --> recycle bin properties`

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    `Reference <https://www.computerhope.com/issues/ch001276.htm>`_

    .. wregedit:: Remove Recycle Bin from Desktop
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion
                  Explorer\Desktop\NameSpace
      :names:     {645FF040-5081-101B-9F08-00AA002F954E}
      :types:     {DELETE}
      :data:      {DELETE}
      :no_section:
      :no_caption:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    `Reference <https://www.pelegit.co.il/remove-recycle-bin-using-group-policy/>`_

    .. wgpolicy:: Remove Recycle Bin from Desktop
      :key_title: User Configuration -->
                  Administrative Templates -->
                  Desktop -->
                  Remove Recycle Bin icon from desktop
      :option:    ☑
      :setting:   Enabled
      :no_section:
      :no_caption:
