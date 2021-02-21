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

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Disable apps using voice activation
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  App Privacy -->
                  Let Windows apps activate with voice
      :option:    ☑,
                  Default for all apps
      :setting:   Enabled,
                  Force Deny
      :no_section:
      :no_caption:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    ``0`` enable apps access to voice activation.

    .. wregedit:: Disable apps using voice activation
      :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
      :names:     LetAppsActivateWithVoice
      :types:     DWORD
      :data:      2
      :no_section:
      :no_caption:

  `Reference <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#bkmk-voice-act>`__

Allow apps to use voice activation when this device is locked
*************************************************************
.. dropdown:: Disable Allow apps to use voice activation when this device is locked
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Disable app using voice activation when device locked
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  App Privacy -->
                  Let Windows apps activate with voice while the system is locked
      :option:    ☑,
                  Default for all apps
      :setting:   Enabled,
                  Force Deny
      :no_section:
      :no_caption:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    ``0`` enable apps access to voice activation on lockscreen.

    .. wregedit:: Disable app using voice activation when device locked
      :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\Messaging
      :names:     LetAppsActivateWithVoiceAboveLock
      :types:     DWORD
      :data:      2
      :no_section:
      :no_caption:

  `References <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#bkmk-voice-act>`__

Choose your default app for headset button press
************************************************
.. dropdown:: Disable Choose your default app for headset button press
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    ``1`` enables.

    .. wregedit:: Disable app using voice activation when device locked
      :key_title: HKEY_CURRENT_USER\SOFTWARE\Microsoft\Speech_OneCore\Settings
                  VoiceActivation\UserPreferenceForAllApps
      :names:     AgentActivationLastUsed
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

Choose which apps can use voice activation
******************************************
See :ref:`w10-20h2-settings-privacy-voice-activation`.
