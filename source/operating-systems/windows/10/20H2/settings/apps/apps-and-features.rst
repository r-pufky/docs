.. _w10-20h2-settings-apps-apps-and-features:

Apps & features
###############
.. dropdown:: Choose where to get apps
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in
  :open:

  Allow install from anywhere.
    
  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Choose where to get apps
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Windows Defender SmartScreen -->
                  Explorer -->
                  Configure App Install Control
      :option:    ☑,
                  › 
      :setting:   Enabled,
                  Turn off app recommendations
      :no_section:
      :no_caption:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Choose where to get apps
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion
                  Explorer
      :names:     AicEnabled
      :types:     STRING
      :data:      Anywhere
      :no_section:
      :no_caption:

  `Reference <https://www.tenforums.com/tutorials/78213-choose-where-apps-can-installed-windows-10-a.html>`__
