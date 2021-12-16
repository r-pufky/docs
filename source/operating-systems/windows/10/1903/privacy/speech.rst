.. _w10-1903-reasonable-privacy-speech:

Speech
######
:cmdmenu:`⌘ + r --> ms-settings:privacy-speech`

.. dropdown:: Online speech recognition
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. gpo::    Disable Online Speech Recognition
    :path:    Computer Configuration -->
              Administrative Templates -->
              Control Panel -->
              Regional and Language value0s -->
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

.. dropdown:: Automatic updates of speech data
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. gpo::    Disable automatic updates of speech data
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Speech -->
              Allow automatic updates of Speech Data
    :value0:  ☑, {DISABLED}
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#bkmk-priv-speech
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable automatic updates of speech data
    :path:     HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Speech
    :value0:   AllowSpeechModelUpdate, {DWORD}, 0
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#bkmk-priv-speech
    :update:   2021-02-19
    :generic:
    :open:
