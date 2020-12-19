.. _w10-1903-reasonable-privacy-diagnostics-feedback:

Diagnostics & Feedback
######################
:cmdmenu:`⌘ + r --> ms-settings:privacy-feedback`

.. dropdown:: Diagnostic data
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Only ``Enterprise`` editions of Windows can disable diagnostic data entirely.
  ``Basic`` is the most restricted otherwise.

  See :ref:`w10-1903-disable-telemetry` for additional diagnostic data
  blocking.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Restrict data collection to basic
      :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\
                  DataCollection
      :names:     AllowTelemetry
      :types:     DWORD
      :data:      1
      :no_section:
      :no_caption:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

    .. wgpolicy:: Restrict data collection to basic
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Data Collection and Preview Builds
      :option:    ☑,
                  1
      :setting:   Enabled,
                  Basic
      :no_section:
      :no_caption:

.. dropdown:: Improve inking and typing
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Disable sending inking and typing data to Microsoft.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Disable sending inking and typing data to Microsoft
      :key_title: HKEY_CURRENT_USER\Software\Microsoft\Input\TIPC
      :names:     Enabled
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

    .. wgpolicy:: Disable sending inking and typing data to Microsoft
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Text Input -->
                  Improve inking and typing recognition
      :option:    ☑
      :setting:   Disabled
      :no_section:
      :no_caption:

.. dropdown:: Tailored experiences
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Disable Microsoft consumer experiences.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Disable Microsoft consumer experiences
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\
                  CloudContent
      :names:     DisableWindowsConsumerFeatures
      :types:     DWORD
      :data:      1
      :no_section:
      :no_caption:

    .. wregedit:: Disable tailored experiences with diagnostic data
      :key_title: HKEY_CURRENT_USER\SOFTWARE\Policies\Microsoft\Windows\CloudContent
      :names:     DisableTailoredExperiencesWithDiagnosticData
      :types:     DWORD
      :data:      1
      :no_section:
      :no_caption:
      :no_launch:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

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

.. dropdown:: View diagnostic data
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Disable viewing of diagnostic data.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Disable view diagnostic data
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
                  Diagnostics\DiagTrack\EventTranscriptKey
      :names:     EnableEventTranscript
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

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

.. dropdown:: Delete diagnostic data
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Enable deletion of diagnostic data
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\
                  DataCollection
      :names:     DisableDeviceDelete
      :types:     DWORD
      :data:      {DELETE}
      :no_section:
      :no_caption:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

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

.. dropdown:: Feedback frequency
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Disable Windows feedback requests.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

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
      :data:      0
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

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

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

.. rubric:: Rreferences

#. `Diagnostics & Feedback Management Settings <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1816-feedback--diagnostics>`_
#. `Disable Diagnostic Data Viewer <https://www.tenforums.com/tutorials/103059-enable-disable-diagnostic-data-viewer-windows-10-a.html>`_
#. `Enable Deletion of Diagnostic Data <https://www.tenforums.com/tutorials/118019-enable-disable-delete-diagnostic-data-windows-10-a.html>`_
