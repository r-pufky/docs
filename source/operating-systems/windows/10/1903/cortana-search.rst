.. _w10-1903-disable-cortana-search:

`Disable Cortana & Search`_
###########################
By default `Cortana data privacy`_ will transfer all data to Microsoft services,
including location, browsing, voice, and search data.

.. danger::
  After every major windows update, verify these settings.

.. note::
  Most settings are managed via GPO.

  :cmdmenu:`⌘ + r --> ms-settings:cortana`

     * Disable all options.
     * Clear all data.

:term:`Registry` Machine
************************
.. wregedit:: Disable Cortana via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\
              Windows Search
  :names:     AllowCortana
  :types:     DWORD
  :data:      0
  :no_section:

.. wregedit:: Disable Cortana and Search location access via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\
              Windows Search
  :names:     AllowSearchToUseLocation
  :types:     DWORD
  :data:      0
  :no_section:
  :no_launch:

.. wregedit:: Disable Cortana and Search location access via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\
              Windows Search
  :names:     DisableWebSearch
  :types:     DWORD
  :data:      1
  :no_section:
  :no_launch:

.. wregedit:: Disable web search from Cortana via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\
              Windows Search
  :names:     ConnectedSearchUseWeb
  :types:     DWORD
  :data:      0
  :no_section:
  :no_launch:

.. wregedit:: Block outbound Cortana connections via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\WindowsFirewall\
              FirewallRules
  :names:     {0DE40C8E-C126-4A27-9371-A27DAB1039F7}
  :types:     SZ
  :data:      v2.25|Action=Block|Active=TRUE|Dir=Out|Protocol=6|App=%windir%\SystemApps\Microsoft.Windows.Cortana_cw5n1h2txyewy\searchUI.exe|Name=Block outbound Cortana|
  :no_section:
  :no_launch:

:term:`GPO` Computer
********************
.. wgpolicy:: Disable Cortana via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Search -->
              Allow Cortana
  :option:    ☑
  :setting:   Disabled
  :no_section:

.. wgpolicy:: Disable Cortana and Search location access via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Search -->
              Allow search and Cortana to use location
  :option:    ☑
  :setting:   Disabled
  :no_section:
  :no_launch:

.. wgpolicy:: Disable web search from windows desktop via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Search -->
              Do not allow web search
  :option:    ☑
  :setting:   Enabled
  :no_section:
  :no_launch:

.. wgpolicy:: Disable Windows cloud search from windows desktop via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Search -->
              Allow Cloud Search
  :option:    ☑
  :setting:   Disabled
  :no_section:
  :no_launch:

.. wgpolicy:: Disable Cortana on lock screen via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Search -->
              Allow Cortana above lock screen
  :option:    ☑
  :setting:   Disabled
  :no_section:
  :no_launch:

.. wgpolicy:: Prevent Cortana from unlocking and indexing encrypted files via
              machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Search -->
              Allow indexing of encrypted files
  :option:    ☑
  :setting:   Disabled
  :no_section:
  :no_launch:

.. wgpolicy:: Prevent search from indexing network files via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Search -->
              Prevent automatically adding shared folders to the Windows Search index
  :option:    ☑
  :setting:   Enabled
  :no_section:
  :no_launch:

.. wgpolicy:: Disable web search from Cortana via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Search -->
              Don't search the web or display web results in Search
  :option:    ☑
  :setting:   Enabled
  :no_section:
  :no_launch:

.. wgpolicy:: Disable web search over metered connections from Cortana via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Search -->
              Don't search the web or display web results in Search over metered connections
  :option:    ☑
  :setting:   Enabled
  :no_section:
  :no_launch:

.. wgpolicy:: Disable indexing of online exchange mailboxes via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Search -->
              Enable indexing of online delegate mailboxes
  :option:    ☑
  :setting:   Disabled
  :no_section:
  :no_launch:

.. wgpolicy:: Prevent adding UNC locations to index via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Search -->
              Prevent adding UNC locations to index from Control Panel
  :option:    ☑
  :setting:   Enabled
  :no_section:
  :no_launch:

