.. _w10-1903-disable-windows-store-promotions:

`Disable Windows Store Promotions`_
###################################
Windows Store will automatically install promoted and unwanted applications,
then advertise them in the start menu. Disables those downloads and removes
promoted tiles from the start menu.

.. danger::
  After every major windows update, verify these settings.

.. note::
  Applications installed from the Windows Store must be manually updated after
  this.

.. ggui:: Disable Windows Store App Installs from user app.
  :key_title: ⌘ + r -->
              ms-windows-store://home -->
              User Icon (⋮ if signed in) -->
              Settings
  :option:  Update apps automatically,
            Show products on tile
  :setting: Disabled,
            Disabled
  :no_section:
  :no_caption:
  :no_launch:

:term:`Registry` Machine
************************
.. wregedit:: Disable tiles for install apps via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\CloudContent
  :names:     DisableWindowsConsumerFeatures
  :types:     DWORD
  :data:      1
  :no_section:

.. wregedit:: Disable silent app installs per user via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\WindowsStore
  :names:     AutoDownload
  :types:     DWORD
  :data:      2
  :admin:
  :no_section:
  :no_launch:

:term:`Registry` User
*********************
.. wregedit:: Disable silent app installs per user via Registry
  :key_title: HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\
              ContentDeliveryManager
  :names:     SilentInstalledAppsEnabled
  :types:     DWORD
  :data:      0
  :admin:
  :no_section:
  :no_launch:

.. wregedit:: Disable all suggested apps regedit
  :key_title: HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\
              ContentDeliveryManager\SuggestedApps
  :names:     *
  :types:     DWORD
  :data:      0
  :admin:
  :no_section:
  :no_launch:

    .. note::
      Set all applications listed here; this list changes over time as Microsoft
      adds and removes applications. They should all be disabled (set to **0**).

:term:`GPO` Computer
********************
.. wgpolicy:: Disable Windows store automatic install and updates via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Store -->
              Turn off Automatic Download and Install of updates
  :option:    ☑
  :setting:   Enabled
  :no_section:

.. wgpolicy:: Disable Suggested Apps in Windows store via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Cloud Content -->
              Turn off Microsoft consumer experiences
  :option:    ☑
  :setting:   Enabled
  :no_section:
  :no_launch:

.. wgpolicy:: Disable Suggested Apps Tips in Windows store via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Cloud Content -->
              Do not show Windows tips
  :option:    ☑
  :setting:   Enabled
  :no_section:
  :no_launch:

.. rubric:: References

#. `Disable Silent App Installs <https://www.youtube.com/watch?v=wgKJMsJ-6XU&feature=youtu.be&t=4m47s>`_
#. `Disable Promoted Windows Store App Installs <https://www.easeus.com/computer-instruction/stop-windows-10-installing-apps.html>`_
#. `Disable Suggested Apps in Windows <https://www.howtogeek.com/259946/how-to-get-rid-of-suggested-apps-in-windows-10>`_

.. _Disable Windows Store Promotions: https://superuser.com/questions/1221042/stop-windows-10-from-automatically-downloading-promoted-apps
