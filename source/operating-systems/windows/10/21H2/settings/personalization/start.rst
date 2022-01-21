.. _w10-21h2-settings-personalization-start:

Start
#####
.. todo::
  ``Show more tiles on Start`` updates a database, not the registry or GPO as
  Internet sources specify. `Reference <https://www.windowsphoneinfo.com/threads/turn-on-or-off-show-more-tiles-on-start-in-windows-10.7039/>`_.

.. gpo::   Disable Show recently added apps
  :path:   Computer Configuration -->
           Administrative Templates -->
           Start Menu and Taskbar -->
           Remove "Recently Added" list from Start Menu
  :value0: ☑, {ENABLED}
  :ref:    https://social.technet.microsoft.com/Forums/windows/en-US/9fe12468-46d9-4efb-b4ed-2df4dd2204c5/group-policy-show-recently-added-apps?forum=win10itprogeneral
  :update: 2021-02-19

.. _w10-21h2-settings-personalization-start-most-used-apps:

.. dropdown:: Disable Show most used apps
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. gpo::    Disable Show most used apps
    :path:    Computer Configuration -->
              Administrative Templates -->
              Start Menu and Taskbar -->
              Remove frequent programs list from the Start Menu
    :value0:  ☑, {ENABLED}
    :ref:     https://superuser.com/questions/1344696/windows-10-changing-the-show-the-most-used-apps-to-on-through-registry-gpo
    :update:  2021-02-19
    :generic:
    :open:

.. dropdown:: Disable Show suggestions occasionally in Start
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  GPO settings apply in ``Education`` and ``Enterprise`` Windows versions but
  should be set regardless.

  See :ref:`w10-21h2-settings-privacy-diagnostics-and-feedback-tailored-experiences`.

  `Reference <https://www.tenforums.com/tutorials/38945-enable-disable-app-suggestions-start-windows-10-a.html>`__

.. dropdown:: Disable Use Start full screen
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. gpo::    Disable Use Start full screen
    :path:    Computer Configuration -->
              Administrative Templates -->
              Start Menu and Taskbar -->
              Force Start to be either full screen or menu size
    :value0:  ☑, {ENABLED}
    :value1:  ›, Start menu
    :ref:     https://www.tenforums.com/tutorials/3680-turn-off-full-screen-start-menu-windows-10-a.html#option2
    :update:  2021-02-19
    :generic:
    :open:

.. dropdown:: Disable Show recently opened items in Jump Lists on Start or the
              taskbar and in File Explorer Quick Access
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. gpo::    Disable Show recently opened items in Jump Lists on Start or
              the taskbar and in File Explorer Quick Access
    :path:    Computer Configuration -->
              Administrative Templates -->
              Start Menu and Taskbar -->
              Do not keep history of recently opened documents
    :value0:  ☑, {ENABLED}
    :ref:     https://www.download3k.com/articles/How-to-Disable-Recent-Items-and-Frequent-Places-in-Windows-10-01398
    :update:  2021-02-19
    :generic:
    :open:
