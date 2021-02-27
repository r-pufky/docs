.. _w10-1903-disable-windows-defender:

`Disable Windows Defender`_
###########################
Don't turn this off unless you know what you are doing. You should first disable
all of the options for windows defender before disabling the service, as
cloud-based protection will cause 100% disk usage (in settings).

See :ref:`w10-1903-disable-telemetry` for additional telemetry services.

.. danger::
  After every major windows update, verify these settings.

.. dropdown:: Disable tamper protection
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Windows 1903+ requires ``Tamper Protection`` to be **disabled** before Windows
  Defender can be disabled.

  .. dropdown:: Manual
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. ggui:: Disable Tamper Protection to remove Windows Defender
      :key_title: ⌘ + r -->
                  windowsdefender://settings -->
                  Virus & threat protection settings -->
                  Manage Settings
      :option:    Tamper Protection
      :setting:   ☐
      :no_section:
      :no_caption:
      :no_launch:

  .. regedit:: Disable Tamper Protection
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Defender\Features
    :value0:   TamperProtection, {DWORD}, 0
    :ref:      https://www.tenforums.com/tutorials/123792-turn-off-tamper-protection-microsoft-defender-antivirus.html
    :update:   2021-02-19
    :generic:
    :open:

    There is no :term:`GPO` for this. ``5`` enables protection.

  .. dropdown:: PS Exec
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. code-block:: powershell
      :caption: powershell (as admin)

      PsExec64.exe -accepteula -d -i -s powershell -ExecutionPolicy Bypass Set-Itemproperty -path 'HKLM:SOFTWARE\Microsoft\Windows Defender\Features' -Name 'TamperProtection' -value 0

    Sysinternals `PSTools`_ need to be installed disable via powershell.

.. dropdown:: Disconnect from Microsoft Antimalware Protection Service
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Uploads files and file hashes to Microsoft for any suspect file.

  .. gpo::   Disconnect from Microsoft Antimalware Protection Service
    :path:   Computer Configuration -->
             Administrative Templates -->
             Windows Components -->
             Windows Defender Antivirus -->
             MAPS -->
             Join Microsoft MAPS
    :value0: ☑, {DISABLED}
    :update: 2021-02-19
    :generic:
    :open:

  .. regedit:: Disconnect from Microsoft Antimalware Protection Service
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\
               Spynet
    :value0:   SpyNetReporting, {DWORD}, 0
    :value1:   SubmitSamplesConsent, {DWORD}, 2
    :update:   2021-02-19
    :generic:
    :open:

.. gpo::   Disable Windows Defender notifications
  :path:   Computer Configuration -->
           Administrative Templates -->
           Windows Components -->
           Windows Defender Antivirus -->
           Client Interface -->
           Suppress all notifications
  :value0: ☑, {ENABLED}
  :update: 2021-02-19

.. dropdown:: Disable Windows Defender Enhanced Notifications
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. gpo::   Disable Windows Defender Enhanced Notifications
    :path:   Computer Configuration -->
             Administrative Templates -->
             Windows Components -->
             Windows Defender Antivirus -->
             Reporting -->
             Turn off enhanced notifications
    :value0: ☑, {ENABLED}
    :update: 2021-02-19
    :generic:
    :open:

  .. regedit:: Disable Windows Defender Enhanced Notifications
    :path:      HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\
                Reporting
    :value0:    DisableEnhancedNotifications, {SZ}, 1
    :update:    2021-02-19
    :generic:
    :open:

.. dropdown:: Disable Windows Defender Updates
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. gpo::   Stop downloading updates for Windows Defender
    :path:   Computer Configuration -->
             Administrative Templates -->
             Windows Components -->
             Windows Defender Antivirus -->
             Security Intelligence Updates
             Allow real-time security intelligence updates based on reports to Microsoft MAPS
    :value0: ☑, {ENABLED}
    :update: 2021-02-19
    :generic:
    :open:

  .. regedit:: Delete named setting for Windows Defender
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\
               Updates
    :value0:   named, {DELETE}, {DELETE}
    :update:   2021-02-19
    :generic:
    :open:

  .. regedit:: Stop downloading updates for Windows Defender
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\
               Signature Updates
    :value0:   FallbackOrder, {SZ}, FileShares
    :value1:   DefinitionUpdateFileSharesSources, {DELETE}, {DELETE}
    :update:   2021-02-19
    :generic:
    :open:

