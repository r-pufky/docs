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

     * Disable all options.
     * Clear all data.

.. dropdown:: Disable Cortana
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Disable Cortana
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\
                  Windows Search
      :names:     AllowCortana
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

    .. wgpolicy:: Disable Cortana
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Search -->
                  Allow Cortana
      :option:    ☑
      :setting:   Disabled
      :no_section:
      :no_caption:

.. dropdown:: Disable Cortana & Search access to location
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Disable Cortana and Search access to location
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\
                  Windows Search
      :names:     AllowSearchToUseLocation
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

    .. wgpolicy:: Disable Cortana and Search access to location
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Search -->
                  Allow search and Cortana to use location
      :option:    ☑
      :setting:   Disabled
      :no_section:
      :no_caption:

.. dropdown:: Disable web search from windows desktop & Cortana
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Disable web search from windows desktop
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\
                  Windows Search
      :names:     DisableWebSearch
      :types:     DWORD
      :data:      1
      :no_section:
      :no_caption:

    .. wregedit:: Disable web search from Cortana
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\
                  Windows Search
      :names:     ConnectedSearchUseWeb
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:
      :no_launch:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

    .. wgpolicy:: Disable web search from windows desktop
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Search -->
                  Do not allow web search
      :option:    ☑
      :setting:   Enabled
      :no_section:
      :no_caption:

    .. wgpolicy:: Disable Windows cloud search from windows desktop
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Search -->
                  Allow Cloud Search
      :option:    ☑
      :setting:   Disabled
      :no_section:
      :no_caption:
      :no_launch:

    .. wgpolicy:: Disable web search from Cortana
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Search -->
                  Don't search the web or display web results in Search
      :option:    ☑
      :setting:   Enabled
      :no_section:
      :no_caption:
      :no_launch:

.. dropdown:: Disable Cortana & Search indexing
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

    .. wgpolicy:: Disable Cortana & Search indexing
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Search
      :option:    Prevent automatically adding shared folders to the Windows Search index,
                  Enable indexing of online delegate mailboxes,
                  Allow indexing of encrypted files,
                  Prevent indexing when running on battery power to conserve energy,
                  Prevent indexing e-mail attachments,
                  Prevent indexing files in offline files cache,
                  Prevent indexing Microsoft Office Outlook,
                  Prevent indexing public folders,
                  Enable indexing uncached Exchange folders,
                  Prevent clients from querying the index remotely,
                  Prevent adding UNC locations to index from Control Panel
      :setting:   Enabled,
                  Disabled,
                  Disabled,
                  Enabled,
                  Enabled,
                  Enabled,
                  Enabled,
                  Enabled,
                  Disabled,
                  Enabled,
                  Enabled
      :no_section:
      :no_caption:

.. dropdown:: Disable Cortana on lock screen
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Disable Cortana on lock screen
      :key_title: HKEY_CURRENT_USER\SOFTWARE\Microsoft\Speech_OneCore\
                  Preferences
      :names:     VoiceActivationEnableAboveLockscreen
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

    .. wgpolicy:: Disable Cortana on lock screen
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Search -->
                  Allow Cortana above lock screen
      :option:    ☑
      :setting:   Disabled
      :no_section:
      :no_caption:

.. dropdown:: Disable web search over metered connections
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

    .. wgpolicy:: Disable web search over metered connections
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Search -->
                  Don't search the web or display web results in Search over metered connections
      :option:    ☑
      :setting:   Enabled
      :no_section:
      :no_caption:

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

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Block outbound Cortana connections
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\WindowsFirewall\
                  FirewallRules
      :names:     {0DE40C8E-C126-4A27-9371-A27DAB1039F7}
      :types:     SZ
      :data:      v2.25|Action=Block|Active=TRUE|Dir=Out|Protocol=6|App=%windir%\SystemApps\Microsoft.Windows.Cortana_cw5n1h2txyewy\searchUI.exe|Name=Block outbound Cortana|
      :no_section:
      :no_caption:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

    .. wgpolicy:: Block outbound Cortana connections
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
      :no_caption:

.. dropdown:: Cortana and Search endpoints
  :container: + shadow
  :title: bg-info text-white font-weight-bold
  :animate: fade-in

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
    :no_caption:
    :no_launch:
    :delim: ;

.. rubric:: References

#. `Cortana Endpoints to Microsoft Services <https://docs.microsoft.com/en-us/windows/privacy/manage-windows-1903-endpoints>`_
#. `Configure Windows Diagnostic Data <https://docs.microsoft.com/en-us/windows/privacy/configure-windows-diagnostic-data-in-your-organization>`_

.. _Cortana data privacy: https://support.microsoft.com/en-us/topic/cortana-and-privacy-47e5856e-3680-d930-22e1-71ec6cdde231
.. _Disable Cortana: https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#bkmk-cortana
