.. _w10-21h2-settings-search-permissions-and-history:

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
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Disable both ``Microsoft account`` and ``Work or School account`` searching.

  .. gpo::    Disable Cloud content search
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Search -->
              Allow Cloud Search
    :value0:                     ☑, {ENABLED}
    :value1:  Cloud Search Setting, Disable Cloud Search
    :ref:     https://www.tenforums.com/tutorials/88731-enable-disable-show-cloud-content-search-results-windows-10-a.html
    :update:  2021-02-19
    :generic:
    :open:

History
*******
.. regedit:: Disable Search history on this device
  :path:     HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion
             SearchSettings
  :value0:   IsDeviceSearchHistoryEnabled, {DWORD}, 0
  :ref:      https://www.tenforums.com/tutorials/133365-how-turn-off-device-search-history-windows-10-a.html
  :update:   2021-02-19