.. dropdown:: Disable Malicious Software Reporting Tool
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  This reports file information to Microsoft.

  .. gpo::    Disable Malicious Software Reporting Tool
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Windows Defender Antivirus -->
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

.. dropdown:: Disable Windows Defender Smart Screen
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. gpo::    Disable Windows Defender Smart Screen for system
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Windows Defender SmartScreen -->
              Explorer -->
              Configure Windows Defender SmartScreen
    :value0:  ☑, {DISABLED}
    :update:  2021-02-19
    :generic:
    :open:

  .. gpo::    Disable Windows Defender Smart Screen Windows store only app
              recommendations
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Windows Defender SmartScreen -->
              Explorer -->
              Configure App Install Control
    :value0:  ☑, {ENABLED}
    :value1:  ›, Turn off app recommendations
    :update:  2021-02-19
    :generic:
    :open:

  .. gpo::    Disable Windows Defender Smart Screen for file explorer
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              File Explorer -->
              Configure Windows Defender SmartScreen
    :value0:  ☑, {DISABLED}
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable Windows Defender Smart Screen for system
    :path:     HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\System
    :value0:   EnableSmartScreen, {DWORD}, 0
    :update:   2021-02-19
    :generic:
    :open:

  .. regedit:: Disable Windows Defender Smart Screen Windows store only app
               recommendations
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\
               SmartScreen
    :value0:   ConfigureAppInstallControlEnabled, {DWORD}, 1
    :value1:   ConfigureAppInstallControl, {SZ}, Anywhere
    :update:   2021-02-19
    :generic:
    :open:

    Logically inversed from the equivalent GPO.

.. gpo::    Disable Windows Defender real-time protection
  :path:    Computer Configuration -->
            Administrative Templates -->
            Windows Components -->
            Windows Defender Antivirus -->
            Real-time Protection
  :value0:                                                 Turn off real-time protection, {ENABLED}
  :value1:                                                   Turn on behavior monitoring, {DISABLED}
  :value2:                                     Scan all downloaded files and attachments, {DISABLED}
  :value3:                            Monitor file and program activity on your computer, {DISABLED}
  :value4:                                        Turn on raw volume write notifications, {DISABLED}
  :value5:             Turn on process scanning whenever real-time protection is enabled, {DISABLED}
  :value6:     Define the maximum size of downloaded files and attachments to be scanned, {DISABLED}
  :value7:              Configure local setting override for turn on behavior monitoring, {DISABLED}
  :value8:  Configure local setting override for scanning all downloaded files and attachments,
            {DISABLED}
  :value9:  Configure local setting override for monitoring file and program activity on your computer,
            {DISABLED}
  :value10:             Configure local setting override to turn on real-time protection, {DISABLED}
  :value11: Configure local setting override for monitoring for incoming and outgoing file activity,
            {DISABLED}
  :value12:     Configure monitoring for incoming and outgoing file and program activity, {DISABLED}
  :update:  2021-02-19

.. dropdown:: Disable windows defender notification icon
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

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
    :value0:  Windows Defender notification icon, {DISABLED}
    :ref:     https://appuals.com/how-to-remove-windows-defender-icon-on-windows-10/
    :update:  2021-02-19
    :generic:
    :open:

.. dropdown:: Disable Windows Defender
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  As of Windows ``1903`` this setting only `disables Windows Defender`_ for
  Windows Server. It can only be manually disabled via the GUI. Other settings
  still apply.

  .. gpo::    Turn off Windows Defender
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Windows Defender Antivirus -->
              Turn off Windows Defender Antivirus
    :value0:  ☑, {ENABLED}
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable Windows Defender
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender
    :value0:   DisableAntiSpyware, {DWORD}, 1
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
#. `Remove Windows Defender Telemetry <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#bkmk-defender>`_

.. _Endpoints for telemetry: https://docs.microsoft.com/en-us/windows/privacy/configure-windows-diagnostic-data-in-your-organization#how-microsoft-handles-diagnostic-data
.. _Disable Windows Defender: https://www.tenforums.com/tutorials/5918-how-turn-off-microsoft-defender-antivirus-windows-10-a.html
.. _PSTools: https://docs.microsoft.com/en-us/sysinternals/downloads/pstools
.. _disables Windows Defender: https://docs.microsoft.com/en-us/windows-hardware/customize/desktop/unattend/security-malware-windows-defender-disableantispyware
