.. _w10-20h2-settings-privacy-voice-activation:

Voice Activation
################
:cmdmenu:`⌘ + r --> ms-settings:privacy-voiceactivation`

Allow apps to use voice activation
**********************************
.. dropdown:: Disable Allow apps to use voice activation
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

    ``0`` enable apps access to voice activation.

  .. regedit:: Disable apps using voice activation
    :path:     HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
    :value0:   LetAppsActivateWithVoice, {DWORD}, 2
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#bkmk-voice-act
    :update:   2021-02-19
    :generic:
    :open:

Allow apps to use voice activation when this device is locked
*************************************************************
.. dropdown:: Disable Allow apps to use voice activation when this device is locked
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. gpo::    Disable app using voice activation when device locked
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              App Privacy -->
              Let Windows apps activate with voice while the system is locked
    :value0:  ☑, {ENABLED}
    :value1:  Default for all apps, Force Deny
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#bkmk-voice-act
    :update:  2021-02-19
    :generic:
    :open:

    ``0`` enable apps access to voice activation on lockscreen.

  .. regedit:: Disable app using voice activation when device locked
    :path:     HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\Messaging
    :value0:   LetAppsActivateWithVoiceAboveLock, {DWORD}, 2
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#bkmk-voice-act
    :update:   2021-02-19
    :generic:
    :open:

Choose your default app for headset button press
************************************************
.. regedit:: Disable Choose your default app for headset button press
  :path:     HKEY_CURRENT_USER\SOFTWARE\Microsoft\Speech_OneCore\Settings
             VoiceActivation\UserPreferenceForAllApps
  :value0:   AgentActivationLastUsed, {DWORD}, 0
  :update:   2021-02-19

  ``1`` enables.

Choose which apps can use voice activation
******************************************
See :ref:`w10-20h2-settings-privacy-voice-activation`.
