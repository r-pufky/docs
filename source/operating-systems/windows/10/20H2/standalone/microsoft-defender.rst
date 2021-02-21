.. _w10-20h2-standalone-microsoft-defender:

Microsoft Defender
##################
Don't turn this off unless you know what you are doing. You should first disable
all of the options for windows defender before disabling the service, as
cloud-based protection will cause 100% disk usage (in settings).

See :ref:`w10-20h2-security-virus-and-threat-protection-settings` for Windows
Defender GUI settings. ref:`w10-20h2-standalone-telemetry` for telemetry
services.

.. danger::
  As of ``20H2`` Microsoft Defender can no longer be disabled; it will only
  disable on detection of other certified antivirus software. Disable all live
  scanning services instead.

  After every major windows update, verify these settings.

  `Reference <https://www.tenforums.com/tutorials/5918-how-turn-off-microsoft-defender-antivirus-windows-10-a.html>`__
  `Reference <https://docs.microsoft.com/en-us/windows-hardware/customize/desktop/unattend/security-malware-windows-defender-disableantispyware>`__

.. dropdown:: Disable tamper protection
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. note::
    ``Tamper Protection`` can no longer be disabled (registry settings not
    honored). It must be **disabled manually** before changing Windows Defender
    settings.

  .. dropdown:: Manual
    :title: font-weight-bold
    :animate: fade-in

    .. ggui:: Disable Tamper Protection
      :key_title: ⌘ + r -->
                  windowsdefender://settings -->
                  Virus & threat protection settings -->
                  Manage Settings
      :option:    Tamper Protection
      :setting:   ☐
      :no_section:
      :no_caption:
      :no_launch:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    There is no :term:`GPO` for this. ``5`` enables protection.

    .. wregedit:: Disable Tamper Protection
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Microsoft Defender\Features
      :names:     TamperProtection,
                  TamperProtectionSource
      :types:     DWORD,
                  DWORD
      :data:      4,
                  2
      :no_section:
      :no_caption:

  .. dropdown:: PS Exec
    :title: font-weight-bold
    :animate: fade-in

    .. code-block:: powershell
      :caption: powershell (as admin)

      PsExec64.exe -accepteula -d -i -s powershell -ExecutionPolicy Bypass Set-Itemproperty -path 'HKLM:SOFTWARE\Microsoft\Microsoft Defender\Features' -Name 'TamperProtection' -value 4
      PsExec64.exe -accepteula -d -i -s powershell -ExecutionPolicy Bypass Set-Itemproperty -path 'HKLM:SOFTWARE\Microsoft\Microsoft Defender\Features' -Name 'TamperProtectionSource' -value 2

    Sysinternals PSTools need to be installed disable via powershell.

    `Reference <https://www.tenforums.com/tutorials/123792-turn-off-tamper-protection-microsoft-defender-antivirus.html>`__

    .. wregedit:: Disable Cloud-delivered protection (MAPS)
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\
                  Microsoft Defender\Updates
      :names:     named
      :types:     {DELETE}
      :data:      {DELETE}
      :no_section:
      :no_caption:
      :no_launch:

  `Reference <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services>`__
  `Reference <https://docs.microsoft.com/en-us/sysinternals/downloads/pstools>`__

.. dropdown:: Disable Microsoft Defender notifications
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Disable Microsoft Defender notifications
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Microsoft Defender Antivirus -->
                  Client Interface -->
                  Suppress all notifications
      :option:    ☑
      :setting:   Enabled
      :no_section:
      :no_caption:

  `Reference <https://admx.help/?Category=Windows_10_2016&Policy=Microsoft.Policies.WindowsDefender::Reporting_DisableEnhancedNotifications>`__

.. dropdown:: Disable Microsoft Defender Enhanced Notifications
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Disable Microsoft Defender Enhanced Notifications
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Microsoft Defender\
                  Reporting
      :names:     DisableEnhancedNotifications
      :types:     SZ
      :data:      1
      :no_section:
      :no_caption:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

    .. wgpolicy:: Disable Microsoft Defender Enhanced Notifications
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Microsoft Defender Antivirus -->
                  Reporting -->
                  Turn off enhanced notifications
      :option:    ☑
      :setting:   Enabled
      :no_section:
      :no_caption:

.. dropdown:: Disable Microsoft Defender Updates
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Delete named setting for Microsoft Defender
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Microsoft Defender\
                  Updates
      :names:     named
      :types:     {DELETE}
      :data:      {DELETE}
      :no_section:
      :no_caption:

    .. wregedit:: Stop downloading updates for Microsoft Defender
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Microsoft Defender\
                  Signature Updates
      :names:     FallbackOrder,
                  DefinitionUpdateFileSharesSources
      :types:     SZ,
                  {DELETE}
      :data:      FileShares,
                  {DELETE}
      :no_section:
      :no_caption:
      :no_launch:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

    .. wgpolicy:: Stop downloading updates for Microsoft Defender
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Microsoft Defender Antivirus -->
                  Security Intelligence Updates
                  Allow real-time security intelligence updates based on reports to Microsoft MAPS
      :option:    ☑
      :setting:   Enabled
      :no_section:
      :no_caption:

