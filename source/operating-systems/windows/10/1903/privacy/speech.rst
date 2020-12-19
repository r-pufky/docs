.. _w10-1903-reasonable-privacy-speech:

Speech
######
:cmdmenu:`⌘ + r --> ms-settings:privacy-speech`

.. dropdown:: Online speech recognition
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Disable Online Speech Recognition
      :key_title: HKEY_CURRENT_USER\Software\Microsoft\Speech_OneCore\Settings\
                  OnlineSpeechPrivacy
      :names:     HasAccepted
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

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

.. dropdown:: Automatic updates of speech data
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Disable automatic updates of speech data
      :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Speech
      :names:     AllowSpeechModelUpdate
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

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

.. rubric:: Rreferences

#. `Speech Windows Management Settings <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#bkmk-priv-speech>`_
