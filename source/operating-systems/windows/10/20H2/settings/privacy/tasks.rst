.. _w10-20h2-settings-privacy-tasks:

Tasks
#####
:cmdmenu:`⌘ + r --> ms-settings:privacy-tasks`

See :ref:`wbase-determining-app-list` to generate a list of apps for more fine
grained control of app access.

Allow access to tasks on this device
************************************
.. dropdown:: Disable Allow access to tasks on this device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  This disables all email options. See
  :ref:`w10-20h2-settings-privacy-tasks-apps` to manage access on a per app
  basis.

  .. gpo::    Disable Allow access to tasks on this device
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

  .. regedit:: Disable Allow access to tasks on this device
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
               CapabilityAccessManager\ConsentStore\userDataTasks
    :value0:   Value, {SZ}, Deny
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1819-tasks
    :update:   2021-02-19
    :generic:
    :open:

    ``Allow`` enable access to tasks on this device.

.. _w10-20h2-settings-privacy-tasks-apps:

Allow apps to access your tasks
*******************************
.. dropdown:: Disable Allow apps to access your tasks
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

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

  .. regedit:: Disable apps to access your tasks
    :path:     HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
    :value0:   LetAppsAccessTasks, {DWORD}, 2
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1819-tasks
    :update:   2021-02-19
    :generic:
    :open:

    ``0`` enables apps access to your tasks.

Choose which apps can access your tasks
***************************************
See :ref:`w10-20h2-settings-privacy-tasks-apps`.
