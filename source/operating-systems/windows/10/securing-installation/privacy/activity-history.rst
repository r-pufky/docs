.. _windows-10-reasonable-privacy-activity-history:

Activity History
################
:cmdmenu:`⌘ + r --> ms-settings:privacy-activityhistory`

.. rubric:: Store my activity history on this device

.. wregedit:: Disable storing of activity history via Registry
  :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\System
  :names:     PublishUserActivities
  :types:     DWORD
  :data:      2
  :no_section:

.. wgpolicy:: Disable storing of activity history via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              System -->
              OS Policies -->
              Allow publishing of User Activites
  :option:    ☑
  :setting:   Disabled
  :no_section:

.. rubric:: Send my activity history to Microsoft

.. wregedit:: Disable sending activity history to Microsoft via Registry
  :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\System
  :names:     UploadUserActivities
  :types:     DWORD
  :data:      2
  :no_section:

.. wgpolicy:: Disable sending activity history to Microsoft via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              System -->
              OS Policies -->
              Allow upload of User Activities
  :option:    ☑
  :setting:   Disabled
  :no_section:

.. rubric:: Activity history

.. wregedit:: Disable activity history via Registry
  :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\System
  :names:     EnableActivityFeed
  :types:     DWORD
  :data:      2
  :no_section:

.. wgpolicy:: Disable activity history via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              System -->
              OS Policies -->
              Enables Activity Feed
  :option:    ☑
  :setting:   Disabled
  :no_section:

.. rubric:: Rreferences

#. `Activity History Windows Management Settings <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1822-activity-history>`_