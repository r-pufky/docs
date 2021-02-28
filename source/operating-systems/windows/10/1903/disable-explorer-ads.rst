.. _w10-1903-disable-explorer-ads:

`Disable Explorer Ads`_
#######################
`Sync providers`_ for windows explorer can now show Ads. Disable it.

.. danger::
  Set `Explorer to use This PC`_ **before** setting the Quick Pane registry
  option or this will break explorer. See `disable quick access pane in windows
  explorer`_.

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
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Set Explorer to use `this PC`_
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced
    :value0:   LaunchTo, {DWORD}, 1
    :update:   2021-02-19
    :generic:
    :open:

.. regedit:: Disable Quick Access Pane
  :path:      HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
              Explorer
  :value0:    HubMode, {DWORD}, 1
  :update:    2021-02-19

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
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced
    :value0:   ShowSyncProviderNotifications, {DWORD}, 0
    :update:   2021-02-19
    :generic:
    :open:

  .. regedit:: Disable sync provider notifications
    :path:     HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced
    :value0:   ShowSyncProviderNotifications, {DWORD}, 0
    :update:   2021-02-19
    :generic:
    :open:

.. rubric:: References

#. `Disable Windows Sync Provider Notifications <https://winaero.com/disable-notifications-in-file-explorer-in-windows-10-sync-provider-notifications/>`_

.. _this PC: https://social.technet.microsoft.com/Forums/en-US/dc89a8e3-9f97-438a-bc2a-ccde6b443549/explorer-quick-access-how-to-set-via-group-policy-but-how-to-stop-users-from-tampering-with?forum=win10itprogeneral
.. _Sync providers: https://www.extremetech.com/computing/245553-microsoft-now-puts-ads-windows-file-explorer
.. _Explorer to use This PC: https://www.maketecheasier.com/remove-quick-access-file-explorer/
.. _disable quick access pane in windows explorer: https://www.winhelponline.com/blog/remove-quick-access-other-shell-folders-file-explorer/
