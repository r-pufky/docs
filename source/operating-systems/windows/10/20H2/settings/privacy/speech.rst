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

  .. gpo::    Disable Online Speech Recognition
    :path:    Computer Configuration -->
              Administrative Templates -->
              Control Panel -->
              Regional and Language Options -->
              Allow users to enable online speech recognition services
    :value0:  ☑, {DISABLED}
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#bkmk-priv-speech
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable Online Speech Recognition
    :path:     HKEY_CURRENT_USER\Software\Microsoft\Speech_OneCore\Settings\
               OnlineSpeechPrivacy
    :value0:   HasAccepted, {DWORD}, 0
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#bkmk-priv-speech
    :update:   2021-02-19
    :generic:
    :open:
