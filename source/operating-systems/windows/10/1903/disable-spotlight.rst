.. _w10-1903-disable-spotlight:

Disable Spotlight
#################
Downloads pictures and advertisments to show while computer is locked. Disable
this.

.. danger::
  After every major windows update, verify these settings.

.. dropdown:: Disable all spotlight features
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Disable all spotlight features
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\CloudContent
      :names:     DisableWindowsSpotlightFeatures
      :types:     DWORD
      :data:      1
      :no_section:
      :no_caption:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

    .. wgpolicy:: Disable all spotlight features
      :key_title: User Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Cloud Content -->
                  Turn off all Windows spotlight features
      :option:    ☑
      :setting:   Enabled
      :no_section:
      :no_caption:

.. dropdown:: Disable third-party content in spotlight
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Disable third-party content in spotlight
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\CloudContent
      :names:     DisableThirdPartySuggestions
      :types:     DWORD
      :data:      1
      :no_section:
      :no_caption:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

    .. wgpolicy:: Disable third-party content in spotlight
      :key_title: User Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Cloud Content -->
                  Do not suggest third-party content in Windows spotlight
      :option:    ☑
      :setting:   Enabled
      :no_section:
      :no_caption:

.. dropdown:: Disable diagnostic data for spotlight
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Disable diagnostic data for spotlight
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\CloudContent
      :names:     DisableTailoredExperiencesWithDiagnosticData
      :types:     DWORD
      :data:      1
      :no_section:
      :no_caption:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

    .. wgpolicy:: Disable diagnostic data for spotlight
      :key_title: User Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Cloud Content -->
                  Do not use diagnostic data for tailored experiences
      :option:    ☑
      :setting:   Enabled
      :no_section:
      :no_caption:

.. dropdown:: Disable all spotlight features on lock screen
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Disable all spotlight features on lock screen
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\CloudContent
      :names:     ConfigureWindowsSpotlight
      :types:     DWORD
      :data:      2
      :no_section:
      :no_caption:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

    .. wgpolicy:: Disable all spotlight features on lock screen
      :key_title: User Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Cloud Content -->
                  Configure Windows spotlight on lock screen
      :option:    ☑
      :setting:   Disabled
      :no_section:
      :no_caption:

.. dropdown:: Disable spotlight action center notifications
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Disable spotlight action center notifications
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\CloudContent
      :names:     DisableWindowsSpotlightOnActionCenter
      :types:     DWORD
      :data:      1
      :no_section:
      :no_caption:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

    .. wgpolicy:: Disable spotlight action center notifications
      :key_title: User Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Cloud Content -->
                  Turn off Windows Spotlight on Action Center
      :option:    ☑
      :setting:   Enabled
      :no_section:
      :no_caption:

.. dropdown:: Disable spotlight settings notifications
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Disable spotlight settings notifications
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\CloudContent
      :names:     DisableWindowsSpotlightOnSettings
      :types:     DWORD
      :data:      1
      :no_section:
      :no_caption:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

    .. wgpolicy:: Disable spotlight notifications for settings via user GPO
      :key_title: User Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Cloud Content -->
                  Turn off Windows Spotlight on Settings
      :option:    ☑
      :setting:   Enabled
      :no_section:
      :no_caption:

.. dropdown:: Disable spotlight Windows welcome experience
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Disable spotlight Windows welcome experience
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\CloudContent
      :names:     DisableWindowsSpotlightWindowsWelcomeExperience
      :types:     DWORD
      :data:      1
      :no_section:
      :no_caption:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

    .. wgpolicy:: Disable spotlight Windows welcome experience
      :key_title: User Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Cloud Content -->
                  Turn off the Windows Welcome Experience
      :option:    ☑
      :setting:   Enabled
      :no_section:
      :no_caption:

.. rubric:: References

#. `Manage Windows Spotlight Group Policy <https://docs.microsoft.com/en-us/windows/configuration/windows-spotlight>`_
#. `Manage Windows Spotlight Registry <https://getadmx.com/?Category=Windows_10_2016&Policy=Microsoft.Policies.CloudContent::DisableWindowsSpotlightFeatures>`_
