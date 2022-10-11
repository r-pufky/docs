.. _w10-20h2-standalone-explorer-ads:

Explorer Ads
############
`Sync providers`_ for windows explorer can now show Ads. Disable them.

.. danger::
  Set Explorer to use This PC **before** setting the Quick Pane registry
  option or this will break explorer.

.. dropdown:: Set explorer to use this PC
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. gui::    Set explorer to use this PC
    :path:    ⌘ + e -->
              File -->
              Change folder and search options -->
              General
    :value0:  Open File Explorer to, This PC
    :ref:     https://www.maketecheasier.com/remove-quick-access-file-explorer/,
              https://social.technet.microsoft.com/Forums/en-US/dc89a8e3-9f97-438a-bc2a-ccde6b443549/explorer-quick-access-how-to-set-via-group-policy-but-how-to-stop-users-from-tampering-with?forum=win10itprogeneral
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Set Explorer to use this PC
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
               Explorer\Advanced
    :value0:   LaunchTo, {DWORD}, 1
    :ref:      https://www.maketecheasier.com/remove-quick-access-file-explorer/,
               https://social.technet.microsoft.com/Forums/en-US/dc89a8e3-9f97-438a-bc2a-ccde6b443549/explorer-quick-access-how-to-set-via-group-policy-but-how-to-stop-users-from-tampering-with?forum=win10itprogeneral
    :update:   2021-02-19
    :generic:
    :open:

.. regedit:: Disable Quick Access Pane
  :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
             Explorer
  :value0:   HubMode, {DWORD}, 1
  :ref:      https://www.winhelponline.com/blog/remove-quick-access-other-shell-folders-file-explorer/,
  :update:   2021-02-19

.. dropdown:: Disable sync provider notifications
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: GUI
    :title: font-weight-bold
    :animate: fade-in
    :open:

    Typically done via explorer:

    :cmdmenu:`⌘ + e --> view --> options --> view`

       * ☐ show sync provider notifications.

  .. regedit:: Disable sync provider notifications
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
               Explorer\Advanced
    :value0:   ShowSyncProviderNotifications, {DWORD}, 0
    :ref:      https://winaero.com/disable-notifications-in-file-explorer-in-windows-10-sync-provider-notifications/
    :update:   2021-02-19
    :generic:
    :open:

  .. regedit:: Disable sync provider notifications
    :path:     HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\
               Explorer\Advanced
    :value0:   ShowSyncProviderNotifications, {DWORD}, 0
    :ref:      https://winaero.com/disable-notifications-in-file-explorer-in-windows-10-sync-provider-notifications/
    :update:   2021-02-19
    :generic:
    :open:

.. _Sync providers: https://www.extremetech.com/computing/245553-microsoft-now-puts-ads-windows-file-explorer
