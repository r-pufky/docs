.. _w10-1903-disable-cortana-search:

`Disable Cortana & Search`_
###########################
By default `Cortana data privacy`_ will transfer all data to Microsoft services,
including location, browsing, voice, and search data.

.. danger::
  After every major windows update, verify these settings.

.. dropdown:: Manually disable Cortana
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Most settings are managed via GPO; not needed if applying Registry/GPO
  policies.

  :cmdmenu:`⌘ + r --> ms-settings:cortana`

     * Disable all value0s.
     * Clear all data.

.. dropdown:: Disable Cortana
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. gpo::    Disable Cortana
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Search -->
              Allow Cortana
    :value0:  ☑, {DISABLED}
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable Cortana
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\
               Windows Search
    :value0:   AllowCortana, {DWORD}, 0
    :update:   2021-02-19
    :generic:
    :open:

.. dropdown:: Disable Cortana & Search access to location
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. gpo::    Disable Cortana and Search access to location
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Search -->
              Allow search and Cortana to use location
    :value0:  ☑, {DISABLED}
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable Cortana and Search access to location
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\
               Windows Search
    :value0:   AllowSearchToUseLocation, {DWORD}, 0
    :update:   2021-02-19
    :generic:
    :open:

.. dropdown:: Disable web search from windows desktop & Cortana
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. gpo::    Disable web search from windows desktop
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Search -->
              Do not allow web search
    :value0:  ☑, {ENABLED}
    :update:  2021-02-19
    :generic:
    :open:

  .. gpo::    Disable Windows cloud search from windows desktop
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Search -->
              Allow Cloud Search
    :value0:  ☑i, {DISABLED}
    :update:  2021-02-19
    :generic:
    :open:

  .. gpo::    Disable web search from Cortana
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Search -->
              Don't search the web or display web results in Search
    :value0:  ☑, {ENABLED}
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable web search from windows desktop
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\
               Windows Search
    :value0:   DisableWebSearch,      {DWORD}, 1
    :value1:   ConnectedSearchUseWeb, {DWORD}, 0
    :update:   2021-02-19
    :generic:
    :open:

.. gpo::    Disable Cortana & Search indexing
  :path:    Computer Configuration -->
            Administrative Templates -->
            Windows Components -->
            Search
  :value0:  Prevent automatically adding shared folders to the Windows Search index, {ENABLED}
  :value1:                             Enable indexing of online delegate mailboxes, {DISABLED}
  :value2:                                        Allow indexing of encrypted files, {DISABLED}
  :value3:        Prevent indexing when running on battery power to conserve energy, {ENABLED}
  :value4:                                      Prevent indexing e-mail attachments, {ENABLED}
  :value5:                            Prevent indexing files in offline files cache, {ENABLED}
  :value6:                                Prevent indexing Microsoft Office Outlook, {ENABLED}
  :value7:                                          Prevent indexing public folders, {ENABLED}
  :value8:                                Enable indexing uncached Exchange folders, {DISABLED}
  :value9:                         Prevent clients from querying the index remotely, {ENABLED}
  :value10:                Prevent adding UNC locations to index from Control Panel, {ENABLED}
  :update:   2021-02-19

.. dropdown:: Disable Cortana on lock screen
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. gpo::    Disable Cortana on lock screen
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Search -->
              Allow Cortana above lock screen
    :value0:  ☑, {DISABLED}
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable Cortana on lock screen
    :path:     HKEY_CURRENT_USER\SOFTWARE\Microsoft\Speech_OneCore\
               Preferences
    :value0:   VoiceActivationEnableAboveLockscreen, {DWORD}, 0
    :update:   2021-02-19
    :generic:
    :open:

.. gpo::    Disable web search over metered connections
  :path:    Computer Configuration -->
            Administrative Templates -->
            Windows Components -->
            Search -->
            Don't search the web or display web results in Search over metered connections
  :value0:  ☑, {ENABLED}
  :update:  2021-02-19

Firewall
********
`Cortana Endpoints to Microsoft Services`_ may change. Peridiocally verify these
have not changed. See references for additional documentation.

.. warning::
  These endpoints should be blocked or routed to a blackhole. See
  :ref:`service-pihole` and :ref:`networking-dnat-for-captive-dns`.

.. dropdown:: Block outbound Cortana Connections
  :container: + shadow
  :title: bg-info text-white font-weight-bold
  :animate: fade-in

  .. gpo::    Block outbound Cortana connections
    :path:    Computer Configuration -->
              Windows Settings -->
              Security Settings -->
              Windows Defender Firewall with Advanced Security -->
              Windows Defender Firewall with Advanced Security - Local Group Policy Object -->
              Outbound Rules -->
              New Rule
    :value0:  Rule Type, Program
    :value1:  This program path, %windir%\systemapps\Microsoft.Windows.Cortana_cw5n1h2txyewy\SearchUI.exe
    :value2:  Action, Block the connection
    :value3:  Profile,
    :value4:  › Domain, ☑
    :value5:  › Private, ☑
    :value6:  › Public, ☑
    :value7:  Name, Block outbound Cortana
    :value8:  Protocols and Ports,
    :value9:  Protocol Type, {TCP}
    :value10: Local port, All Ports
    :value11: Remote port, All Ports
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Block outbound Cortana connections
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\WindowsFirewall\
               FirewallRules
    :value0:   {0DE40C8E-C126-4A27-9371-A27DAB1039F7},
               {SZ},
               v2.25|Action=Block|Active=TRUE|Dir=Out|Protocol=6|App=%windir%\SystemApps\Microsoft.Windows.Cortana_cw5n1h2txyewy\searchUI.exe|Name=Block outbound Cortana|
    :update:   2021-02-19
    :generic:
    :open:

.. dropdown:: Cortana and Search endpoints
  :container: + shadow
  :title: bg-info text-white font-weight-bold
  :animate: fade-in

  +--------------------------------------+-----------------------------------------+
  | Service                              | Endpoint                                |
  +======================================+=========================================+
  | Cortana, Greetings, Tips, Live Tiles | https://www.bing.com/client             |
  +--------------------------------------+-----------------------------------------+
  | ›                                    | https://www.bing.com                    |
  +--------------------------------------+-----------------------------------------+
  | ›                                    | https://www.bing.com/proactive          |
  +--------------------------------------+-----------------------------------------+
  | ›                                    | https://www.bing.com/threshold/xls.aspx |
  +--------------------------------------+-----------------------------------------+
  | ›                                    | http://exo-ring.msedge.net              |
  +--------------------------------------+-----------------------------------------+
  | ›                                    | http://fp.msedge.net                    |
  +--------------------------------------+-----------------------------------------+
  | ›                                    | http://fp-vp.azureedge.net              |
  +--------------------------------------+-----------------------------------------+
  | ›                                    | http://odinvzc.azureedge.net            |
  +--------------------------------------+-----------------------------------------+
  | ›                                    | http://spo-ring.msedge.net              |
  +--------------------------------------+-----------------------------------------+

.. rubric:: References

#. `Cortana Endpoints to Microsoft Services <https://docs.microsoft.com/en-us/windows/privacy/manage-windows-1903-endpoints>`_
#. `Configure Windows Diagnostic Data <https://docs.microsoft.com/en-us/windows/privacy/configure-windows-diagnostic-data-in-your-organization>`_

.. _Cortana data privacy: https://support.microsoft.com/en-us/topic/cortana-and-privacy-47e5856e-3680-d930-22e1-71ec6cdde231
.. _Disable Cortana: https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#bkmk-cortana
