.. _w10-20h2-standalone-spotlight:

Spotlight
#########
Downloads pictures and advertisments to show while computer is locked. Disable
this.

.. danger::
  After every major windows update, verify these settings.

.. dropdown:: Disable all spotlight features
  :color: primary
  :icon: note
  :animate: fade-in
  :class-container: sd-shadow-sm

  .. gpo::    Disable all spotlight features
    :path:    User Configuration -->
              Administrative Templates -->
              Windows Components -->
              Cloud Content -->
              Turn off all Windows spotlight features
    :value0:  ☑, {ENABLED}
    :ref:     https://docs.microsoft.com/en-us/windows/configuration/windows-spotlight
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable all spotlight features
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\CloudContent
    :value0:   DisableWindowsSpotlightFeatures, {DWORD}, 1
    :ref:      https://getadmx.com/?Category=Windows_10_2016&Policy=Microsoft.Policies.CloudContent::DisableWindowsSpotlightFeatures
    :update:   2021-02-19
    :generic:
    :open:

.. dropdown:: Disable third-party content in spotlight
  :color: primary
  :icon: note
  :animate: fade-in
  :class-container: sd-shadow-sm

  .. gpo::    Disable third-party content in spotlight
    :path:    User Configuration -->
              Administrative Templates -->
              Windows Components -->
              Cloud Content -->
              Do not suggest third-party content in Windows spotlight
    :value0:  ☑, {ENABLED}
    :ref:     https://docs.microsoft.com/en-us/windows/configuration/windows-spotlight
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable third-party content in spotlight
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\CloudContent
    :value0:   DisableThirdPartySuggestions, {DWORD}, 1
    :ref:      https://getadmx.com/?Category=Windows_10_2016&Policy=Microsoft.Policies.CloudContent::DisableWindowsSpotlightFeatures
    :update:   2021-02-19
    :generic:
    :open:

.. dropdown:: Disable all spotlight features on lock screen
  :color: primary
  :icon: note
  :animate: fade-in
  :class-container: sd-shadow-sm

  .. gpo::    Disable all spotlight features on lock screen
    :path:    User Configuration -->
              Administrative Templates -->
              Windows Components -->
              Cloud Content -->
              Configure Windows spotlight on lock screen
    :value0:  ☑, {DISABLED}
    :ref:     https://docs.microsoft.com/en-us/windows/configuration/windows-spotlight
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable all spotlight features on lock screen
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\CloudContent
    :value0:   ConfigureWindowsSpotlight, {DWORD}, 2
    :ref:      https://getadmx.com/?Category=Windows_10_2016&Policy=Microsoft.Policies.CloudContent::DisableWindowsSpotlightFeatures
    :update:   2021-02-19
    :generic:
    :open:

.. dropdown:: Disable spotlight action center notifications
  :color: primary
  :icon: note
  :animate: fade-in
  :class-container: sd-shadow-sm

  .. gpo::    Disable spotlight action center notifications
    :path:    User Configuration -->
              Administrative Templates -->
              Windows Components -->
              Cloud Content -->
              Turn off Windows Spotlight on Action Center
    :value0:  ☑, {ENABLED}
    :ref:     https://docs.microsoft.com/en-us/windows/configuration/windows-spotlight
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable spotlight action center notifications
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\CloudContent
    :value0:   DisableWindowsSpotlightOnActionCenter, {DWORD}, 1
    :ref:      https://getadmx.com/?Category=Windows_10_2016&Policy=Microsoft.Policies.CloudContent::DisableWindowsSpotlightFeatures
    :update:   2021-02-19
    :generic:
    :open:

.. dropdown:: Disable spotlight settings notifications
  :color: primary
  :icon: note
  :animate: fade-in
  :class-container: sd-shadow-sm

  .. gpo::    Disable spotlight notifications for settings via user GPO
    :path:    User Configuration -->
              Administrative Templates -->
              Windows Components -->
              Cloud Content -->
              Turn off Windows Spotlight on Settings
    :value0:  ☑, {ENABLED}
    :ref:     https://docs.microsoft.com/en-us/windows/configuration/windows-spotlight
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable spotlight settings notifications
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\CloudContent
    :value0:   DisableWindowsSpotlightOnSettings, {DWORD}, 1
    :ref:      https://getadmx.com/?Category=Windows_10_2016&Policy=Microsoft.Policies.CloudContent::DisableWindowsSpotlightFeatures
    :update:   2021-02-19
    :generic:
    :open:

.. regedit:: Disable spotlight Windows welcome experience
  :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\CloudContent
  :value0:   DisableWindowsSpotlightWindowsWelcomeExperience, {DWORD}, 1
  :ref:      https://getadmx.com/?Category=Windows_10_2016&Policy=Microsoft.Policies.CloudContent::DisableWindowsSpotlightFeatures
  :update:   2021-02-19
  :generic:
  :open:
