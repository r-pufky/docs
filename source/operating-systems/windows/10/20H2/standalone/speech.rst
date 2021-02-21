.. _w10-20h2-standalone-privacy-speech:

Speech
######
:cmdmenu:`⌘ + r › ms-settings:privacy-speech`

These speech options are not available in the GUI. See
:ref:`w10-20h2-settings-privacy-speech` for GUI options.

.. dropdown:: Disable Automatic updates of speech data
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in
  :open:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Disable automatic updates of speech data
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Speech -->
                  Allow automatic updates of Speech Data
      :option:    ☑
      :setting:   Disabled
      :no_section:
      :no_caption:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Disable automatic updates of speech data
      :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Speech
      :names:     AllowSpeechModelUpdate
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

  `Reference <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#bkmk-priv-speech>`_
