.. _w10-20h2-settings-search-permissions-and-history:

Permissions & History
#####################
.. regedit:: Disable SafeSearch
  :path:     HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion
             SearchSettings
  :value0:   SafeSearchMode, {DWORD}, 0
  :ref:      https://www.tenforums.com/tutorials/82478-change-safesearch-setting-windows-10-a.html#option2
  :update:   2021-02-19

  Prevent filtering of results by Windows Search. Note the GPO only applies to
  Windows versions before 10.

  ``1`` moderate, ``2`` strict.

Cloud content search
********************
.. dropdown:: Disable Cloud content search
  :color: primary
  :icon: note
  :animate: fade-in
  :class-container: sd-shadow-sm

  Disable both ``Microsoft account`` and ``Work or School account`` searching.

  .. gpo::    Disable Cloud content search
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Search -->
              Allow Cloud Search
    :value0:  ☑, {DISABLED}
    :ref:     https://www.tenforums.com/tutorials/88731-enable-disable-show-cloud-content-search-results-windows-10-a.html
    :update:  2021-02-19
    :generic:
    :open:

    Enabling the policy and setting ``Disable Cloud Search`` has the same
    affect.

  .. regedit:: Disable Cloud content search
    :path:     HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion
               SearchSettings
    :value0:   IsMSACloudSearchEnabled, {DWORD}, 0
    :value1:   IsAADCloudSearchEnabled, {DWORD}, 0
    :ref:      https://www.tenforums.com/tutorials/88731-enable-disable-show-cloud-content-search-results-windows-10-a.html
    :update:   2021-02-19
    :generic:
    :open:

    ``MSA`` handles Microsoft accounts, ``AAD`` handles Azure Active Directory
    accounts (work or school accounts).

History
*******
.. regedit:: Disable Search history on this device
  :path:     HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion
             SearchSettings
  :value0:   IsDeviceSearchHistoryEnabled, {DWORD}, 0
  :ref:      https://www.tenforums.com/tutorials/133365-how-turn-off-device-search-history-windows-10-a.html
  :update:   2021-02-19
