.. _w10-1903-disable-update-notifications:

Disable Update Notifications
############################
Taskbar is very noisey by default. Remore spurious alerts and information that
is not needed.

.. dropdown:: Disable customer experience improvment program
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in
  :open:

  .. gui::    Disable Taskbar Update Notifications
    :path:    ⌘ + r -->
              ms-settings:taskbar -->
              Select which icons appear on the taskbar
    :value0:  Windows Update Status, ☐
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable Taskbar Update Notifications
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WindowsUpdate\UX\Settings
    :value0:   TrayIconVisibility, {DWORD}, 0
    :ref:      https://www.majorgeeks.com/content/page/enable_or_disable_the_windows_update_status_taskbar_notification.html
    :update:   2021-02-19
    :generic:
    :open:
