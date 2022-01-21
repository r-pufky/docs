.. _w10-21h2-security-reputation-based-protection-settings:

Reputation-based protection settings
####################################
Check apps and files
*********************
.. dropdown:: Disable Check apps and files
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. gpo::    Disable Check apps and files
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              File Explorer -->
              Configure Windows Defender SmartScreen
    :value0:  ☑, {DISABLED}
    :ref:     https://www.tenforums.com/tutorials/5593-turn-off-smartscreen-apps-files-web-windows-10-a.html
    :update:  2021-02-19
    :generic:
    :open:

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

  .. gpo::    Disable Potentially unwanted app blocking
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Microsoft Defender Antivirus -->
              Configure detection for potentially unwanted applications
    :value0:  ☑, {ENABLED}
    :value1:  Options, Disabled (Default)
    :ref:     https://www.tenforums.com/tutorials/32236-enable-disable-microsoft-defender-pua-protection-windows-10-a.html,
              https://admx.help/?Category=Windows_10_2016&Policy=Microsoft.Policies.WindowsDefender::Root_PUAProtectio,
              https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-antivirus/detect-block-potentially-unwanted-apps-microsoft-defender-antivirus,
              https://www.winhelponline.com/blog/defender-enable-pua-pup-adware-protection/,
              https://www.winhelponline.com/blog/windows-defender-hostsfilehijack-alert-telemetry-block/
    :update:  2021-02-19
    :generic:
    :open:
