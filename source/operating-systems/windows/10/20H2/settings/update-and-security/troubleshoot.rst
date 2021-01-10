.. _w10-20h2-troubleshoot:

Troubleshoot
############
.. dropdown:: Don't run any troubleshooters
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in
  
  Data uploading is turned off so this won't work anyways.

  `Reference <https://www.tenforums.com/tutorials/113553-turn-off-automatic-recommended-troubleshooting-windows-10-a.html>`_
    
  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Don't run any troubleshooters
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WindowsMitigation
      :names:     UserPreference
      :types:     DWORD
      :data:      1
      :no_section:
      :no_caption:
