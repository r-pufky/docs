.. _w10-20h2-settings-privacy-activity-history:

Activity History
################
:cmdmenu:`⌘ + r --> ms-settings:privacy-activityhistory`

.. dropdown:: Disable Store my activity history on this device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Disable storing activity history.

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Disable storing of activity history
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  System -->
                  OS Policies -->
                  Allow publishing of User Activites
      :option:    ☑
      :setting:   Disabled
      :no_section:
      :no_caption:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Disable storing of activity history
      :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\System
      :names:     PublishUserActivities
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

  `Reference <https://www.tenforums.com/tutorials/100341-enable-disable-collect-activity-history-windows-10-a.html>`__

.. dropdown:: Disable Send my activity history to Microsoft
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Disable sending activity to Microsoft. Apply timeline changes as well
  :ref:`w10-20h2-settings-system-timeline-suggestions`.

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Disable sending activity history to Microsoft
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  System -->
                  OS Policies -->
                  Allow upload of User Activities
      :option:    ☑
      :setting:   Disabled
      :no_section:
      :no_caption:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Disable sending activity history to Microsoft
      :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\System
      :names:     UploadUserActivities
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

  `Reference <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1822-activity-history>`__
