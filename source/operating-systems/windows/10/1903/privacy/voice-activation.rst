.. _w10-1903-reasonable-privacy-voice-activation:

Voice Activation
################
:cmdmenu:`⌘ + r --> ms-settings:privacy-voiceactivation`

.. rubric:: Allow apps to use voice activation

.. wregedit:: Disable apps using voice activation via Registry
  :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
  :names:     LetAppsActivateWithVoice
  :types:     DWORD
  :data:      2
  :no_section:

.. wgpolicy:: Disable apps using voice activation via machine GPO
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

.. rubric:: Allow apps to use voice activation when this device is locked

.. wregedit:: Disable app using voice activation when device locked via Registry
  :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\Messaging
  :names:     LetAppsActivateWithVoiceAboveLock
  :types:     DWORD
  :data:      2
  :no_section:

.. wgpolicy:: Disable app using voice activation when device locked via machine GPO
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

.. rubric:: Rreferences

#. `Voice Activation Management Settings <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#bkmk-voice-act>`_