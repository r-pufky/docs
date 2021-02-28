.. _w10-20h2-security-virus-and-threat-protection-settings:

Virus & threat protection settings
##################################
.. danger::
  As of ``20H2`` `Microsoft Defender can no longer be disabled`_ unless
  antivirus is installed. ``Tamper Protection`` can no longer be disabled.
  
  After every major windows update, verify these settings.

Windows Defender renamed to *Microsoft Defender* in 20H2. See 
:ref:`w10-20h2-standalone-microsoft-defender` for non-GUI Microsoft Defender
settings. :ref:`w10-20h2-standalone-telemetry` for telemetry services.

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

    Policy must be enabled and set to disable to apply.

  .. regedit:: Disable Cloud-delivered protection (MAPS)
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\
               Microsoft Defender\Spynet
    :value0:   SpyNetReporting, {DWORD}, 0
    :ref:      http://windowsbulletin.com/how-to-enable-or-disable-sample-submission-in-windows-defender/
    :update:   2021-02-19
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

  .. regedit:: Disable Automatic sample submission
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\
               Microsoft Defender\Spynet
    :value0:   SubmitSamplesConsent, {DWORD}, 2
    :ref:      http://windowsbulletin.com/how-to-enable-or-disable-sample-submission-in-windows-defender/
    :update:   2021-02-19
    :generic:
    :open:

Exclusions
**********
.. dropdown:: Add hosts file exclusion
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  ``20H2`` always notifies on host file changes, even if they are valid DNS
  blackholes for telemetry. Do *not* add this exlcusion if you are not managing
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

  .. regedit:: Add hosts file exclusion
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Defender\
               Exclusions\Paths
    :value0:   C:\Windows\System32\drivers\etc\hosts, {DWORD}, 0
    :ref:      https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-antivirus/configure-extension-file-exclusions-microsoft-defender-antivirus
    :update:   2021-02-19
    :generic:
    :open:

Notifications
*************
Virus & threat protection notifications
=======================================
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
               Windows Defender Security Center\Account protection]
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
