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

  .. dropdown:: GUI
    :title: font-weight-bold
    :animate: fade-in

    .. ggui:: Set explorer to use `this PC`_
      :key_title: ⌘ + e -->
                  File -->
                  Change folder and search options -->
                  General
      :option:    Open File Explorer to
      :setting:   This PC
      :no_section:
      :no_caption:
      :no_launch:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Set Explorer to use `this PC`_
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced
      :names:     LaunchTo
      :types:     DWORD
      :data:      1
      :no_section:
      :no_caption:

.. dropdown:: Disable Quick Access Pane
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Disable Quick Access Pane
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
                  Explorer
      :names:     HubMode
      :types:     DWORD
      :data:      1
      :no_section:
      :no_caption:

.. dropdown:: Disable sync provider notifications
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: GUI
    :title: font-weight-bold
    :animate: fade-in

    Typically done via explorer:

    :cmdmenu:`⌘ + e --> view --> options --> view`

       * ☐ show sync provider notifications.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Disable sync provider notifications
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced
      :names:     ShowSyncProviderNotifications
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

    .. wregedit:: Disable sync provider notifications
      :key_title: HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced
      :names:     ShowSyncProviderNotifications
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:
      :no_launch:

.. rubric:: References

#. `Disable Windows Sync Provider Notifications <https://winaero.com/disable-notifications-in-file-explorer-in-windows-10-sync-provider-notifications/>`_

.. _this PC: https://social.technet.microsoft.com/Forums/en-US/dc89a8e3-9f97-438a-bc2a-ccde6b443549/explorer-quick-access-how-to-set-via-group-policy-but-how-to-stop-users-from-tampering-with?forum=win10itprogeneral
.. _Sync providers: https://www.extremetech.com/computing/245553-microsoft-now-puts-ads-windows-file-explorer
.. _Explorer to use This PC: https://www.maketecheasier.com/remove-quick-access-file-explorer/
.. _disable quick access pane in windows explorer: https://www.winhelponline.com/blog/remove-quick-access-other-shell-folders-file-explorer/