.. wgpolicy:: Prevent indexing while on battery power via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Search -->
              Prevent indexing when running on battery power to conserve energy
  :option:    ☑
  :setting:   Enabled
  :no_section:
  :no_launch:

.. wgpolicy:: Prevent indexing email attachments via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Search -->
              Prevent indexing e-mail attachments
  :option:    ☑
  :setting:   Enabled
  :no_section:
  :no_launch:

.. wgpolicy:: Prevent indexing files in offline files via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Search -->
              Prevent indexing files in offline files cache
  :option:    ☑
  :setting:   Enabled
  :no_section:
  :no_launch:

.. wgpolicy:: Prevent indexing Microsoft Outlook via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Search -->
              Prevent indexing Microsoft Office Outlook
  :option:    ☑
  :setting:   Enabled
  :no_section:
  :no_launch:

.. wgpolicy:: Prevent indexing Microsoft Outlook Public Folders via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Search -->
              Prevent indexing public folders
  :option:    ☑
  :setting:   Enabled
  :no_section:
  :no_launch:

.. wgpolicy:: Disable indexing of uncached Exchange folders via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Enable indexing uncached Exchange folders
  :option:    ☑
  :setting:   Disabled
  :no_section:
  :no_launch:

.. wgpolicy:: Prevent remote index queries via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Search -->
              Prevent clients from querying the index remotely
  :option:    ☑
  :setting:   Enabled
  :no_section:
  :no_launch:

.. wgpolicy:: Block outbound Cortana connections via machine GPO
  :key_title: Computer Configuration -->
              Windows Settings -->
              Security Settings -->
              Windows Defender Firewall with Advanced Security -->
              Windows Defender Firewall with Advanced Security - Local Group Policy Object -->
              Outbound Rules -->
              New Rule
  :option:    Rule Type,
              This program path,
              Action,
              Profile,
              › Domain,
              › Private,
              › Public,
              Name,
              Protocols and Ports,
              Protocol Type,
              Local port,
              Remote port
  :setting:   Program,
              %windir%\systemapps\Microsoft.Windows.Cortana_cw5n1h2txyewy\SearchUI.exe,
              Block the connection,
              ,
              ☑,
              ☑,
              ☑,
              Block outbound Cortana,
              ,
              TCP,
              All Ports,
              All Ports
  :no_section:
  :no_launch:

Firewall
********
`Cortana Endpoints to Microsoft Services`_ may change. Peridiocally verify these
have not changed. See references for additional documentation.

.. warning::
  These endpoints should be blocked or routed to a blackhole. See
  :ref:`service-pihole` and :ref:`networking-dnat-for-captive-dns`.

.. gtable:: Cortana and Search
  :header: Service;
           Endpoint
  :c0:     Cortana, Greetings, Tips, Live Tiles;
           ›;
           ›;
           ›;
           ›;
           ›;
           ›;
           ›;
           ›
  :c1:     https://www.bing.com/client;
           https://www.bing.com;
           https://www.bing.com/proactive;
           https://www.bing.com/threshold/xls.aspx;
           http://exo-ring.msedge.net;
           http://fp.msedge.net;
           http://fp-vp.azureedge.net;
           http://odinvzc.azureedge.net;
           http://spo-ring.msedge.net
  :no_key_title:
  :no_section:
  :no_launch:
  :delim: ;

.. rubric:: References

#. `Cortana Endpoints to Microsoft Services <https://docs.microsoft.com/en-us/windows/privacy/manage-windows-1903-endpoints>`_
#. `Configure Windows Diagnostic Data <https://docs.microsoft.com/en-us/windows/privacy/configure-windows-diagnostic-data-in-your-organization>`_

.. _Cortana data privacy: https://support.microsoft.com/en-us/topic/cortana-and-privacy-47e5856e-3680-d930-22e1-71ec6cdde231
.. _Disable Cortana: https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#bkmk-cortana
