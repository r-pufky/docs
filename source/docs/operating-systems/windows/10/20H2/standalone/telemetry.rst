.. _w10-20h2-standalone-telemetry:

Telemetry
#########
These services either do user data tracking, or are an unnecessary performance
hit. See `Telemetry Info`_.

.. danger::
  After every major windows update, verify these settings.

.. note::
  As of 20H2, only :term:`GPO`'s are covered, unless the value0 cannot be set or
  enforced via GPO. A reference link is provided to determine the appropriate
  :term:`Registry` value to use.

.. gui::   Disable Connected User Experiences and Telemetry Service
  :label:  Service
  :nav:    ⌘ --> services.msc
  :path:   Connected User Experiences and Telemetry --> General
  :value0:   Service name, DiagTrack
  :value1:   Startup type, {DISABLED}
  :value2: Service status, {STOPPED}
  :ref:    https://docs.microsoft.com/en-us/windows-server/security/windows-services/security-guidelines-for-disabling-system-services-in-windows-server#connected-user-experiences-and-telemetry
  :update: 2021-02-19

  Windows 10 collects user data and sends it to Microsoft.

  See :ref:`w10-20h2-settings-privacy-diagnostics-and-feedback` to restrict data
  collection.

.. gpo::   Disable application telemetry
  :path:   Computer Configuration -->
           Administrative Templates -->
           Windows Components -->
           Application Compatibility -->
           Turn off Application Telemetry
  :value0: ☑, {ENABLED}
  :ref:    https://admx.help/?Category=Windows_10_2016&Policy=Microsoft.Policies.ApplicationCompatibility::AppCompatTurnOffApplicationImpactTelemetry
  :update: 2021-02-19

  Windows 10 collect information on application usage.

.. gpo::   Disable customer experience improvement program
  :path:   Computer Configuration -->
           Administrative Templates -->
           System -->
           Internet Communication Management -->
           Internet Communication settings -->
           Turn off Windows Customer Experience Improvement Program
  :value0: ☑, {ENABLED}
  :ref:    https://admx.help/?Category=Windows_10_2016&Policy=Microsoft.Policies.InternetCommunicationManagement::CEIPEnable,
           https://www.windowscentral.com/how-opt-out-customer-experience-improvement-program-windows-10
  :update: 2021-02-19

  Windows 10 devices send hardware and software usage information to Microsoft
  via customer experience improvement program.

.. dropdown:: Disable sending browser history for Edge
  :color: primary
  :icon: shield-lock
  :animate: fade-in
  :class-container: sd-shadow-sm

  Edge browser automatically reports browser history to Microsoft.

  .. gpo::    Disable sending browser history for Edge
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Data Collection and Preview Builds -->
              Configure collection of browsing data for Desktop Analytics
    :value0:  ☑, {DISABLED}
    :ref:     https://admx.help/?Category=Windows_10_2016&Policy=Microsoft.Policies.MicrosoftEdge::ConfigureTelemetryForMicrosoft365Analytics
    :update:  2021-02-19
    :generic:
    :open:

  .. gpo::    Disable sending browser history for Edge
    :path:    User Configuration -->
              Administrative Templates -->
              Windows Components -->
              Data Collection and Preview Builds -->
              Configure collection of browsing data for Desktop Analytics
    :value0:  ☑, {DISABLED}
    :ref:     https://admx.help/?Category=Windows_10_2016&Policy=Microsoft.Policies.MicrosoftEdge::ConfigureTelemetryForMicrosoft365Analytics
    :update:  2021-02-19
    :generic:
    :open:

.. regedit:: Disable Malicious Software Removal Tool infection reporting
  :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\MRT
  :value0:   DontReportInfectionInformation, {DWORD}, 1
  :ref:      https://support.microsoft.com/en-us/help/891716/deploy-windows-malicious-software-removal-tool-in-an-enterprise-enviro
  :update:   2021-02-19

  Windows 10 Malicious Software Removal Tool automatically uploads file metadata
  for infection reporting.

.. gpo::   Disable inventory collector
  :path:   Computer Configuration -->
           Administrative Templates -->
           Windows Components -->
           Application Compatibility -->
           Turn off Inventory Collector
  :value0: ☑, {ENABLED}
  :ref:    https://admx.help/?Category=Windows_10_2016&Policy=Microsoft.Policies.ApplicationCompatibility::AppCompatTurnOffProgramInventory
  :update: 2021-02-19

  Windows 10 Inventory Collector inventories applications, files, devices, and
  drivers on the system and sends the information to Microsoft.

.. gpo::   Disable program compatibility assistant
  :path:   Computer Configuration -->
           Administrative Templates -->
           Windows Components -->
           Application Compatibility -->
           Turn off Program Compatibility Assistant
  :value0: ☑, {ENABLED}
  :ref:    https://admx.help/?Category=Windows_10_2016&Policy=Microsoft.Policies.ApplicationCompatibility::AppCompatTurnOffProgramCompatibilityAssistant_2
  :update: 2021-02-19

  The Program Compatibility Assistant detects known compatibility issues in
  older programs. After you have run an older program in this version of
  Windows, it notifies you if there is a problem and offers to fix it the next
  time you run the program. If the compatibility issue is serious, the Program
  Compatibility Assistant might warn you or block the program from running.

