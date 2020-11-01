.. _w10-1903-taskbar-notifications:

Taskbar Notifications
#####################
Taskbar is very noisey by default. Remore spurious alerts and information that
is not needed.

.. ggui:: Disable Delivery Optimization
  :key_title: ⌘ + r -->
              ms-settings:taskbar -->
              Select which icons appear on the taskbar
  :option:    Windows Update Status
  :setting:   ☐
  :no_section:
  :no_launch:

:term:`Registry`
****************
.. wregedit:: `Disable Taskbar Update Notifications`_ via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WindowsUpdate\UX\Settings
  :names:     TrayIconVisibility
  :types:     DWORD
  :data:      0
  :no_section:

.. _Disable Taskbar Update Notifications: https://www.majorgeeks.com/content/page/enable_or_disable_the_windows_update_status_taskbar_notification.html