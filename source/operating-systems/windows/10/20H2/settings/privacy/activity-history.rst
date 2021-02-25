.. _w10-20h2-settings-privacy-activity-history:

Activity History
################
:cmdmenu:`⌘ + r --> ms-settings:privacy-activityhistory`

.. dropdown:: Disable Store my activity history on this device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Disable storing activity history.

  .. gpo::    Disable storing of activity history
    :path:    Computer Configuration -->
              Administrative Templates -->
              System -->
              OS Policies -->
              Allow publishing of User Activites
    :value0:  ☑, {DISABLED}
    :ref:     https://www.tenforums.com/tutorials/100341-enable-disable-collect-activity-history-windows-10-a.html
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable storing of activity history
    :path:     HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\System
    :value0:   PublishUserActivities, {DWORD}, 0
    :ref:      https://www.tenforums.com/tutorials/100341-enable-disable-collect-activity-history-windows-10-a.html
    :update:   2021-02-19
    :generic:
    :open:

.. dropdown:: Disable Send my activity history to Microsoft
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Disable sending activity to Microsoft. Apply timeline changes as well
  :ref:`w10-20h2-settings-system-timeline-suggestions`.

  .. gpo::    Disable sending activity history to Microsoft
    :path:    Computer Configuration -->
              Administrative Templates -->
              System -->
              OS Policies -->
              Allow upload of User Activities
    :value0:  ☑, {DISABLED}
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1822-activity-history
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable sending activity history to Microsoft
    :path:     HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\System
    :value0:   UploadUserActivities, {DWORD}, 0
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1822-activity-history
    :update:   2021-02-19
    :generic:
    :open:
