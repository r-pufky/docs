.. _w10-21h2-security-virus-and-threat-protection-settings:

Virus & threat protection settings
##################################
.. danger::
  As of ``20H2`` `Microsoft Defender can no longer be disabled`_ unless
  antivirus is installed. ``Tamper Protection`` can no longer be disabled.

  After every major windows update, verify these settings.

Windows Defender renamed to *Microsoft Defender* in 20H2. See
:ref:`w10-21h2-standalone-microsoft-defender` for non-GUI Microsoft Defender
settings. :ref:`w10-21h2-standalone-telemetry` for telemetry services.

Real-time protection
********************
.. dropdown:: Disable Real-Time protection
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. warning::
    Only disable if you know what you are doing.

.. gpo::    Disable Real-Time protection
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

Cloud-delivered protection
**************************
.. dropdown:: Disable Cloud-delivered protection
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Previous versions labeled this as 'Microsoft Antimalware Protection Service'
  (MAPS). Uploads files and file hashes to Microsoft for any suspect file.

  .. gpo::    Disable Cloud-delivered protection (MAPS)
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Microsoft Defender Antivirus -->
              MAPS -->
              Join Microsoft MAPS
    :value0:  ☑, {ENABLED}
    :value1:  Join Microsoft MAPS, {DISABLED}
    :ref:     http://windowsbulletin.com/how-to-enable-or-disable-sample-submission-in-windows-defender/
    :update:  2021-02-19
    :generic:
    :open:

Automatic sample submission
***************************
.. dropdown:: Disable Automatic sample submission
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. gpo::    Disable Automatic sample submission
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Microsoft Defender Antivirus -->
              MAPS -->
              Send sample files when further analysis is required
    :value0:  ☑, {ENABLED}
    :value1:  Send sample files when further analysis is required, Never
    :ref:     http://windowsbulletin.com/how-to-enable-or-disable-sample-submission-in-windows-defender/
    :update:  2021-02-19
    :generic:
    :open:

Exclusions
**********
.. dropdown:: Add hosts file exclusion
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  ``20H2+`` always notifies on host file changes, even if they are valid DNS
  blackholes for telemetry. Do *not* add this exclusion if you are not managing
  the host file yourself.

  .. gpo::    Add hosts file exclusion
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Microsoft Defender Antivirus -->
              Exclusions -->
              Path Exclusions
    :value0:  ☑, {ENABLED}
    :value1:  Path Exclusions,
    :value2:  › Value Name, C:\Windows\System32\drivers\etc\hosts
    :value3:  › Value, 0
    :ref:     https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-antivirus/configure-extension-file-exclusions-microsoft-defender-antivirus
    :update:  2021-02-19
    :generic:
    :open:

Notifications
*************
Virus & threat protection notifications
=======================================
.. gpo::    Turn off enhanced notifications
  :path:    Computer Configuration -->
            Administrative Templates -->
            Windows Components -->
            Microsoft Defender Antivirus -->
            Reporting -->
            Turn off enhanced notifications
  :value0:  ☑, {ENABLED}
  :ref:     https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/configure-notifications-microsoft-defender-antivirus?view=o365-worldwide
  :update:  2022-01-20

.. gpo::    Hide notifications
  :path:    Computer Configuration -->
            Administrative Templates -->
            Windows Components -->
            Microsoft Defender Antivirus -->
            Client interface -->
            Suppress all notifications
  :value0:  ☑, {ENABLED}
  :ref:     https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/configure-notifications-microsoft-defender-antivirus?view=o365-worldwide
  :update:  2022-01-20

.. gpo::    Hide reboot notifications
  :path:    Computer Configuration -->
            Administrative Templates -->
            Windows Components -->
            Microsoft Defender Antivirus -->
            Client interface -->
            Suppresses reboot notifications
  :value0:  ☑, {ENABLED}
  :ref:     https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/configure-notifications-microsoft-defender-antivirus?view=o365-worldwide
  :update:  2022-01-20

.. dropdown:: Disable Get informational notifications
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. regedit:: Disable Get informational notifications
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\
               Windows Defender Security Center\Notifications
    :value0:   DisableEnhancedNotifications, {DWORD}, 1
    :update:   2021-02-19
    :generic:
    :open:

.. dropdown:: Disable Recent activity and scan results
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. regedit:: Disable Recent activity and scan results
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\
               Windows Defender Security Center\Virus and threat protection
    :value0:   SummaryNotificationDisabled, {DWORD}, 1
    :update:   2021-02-19
    :generic:
    :open:

.. dropdown:: Disable Threats found but no immediate action is needed
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. regedit:: Disable Threats found but no immediate action is needed
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\
               Windows Defender Security Center\Virus and threat protection
    :value0:   NoActionNotificationDisabled, {DWORD}, 1
    :update:   2021-02-19
    :generic:
    :open:

.. dropdown:: Disable Files or activities are blocked
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. regedit:: Disable Files or activities are blocked
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\
               Windows Defender Security Center\Virus and threat protection
    :value0:   FilesBlockedNotificationDisabled, {DWORD}, 1
    :update:   2021-02-19
    :generic:
    :open:

Get account protection notifications
====================================
.. dropdown:: Disable Get account protection notifications
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. regedit:: Disable Get account protection notifications
    :path:     HKEY_USERS\{SID}\SOFTWARE\Microsoft\
               Windows Defender Security Center\Account protection
    :value0:   DisableNotifications, {DWORD}, 1
    :ref:      https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-antivirus/configure-notifications-microsoft-defender-antivirus
    :update:   2021-02-19
    :generic:
    :open:

.. dropdown:: Disable Problems with Windows Hello
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. regedit:: Disable Problems with Windows Hello
    :path:     HKEY_USERS\{SID}\SOFTWARE\Microsoft\
               Windows Defender Security Center\Account protection
    :value0:   DisableWindowsHelloNotifications, {DWORD}, 1
    :ref:      https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-antivirus/configure-notifications-microsoft-defender-antivirus
    :update:   2021-02-19
    :generic:
    :open:

.. dropdown:: Disable Problems with Dynamic lock
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. regedit:: Disable Problems with Dynamic lock
    :path:     HKEY_USERS\{SID}\SOFTWARE\Microsoft\
               Windows Defender Security Center\Account protection
    :value0:   DisableDynamiclockNotifications, {DWORD}, 1
    :ref:      https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-antivirus/configure-notifications-microsoft-defender-antivirus
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
  :container: + shadow
  :title: bg-info text-white font-weight-bold
  :animate: fade-in

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
.. _Microsoft Defender can no longer be disabled: https://docs.microsoft.com/en-us/windows-hardware/customize/desktop/unattend/security-malware-windows-defender-disableantispyware
