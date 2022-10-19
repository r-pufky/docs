.. _w10-21h2-standalone-update-notifications:

Update Notifications
####################
Taskbar is very noisy by default. Remove spurious alerts and information that
is not needed.

.. dropdown:: Disable Taskbar Update Notifications
  :color: primary
  :icon: shield-lock
  :animate: fade-in
  :class-container: sd-shadow-sm
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
