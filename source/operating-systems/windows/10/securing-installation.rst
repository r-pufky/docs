.. _windows-10-pro-securing-install-old:

Windows 10 Pro Securing Install (Old)
#####################################
A reboot is required once these changes are made. Group policy edits are
preferred and registry/other equivalents are provided as well. Any may be
applied.

Disable Services
****************
.. wservice:: Disable razer game scanner service
  :key_title: Razer Game Scanner --> General
  :option:    Startup type,
              Service status
  :setting:   Disabled,
              Stopped
  :no_section:
  :no_launch:
  :no_caption:

Set Reasonable Privacy Settings
*******************************
:cmdmenu:`start --> settings --> privacy`

   * Disable `all options on all 13 pages`_ and re-enable to taste.
   * `Disable Ad Tracking`_.
   * :cmdmenu:`Background Apps`: Leave background service enable, but disable
     all apps. This will prevent searching from the start menu from breaking.

     .. note::
       If start menu searches start to fail, it is because background apps
       service has been disabled. See :ref:`windows-background-apps`.

   * :cmdmenu:`Microphone`: Leave enabled, but disable all apps. This will allow
     mumble to use the microphone. See `1803 update breaks microphone`_.

Disable Wi-Fi Sharing
*********************
:cmdmenu:`start --> settings --> change network settings --> manage wifi settings`

   * ☐ all for sharing.

Remove Unused Optional Windows Features
***************************************
:cmdmenu:`start --> settings --> manage optional features`

   * English (united states) retail demo content.
   * Neutral retail demo content (cortana demo).
   * News hub.
   * Microsoft Quick Assist.
   * Contact Support.

Disable Paging, Restore Points, and Automatic Driver Updates
************************************************************
:cmdmenu:`start --> view advanced system settings --> advanced --> performance`

   * Disable all paging on all drives.

:cmdmenu:`start --> view advanced system settings --> system protection`

   * Disable protection for all drives.

:cmdmenu:`start --> view advanced system settings --> hardware --> device installation settings`

   * No (Disable).

Disable Windows Explorer Ads
****************************
`Sync providers`_ for windows explorer can now show Ads. Disable it.

:cmdmenu:`⌘ + e --> view --> options --> view`

   * ☐ show sync provider notifications.

.. wregedit:: Disable Quick Access Pane
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
              Explorer
  :names:     HubMode
  :types:     DWORD
  :data:      1
  :admin:
  :no_section:
  :no_caption:

    .. danger::
      Set `explorer to use this pc`_ instead of quick access **before** setting
      registry options or this will break explorer.

      :cmdmenu:`explorer --> change folder and search options --> general --> open file explorer to: This PC`

    `See disable quick access pane in windows explorer`_.

`Remove Services from Being Listed in Task Manager`_
****************************************************
.. wregedit:: Remove local machine startup services regedit
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
              Explorer\StartupApproved\Run
  :names:     *
  :types:     REG_BINARY
  :data:      Delete
  :admin:
  :no_section:
  :no_caption:

    .. note::
      Delete entries that should not appear (or can't be removed from startup by
      other means). This applies to the entire **system**.

.. wregedit:: Remove local user startup services regedit
  :key_title: HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\
              Explorer\StartupApproved\Run
  :names:     *
  :types:     REG_BINARY
  :data:      Delete
  :admin:
  :no_section:
  :no_caption:
  :no_launch:

    .. note::
      Delete entries that should not appear (or can't be removed from startup by
      other means). This applies to the current **user**.

.. _meltdown-spectre-patch:

`Meltdown and Spectre Patch`_
*****************************
Windows 10 will not automatically patch for meltdown and spectre due to
anti-virus software causing BSOD's. If you are running anti-virus software
ensure you are not affected by checking the `anti-virus compatibly list`_.

`InSpectre`_ can be used to validate patches are applied.

.. wregedit:: Meltdown and sepctre patch regedit
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
              QualityCompat
  :names:     cadca5fe-87d3-4b96-b7fb-a231484277cc
  :types:     DWORD
  :data:      0
  :admin:
  :no_section:
  :no_caption:

    Reboot to apply changes.

:download:`regedit script <source/enable-meltdown-spectre-update.reg>`.

.. _all options on all 13 pages: https://bgr.com/2015/07/31/windows-10-upgrade-spying-how-to-opt-out/
.. _1803 update breaks microphone: https://www.ghacks.net/2018/05/01/all-the-issues-of-windows-10-version-1803-you-may-run-into/
.. _Disable Ad Tracking: https://account.microsoft.com/privacy/ad-settings/signedout?ru=https%3A%2F%2Faccount.microsoft.com%2Fprivacy%2Fad-settings
.. _See disable quick access pane in windows explorer: https://www.winhelponline.com/blog/remove-quick-access-other-shell-folders-file-explorer/
.. _explorer to use this pc: https://www.maketecheasier.com/remove-quick-access-file-explorer/
.. _Remove Services from Being Listed in Task Manager:  https://www.tenforums.com/tutorials/2944-add-delete-enable-disable-startup-items-windows-10-a.html
.. _Sync providers: https://www.extremetech.com/computing/245553-microsoft-now-puts-ads-windows-file-explorer
.. _Meltdown and Spectre Patch: https://support.microsoft.com/en-us/help/4056892/windows-10-update-kb4056892
.. _anti-virus compatibly list: https://docs.google.com/spreadsheets/d/184wcDt9I9TUNFFbsAVLpzAtckQxYiuirADzf3cL42FQ/htmlview?usp=sharing&sle=true
.. _InSpectre: https://www.grc.com/inspectre.htm