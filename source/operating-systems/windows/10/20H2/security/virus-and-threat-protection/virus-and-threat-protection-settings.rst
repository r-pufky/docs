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

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    Policy must be enabled and set to disable to apply.

    .. wgpolicy:: Disable Cloud-delivered protection (MAPS)
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Microsoft Defender Antivirus -->
                  MAPS -->
                  Join Microsoft MAPS
      :option:    ☑,
                  Join Microsoft MAPS
      :setting:   Enabled,
                  Disabled
      :no_section:
      :no_caption:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Disable Cloud-delivered protection (MAPS)
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\
                  Microsoft Defender\Spynet
      :names:     SpyNetReporting
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

  `Reference <http://windowsbulletin.com/how-to-enable-or-disable-sample-submission-in-windows-defender/>`__

Automatic sample submission
***************************
.. dropdown:: Disable Automatic sample submission
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Disable Automatic sample submission
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Microsoft Defender Antivirus -->
                  MAPS -->
                  Send sample files when further analysis is required
      :option:    ☑,
                  Send sample files when further analysis is required
      :setting:   Enabled,
                  Never
      :no_section:
      :no_caption:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Disable Automatic sample submission
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\
                  Microsoft Defender\Spynet
      :names:     SubmitSamplesConsent
      :types:     DWORD
      :data:      2
      :no_section:
      :no_caption:

  `Reference <http://windowsbulletin.com/how-to-enable-or-disable-sample-submission-in-windows-defender/>`__

Exclusions
**********
.. dropdown:: Add hosts file exclusion
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  ``20H2`` always notifies on host file changes, even if they are valid DNS
  blackholes for telemetry. Do *not* add this exlcusion if you are not managing
  the host file yourself.

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Add hosts file exclusion
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Microsoft Defender Antivirus -->
                  Exclusions -->
                  Path Exclusions
      :option:    ☑,
                  Path Exclusions,
                  › Value Name,
                  › Value
      :setting:   Enabled,
                  ,
                  C:\Windows\System32\drivers\etc\hosts,
                  0
      :no_section:
      :no_caption:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Add hosts file exclusion
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Defender\
                  Exclusions\Paths
      :names:     C:\Windows\System32\drivers\etc\hosts
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

  `Reference <https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-antivirus/configure-extension-file-exclusions-microsoft-defender-antivirus>`__

Notifications
*************
Virus & threat protection notifications
=======================================
.. dropdown:: Disable Get informational notifications
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Disable Get informational notifications
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\
                  Windows Defender Security Center\Notifications
      :names:     DisableEnhancedNotifications
      :types:     DWORD
      :data:      1
      :no_section:
      :no_caption:

.. dropdown:: Disable Recent activity and scan results
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Disable Recent activity and scan results
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\
                  Windows Defender Security Center\Virus and threat protection
      :names:     SummaryNotificationDisabled
      :types:     DWORD
      :data:      1
      :no_section:
      :no_caption:

.. dropdown:: Disable Threats found but no immediate action is needed
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Disable Threats found but no immediate action is needed
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\
                  Windows Defender Security Center\Virus and threat protection
      :names:     NoActionNotificationDisabled
      :types:     DWORD
      :data:      1
      :no_section:
      :no_caption:

.. dropdown:: Disable Files or activities are blocked
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Disable Files or activities are blocked
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\
                  Windows Defender Security Center\Virus and threat protection
      :names:     FilesBlockedNotificationDisabled
      :types:     DWORD
      :data:      1
      :no_section:
      :no_caption:

Get account protection notifications
====================================
.. dropdown:: Disable Get account protection notifications
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Disable Get account protection notifications
      :key_title: HKEY_USERS\{SID}\SOFTWARE\Microsoft\
                  Windows Defender Security Center\Account protection]
      :names:     DisableNotifications
      :types:     DWORD
      :data:      1
      :no_section:
      :no_caption:

.. dropdown:: Disable Problems with Windows Hello
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Disable Problems with Windows Hello
      :key_title: HKEY_USERS\{SID}\SOFTWARE\Microsoft\
                  Windows Defender Security Center\Account protection]
      :names:     DisableWindowsHelloNotifications
      :types:     DWORD
      :data:      1
      :no_section:
      :no_caption:

.. dropdown:: Disable Problems with Dynamic lock
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Disable Problems with Dynamic lock
      :key_title: HKEY_USERS\{SID}\SOFTWARE\Microsoft\
                  Windows Defender Security Center\Account protection]
      :names:     DisableDynamiclockNotifications
      :types:     DWORD
      :data:      1
      :no_section:
      :no_caption:

`Reference <https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-antivirus/configure-notifications-microsoft-defender-antivirus>`__

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
.. _Microsoft Defender can no longer be disabled: https://docs.microsoft.com/en-us/windows-hardware/customize/desktop/unattend/security-malware-windows-defender-disableantispyware