.. gpo::   Disable steps recorder
  :path:   Computer Configuration -->
           Administrative Templates -->
           Windows Components -->
           Application Compatibility -->
           Turn off Steps Recorder
  :value0: ☑, {ENABLED}
  :ref:    https://admx.help/?Category=Windows_8.1_2012R2&Policy=Microsoft.Policies.ApplicationCompatibility::AppCompatTurnOffUserActionRecord
  :update: 2021-02-19

  Steps Recorder automatically capture steps you take on a PC, including a text
  description of what you did and a picture of the screen during each step.

.. gpo::   Force desktop analytics to honor telemetry settings
  :path:   Computer Configuration -->
           Administrative Templates -->
           Windows Components -->
           Data Collection and Preview Builds -->
           Limit Enhanced diagnostic data to the minimum required by Windows Analytics
  :value0: ☑, {DISABLED}
  :ref:    https://admx.help/?Category=Windows_10_2016&Policy=Microsoft.Policies.DataCollection::LimitEnhancedDiagnosticDataWindowsAnalytics
  :update: 2021-02-19

  Desktop Analytics will report additional telemetry information if enabled.

Firewall
********
`Endpoints for telemetry`_ may change. Peridiocally verify these have not
changed. See references for additional documentation.

.. warning::
  These endpoints should be blocked or routed to a blackhole. See
  :ref:`service-pihole` and :ref:`networking-dnat-for-captive-dns`.

.. dropdown:: Connected User Experiences and Telemetry endpoints
  :color: info
  :icon: shield-lock
  :animate: fade-in
  :class-container: sd-shadow-sm

  Microsoft Defender Advanced Threat Protection is country specific and the
  prefix changes by country, e.g.: **de**.vortex-win.data.microsoft.com

  +----------------------------------------+------------------------------------+-----------------------------------+---------------------------------+
  | Release                                | Diagnostic Endpoint                | Functional Endpoint               | Settings Endpoint               |
  +========================================+====================================+===================================+=================================+
  | 1703 with 2018-09 cumulative update    | v10c.vortex-win.data.microsoft.com | v20.vortex-win.data.microsoft.com | settings-win.data.microsoft.com |
  +----------------------------------------+------------------------------------+-----------------------------------+---------------------------------+
  | 1803 without 2018-09 cumulative update | v10.events.data.microsoft.com      | v20.vortex-win.data.microsoft.com | settings-win.data.microsoft.com |
  +----------------------------------------+------------------------------------+-----------------------------------+---------------------------------+
  | 1709 or earlier                        | v10.vortex-win.data.microsoft.com  | v20.vortex-win.data.microsoft.com | settings-win.data.microsoft.com |
  +----------------------------------------+------------------------------------+-----------------------------------+---------------------------------+

.. dropdown:: Diagnostic data services endpoints
  :color: info
  :icon: shield-lock
  :animate: fade-in
  :class-container: sd-shadow-sm

  +-----------------------------------------------+----------------------------------------------+
  | Service                                       | Endpoint                                     |
  +===============================================+==============================================+
  | Windows Error Reporting                       | watson.telemetry.microsoft.com               |
  +-----------------------------------------------+----------------------------------------------+
  | ›                                             | ceuswatcab01.blob.core.windows.net           |
  +-----------------------------------------------+----------------------------------------------+
  | ›                                             | ceuswatcab02.blob.core.windows.net           |
  +-----------------------------------------------+----------------------------------------------+
  | ›                                             | eaus2watcab01.blob.core.windows.net          |
  +-----------------------------------------------+----------------------------------------------+
  | ›                                             | eaus2watcab02.blob.core.windows.net          |
  +-----------------------------------------------+----------------------------------------------+
  | ›                                             | weus2watcab01.blob.core.windows.net          |
  +-----------------------------------------------+----------------------------------------------+
  | ›                                             | weus2watcab02.blob.core.windows.net          |
  +-----------------------------------------------+----------------------------------------------+
  | Online Crash Analysis                         | oca.telemetry.microsoft.com                  |
  +-----------------------------------------------+----------------------------------------------+
  | OneDrive app for Windows 10                   | https://vortex.data.microsoft.com/collect/v1 |
  +-----------------------------------------------+----------------------------------------------+
  | ›                                             | vortex.data.microsoft.com/collect/v1         |
  +-----------------------------------------------+----------------------------------------------+
  | Microsoft Defender Advanced Threat Protection | https://wdcp.microsoft.com                   |
  +-----------------------------------------------+----------------------------------------------+
  | ›                                             | https://wdcpalt.microsoft.com                |
  +-----------------------------------------------+----------------------------------------------+

.. rubric:: References

#. `All Windows 10 GPO Settings <https://4sysops.com/archives/windows-10-privacy-all-group-policy-settings/>`_
#. `Configure Windows Diagnostic Data <https://docs.microsoft.com/en-us/windows/privacy/configure-windows-diagnostic-data-in-your-organization>`_
#. `Manage connections from Windows 10 to Microsoft Services <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services>`_
#. `Manage connections from Windows 10 OS components to Microsoft Services <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services>`_
#. `Application Telemetry <https://getadmx.com/HKLM/Software/Policies/Microsoft/Windows/AppCompat>`_

.. _Telemetry Info: https://www.forbes.com/sites/gordonkelly/2015/11/24/windows-10-automatic-spying-begins-again/
.. _Endpoints for telemetry: https://docs.microsoft.com/en-us/windows/privacy/configure-windows-diagnostic-data-in-your-organization#how-microsoft-handles-diagnostic-data
