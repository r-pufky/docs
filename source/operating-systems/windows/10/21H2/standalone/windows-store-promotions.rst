.. _w10-21h2-standalone-windows-store-promotions:

Windows Store Promotions
########################
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
  :value0:  Update apps automatically, {ENABLED}
  :value1:      Show products on tile, {DISABLED}
  :value2:             Video Autoplay, {DISABLED}
  :update:  2022-01-20

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
    :ref:     https://www.easeus.com/computer-instruction/stop-windows-10-installing-apps.html,
              https://www.youtube.com/watch?v=wgKJMsJ-6XU&feature=youtu.be&t=4m47s
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable silent app installs per user
    :path:     HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\
               ContentDeliveryManager
    :value0:   SilentInstalledAppsEnabled, {DWORD}, 0
    :ref:      https://www.easeus.com/computer-instruction/stop-windows-10-installing-apps.html,
               https://www.youtube.com/watch?v=wgKJMsJ-6XU&feature=youtu.be&t=4m47s
    :update:   2021-02-19
    :generic:
    :open:

.. regedit:: Disable suggested apps
  :path:     HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\
             ContentDeliveryManager\SuggestedApps
  :value0:   {ANY}, {DWORD}, 0
  :ref:      https://www.howtogeek.com/259946/how-to-get-rid-of-suggested-apps-in-windows-10,
             https://superuser.com/questions/1221042/stop-windows-10-from-automatically-downloading-promoted-apps
  :update:   2021-02-19

  Set all applications listed here; this list changes over time as Microsoft
  adds and removes applications. They should all be disabled (set to ``0``).

  See :ref:`w10-21h2-settings-privacy-diagnostics-and-feedback-tailored-experiences`
  to Disable Tailored experiences.
