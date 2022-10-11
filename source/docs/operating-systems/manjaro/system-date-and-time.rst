.. _manajaro-kde-system-date-and-time:

System Date and Time
####################

.. gui:: Time and Date
  :nav:    ⌘ --> manjaro settings manager
  :path:   time and date
  :value0: ☑, set time and date automatically
  :update: 2021-12-15
  :open:

.. code-block:: bash
  :caption: Set RTC (realtime clock) to UTC, use NTP with timezone.

  timedatectl set-local-rtc 0
  systemctl enable --now systemd-timesyncd
  sudo ln -sf /usr/share/zoneinfo/America/Los_Angeles /etc/localtime

Windows Dual boot
*****************
Dual booting requires Windows 10 to use UTC instead of RTC. Disable the NTP
client for windows use manjaro to adjust the clock. See:
:ref:`w10-21h2-settings-time-and-language-date-and-time-utc-realtime-clock`.

Force ISO8601 date/time
***********************
Forces YYYY-MM-DD 24H time for KDE lockscreens / clock.

.. code-block:: bash
  :caption: **0644 root root** ``/usr/share/plasma/look-and-feel/org.kde.breeze.desktop/contents/components/Clock.qml``

  // text: Qt.formatTime(timeSource.data["Local"]["DateTime"])
  text: Qt.formatTime(timeSource.data["Local"]["DateTime"], "hh:mm:ss")

  // text: Qt.formatTime(timeSource.data["Local"]["DateTime"], Qt.DefaultLocaleLongDate)
  text: Qt.formatDate(timeSource.data["Local"]["DateTime"], "yyyy-MM-dd")

`Reference <https://askubuntu.com/questions/783184/how-to-display-kde-lock-screen-time-in-24-hour-format>`__
