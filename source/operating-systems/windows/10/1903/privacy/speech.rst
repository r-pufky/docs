.. _w10-1903-reasonable-privacy-speech:

Speech
######
:cmdmenu:`⌘ + r --> ms-settings:privacy-speech`

.. rubric:: Online speech recognition

.. wregedit:: Disable Online Speech Recognition via Registry
  :key_title: HKEY_CURRENT_USER\Software\Microsoft\Speech_OneCore\Settings\
              OnlineSpeechPrivacy
  :names:     HasAccepted
  :types:     DWORD
  :data:      0
  :no_section:

.. wgpolicy:: Disable Online Speech Recognition via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Control Panel -->
              Regional and Language Options -->
              Allow users to enable online speech recognition services
  :option:    ☑
  :setting:   Disabled
  :no_section:

.. rubric:: Automatic updates of speech data

.. note::
  There is no GUI equivalent.

.. wregedit:: Disable automatic updates of speech data via Registry
  :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Speech
  :names:     AllowSpeechModelUpdate
  :types:     DWORD
  :data:      0
  :no_section:

.. wgpolicy:: Disable automatic updates of speech data via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Speech -->
              Allow automatic updates of Speech Data
  :option:    ☑
  :setting:   Disabled
  :no_section:

.. rubric:: Rreferences

#. `Speech Windows Management Settings <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#bkmk-priv-speech>`_