.. _w10-20h2-multitasking:

Multitasking
############

Timeline
********

.. _w10-20h2-timeline-suggestions:

.. dropdown:: Disable show suggestions in your timeline
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  App usage is recorded to show suggestions.

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    `Reference <https://www.top-password.com/blog/disable-windows-10-timeline-with-group-policy/>`_

    .. wgpolicy:: Disable timeline
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  System -->
                  OS Policies -->
                  Enables Activity Feed
      :option:    ☑
      :setting:   Disabled
      :no_section:
      :no_caption:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    `Reference <https://www.tenforums.com/tutorials/102071-turn-off-timeline-suggestions-windows-10-a.html>`_

    .. wregedit:: Disable show suggestions in your timeline
      :key_title: HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\
                  ContentDeliveryManager
      :names:     SubscribedContent-353698Enabled
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

    `Reference <https://www.top-password.com/blog/disable-windows-10-timeline-with-group-policy/>`_

    .. wregedit:: Disable timeline
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\System
      :names:     EnableActivityFeed
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:
      :no_launch:

.. dropdown:: Remove Edge tabs from alt+tab navigation
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  :cmdmenu:`alt` + :cmdmenu:`tab` is for OS window navigation, not OS+specific browser window
  navigation.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Remove Edge tabs from alt+tab nagivation
      :key_title: HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\
                  Explorer\Advanced
      :names:     MultiTaskingAltTabFilter
      :types:     DWORD
      :data:      3
      :no_section:
      :no_caption:
