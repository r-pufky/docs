.. _w10-20h2-settings-privacy-diagnostics-and-feedback:

Diagnostics & Feedback
######################
:cmdmenu:`⌘ + r --> ms-settings:privacy-feedback`

Diagnostic data
***************
.. dropdown:: Required Diagnostic data
  :color: primary
  :icon: note
  :animate: fade-in
  :class-container: sd-shadow-sm

  Only ``Enterprise`` editions of Windows can disable diagnostic data entirely.
  ``Required`` is the most restricted otherwise. See `diagnostic data levels`_.

  .. warning::
    If the option is not set or set incorrectly, it will default to **full**.

  See :ref:`w10-20h2-standalone-telemetry` for additional diagnostic data
  & telemetry blocking.

  .. gpo::    Required Diagnostic data
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Data Collection and Preview Builds -->
              Allow Telemetry
    :value0:  ☑, {ENABLED}
    :value1:  1, Required
    :ref:     https://www.tenforums.com/tutorials/7032-change-diagnostic-data-settings-windows-10-a.html
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Required Diagnostic data
    :path:     HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\
               DataCollection
    :value0:   AllowTelemetry, {DWORD}, 1
    :ref:      https://www.tenforums.com/tutorials/7032-change-diagnostic-data-settings-windows-10-a.html
    :update:   2021-02-19
    :generic:
    :open:

  .. regedit:: Required Diagnostic data levels
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion
               Policies\DataCollection
    :value0:   AllowTelemetry, {DWORD}, 1
    :value1:   MaxTelemetryAllowed, {DWORD}, 1
    :ref:      https://www.tenforums.com/tutorials/7032-change-diagnostic-data-settings-windows-10-a.html
    :update:   2021-02-19
    :generic:
    :open:

  .. regedit:: Required Diagnostic data notifications
    :path:     HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion
               Diagnostics\DiagTrack
    :value0:   ShowedToastAtLevel, {DWORD}, 1
    :ref:      https://www.tenforums.com/tutorials/7032-change-diagnostic-data-settings-windows-10-a.html
    :update:   2021-02-19
    :generic:
    :open:

Improve inking and typing
*************************
.. dropdown:: Disable Improve inking and typing
  :color: primary
  :icon: stack
  :animate: fade-in
  :class-container: sd-shadow-sm

  Disable sending inking and typing data to Microsoft. Apply
  :ref:`w10-20h2-settings-privacy-ink-and-typing-personalization`.

  .. regedit:: Disable sending inking and typing for all users
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion
               Policies\TextInput
    :value0:   AllowLinguisticDataCollection, {DWORD}, 0
    :ref:      https://www.tenforums.com/tutorials/107050-turn-off-improve-inking-typing-recognition-windows-10-a.html
    :update:   2020-02-19
    :generic:
    :open:

  .. regedit:: Disable sending inking and typing data to Microsoft
    :path:     HKEY_CURRENT_USER\Software\Microsoft\Input\TIPC
    :value0:   Enabled, {DWORD}, 0
    :ref:      https://www.tenforums.com/tutorials/107050-turn-off-improve-inking-typing-recognition-windows-10-a.html
    :update:   2020-02-19
    :generic:
    :open:

.. _w10-20h2-settings-privacy-diagnostics-and-feedback-tailored-experiences:

Tailored experiences
********************
.. dropdown:: Disable Tailored experiences
  :color: primary
  :icon: note
  :animate: fade-in
  :class-container: sd-shadow-sm

  Disable Microsoft consumer experiences. GPO's are only applied in
  ``Enterprise`` and ``Education`` editions, but should be set regardless.

  .. gpo::    Disable Microsoft consumer experiences
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Cloud Content -->
              Turn off Microsoft consumer experiences
    :value0:  ☑, {ENABLED}
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1816-feedback--diagnostics
    :update:  2020-02-19
    :generic:
    :open:

  .. gpo::    Disable tailored experiences with diagnostic data
    :path:    User Configuration -->
              Administrative Templates -->
              Windows Components -->
              Cloud Content -->
              Do not use diagnostic data for tailored experiences
    :value0:  ☑, {ENABLED}
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1816-feedback--diagnostics
    :update:  2020-02-19
    :generic:
    :open:

  .. regedit:: Disable Microsoft consumer experiences
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\
               CloudContent
    :value0:   DisableWindowsConsumerFeatures, {DWORD}, 1
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1816-feedback--diagnostics
    :update:  2020-02-19
    :generic:
    :open:

  .. regedit:: Disable tailored experiences with diagnostic data
    :path:     HKEY_CURRENT_USER\SOFTWARE\Policies\Microsoft\Windows
               CloudContent
    :value0:   DisableTailoredExperiencesWithDiagnosticData, {DWORD}, 1
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1816-feedback--diagnostics
    :update:  2020-02-19
    :generic:
    :open:

