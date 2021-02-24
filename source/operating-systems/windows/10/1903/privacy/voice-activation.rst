.. _w10-1903-reasonable-privacy-voice-activation:

Voice Activation
################
:cmdmenu:`⌘ + r --> ms-settings:privacy-voiceactivation`

.. dropdown:: Allow apps to use voice activation
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. gpo::    Disable apps using voice activation
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              App Privacy -->
              Let Windows apps activate with voice
    :value0:  ☑, {ENABLED}
    :value1:  Default for all apps, Force Deny
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#bkmk-voice-act
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable apps using voice activation
    :path:     HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
    :value0:   LetAppsActivateWithVoice, {DWORD}, 2
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#bkmk-voice-act
    :update:   2021-02-19
    :generic:
    :open:

    ``0`` enable apps access to voice activation.

.. dropdown:: Allow apps to use voice activation when this device is locked
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. gpo::    Disable app using voice activation when device locked
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              App Privacy -->
              Let Windows apps activate with voice
    :value0:  ☑, {ENABLED}
    :value1:  Default for all apps, Force Deny
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#bkmk-voice-act
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable app using voice activation when device locked
    :path:     HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\Messaging
    :value0:   LetAppsActivateWithVoiceAboveLock, {DWORD}, 2
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#bkmk-voice-act
    :update:   2021-02-19
    :generic:
    :open:

    ``0`` enable apps access to voice activation on lockscreen.
