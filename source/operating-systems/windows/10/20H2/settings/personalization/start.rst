.. _w10-20h2-settings-personalization-start:

Start
#####
.. TODO::
  ``Show more tiles on Start`` updates a database, not the registry or GPO as
  Internet sources specify. `Reference <https://www.windowsphoneinfo.com/threads/turn-on-or-off-show-more-tiles-on-start-in-windows-10.7039/>`_.

.. dropdown:: Disable Show recently added apps 
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Disable Show recently added apps
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Start Menu and Taskbar -->
                  Remove "Recently Added" list from Start Menu
      :option:    ☑
      :setting:   Enabled
      :no_section:
      :no_caption:

  `Reference <https://social.technet.microsoft.com/Forums/windows/en-US/9fe12468-46d9-4efb-b4ed-2df4dd2204c5/group-policy-show-recently-added-apps?forum=win10itprogeneral>`__

.. _w10-20h2-settings-personalization-start-most-used-apps:

.. dropdown:: Disable Show most used apps
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Disable Show most used apps
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Start Menu and Taskbar -->
                  Remove frequent programs list from the Start Menu
      :option:    ☑
      :setting:   Enabled
      :no_section:
      :no_caption:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Disable Show most used apps
      :key_title: HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion
                  Explorer\Advanced
      :names:     Start_TrackProgs
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

  `Reference <https://superuser.com/questions/1344696/windows-10-changing-the-show-the-most-used-apps-to-on-through-registry-gpo>`__

.. dropdown:: Disable Show suggestions occasionally in Start
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  GPO settings apply in ``Education`` and ``Enterprise`` Windows versions but
  should be set regardless.

  See :ref:`w10-20h2-settings-privacy-diagnostics-and-feedback-tailored-experiences`.

  `Reference <https://www.tenforums.com/tutorials/38945-enable-disable-app-suggestions-start-windows-10-a.html>`__

.. dropdown:: Disable Use Start full screen
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Disable Use Start full screen
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Start Menu and Taskbar -->
                  Force Start to be either full screen or menu size
      :option:    ☑,
                  ›
      :setting:   Enabled,
                  Start menu
      :no_section:
      :no_caption:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    ``2`` will force fullscreen start menu.

    .. wregedit:: Disable Use Start full screen
      :key_title: HHKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Explorer
      :names:     ForceStartSize
      :types:     DWORD
      :data:      1
      :no_section:
      :no_caption:

  `Reference <https://www.tenforums.com/tutorials/3680-turn-off-full-screen-start-menu-windows-10-a.html#option2>`__

.. dropdown:: Disable Show recently opened items in Jump Lists on Start or the
              taskbar and in File Explorer Quick Access
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Disable Show recently opened items in Jump Lists on Start or
                  the taskbar and in File Explorer Quick Access
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Start Menu and Taskbar -->
                  Do not keep history of recently opened documents
      :option:    ☑
      :setting:   Enabled
      :no_section:
      :no_caption:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Disable Show recently opened items in Jump Lists on Start or
                  the taskbar and in File Explorer Quick Access
      :key_title: HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion
                  Explorer\Advanced
      :names:     Start_TrackDocs
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

  `Reference <https://www.download3k.com/articles/How-to-Disable-Recent-Items-and-Frequent-Places-in-Windows-10-01398>`__
