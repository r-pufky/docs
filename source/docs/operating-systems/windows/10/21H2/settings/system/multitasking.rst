.. _w10-21h2-settings-system-multitasking:

Multitasking
############

.. _w10-21h2-settings-system-timeline-suggestions:

Timeline
********

.. dropdown:: Disable show suggestions in your timeline
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  App usage is recorded to show suggestions.

  .. regedit:: Disable show suggestions in your timeline
    :path:     HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\
               ContentDeliveryManager
    :value0:   SubscribedContent-353698Enabled, {DWORD}, 0
    :ref:      https://www.tenforums.com/tutorials/102071-turn-off-timeline-suggestions-windows-10-a.html
    :update:   2021-02-19
    :generic:
    :open:

  .. gpo::    Disable timeline
    :path:    Computer Configuration -->
              Administrative Templates -->
              System -->
              OS Policies -->
              Enables Activity Feed
    :value0:  ☑, {DISABLED}
    :ref:     https://www.top-password.com/blog/disable-windows-10-timeline-with-group-policy/
    :update:  2021-02-19
    :generic:
    :open:

.. regedit:: Remove Edge tabs from alt+tab nagivation
  :path:     HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\
             Explorer\Advanced
  :value0:   MultiTaskingAltTabFilter, {DWORD}, 3
  :update:   2021-02-19

  :cmdmenu:`alt` + :cmdmenu:`tab` is for OS window navigation, not OS+specific browser window
  navigation.
