.. _w10-20h2-standalone-update-notifications:

Update Notifications
####################
Taskbar is very noisey by default. Remore spurious alerts and information that
is not needed.

.. dropdown:: Disable customer experience improvment program
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in
  :open:

  .. dropdown:: GUI
    :title: font-weight-bold
    :animate: fade-in

    .. ggui:: `Disable Taskbar Update Notifications`_
      :key_title: ⌘ + r -->
                  ms-settings:taskbar -->
                  Select which icons appear on the taskbar
      :option:    Windows Update Status
      :setting:   ☐
      :no_section:
      :no_caption:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: `Disable Taskbar Update Notifications`_
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WindowsUpdate\UX\Settings
      :names:     TrayIconVisibility
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

  `Reference <https://www.majorgeeks.com/content/page/enable_or_disable_the_windows_update_status_taskbar_notification.html>`__
