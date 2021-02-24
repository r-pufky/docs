.. _w10-1903-reasonable-privacy-tasks:

Tasks
#####
:cmdmenu:`⌘ + r --> ms-settings:privacy-tasks`

.. dropdown:: Allow access to tasks on this device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  This disables all email value0s. See
  :ref:`Allow apps to access your tasks <w10-1903-privacy-tasks>` to manage
  access on a per app basis.

  .. gpo::    Disable apps access your tasks
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              App Privacy -->
              Let Windows apps access Tasks
    :value0:  ☑, {ENABLED}
    :value1:  Default for all apps, Force Deny
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1819-tasks
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable access to tasks on this device
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
               CapabilityAccessManager\ConsentStore\userDataTasks
    :value0:   Value, {SZ}, Deny
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1819-tasks
    :update:   2021-02-19
    :generic:
    :open:

    ``Allow`` enable access to tasks on this device.

.. _w10-1903-privacy-tasks:

.. dropdown:: Allow apps to access your tasks
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more fine
  grained control of app access.

  .. gpo::    Disable apps access your tasks
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              App Privacy -->
              Let Windows apps access Tasks
    :value0:  ☑, {ENABLED}
              Default for all apps, Force Deny
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1819-tasks
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable apps to access your tasks
    :path:     HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
    :value0:   LetAppsAccessTasks, {DWORD}, 2
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1819-tasks
    :update:   2021-02-19
    :generic:
    :open:

    ``0`` enables apps access to your tasks.
