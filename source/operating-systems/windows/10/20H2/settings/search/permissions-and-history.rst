.. _w10-20h2-permissions-and-history:

Permissions & History
#####################
.. dropdown:: Disable SafeSearch
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Prevent filtering of results by Windows Search. Note the GPO only applies to
  Windows versions before 10.
  
  `Reference <https://www.tenforums.com/tutorials/82478-change-safesearch-setting-windows-10-a.html#option2>`_
    
  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    ``1`` moderate, ``2`` strict.

    .. wregedit:: Disable SafeSearch
      :key_title: HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion
                  SearchSettings
      :names:     SafeSearchMode
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

Cloud content search
********************
.. dropdown:: Disable Cloud content search
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Disable both ``Microsoft account`` and ``Work or School account`` searching.

  `Reference <https://www.tenforums.com/tutorials/88731-enable-disable-show-cloud-content-search-results-windows-10-a.html>`_
    
  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    Enabling the policy and setting ``Disable Cloud Search`` has the same
    affect.

    .. wgpolicy:: Disable Cloud content search
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Search -->
                  Allow Cloud Search
      :option:    ☑
      :setting:   Disabled
      :no_section:
      :no_caption:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    ``MSA`` handles Microsoft accounts, ``AAD`` handles Azure Active Directory
    accounts (work or school accounts).

    .. wregedit:: Disable Cloud content search
      :key_title: HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion
                  SearchSettings
      :names:     IsMSACloudSearchEnabled,
                  IsAADCloudSearchEnabled
      :types:     DWORD,
                  DWORD
      :data:      0,
                  0
      :no_section:
      :no_caption:

History
*******
.. dropdown:: Disable Search history on this device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  `Reference <https://www.tenforums.com/tutorials/133365-how-turn-off-device-search-history-windows-10-a.html>`_

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Disable Search history on this device
      :key_title: HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion
                  SearchSettings
      :names:     IsDeviceSearchHistoryEnabled
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:
