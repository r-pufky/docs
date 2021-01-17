.. _w10-20h2-settings-privacy-diagnostics-and-feedback:

Diagnostics & Feedback
######################
:cmdmenu:`⌘ + r --> ms-settings:privacy-feedback`

Diagnostic data
***************
.. dropdown:: Required Diagnostic data
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Only ``Enterprise`` editions of Windows can disable diagnostic data entirely.
  ``Required`` is the most restricted otherwise. See `diagnostic data levels`_.
  
  .. warning::
    If the option is not set or set incorrectly, it will default to **full**.

  See :ref:`w10-20h2-disable-telemetry` for additional diagnostic data
  & telemetry blocking.

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Required Diagnostic data
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Data Collection and Preview Builds -->
                  Allow Telemetry
      :option:    ☑,
                  1
      :setting:   Enabled,
                  Required
      :no_section:
      :no_caption:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Required Diagnostic data
      :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\
                  DataCollection
      :names:     AllowTelemetry
      :types:     DWORD
      :data:      1
      :no_section:
      :no_caption:

    .. wregedit:: Required Diagnostic data levels
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion
                  Policies\DataCollection
      :names:     AllowTelemetry,
                  MaxTelemetryAllowed
      :types:     DWORD,
                  DWORD
      :data:      1,
                  1
      :no_section:
      :no_caption:
      :no_launch:

    .. wregedit:: Required Diagnostic data notifications
      :key_title: HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion
                  Diagnostics\DiagTrack
      :names:     ShowedToastAtLevel
      :types:     DWORD
      :data:      1
      :no_section:
      :no_caption:
      :no_launch:

  `Reference <https://www.tenforums.com/tutorials/7032-change-diagnostic-data-settings-windows-10-a.html>`__

Improve inking and typing
*************************
.. dropdown:: Disable Improve inking and typing
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Disable sending inking and typing data to Microsoft. Apply
  :ref:`w10-20h2-settings-privacy-ink-and-typing-personalization`.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Disable sending inking and typing for all users
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion
                  Policies\TextInput
      :names:     AllowLinguisticDataCollection
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

    .. wregedit:: Disable sending inking and typing data to Microsoft
      :key_title: HKEY_CURRENT_USER\Software\Microsoft\Input\TIPC
      :names:     Enabled
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:
      :no_launch:

  `Reference <https://www.tenforums.com/tutorials/107050-turn-off-improve-inking-typing-recognition-windows-10-a.html>`__

.. _w10-20h2-settings-privacy-diagnostics-and-feedback-tailored-experiences:

Tailored experiences
********************
.. dropdown:: Disable Tailored experiences
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Disable Microsoft consumer experiences. GPO's are only applied in
  ``Enterprise`` and ``Education`` editions, but should be set regardless.

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Disable Microsoft consumer experiences
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Cloud Content -->
                  Turn off Microsoft consumer experiences
      :option:    ☑
      :setting:   Enabled
      :no_section:
      :no_caption:

    .. wgpolicy:: Disable tailored experiences with diagnostic data
      :key_title: User Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Cloud Content -->
                  Do not use diagnostic data for tailored experiences
      :option:    ☑
      :setting:   Enabled
      :no_section:
      :no_caption:
      :no_launch:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Disable Microsoft consumer experiences
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\
                  CloudContent
      :names:     DisableWindowsConsumerFeatures
      :types:     DWORD
      :data:      1
      :no_section:
      :no_caption:

    .. wregedit:: Disable tailored experiences with diagnostic data
      :key_title: HKEY_CURRENT_USER\SOFTWARE\Policies\Microsoft\Windows
                  CloudContent
      :names:     DisableTailoredExperiencesWithDiagnosticData
      :types:     DWORD
      :data:      1
      :no_section:
      :no_caption:
      :no_launch:

  `Reference <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1816-feedback--diagnostics>`__

View diagnostic data
********************
.. dropdown:: Disable View diagnostic data
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Disable viewing of diagnostic data.

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Disable view diagnostic data
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Data Collection and Preview Builds -->
                  Disable diagnostic data viewer
      :option:    ☑
      :setting:   Enabled
      :no_section:
      :no_caption:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Disable view diagnostic data
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
                  Diagnostics\DiagTrack\EventTranscriptKey
      :names:     EnableEventTranscript
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

  `Reference <https://www.tenforums.com/tutorials/103059-enable-disable-diagnostic-data-viewer-windows-10-a.html>`__

Delete diagnostic data
**********************
.. dropdown:: Enable Delete diagnostic data
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Enable user deletion of diagnostic data.

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Enable deletion of diagnostic data
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Data Collection and Preview Builds -->
                  Disable deleting diagnostic data
      :option:    ☑
      :setting:   Disabled
      :no_section:
      :no_caption:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Enable deletion of diagnostic data
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\
                  DataCollection
      :names:     DisableDeviceDelete
      :types:     DWORD
      :data:      {DELETE}
      :no_section:
      :no_caption:

  `Reference <https://www.tenforums.com/tutorials/118019-enable-disable-delete-diagnostic-data-windows-10-a.html>`__

Feedback frequency
******************
.. dropdown:: Disable Windows should ask for my feedback
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Disable Windows feedback requests.

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Disable Windows asking for feedback
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Data Collection and Preview Builds -->
                  Do not show feedback notifications
      :option:    ☑
      :setting:   Enabled
      :no_section:
      :no_caption:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Disable Windows asking for feedback
      :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\
                  DataCollection
      :names:     DoNotShowFeedbackNotifications
      :types:     DWORD
      :data:      1
      :no_section:
      :no_caption:

    .. wregedit:: Disable Windows asking for feedback second timer
      :key_title: HKEY_CURRENT_USER\Software\Microsoft\Siuf\Rules
      :names:     PeriodInNanoSeconds
      :types:     DWORD
      :data:      {DELETE}
      :no_section:
      :no_caption:
      :no_launch:

    .. wregedit:: Disable Windows asking for feedback period timer
      :key_title: HKEY_CURRENT_USER\Software\Microsoft\Siuf\Rules
      :names:     NumberOfSIUFInPeriod
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:
      :no_launch:

  `Reference <https://www.tenforums.com/tutorials/2441-how-change-feedback-frequency-windows-10-a.html>`__

.. _diagnostic data levels: https://docs.microsoft.com/en-us/windows/privacy/configure-windows-diagnostic-data-in-your-organization
