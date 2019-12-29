.. _windows-10-disable-telemetry:

Disable Telemetry
#################
These services either do user data tracking, or are an unnecessary performance
hit. See `Telemetry Info`_.

.. warning::
  ``0 - Security`` (the most restrictive option) can only be used in
  enterprise installations. See `diagnostic data levels`_ for information
  transmitted. *Disabling* removes policy and reverts to ``3 - Full``; so the
  most restrictive policy is setup in case telemetry services are re-enabled on
  updates.

.. danger::
  After every major windows update, verify these settings.

Services
********
.. wservice:: Disable Connected User Experiences and Telemetry
  :key_title: Connected User Experiences and Telemetry --> General
  :option:    Service name,
              Startup type,
              Service status
  :setting:   DiagTrack,
              Disabled,
              Stopped
  :no_section:

    .. note::
      Older versions of Windows 10 labeled this ``Diagnostic Tracking Services``
      It is the same service name ``DiagTrack``.

:term:`Registry`
****************
.. wregedit:: Restrict data collection to basic via Registry
  :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\
              DataCollection
  :names:     AllowTelemetry
  :types:     DWORD
  :data:      1
  :no_section:

.. wregedit:: `Disable infection reporting`_. via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\MRT
  :names:     DontReportInfectionInformation
  :types:     DWORD
  :data:      1
  :no_section:
  :no_launch:

:term:`GPO`
***********
.. note::
  The most restrictive :term:`GPO` is applied if both machine and user
  :term:`GPO`'s are set.

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

.. wgpolicy:: Restrict data collection to basic via user GPO
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
  :no_launch:

.. wgpolicy:: Disable application telemetry via machine GPO
  :key_title: User Configuration -->
              Administrative Templates -->
              Windows Components -->
              Application Compatibility -->
              Turn off Application Telemetry
  :option:    ☑
  :setting:   Enabled
  :no_section:
  :no_launch:

.. wgpolicy:: Make Desktop Analytics use Telemetry setting via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Data Collection and Preview Builds -->
              Limit Enhanced diagnostic data to the minimum required by Windows Analytics
  :option:    ☑
  :setting:   Disabled
  :no_section:
  :no_launch:

.. wgpolicy:: Disable sending browser history for Edge via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Data Collection and Preview Builds -->
              Configure collection of browsing data for Microsoft 365 Analytics
  :option:    ☑
  :setting:   Disabled
  :no_section:

.. wgpolicy:: Disable sending browser history for Edge via machine GPO
  :key_title: User Configuration -->
              Administrative Templates -->
              Windows Components -->
              Data Collection and Preview Builds -->
              Configure collection of browsing data for Microsoft 365 Analytics
  :option:    ☑
  :setting:   Disabled
  :no_section:
  :no_launch:

Firewall
********
`Endpoints for telemetry`_ may change. Peridiocally verify these have not
changed. See references for additional documentation.

.. warning::
  These endpoints should be blocked or routed to a blackhole. See
  :ref:`service-pihole` and :ref:`networking-dnat-for-captive-dns`.

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
  :no_launch:

    .. note::
      Microsoft Defender Advanced Threat Protection is country specific and the
      prefix changes by country, e.g.: **de**.vortex-win.data.microsoft.com

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
  :no_launch:

.. rubric:: References

#. `All Windows 10 GPO Settings <https://4sysops.com/archives/windows-10-privacy-all-group-policy-settings/>`_
#. `Configure Windows Diagnostic Data <https://docs.microsoft.com/en-us/windows/privacy/configure-windows-diagnostic-data-in-your-organization>`_
#. `Manage connections from Windows 10 to Microsoft Services <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services>`_
#. `Manage connections from Windows 10 OS components to Microsoft Services <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services>`_

.. _Telemetry Info: https://www.forbes.com/sites/gordonkelly/2015/11/24/windows-10-automatic-spying-begins-again/
.. _diagnostic data levels: https://docs.microsoft.com/en-us/windows/privacy/configure-windows-diagnostic-data-in-your-organization#security-level
.. _Disable infection reporting: https://support.microsoft.com/en-us/help/891716/deploy-windows-malicious-software-removal-tool-in-an-enterprise-enviro
.. _Endpoints for telemetry: https://docs.microsoft.com/en-us/windows/privacy/configure-windows-diagnostic-data-in-your-organization#how-microsoft-handles-diagnostic-data