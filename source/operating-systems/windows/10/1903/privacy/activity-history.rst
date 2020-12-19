.. _w10-1903-reasonable-privacy-activity-history:

Activity History
################
:cmdmenu:`⌘ + r --> ms-settings:privacy-activityhistory`

.. dropdown:: Store my activity history on this device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Disable storing activity history.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Disable storing of activity history
      :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\System
      :names:     PublishUserActivities
      :types:     DWORD
      :data:      2
      :no_section:
      :no_caption:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

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

.. dropdown:: Send my activity history to Microsoft
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Disable sending activity to Microsoft.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Disable sending activity history to Microsoft
      :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\System
      :names:     UploadUserActivities
      :types:     DWORD
      :data:      2
      :no_section:
      :no_caption:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

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

.. dropdown:: Activity history
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Disable activity history.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Disable activity history
      :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\System
      :names:     EnableActivityFeed
      :types:     DWORD
      :data:      2
      :no_section:
      :no_caption:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

    .. wgpolicy:: Disable activity history
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  System -->
                  OS Policies -->
                  Enables Activity Feed
      :option:    ☑
      :setting:   Disabled
      :no_section:
      :no_caption:

.. rubric:: Rreferences

#. `Activity History Windows Management Settings <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1822-activity-history>`_
