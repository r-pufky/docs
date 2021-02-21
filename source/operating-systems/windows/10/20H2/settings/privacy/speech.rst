.. _w10-20h2-settings-privacy-speech:

Speech
######
:cmdmenu:`⌘ + r --> ms-settings:privacy-speech`

Online speech recognition
*************************
.. dropdown:: Disable Online speech recognition
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in
  :open:
 
  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Disable Online Speech Recognition
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Control Panel -->
                  Regional and Language Options -->
                  Allow users to enable online speech recognition services
      :option:    ☑
      :setting:   Disabled
      :no_section:
      :no_caption:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Disable Online Speech Recognition
      :key_title: HKEY_CURRENT_USER\Software\Microsoft\Speech_OneCore\Settings\
                  OnlineSpeechPrivacy
      :names:     HasAccepted
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

  `Reference <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#bkmk-priv-speech>`__
