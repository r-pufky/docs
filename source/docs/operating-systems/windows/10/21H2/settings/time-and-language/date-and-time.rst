.. _w10-21h2-settings-time-and-language-date-and-time:

Date & Time
###########

.. _w10-21h2-settings-time-and-language-date-and-time-utc-realtime-clock:

UTC Realtime Clock
******************
Only required if dual booting requires Windows 10. Set BIOS clock to UTC and
update windows to interpret the Realtime Clock (RTC) using the UTC timezone.
Disable NTP updates and let other operation system handle clock updates.

.. regedit:: Use UTC for windows system clock
  :path:     HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\TimeZoneInformation
  :value0:   RealTimeIsUniversal, {DWORD}, 1
  :ref:      https://forum.manjaro.org/t/root-tip-get-your-time-timezone-right-using-manjaro-windows-dual-boot/1167
  :update:   2021-12-15

.. regedit:: Disable NTP sync
  :path:     HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\W32Time\
             TimeProviders\NtpClient
  :value0:   Enabled, {DWORD}, 0
  :ref:      https://forum.manjaro.org/t/root-tip-get-your-time-timezone-right-using-manjaro-windows-dual-boot/1167
  :update:   2021-12-15

Reboot.
