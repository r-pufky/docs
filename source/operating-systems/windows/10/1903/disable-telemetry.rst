.. _w10-1903-disable-telemetry:

Disable Telemetry
#################
These services either do user data tracking, or are an unnecessary performance
hit. See `Telemetry Info`_.

.. danger::
  After every major windows update, verify these settings.

.. dropdown:: Disable Connected User Experiences and Telemetry Service
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Older versions of Windows 10 labeled this ``Diagnostic Tracking Services``. It
  is the same service name ``DiagTrack``.

  .. wservice:: Disable Connected User Experiences and Telemetry
    :key_title: Connected User Experiences and Telemetry --> General
    :option:    Service name,
                Startup type,
                Service status
    :setting:   DiagTrack,
                Disabled,
                Stopped
    :no_section:
    :no_caption:

.. dropdown:: Restrict data collection to Basic 
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Windows 10 collects user data and sends it to Microsoft.

  .. warning::
    ``0 - Security`` (the most restrictive option) can only be used in
    enterprise (AD) installations. See `diagnostic data levels`_ for information
    transmitted. *Disabling* removes policy and reverts to ``3 - Full``; so the
    most restrictive policy is setup in case telemetry services are re-enabled
    on updates.

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
                  Data Collection and Preview Builds -->
                  Allow Telemetry
      :option:    ☑,
                  1
      :setting:   Enabled,
                  Basic
      :no_section:
      :no_caption:

    .. wgpolicy:: Restrict data collection to basic
      :key_title: User Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Data Collection and Preview Builds -->
                  Allow Telemetry
      :option:    ☑,
                  1
      :setting:   Enabled,
                  Basic
      :no_section:
      :no_caption:
      :no_launch:

.. dropdown:: Disable application telemetry 
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Windows 10 collect information on application usage.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Turn off application telemetry
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\AppCompat
      :names:     AITEnable
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

    .. wgpolicy:: Disable application telemetry
      :key_title: User Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Application Compatibility -->
                  Turn off Application Telemetry
      :option:    ☑
      :setting:   Enabled
      :no_section:
      :no_caption:

.. dropdown:: Disable customer experience improvment program 
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Windows 10 devices send hardware and software usage information to Microsoft
  via `customer experience improvement program`_.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Disable `customer experience improvement program`_
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SQMClient\Windows
      :names:     CEIPEnable
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

    .. wgpolicy:: Disable `customer experience improvement program`_
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  System -->
                  Internet Communication Management -->
                  Internet Communication settings -->
                  Turn off Windows Customer Experience Improvement Program
      :option:    ☑
      :setting:   Enabled
      :no_section:
      :no_caption:

.. dropdown:: Disable sending browser history for Edge
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Edge browser automatically reports browser history to Microsoft.

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

    .. wgpolicy:: Disable sending browser history for Edge
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Data Collection and Preview Builds -->
                  Configure collection of browsing data for Microsoft 365 Analytics
      :option:    ☑
      :setting:   Disabled
      :no_section:
      :no_caption:

    .. wgpolicy:: Disable sending browser history for Edge
      :key_title: User Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Data Collection and Preview Builds -->
                  Configure collection of browsing data for Microsoft 365 Analytics
      :option:    ☑
      :setting:   Disabled
      :no_section:
      :no_caption:
      :no_launch:

.. dropdown:: Disable infection reporting
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Windows 10 Malicious Software Removal Tool automatically uploads file metadata
  for infection reporting.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: `Disable infection reporting`_
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\MRT
      :names:     DontReportInfectionInformation
      :types:     DWORD
      :data:      1
      :no_section:
      :no_caption:

.. dropdown:: Disable inventory collector
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Windows 10 Inventory Collector inventories applications, files, devices, and
  drivers on the system and sends the information to Microsoft.
  
  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Disable inventory collector
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\AppCompat
      :names:     DisableInventory
      :types:     DWORD
      :data:      1
      :no_section:
      :no_caption:

.. dropdown:: Disable program compatibility assistant
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  The Program Compatibility Assistant detects known compatibility issues in
  older programs. After you have run an older program in this version of
  Windows, it notifies you if there is a problem and offers to fix it the next
  time you run the program. If the compatibility issue is serious, the Program
  Compatibility Assistant might warn you or block the program from running.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Disable program compatibility assistant
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\AppCompat
      :names:     DisablePCA
      :types:     DWORD
      :data:      1
      :no_section:
      :no_caption:

.. dropdown:: Disable steps recorder
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Steps Recorder automatically capture steps you take on a PC, including a text
  description of what you did and a picture of the screen during each step.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Disable steps recorder
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\AppCompat
      :names:     DisableUAR
      :types:     DWORD
      :data:      1
      :no_section:
      :no_caption:

