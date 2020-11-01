.. _w10-1903-disable-spotlight:

Disable Spotlight
#################
Downloads pictures and advertisments to show while computer is locked. Disable
this.

.. danger::
  After every major windows update, verify these settings.

:term:`Registry`
****************
.. wregedit:: Disable all spotlight features via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\CloudContent
  :names:     DisableWindowsSpotlightFeatures
  :types:     DWORD
  :data:      1
  :no_section:

.. wregedit:: Disable third-party content in spotlight via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\CloudContent
  :names:     DisableThirdPartySuggestions
  :types:     DWORD
  :data:      1
  :no_section:
  :no_launch:

.. wregedit:: Disable diagnostic data for spotlight via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\CloudContent
  :names:     DisableTailoredExperiencesWithDiagnosticData
  :types:     DWORD
  :data:      1
  :no_section:
  :no_launch:

.. wregedit:: Disable all spotlight features on lock screen via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\CloudContent
  :names:     ConfigureWindowsSpotlight
  :types:     DWORD
  :data:      2
  :no_section:
  :no_launch:

.. wregedit:: Disable action center notifications on spotlight via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\CloudContent
  :names:     DisableWindowsSpotlightOnActionCenter
  :types:     DWORD
  :data:      1
  :no_section:
  :no_launch:

.. wregedit:: Disable spotlight notifications for settings via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\CloudContent
  :names:     DisableWindowsSpotlightOnSettings
  :types:     DWORD
  :data:      1
  :no_section:
  :no_launch:

.. wregedit:: Disable spotlight windows experience via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\CloudContent
  :names:     DisableWindowsSpotlightWindowsWelcomeExperience
  :types:     DWORD
  :data:      1
  :no_section:
  :no_launch:

:term:`GPO`
***********
.. wgpolicy:: Disable all spotlight features via user GPO
  :key_title: User Configuration -->
              Administrative Templates -->
              Windows Components -->
              Cloud Content -->
              Turn off all Windows spotlight features
  :option:    ☑
  :setting:   Enabled
  :no_section:

.. wgpolicy:: Disable third-party content in spotlight via user GPO
  :key_title: User Configuration -->
              Administrative Templates -->
              Windows Components -->
              Cloud Content -->
              Do not suggest third-party content in Windows spotlight
  :option:    ☑
  :setting:   Enabled
  :no_section:
  :no_launch:

.. wgpolicy:: Disable diagnostic data for spotlight via user GPO
  :key_title: User Configuration -->
              Administrative Templates -->
              Windows Components -->
              Cloud Content -->
              Do not use diagnostic data for tailored experiences
  :option:    ☑
  :setting:   Enabled
  :no_section:
  :no_launch:

.. wgpolicy:: Disable all spotlight features on lock screen via user GPO
  :key_title: User Configuration -->
              Administrative Templates -->
              Windows Components -->
              Cloud Content -->
              Configure Windows spotlight on lock screen
  :option:    ☑
  :setting:   Disabled
  :no_section:
  :no_launch:

.. wgpolicy:: Disable action center notifications on spotlight via user GPO
  :key_title: User Configuration -->
              Administrative Templates -->
              Windows Components -->
              Cloud Content -->
              Turn off Windows Spotlight on Action Center
  :option:    ☑
  :setting:   Enabled
  :no_section:
  :no_launch:

.. wgpolicy:: Disable spotlight notifications for settings via user GPO
  :key_title: User Configuration -->
              Administrative Templates -->
              Windows Components -->
              Cloud Content -->
              Turn off Windows Spotlight on Settings
  :option:    ☑
  :setting:   Enabled
  :no_section:
  :no_launch:

.. wgpolicy:: Disable spotlight windows experience via user GPO
  :key_title: User Configuration -->
              Administrative Templates -->
              Windows Components -->
              Cloud Content -->
              Turn off the Windows Welcome Experience
  :option:    ☑
  :setting:   Enabled
  :no_section:
  :no_launch:

.. rubric:: References

#. `Manage Windows Spotlight Group Policy <https://docs.microsoft.com/en-us/windows/configuration/windows-spotlight>`_
#. `Manage Windows Spotlight Registry <https://getadmx.com/?Category=Windows_10_2016&Policy=Microsoft.Policies.CloudContent::DisableWindowsSpotlightFeatures>`_