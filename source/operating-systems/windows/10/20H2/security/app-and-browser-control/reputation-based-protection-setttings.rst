.. _w10-20h2-security-reputation-based-protection-settings:

Reputation-based protection settings
####################################
Check apps and files
*********************
.. dropdown:: Disable Check apps and files
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    Policy must be enabled and set to disable to apply.

    .. wgpolicy:: Disable Check apps and files
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  File Explorer -->
                  Configure Windows Defender SmartScreen
      :option:    ☑
      :setting:   Disabled
      :no_section:
      :no_caption:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Disable Check apps and files
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
                  Explorer
      :names:     SmartScreenEnabled
      :types:     SZ
      :data:      Off
      :no_section:
      :no_caption:

    .. wregedit:: Disable Check apps and files
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\System
      :names:     EnableSmartScreen
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:
      :no_launch:

  `Reference <https://www.tenforums.com/tutorials/5593-turn-off-smartscreen-apps-files-web-windows-10-a.html>`__

SmartScreen for Microsoft Edge
******************************
Edge will eventually be removed; until then, leave enabled for Edge browser.

`Reference <https://www.tenforums.com/tutorials/5520-turn-off-smartscreen-microsoft-edge-windows-10-a.html>`__

Potentially unwanted app blocking
*********************************
.. dropdown:: Disable Potentially unwanted app blocking
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Blocking downloads cannot be managed. Leave download blocking enabled.

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    Policy must be enabled and set to disable to apply.

    .. wgpolicy:: Disable Potentially unwanted app blocking
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Microsoft Defender Antivirus -->
                  Configure detection for potentially unwanted applications
      :option:    ☑,
                  Options
      :setting:   Enabled,
                  Disabled (Default)
      :no_section:
      :no_caption:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Disable Potentially unwanted app blocking
      :key_title: HHKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Defender
      :names:     PUAProtection
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

`Reference <https://www.tenforums.com/tutorials/32236-enable-disable-microsoft-defender-pua-protection-windows-10-a.html>`__
`Reference <https://admx.help/?Category=Windows_10_2016&Policy=Microsoft.Policies.WindowsDefender::Root_PUAProtectio>`__
`Reference <https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-antivirus/detect-block-potentially-unwanted-apps-microsoft-defender-antivirus>`__
`Reference <https://www.winhelponline.com/blog/defender-enable-pua-pup-adware-protection/>`__
`Reference <https://www.winhelponline.com/blog/windows-defender-hostsfilehijack-alert-telemetry-block/>`__

SmartScreen for Microsoft Store apps
************************************
.. dropdown:: Disable SmartScreen for Microsoft Store apps
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Warnings will occur if notifications are enabled. 

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Disable SmartScreen for Microsoft Store apps
      :key_title: HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\
                  AppHost
      :names:     EnableWebContentEvaluation,
                  PreventOverride                
      :types:     DWORD,
                  DWORD
      :data:      0,
                  0
      :no_section:
      :no_caption:

    .. wregedit:: Disable SmartScreen for Microsoft Store apps
      :key_title: HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\
                  AppHost
      :names:     EnableWebContentEvaluation,
                  PreventOverride                
      :types:     DWORD,
                  DWORD
      :data:      0,
                  0
      :no_section:
      :no_caption:
      :no_launch:

  `Reference <https://www.tenforums.com/tutorials/81139-turn-off-smartscreen-microsoft-store-apps-windows-10-a.html>`__