.. dropdown:: Force desktop analytics to honor telemetry settings
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  `Desktop Analytics`_ will report additional telemetry information if enabled.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Make Desktop Analytics use Telemetry setting
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\DataCollection
      :names:     LimitEnhancedDiagnosticDataWindowsAnalytics
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

    .. wgpolicy:: Make Desktop Analytics use Telemetry setting
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Data Collection and Preview Builds -->
                  Limit Enhanced diagnostic data to the minimum required by Windows Analytics
      :option:    ☑
      :setting:   Disabled
      :no_section:
      :no_caption:

Firewall
********
`Endpoints for telemetry`_ may change. Peridiocally verify these have not
changed. See references for additional documentation.

.. warning::
  These endpoints should be blocked or routed to a blackhole. See
  :ref:`service-pihole` and :ref:`networking-dnat-for-captive-dns`.

.. dropdown:: Connected User Experiences and Telemetry endpoints
  :container: + shadow
  :title: bg-info text-white font-weight-bold
  :animate: fade-in

  Microsoft Defender Advanced Threat Protection is country specific and the
  prefix changes by country, e.g.: **de**.vortex-win.data.microsoft.com

  .. gtable:: Connected User Experiences and Telemetry endpoints
    :header: Release,
             Diagnostic Endpoint,
             Functional Endpoint,
             Settings Endpoint
    :c0:     1703 with 2018-09 cumulative update,
             1803 without 2018-09 cumulative update,
             1709 or earlier
    :c1:     v10c.vortex-win.data.microsoft.com,
             v10.events.data.microsoft.com,
             v10.vortex-win.data.microsoft.com
    :c2:     v20.vortex-win.data.microsoft.com,
             v20.vortex-win.data.microsoft.com,
             v20.vortex-win.data.microsoft.com
    :c3:     settings-win.data.microsoft.com,
             settings-win.data.microsoft.com,
             settings-win.data.microsoft.com
    :no_key_title:
    :no_section:
    :no_caption:
    :no_launch:

.. dropdown:: Diagnostic data services endpoints
  :container: + shadow
  :title: bg-info text-white font-weight-bold
  :animate: fade-in

  .. gtable:: Diagnostic data services
    :header: Service,
             Endpoint
    :c0:     Windows Error Reporting,
             ›,
             ›,
             ›,
             ›,
             ›,
             ›,
             Online Crash Analysis,
             OneDrive app for Windows 10,
             ›,
             Microsoft Defender Advanced Threat Protection,
             ›
    :c1:     watson.telemetry.microsoft.com,
             ceuswatcab01.blob.core.windows.net,
             ceuswatcab02.blob.core.windows.net,
             eaus2watcab01.blob.core.windows.net,
             eaus2watcab02.blob.core.windows.net,
             weus2watcab01.blob.core.windows.net,
             weus2watcab02.blob.core.windows.net,
             oca.telemetry.microsoft.com,
             https://vortex.data.microsoft.com/collect/v1,
             vortex.data.microsoft.com/collect/v1,
             https://wdcp.microsoft.com,
             https://wdcpalt.microsoft.com
    :no_key_title:
    :no_section:
    :no_caption:
    :no_launch:

.. rubric:: References

#. `All Windows 10 GPO Settings <https://4sysops.com/archives/windows-10-privacy-all-group-policy-settings/>`_
#. `Configure Windows Diagnostic Data <https://docs.microsoft.com/en-us/windows/privacy/configure-windows-diagnostic-data-in-your-organization>`_
#. `Manage connections from Windows 10 to Microsoft Services <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services>`_
#. `Manage connections from Windows 10 OS components to Microsoft Services <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services>`_
#. `Application Telemetry <https://getadmx.com/HKLM/Software/Policies/Microsoft/Windows/AppCompat>`_

.. _Telemetry Info: https://www.forbes.com/sites/gordonkelly/2015/11/24/windows-10-automatic-spying-begins-again/
.. _diagnostic data levels: https://docs.microsoft.com/en-us/windows/privacy/configure-windows-diagnostic-data-in-your-organization
.. _Disable infection reporting: https://support.microsoft.com/en-us/help/891716/deploy-windows-malicious-software-removal-tool-in-an-enterprise-enviro
.. _Desktop Analytics: https://admx.help/?Category=Windows_10_2016&Policy=Microsoft.Policies.DataCollection::LimitEnhancedDiagnosticDataWindowsAnalytics
.. _Endpoints for telemetry: https://docs.microsoft.com/en-us/windows/privacy/configure-windows-diagnostic-data-in-your-organization#how-microsoft-handles-diagnostic-data
.. _customer experience improvement program: https://www.windowscentral.com/how-opt-out-customer-experience-improvement-program-windows-10
