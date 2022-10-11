.. _w10-21h2-settings-privacy-tasks:

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

  This disables all email options.

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
