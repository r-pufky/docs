.. _windows-10-disable-defender:

`Disable Windows Defender`_
###########################
Don't turn this off unless you know what you are doing. You should first disable
all of the options for windows defender before disabling the service, as
cloud-based protection will cause 100% disk usage (in settings).

See :ref:`windows-10-disable-telemetry` for additional telemetry services.

.. danger::
  After every major windows update, verify these settings.

.. warning::
  Windows 1903+ may require ``Tamper Protection`` to be **disabled** before
  Windows Defender can be disabled.

    .. ggui:: Disable Tamper Protection to remove Windows Defender
      :key_title: ⌘ + r -->
                  windowsdefender: -->
                  Virus & threat protection -->
                  Manage Settings
      :option:    Tamper Protection
      :setting:   ☐
      :no_section:
      :no_launch:

:term:`Registry`
****************
.. wregedit:: Disconnect from Microsoft Antimalware Protection Service and
              disable sending files to Microsoft via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\
              Spynet
  :names:     SpyNetReporting,
              SubmitSamplesConsent
  :types:     DWORD,
              DWORD
  :data:      0,
              2
  :no_section:

.. wregedit:: Delete named setting for Windows Defender via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\
              Updates
  :names:     named
  :types:     DELETE
  :data:      DELETE
  :no_section:
  :no_launch:

.. wregedit:: Stop downloading updates for Windows Defender via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\
              Signature Updates
  :names:     FallbackOrder,
              DefinitionUpdateFileSharesSources
  :types:     SZ,
              DELETE
  :data:      FileShares,
              DELETE
  :no_section:
  :no_launch:

.. wregedit:: Disable Malicious Software Reporting Tool via Registry
  :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\MRT
  :names:     DontReportInfectionInformation
  :types:     DWORD
  :data:      1
  :no_section:
  :no_launch:

    .. attention::
      This can **only** be set via the Registry.

.. wregedit:: Disable Windows Defender Enhanced Notifications via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\
              Reporting
  :names:     DisableEnhancedNotifications
  :types:     SZ
  :data:      1
  :no_section:
  :no_launch:

.. wregedit:: Disable Windows Defender Smart Screen for system via Registry
  :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\System
  :names:     EnableSmartScreen
  :types:     DWORD
  :data:      0
  :no_section:
  :no_launch:

.. wregedit:: Disable Windows store only app recommendations via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\
              SmartScreen
  :names:     ConfigureAppInstallControlEnabled,
              ConfigureAppInstallControl
  :types:     DWORD,
              SZ
  :data:      1,
              Anywhere
  :no_section:
  :no_launch:

     .. note::
       Logically inversed from the equivalent GPO.

.. wregedit:: Disable Windows Defender via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender
  :names:     DisableAntiSpyware
  :types:     DWORD
  :data:      1
  :no_section:
  :no_launch:

:term:`GPO`
***********
.. wgpolicy:: Disconnect from Microsoft Antimalware Protection Service via
              machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Windows Defender Antivirus -->
              MAPS -->
              Join Microsoft MAPS
  :option:    ☑
  :setting:   Disabled
  :no_section:

.. wgpolicy:: Disable sending files to Microsoft via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Windows Defender Antivirus -->
              MAPS -->
              Send file samples when further analysis is required
  :option:    ☑
  :setting:   Never Send
  :no_section:
  :no_launch:

.. wgpolicy:: Disable Windows Defender Enhanced Notifications via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Windows Defender Antivirus -->
              Reporting -->
              Turn off enhanced notifications
  :option:    ☑
  :setting:   Enabled
  :no_section:
  :no_launch:

.. wgpolicy:: Disable Windows Defender Smart Screen for system via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Windows Defender SmartScreen -->
              Explorer -->
              Configure Windows Defender SmartScreen
  :option:    ☑
  :setting:   Disabled
  :no_section:
  :no_launch:

.. wgpolicy:: Disable Windows Defender Smart Screen Windows store only app
              recommendations via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Windows Defender SmartScreen -->
              Explorer -->
              Configure App Install Control
  :option:    ☑,
              ›
  :setting:   Enabled,
              Turn off app recommendations
  :no_section:
  :no_launch:

.. wgpolicy:: Disable Windows Defender Smart Screen for file explorer via
              machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              File Explorer -->
              Configure Windows Defender SmartScreen
  :option:    ☑
  :setting:   Disabled
  :no_section:
  :no_launch:

.. wgpolicy:: Turn off Windows Defender via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Windows Defender Antivirus -->
              Turn off Windows Defender Antivirus
  :option:    ☑
  :setting:   Enabled
  :no_section:
  :no_caption:

.. wgpolicy:: Disable Windows Defender real-time protection via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Windows Defender Antivirus -->
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
  :no_launch:

.. wgpolicy:: Disable Windows Defender notifications via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Windows Defender Antivirus -->
              Client Interface -->
              Suppress all notifications
  :option:    ☑
  :setting:   Enabled
  :no_section:
  :no_caption:
  :no_launch:

.. wgpolicy:: Disable windows defender notification icon via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Windows Security -->
              Systray
  :option:    Hide Windows Security Systray
  :setting:   Enabled
  :no_section:
  :no_caption:
  :no_launch:

  .. note::
    See `disabling windows defender icon`_.

    .. wtmanager:: Disable windows defender notification icon manager
      :key_title:  More Details --> Startup
      :option:     Windows Defender notification icon
      :setting:    Disabled
      :no_section:
      :no_caption:

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
  :c0:     Microsoft Defender Advanced Threat Protection,
           ›
  :c1:     https://wdcp.microsoft.com,
           https://wdcpalt.microsoft.com
  :no_key_title:
  :no_section:
  :no_launch:

.. rubric:: References

#. `Configure Windows Diagnostic Data <https://docs.microsoft.com/en-us/windows/privacy/configure-windows-diagnostic-data-in-your-organization>`_
#. `Manage connections from Windows 10 to Microsoft Services <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services>`_
#. `Remove Windows Defender Telemetry <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#bkmk-defender>`_

.. _Endpoints for telemetry: https://docs.microsoft.com/en-us/windows/privacy/configure-windows-diagnostic-data-in-your-organization#how-microsoft-handles-diagnostic-data
.. _Disable Windows Defender: https://www.tenforums.com/tutorials/5918-turn-off-windows-defender-antivirus-windows-10-a.html
.. _disabling windows defender icon: https://appuals.com/how-to-remove-windows-defender-icon-on-windows-10/