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

`Disable Cortana`_
******************
:cmdmenu:`start --> cortana & search settings`

   * Disable all options.
   * Clear all data.

.. wgpolicy:: Disable Cortana Policy
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Search
  :option:    Allow Cortana
  :setting:   Disabled
  :no_section:
  :no_caption:

`Disable Suggested Apps in Windows`_
************************************
.. wgpolicy:: Disable suggested apps in Windows
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Cloud Content
  :option:    Turn off Microsoft consumer experiences,
              Do not show Windows tips
  :setting:   Enabled,
              Enabled
  :no_section:
  :no_caption:

Disable Paging, Restore Points, and Automatic Driver Updates
************************************************************
:cmdmenu:`start --> view advanced system settings --> advanced --> performance`

   * Disable all paging on all drives.

:cmdmenu:`start --> view advanced system settings --> system protection`

   * Disable protection for all drives.

:cmdmenu:`start --> view advanced system settings --> hardware --> device installation settings`

   * No (Disable).

`Disable Automatic Resource Exhaustion Resolution`_
***************************************************
By default, windows will automatically force close applications when memory
starts to fill up. Prevent Windows from being dumb.

.. wgpolicy:: Disable automatic resource exhaustion policy
  :key_title: Computer Configuration -->
              Administrative Templates -->
              System -->
              Troubleshooting and Diagnostics -->
              Windows Resource Exhaustion Detection and Resolution
  :option:    Configure Scenario Execution Level
  :setting:   Disabled
  :no_section:
  :no_caption:

.. wservice:: Disable Diagnostic Service.
  :key_title: Diagnostic Policy Service --> General
  :option:    Startup type,
              Service status
  :setting:   Disabled,
              Stopped
  :no_section:
  :no_caption:

`Disable Silent Windows Store App Installs`_
********************************************
.. wregedit:: Disable silent app install regedit
  :key_title: HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\
              ContentDeliveryManager
  :names:     SilentInstalledAppsEnabled
  :types:     DWORD
  :data:      0
  :admin:
  :no_section:
  :no_caption:

.. wregedit:: Disable all suggested apps regedit
  :key_title: HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\
              ContentDeliveryManager\SuggestedApps
  :names:     *
  :types:     DWORD
  :data:      0
  :admin:
  :no_section:
  :no_caption:
  :no_launch:

    .. note::
      Set all applications listed here; this list changes over time as Microsoft
      adds and removes applications. They should all be disabled (set to **0**).

`Disable Windows Store App Installs`_
*************************************
.. ggui:: Disable Windows Store App Installs.
  :key_title: start --> store --> User Icon (⋮ if signed in) --> settings
  :option:  Update apps automatically,
            Show products on tile
  :setting: Disabled,
            Disabled
  :no_section:
  :no_caption:
  :no_launch:

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


Disable Microsoft Game Broadcasting Suite
*****************************************
Nearly every program on windows now wants to record your games and broadcast
them. This disables the built-in windows game broadcasting and recording
software.

Also removes the :cmdmenu:`⌘ + g` prompt when starting games.

This occurs because of the xbox app on Windows 10. Removing the app will also
fix this.
(see [Removing pre-installed Windows Packages](#removing-pre-installed-windows-packages))

.. wgpolicy:: Disable game broadcasting suite policy
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Windows Game Recording and Broadcasting
  :option:    Enables or disables Windows Game Recording and Broadcasting
  :setting:   Disabled
  :no_section:
  :no_caption:

.. wregedit:: Removing ⌘ + g Prompt on Game Launch
  :key_title: HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\
              GameDVR
  :names:     AppCaptureEnabled
  :types:     DWORD
  :data:      0
  :admin:
  :no_caption:

.. wregedit:: Disable xbox Game DVR
  :key_title: HKEY_CURRENT_USER\System\GameConfigStore
  :names:     GameDVR_Enabled
  :types:     DWORD
  :data:      0
  :admin:
  :no_caption:

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

`Removing Preinstalled Windows Packages`_
*****************************************
Certain packages (and windows store applications) cannot be removed with
`programs and applications`_. This removes applications using Windows the
built-in package manager.

Default applications are updated with each major update to windows 10, so
manually removing applications is preferred over a script.

   * ``Remove-AppxProvisionedPackage`` will remove packages for newly
     provisioned accounts.
   * ``Remove-AppxPackage`` removes for the current user.
   * ``Get-AppxPackage -AllUsers`` will return results for all users on system.

:download:`Remove packages script. <source/remove-crapware.ps1>`

.. _all options on all 13 pages: https://bgr.com/2015/07/31/windows-10-upgrade-spying-how-to-opt-out/
.. _1803 update breaks microphone: https://www.ghacks.net/2018/05/01/all-the-issues-of-windows-10-version-1803-you-may-run-into/
.. _Disable Cortana: https://www.howtogeek.com/265027/how-to-disable-cortana-in-windows-10/
.. _Disable Ad Tracking: https://account.microsoft.com/privacy/ad-settings/signedout?ru=https%3A%2F%2Faccount.microsoft.com%2Fprivacy%2Fad-settings
.. _Disable Suggested Apps in Windows: https://www.howtogeek.com/259946/how-to-get-rid-of-suggested-apps-in-windows-10/
.. _Disable Automatic Resource Exhaustion Resolution: https://www.windows-security.org/f4aece067cb4976eb7a4f3add2fda30c/configure-scenario-execution-level
.. _Disable Silent Windows Store App Installs: https://www.youtube.com/watch?v=wgKJMsJ-6XU&feature=youtu.be&t=4m47s
.. _Disable Windows Store App Installs: https://www.easeus.com/computer-instruction/stop-windows-10-installing-apps.html
.. _See disable quick access pane in windows explorer: https://www.winhelponline.com/blog/remove-quick-access-other-shell-folders-file-explorer/
.. _explorer to use this pc: https://www.maketecheasier.com/remove-quick-access-file-explorer/
.. _Remove Services from Being Listed in Task Manager:  https://www.tenforums.com/tutorials/2944-add-delete-enable-disable-startup-items-windows-10-a.html
.. _Disable Microsoft Game Broadcasting Suite: https://www.tenforums.com/tutorials/8637-game-bar-turn-off-windows-10-a.html
.. _Sync providers: https://www.extremetech.com/computing/245553-microsoft-now-puts-ads-windows-file-explorer
.. _Meltdown and Spectre Patch: https://support.microsoft.com/en-us/help/4056892/windows-10-update-kb4056892
.. _anti-virus compatibly list: https://docs.google.com/spreadsheets/d/184wcDt9I9TUNFFbsAVLpzAtckQxYiuirADzf3cL42FQ/htmlview?usp=sharing&sle=true
.. _InSpectre: https://www.grc.com/inspectre.htm
.. _Removing Preinstalled Windows Packages: https://thomas.vanhoutte.be/miniblog/delete-windows-10-apps/
.. _programs and applications: https://www.makeuseof.com/tag/3-clever-powershell-functions-upgrading-windows-10