.. dropdown:: Disable Malicious Software Reporting Tool
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  This reports file information to Microsoft.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Disable Malicious Software Reporting Tool
      :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\MRT
      :names:     DontReportInfectionInformation
      :types:     DWORD
      :data:      1
      :no_section:
      :no_caption:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

    .. wgpolicy:: Disable Malicious Software Reporting Tool
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Microsoft Defender Antivirus -->
                  MAPS -->
                  Send file samples when further analysis is required
      :option:    ☑
      :setting:   Never Send
      :no_section:
      :no_caption:

.. dropdown:: Disable Microsoft Defender Smart Screen
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Disable Microsoft Defender Smart Screen Windows store only app
                  recommendations
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Microsoft Defender\
                  SmartScreen
      :names:     ConfigureAppInstallControlEnabled,
                  ConfigureAppInstallControl
      :types:     DWORD,
                  SZ
      :data:      1,
                  Anywhere
      :no_section:
      :no_caption:
      :no_launch:

        .. note::
          Logically inversed from the equivalent GPO.

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

    .. wgpolicy:: Disable Microsoft Defender Smart Screen for system
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Microsoft Defender SmartScreen -->
                  Explorer -->
                  Configure Microsoft Defender SmartScreen
      :option:    ☑
      :setting:   Disabled
      :no_section:
      :no_caption:

    .. wgpolicy:: Disable Microsoft Defender Smart Screen Windows store only app
                  recommendations
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Microsoft Defender SmartScreen -->
                  Explorer -->
                  Configure App Install Control
      :option:    ☑,
                  ›
      :setting:   Enabled,
                  Turn off app recommendations
      :no_section:
      :no_caption:
      :no_launch:

.. dropdown:: Disable Microsoft Defender real-time protection
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

    .. wgpolicy:: Disable Microsoft Defender real-time protection
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Microsoft Defender Antivirus -->
                  Real-time Protection
      :option:    Turn off real-time protection,
                  Turn on behavior monitoring,
                  Scan all downloaded files and attachments,
                  Monitor file and program activity on your computer,
                  Turn on raw volume write notifications,
                  Turn on process scanning whenever real-time protection is enabled,
                  Define the maximum size of downloaded files and attachments to be scanned,
                  Configure local setting override for turn on behavior monitoring,
                  Configure local setting override for scanning all downloaded files and attachments,
                  Configure local setting override for monitoring file and program activity on your computer,
                  Configure local setting override to turn on real-time protection,
                  Configure local setting override for monitoring for incoming and outgoing file activity,
                  Configure monitoring for incoming and outgoing file and program activity
      :setting:   Enabled,
                  Disabled,
                  Disabled,
                  Disabled,
                  Disabled,
                  Disabled,
                  Disabled,
                  Disabled,
                  Disabled,
                  Disabled,
                  Disabled,
                  Disabled,
                  Disabled
      :no_section:
      :no_caption:

.. dropdown:: Disable windows defender notification icon
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

    .. wgpolicy:: Disable windows defender notification icon
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Windows Security -->
                  Systray
      :option:    Hide Windows Security Systray
      :setting:   Enabled
      :no_section:
      :no_caption:

  .. dropdown:: Scheduled Tasks
    :title: font-weight-bold
    :animate: fade-in

    .. wtmanager:: Disable windows defender notification icon manager
      :key_title:  More Details --> Startup
      :option:     Microsoft Defender notification icon
      :setting:    Disabled
      :no_section:
      :no_caption:

  `Reference <https://appuals.com/how-to-remove-windows-defender-icon-on-windows-10/>`__

.. dropdown:: Disable Microsoft Defender
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  As of Windows ``1903`` this setting only disables Microsoft Defender for
  Windows Server. Other settings still apply.

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

    .. wgpolicy:: Turn off Microsoft Defender
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Microsoft Defender Antivirus -->
                  Turn off Microsoft Defender Antivirus
      :option:    ☑
      :setting:   Enabled
      :no_section:
      :no_caption:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Disable Microsoft Defender
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Microsoft Defender
      :names:     DisableAntiSpyware
      :types:     DWORD
      :data:      1
      :no_section:
      :no_caption:

  `Reference <https://docs.microsoft.com/en-us/windows-hardware/customize/desktop/unattend/security-malware-windows-defender-disableantispyware>`__

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
    :c0:     Microsoft Defender Advanced Threat Protection,
             ›
    :c1:     https://wdcp.microsoft.com,
             https://wdcpalt.microsoft.com
    :no_key_title:
    :no_section:
    :no_caption:
    :no_launch:

.. rubric:: References

#. `Configure Windows Diagnostic Data <https://docs.microsoft.com/en-us/windows/privacy/configure-windows-diagnostic-data-in-your-organization>`_
#. `Manage connections from Windows 10 to Microsoft Services <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services>`_
#. `Remove Microsoft Defender Telemetry <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#bkmk-defender>`_

.. _Endpoints for telemetry: https://docs.microsoft.com/en-us/windows/privacy/configure-windows-diagnostic-data-in-your-organization#how-microsoft-handles-diagnostic-data
