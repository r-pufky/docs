.. _w10-1903-disable-windows-store-promotions:

Disable Windows Store Promotions
################################
Windows Store will automatically install promoted and unwanted applications,
then advertise them in the start menu. Disables those downloads and remove
promoted tiles from the start menu.

.. danger::
  After every major windows update, verify these settings.

.. note::
  Applications installed from the Windows Store must be manually updated after
  this.

.. gui::    Disable Windows Store App Installs from GUI
  :path:    ⌘ + r -->
            ms-windows-store://home -->
            User Icon (⋮ if signed in) -->
            Settings
  :value0:  Update apps automatically, {DISABLED}
  :value1:      Show products on tile, {DISABLED}
  :update:  2021-02-19

.. dropdown:: Disable silent app installs
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. gpo::    Disable silent app installs
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Store -->
              Turn off Automatic Download and Install of updates
    :value0:  ☑, {ENABLED}
    :ref:     https://www.youtube.com/watch?v=wgKJMsJ-6XU&feature=youtu.be&t=4m47s
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable silent app installs
    :path:    HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\WindowsStore
    :value0:  AutoDownload, {DWORD}, 2
    :ref:     https://www.youtube.com/watch?v=wgKJMsJ-6XU&feature=youtu.be&t=4m47s
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable silent app installs per user
    :path:     HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\
               ContentDeliveryManager
    :value0:   SilentInstalledAppsEnabled, {DWORD}, 0
    :ref:      https://www.youtube.com/watch?v=wgKJMsJ-6XU&feature=youtu.be&t=4m47s
    :update:   2021-02-19
    :generic:
    :open:

.. dropdown:: Disable suggested apps
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. gpo::    Disable suggested apps
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Cloud Content -->
              Turn off Microsoft consumer experiences
    :value0:  ☑, {ENABLED}
    :ref:     https://www.howtogeek.com/259946/how-to-get-rid-of-suggested-apps-in-windows-10
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable suggested apps
    :path:     HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\
               ContentDeliveryManager\SuggestedApps
    :value0:   {ANY}, {DWORD}, 0
    :ref:      https://www.howtogeek.com/259946/how-to-get-rid-of-suggested-apps-in-windows-10
    :update:   2021-02-19
    :generic:
    :open:

    Set all applications listed here; this list changes over time as Microsoft
    adds and removes applications. They should all be disabled (set to ``0``).

.. regedit:: Disable tiles for install apps
  :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\CloudContent
  :value0:   DisableWindowsConsumerFeatures, {DWORD}, 1
  :update:   2021-02-19

.. gpo::   Disable Suggested Apps Tips in Windows store
  :path:   Computer Configuration -->
           Administrative Templates -->
           Windows Components -->
           Cloud Content -->
           Do not show Windows tips
  :value0: ☑, {ENABLED}
  :update: 2021-02-19

.. rubric:: References

#. `Disable Promoted Windows Store App Installs <https://www.easeus.com/computer-instruction/stop-windows-10-installing-apps.html>`_
#. `Disable Windows Store Promotions <https://superuser.com/questions/1221042/stop-windows-10-from-automatically-downloading-promoted-apps>`_
