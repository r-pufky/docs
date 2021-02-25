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
    :open:

    .. ggui:: Disable Taskbar Update Notifications
      :key_title: ⌘ + r -->
                  ms-settings:taskbar -->
                  Select which icons appear on the taskbar
      :option:    Windows Update Status
      :setting:   ☐
      :no_section:
      :no_caption:

  .. regedit:: Disable Taskbar Update Notifications
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WindowsUpdate\UX\Settings
    :value0:   TrayIconVisibility, {DWORD}, 0
    :ref:      https://www.majorgeeks.com/content/page/enable_or_disable_the_windows_update_status_taskbar_notification.html
    :update:   2021-02-19
    :generic:
    :open:
