.. _windows-10-reasonable-privacy-diagnostics-feedback:

Diagnostics & Feedback
######################
:cmdmenu:`⌘ + r --> ms-settings:privacy-feedback`

.. rubric:: Diagnostic data

.. note::
  Only ``Enterprise`` editions of Windows can disable diagnostic data entirely.
  ``Basic`` is the most restricted otherwise.

  See :ref:`windows-10-disable-telemetry` for additional diagnostic data
  blocking.

.. wregedit:: Restrict data collection to basic via Registry
  :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\
              DataCollection
  :names:     AllowTelemetry
  :types:     DWORD
  :data:      1
  :no_section:

.. wgpolicy:: Restrict data collection to basic via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Data Collection and Preview Builds
  :option:    ☑,
              1
  :setting:   Enabled,
              Basic
  :no_section:

.. rubric:: Improve inking and typing

.. wregedit:: Disable sending inking and typing data to Microsoft via Registry
  :key_title: HKEY_CURRENT_USER\Software\Microsoft\Input\TIPC
  :names:     Enabled
  :types:     DWORD
  :data:      0
  :no_section:

.. wgpolicy:: Disable sending inking and typing data to Microsoft via machine
              GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Text Input -->
              Improve inking and typing recognition
  :option:    ☑
  :setting:   Disabled
  :no_section:

.. rubric:: Tailored experiences

.. wregedit:: Disable Microsoft consumer experiences via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\
              CloudContent
  :names:     DisableWindowsConsumerFeatures
  :types:     DWORD
  :data:      1
  :no_section:

.. wregedit:: Disable tailored experiences with diagnostic data via Registry
  :key_title: HKEY_CURRENT_USER\SOFTWARE\Policies\Microsoft\Windows\CloudContent
  :names:     DisableTailoredExperiencesWithDiagnosticData
  :types:     DWORD
  :data:      1
  :no_section:
  :no_launch:

.. wgpolicy:: Disable Microsoft consumer experiences via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Cloud Content -->
              Turn off Microsoft consumer experiences
  :option:    ☑
  :setting:   Enabled
  :no_section:

.. wgpolicy:: Disable tailored experiences with diagnostic data via machine GPO
  :key_title: User Configuration -->
              Administrative Templates -->
              Windows Components -->
              Cloud Content -->
              Do not use diagnostic data for tailored experiences
  :option:    ☑
  :setting:   Enabled
  :no_section:
  :no_launch:

.. rubric:: View diagnostic data

.. wregedit:: Disable view diagnostic data via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
              Diagnostics\DiagTrack\EventTranscriptKey
  :names:     EnableEventTranscript
  :types:     DWORD
  :data:      0
  :no_section:

.. wgpolicy:: Disable view diagnostic data via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Data Collection and Preview Builds -->
              Disable diagnostic data viewer
  :option:    ☑
  :setting:   Enabled
  :no_section:

.. rubric:: Delete diagnostic data

.. wregedit:: Enable deletion of diagnostic data via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\
              DataCollection
  :names:     DisableDeviceDelete
  :types:     DWORD
  :data:      {DELETE}
  :no_section:

.. wgpolicy:: Enable deletion of diagnostic data via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Data Collection and Preview Builds -->
              Disable deleting diagnostic data
  :option:    ☑
  :setting:   Disabled
  :no_section:

.. rubric:: Feedback frequency

.. wregedit:: Disable Windows asking for feedback via Registry
  :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\
              DataCollection
  :names:     DoNotShowFeedbackNotifications
  :types:     DWORD
  :data:      1
  :no_section:

.. wregedit:: Disable Windows asking for feedback second timer via Registry
  :key_title: HKEY_CURRENT_USER\Software\Microsoft\Siuf\Rules
  :names:     PeriodInNanoSeconds
  :types:     DWORD
  :data:      0
  :no_section:
  :no_launch:

.. wregedit:: Disable Windows asking for feedback period timer via Registry
  :key_title: HKEY_CURRENT_USER\Software\Microsoft\Siuf\Rules
  :names:     NumberOfSIUFInPeriod
  :types:     DWORD
  :data:      0
  :no_section:
  :no_launch:

.. wgpolicy:: Disable Windows asking for feedback via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Data Collection and Preview Builds -->
              Do not show feedback notifications
  :option:    ☑
  :setting:   Enabled
  :no_section:

.. rubric:: Rreferences

#. `Diagnostics & Feedback Management Settings <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1816-feedback--diagnostics>`_
#. `Disable Diagnostic Data Viewer <https://www.tenforums.com/tutorials/103059-enable-disable-diagnostic-data-viewer-windows-10-a.html>`_
#. `Enable Deletion of Diagnostic Data <https://www.tenforums.com/tutorials/118019-enable-disable-delete-diagnostic-data-windows-10-a.html>`_