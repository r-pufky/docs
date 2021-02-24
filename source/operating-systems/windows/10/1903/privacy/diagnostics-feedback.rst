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

  .. gpo::    Restrict data collection to basic
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Data Collection and Preview Builds
    :value0:  ☑, {ENABLED}
    :value1:  1, Basic
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Restrict data collection to basic
    :path:     HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\
               DataCollection
    :value0:   AllowTelemetry, {DWORD}, 1
    :update:   2021-02-19
    :generic:
    :open:

.. dropdown:: Improve inking and typing
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Disable sending inking and typing data to Microsoft.

  .. gpo::    Disable sending inking and typing data to Microsoft
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Text Input -->
              Improve inking and typing recognition
    :value0:  ☑, {DISABLED}
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable sending inking and typing data to Microsoft
    :path:     HKEY_CURRENT_USER\Software\Microsoft\Input\TIPC
    :value0:   Enabled, {DWORD}, 0
    :update:  2021-02-19
    :generic:
    :open:

.. dropdown:: Tailored experiences
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Disable Microsoft consumer experiences.

  .. gpo::    Disable Microsoft consumer experiences
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Cloud Content -->
              Turn off Microsoft consumer experiences
    :value0:  ☑, {ENABLED}
    :update:  2021-02-19
    :generic:
    :open:

  .. gpo::    Disable tailored experiences with diagnostic data
    :path:    User Configuration -->
              Administrative Templates -->
              Windows Components -->
              Cloud Content -->
              Do not use diagnostic data for tailored experiences
    :value0:  ☑, {ENABLED}
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable Microsoft consumer experiences
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\
               CloudContent
    :value0:   DisableWindowsConsumerFeatures, {DWORD} 1
    :update:   2021-02-19
    :generic:
    :open:

  .. regedit:: Disable tailored experiences with diagnostic data
    :path:     HKEY_CURRENT_USER\SOFTWARE\Policies\Microsoft\Windows\CloudContent
    :value0:   DisableTailoredExperiencesWithDiagnosticData, {DWORD}, 1
    :update:   2021-02-19
    :generic:
    :open:

.. dropdown:: View diagnostic data
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Disable viewing of diagnostic data.

  .. gpo::    Disable view diagnostic data
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Data Collection and Preview Builds -->
              Disable diagnostic data viewer
    :value0:  ☑, {ENABLED}
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable view diagnostic data
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
               Diagnostics\DiagTrack\EventTranscriptKey
    :value0:   EnableEventTranscript, {DWORD}, 0
    :update:   2021-02-19
    :generic:
    :open:

.. dropdown:: Delete diagnostic data
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. gpo::    Enable deletion of diagnostic data
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Data Collection and Preview Builds -->
              Disable deleting diagnostic data
    :value0:  ☑, {DISABLED}
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Enable deletion of diagnostic data
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\
               DataCollection
    :value0:   DisableDeviceDelete, {DWORD}, {DELETE}
    :update:   2021-02-19
    :generic:
    :open:

.. dropdown:: Feedback frequency
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Disable Windows feedback requests.

  .. gpo::    Disable Windows asking for feedback
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Data Collection and Preview Builds -->
              Do not show feedback notifications
    :value0:  ☑, {ENABLED}
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable Windows asking for feedback
    :path:     HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\
               DataCollection
    :value0:   DoNotShowFeedbackNotifications, {DWORD}, 1
    :update:   2021-02-19
    :generic:
    :open:

  .. regedit:: Disable Windows asking for feedback second timer
    :path:     HKEY_CURRENT_USER\Software\Microsoft\Siuf\Rules
    :value0:   PeriodInNanoSeconds, {DWORD}, 0
    :update:   2021-02-19
    :generic:
    :open:

  .. regedit:: Disable Windows asking for feedback period timer
    :path:     HKEY_CURRENT_USER\Software\Microsoft\Siuf\Rules
    :value0:   NumberOfSIUFInPeriod, {DWORD}, 0
    :update:   2021-02-19
    :generic:
    :open:

.. rubric:: Rreferences

#. `Diagnostics & Feedback Management Settings <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1816-feedback--diagnostics>`_
#. `Disable Diagnostic Data Viewer <https://www.tenforums.com/tutorials/103059-enable-disable-diagnostic-data-viewer-windows-10-a.html>`_
#. `Enable Deletion of Diagnostic Data <https://www.tenforums.com/tutorials/118019-enable-disable-delete-diagnostic-data-windows-10-a.html>`_