View diagnostic data
********************
.. dropdown:: Disable View diagnostic data
  :color: primary
  :icon: note
  :animate: fade-in
  :class-container: sd-shadow-sm

  Disable viewing of diagnostic data.

  .. gpo::    Disable view diagnostic data
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Data Collection and Preview Builds -->
              Disable diagnostic data viewer
    :value0:  ☑, {ENABLED}
    :ref:     https://www.tenforums.com/tutorials/103059-enable-disable-diagnostic-data-viewer-windows-10-a.html
    :update:  2020-02-19
    :generic:
    :open:

  .. regedit:: Disable view diagnostic data
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
               Diagnostics\DiagTrack\EventTranscriptKey
    :value0:   EnableEventTranscript, {DWORD}, 0
    :ref:      https://www.tenforums.com/tutorials/103059-enable-disable-diagnostic-data-viewer-windows-10-a.html
    :update:   2020-02-19
    :generic:
    :open:

Delete diagnostic data
**********************
.. dropdown:: Enable Delete diagnostic data
  :color: primary
  :icon: note
  :animate: fade-in
  :class-container: sd-shadow-sm

  Enable user deletion of diagnostic data.

  .. gpo::    Enable deletion of diagnostic data
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Data Collection and Preview Builds -->
              Disable deleting diagnostic data
    :value0:  ☑, {DISABLED}
    :ref:     https://www.tenforums.com/tutorials/118019-enable-disable-delete-diagnostic-data-windows-10-a.html
    :update:  2020-02-19
    :generic:
    :open:

  .. regedit:: Enable deletion of diagnostic data
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\
               DataCollection
    :value0:   DisableDeviceDelete, {DWORD}, {DELETE}
    :ref:     https://www.tenforums.com/tutorials/118019-enable-disable-delete-diagnostic-data-windows-10-a.html
    :update:  2020-02-19
    :generic:
    :open:

Feedback frequency
******************
.. dropdown:: Disable Windows should ask for my feedback
  :color: primary
  :icon: note
  :animate: fade-in
  :class-container: sd-shadow-sm

  Disable Windows feedback requests.

  .. gpo::    Disable Windows asking for feedback
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Data Collection and Preview Builds -->
              Do not show feedback notifications
    :value0:  ☑, {ENABLED}
    :ref:     https://www.tenforums.com/tutorials/2441-how-change-feedback-frequency-windows-10-a.html
    :update:  2020-02-19
    :generic:
    :open:

  .. regedit:: Disable Windows asking for feedback
    :path:     HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\
               DataCollection
    :value0:   DoNotShowFeedbackNotifications, {DWORD}, 1
    :ref:      https://www.tenforums.com/tutorials/2441-how-change-feedback-frequency-windows-10-a.html
    :update:   2020-02-19
    :generic:
    :open:

  .. regedit:: Disable Windows asking for feedback second timer
    :path:     HKEY_CURRENT_USER\Software\Microsoft\Siuf\Rules
    :value0:   PeriodInNanoSeconds, {DWORD}, {DELETE}
    :value1:   NumberOfSIUFInPeriod, {DWORD}, 0
    :ref:      https://www.tenforums.com/tutorials/2441-how-change-feedback-frequency-windows-10-a.html
    :update:   2020-02-19
    :generic:
    :open:

.. _diagnostic data levels: https://docs.microsoft.com/en-us/windows/privacy/configure-windows-diagnostic-data-in-your-organization
