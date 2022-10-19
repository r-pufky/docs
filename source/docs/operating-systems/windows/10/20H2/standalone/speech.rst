.. _w10-20h2-standalone-privacy-speech:

Speech
######
:cmdmenu:`⌘ + r › ms-settings:privacy-speech`

These speech value0s are not available in the GUI. See
:ref:`w10-20h2-settings-privacy-speech` for GUI value0s.

.. dropdown:: Disable Automatic updates of speech data
  :color: primary
  :icon: note
  :animate: fade-in
  :class-container: sd-shadow-sm
  :open:

  .. gpo::   Disable automatic updates of speech data
    :path:   Computer Configuration -->
             Administrative Templates -->
             Windows Components -->
             Speech -->
             Allow automatic updates of Speech Data
    :value0: ☑, {DISABLED}
    :ref:    https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#bkmk-priv-speech
    :update: 2021-02-19
    :generic:
    :open:

  .. regedit:: Disable automatic updates of speech data
    :path: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Speech
    :value0:     AllowSpeechModelUpdate, {DWORD}, 0
    :ref:    https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#bkmk-priv-speech
    :update: 2021-02-19
    :generic:
    :open:
