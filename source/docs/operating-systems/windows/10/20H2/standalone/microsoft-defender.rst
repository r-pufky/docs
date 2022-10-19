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
  :color: primary
  :icon: browser
  :animate: fade-in
  :class-container: sd-shadow-sm

  .. note::
    ``Tamper Protection`` can no longer be disabled (registry settings not
    honored). It must be **disabled manually** before changing Windows Defender
    settings.

  .. gui::    Disable Tamper Protection
    :path:    ⌘ + r -->
              windowsdefender://settings -->
              Virus & threat protection settings -->
              Manage Settings
    :value0:  Tamper Protection, ☐
    :ref:     https://www.tenforums.com/tutorials/123792-turn-off-tamper-protection-microsoft-defender-antivirus.html
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable Tamper Protection
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Microsoft Defender\Features
    :value0:   TamperProtection, {DWORD}, 4
    :value1:   TamperProtectionSource, {DWORD}, 2
    :ref:      https://www.tenforums.com/tutorials/123792-turn-off-tamper-protection-microsoft-defender-antivirus.html
    :update:   2021-02-19
    :generic:
    :open:

    There is no :term:`GPO` for this. ``5`` enables protection.

  .. dropdown:: PS Exec
    :icon: terminal
    :animate: fade-in
    :open:

    .. code-block:: powershell
      :caption: powershell (as admin)

      PsExec64.exe -accepteula -d -i -s powershell -ExecutionPolicy Bypass Set-Itemproperty -path 'HKLM:SOFTWARE\Microsoft\Microsoft Defender\Features' -Name 'TamperProtection' -value 4
      PsExec64.exe -accepteula -d -i -s powershell -ExecutionPolicy Bypass Set-Itemproperty -path 'HKLM:SOFTWARE\Microsoft\Microsoft Defender\Features' -Name 'TamperProtectionSource' -value 2

    Sysinternals PSTools need to be installed disable via powershell.

    `Reference <https://docs.microsoft.com/en-us/sysinternals/downloads/pstools>`__

.. gpo::   Disable Microsoft Defender notifications
  :path:   Computer Configuration -->
           Administrative Templates -->
           Windows Components -->
           Microsoft Defender Antivirus -->
           Client Interface -->
           Suppress all notifications
  :value0: ☑, {ENABLED}
  :ref:    https://admx.help/?Category=Windows_10_2016&Policy=Microsoft.Policies.WindowsDefender::Reporting_DisableEnhancedNotifications
  :update: 2021-02-19

.. dropdown:: Disable Microsoft Defender Enhanced Notifications
  :color: primary
  :icon: note
  :animate: fade-in
  :class-container: sd-shadow-sm

  .. gpo::    Disable Microsoft Defender Enhanced Notifications
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Microsoft Defender Antivirus -->
              Reporting -->
              Turn off enhanced notifications
    :value0:  ☑, {ENABLED}
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable Microsoft Defender Enhanced Notifications
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Microsoft Defender\
               Reporting
    :value0:   DisableEnhancedNotifications, {SZ}, 1
    :update:   2021-02-19
    :generic:
    :open:

.. dropdown:: Disable Microsoft Defender Updates
  :color: primary
  :icon: note
  :animate: fade-in
  :class-container: sd-shadow-sm

  .. gpo::    Stop downloading updates for Microsoft Defender
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Microsoft Defender Antivirus -->
              Security Intelligence Updates
              Allow real-time security intelligence updates based on reports to Microsoft MAPS
    :value0:  ☑, {ENABLED}
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Delete named setting for Microsoft Defender
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\
               Microsoft Defender\Updates
    :value0:   named, {DELETE}, {DELETE}
    :update:   2021-02-19
    :generic:
    :open:

  .. regedit:: Stop downloading updates for Microsoft Defender
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Microsoft Defender\
               Signature Updates
    :value0:   FallbackOrder, {SZ}, FileShares
    :value1:   DefinitionUpdateFileSharesSources, {DELETE}, {DELETE}
    :update:   2021-02-19
    :generic:
    :open:

.. dropdown:: Disable Malicious Software Reporting Tool
  :color: primary
  :icon: note
  :animate: fade-in
  :class-container: sd-shadow-sm

  This reports file information to Microsoft.

  .. gpo::    Disable Malicious Software Reporting Tool
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Microsoft Defender Antivirus -->
              MAPS -->
              Send file samples when further analysis is required
    :value0:  ☑, Never Send
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable Malicious Software Reporting Tool
    :path:     HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\MRT
    :value0:   DontReportInfectionInformation, {DWORD}, 1
    :update:   2021-02-19
    :generic:
    :open:

.. dropdown:: Disable Microsoft Defender Smart Screen
  :color: primary
  :icon: note
  :animate: fade-in
  :class-container: sd-shadow-sm

  .. gpo::    Disable Microsoft Defender Smart Screen for system
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Microsoft Defender SmartScreen -->
              Explorer -->
              Configure Microsoft Defender SmartScreen
    :value0:  ☑, {DISABLED}
    :update:  2021-02-19
    :generic:
    :open:

  .. gpo::    Disable Microsoft Defender Smart Screen Windows store only app
              recommendations
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Microsoft Defender SmartScreen -->
              Explorer -->
              Configure App Install Control
    :value0:  ☑, {ENABLED}
    :value1:  ›, Turn off app recommendations
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable Microsoft Defender Smart Screen Windows store only app
               recommendations
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Microsoft Defender\
               SmartScreen
    :value0:   ConfigureAppInstallControlEnabled, {DWORD}, 1
    :value1:   ConfigureAppInstallControl, {SZ}, Anywhere
    :update:   2021-02-19
    :generic:
    :open:

    Logically inversed from the equivalent GPO.

.. gpo::    Disable Microsoft Defender real-time protection
  :path:    Computer Configuration -->
            Administrative Templates -->
            Windows Components -->
            Microsoft Defender Antivirus -->
            Real-time Protection
  :value0:                                              Turn off real-time protection, {ENABLED}
  :value1:                                                Turn on behavior monitoring, {DISABLED}
  :value2:                                  Scan all downloaded files and attachments, {DISABLED}
  :value3:                         Monitor file and program activity on your computer, {DISABLED}
  :value4:                                     Turn on raw volume write notifications, {DISABLED}
  :value5:          Turn on process scanning whenever real-time protection is enabled, {DISABLED}
  :value6:  Define the maximum size of downloaded files and attachments to be scanned, {DISABLED}
  :value7:           Configure local setting override for turn on behavior monitoring, {DISABLED}
  :value8:  Configure local setting override for scanning all downloaded files and attachments,
            {DISABLED}
  :value9:  Configure local setting override for monitoring file and program activity on your computer,
            {DISABLED}
  :value10:          Configure local setting override to turn on real-time protection, {DISABLED}
  :value11: Configure local setting override for monitoring for incoming and outgoing file activity,
            {DISABLED}
  :value12:  Configure monitoring for incoming and outgoing file and program activity, {DISABLED}
  :update:  2021-02-19

.. dropdown:: Disable windows defender notification icon
  :color: primary
  :icon: note
  :animate: fade-in
  :class-container: sd-shadow-sm

  .. gpo::    Disable windows defender notification icon
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Windows Security -->
              Systray
    :value0:  Hide Windows Security Systray, {ENABLED}
    :ref:     https://appuals.com/how-to-remove-windows-defender-icon-on-windows-10/
    :update:  2021-02-19
    :generic:
    :open:

  .. gui::    Disable windows defender notification icon manager
    :label:   Task Manager
    :nav:     ⌘ --> Task Manager
    :path:    More Details --> Startup
    :value0:  Microsoft Defender notification icon, {DISABLED}
    :ref:     https://appuals.com/how-to-remove-windows-defender-icon-on-windows-10/
    :update:  2021-02-19
    :generic:
    :open:

.. dropdown:: Disable Microsoft Defender
  :color: primary
  :icon: note
  :animate: fade-in
  :class-container: sd-shadow-sm

  As of Windows ``1903`` this setting only disables Microsoft Defender for
  Windows Server. Other settings still apply.

  .. gpo::    Turn off Microsoft Defender
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Microsoft Defender Antivirus -->
              Turn off Microsoft Defender Antivirus
    :value0:  ☑, {ENABLED}
    :ref:     https://docs.microsoft.com/en-us/windows-hardware/customize/desktop/unattend/security-malware-windows-defender-disableantispyware
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable Microsoft Defender
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Microsoft Defender
    :value0:   DisableAntiSpyware, {DWORD}, 1
    :ref:      https://docs.microsoft.com/en-us/windows-hardware/customize/desktop/unattend/security-malware-windows-defender-disableantispyware
    :update:   2021-02-19
    :generic:
    :open:

Firewall
********
`Endpoints for telemetry`_ may change. Peridiocally verify these have not
changed. See references for additional documentation.

.. warning::
  These endpoints should be blocked or routed to a blackhole. See
  :ref:`service-pihole` and :ref:`networking-dnat-for-captive-dns`.

.. dropdown:: Connected User Experiences and Telemetry endpoints
  :color: info
  :icon: table
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
  :icon: table
  :animate: fade-in
  :class-container: sd-shadow-sm

  +-----------------------------------------------+-------------------------------+
  | Service                                       | Endpoint                      |
  +===============================================+===============================+
  | Microsoft Defender Advanced Threat Protection | https://wdcp.microsoft.com    |
  +-----------------------------------------------+-------------------------------+
  | ›                                             | https://wdcpalt.microsoft.com |
  +-----------------------------------------------+-------------------------------+

.. rubric:: References

#. `Configure Windows Diagnostic Data <https://docs.microsoft.com/en-us/windows/privacy/configure-windows-diagnostic-data-in-your-organization>`_
#. `Manage connections from Windows 10 to Microsoft Services <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services>`_
#. `Remove Microsoft Defender Telemetry <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#bkmk-defender>`_

.. _Endpoints for telemetry: https://docs.microsoft.com/en-us/windows/privacy/configure-windows-diagnostic-data-in-your-organization#how-microsoft-handles-diagnostic-data
