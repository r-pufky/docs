.. _w10-20h2-settings-privacy-tasks:

Tasks
#####
:cmdmenu:`⌘ + r --> ms-settings:privacy-tasks`

See :ref:`w10-determining-app-list` to generate a list of apps for more fine
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

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Disable Allow access to tasks on this device
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  App Privacy -->
                  Let Windows apps access Tasks
      :option:    ☑,
                  Default for all apps
      :setting:   Enabled,
                  Force Deny
      :no_section:
      :no_caption:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    ``Allow`` enable access to tasks on this device.

    .. wregedit:: Disable Allow access to tasks on this device
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
                  CapabilityAccessManager\ConsentStore\userDataTasks
      :names:     Value
      :types:     SZ
      :data:      Deny
      :no_section:
      :no_caption:

  `Reference <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1819-tasks>`__

.. _w10-20h2-settings-privacy-tasks-apps:

Allow apps to access your tasks
*******************************
.. dropdown:: Disable Allow apps to access your tasks
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Disable apps access your tasks
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  App Privacy -->
                  Let Windows apps access Tasks
      :option:    ☑,
                  Default for all apps
      :setting:   Enabled,
                  Force Deny
      :no_section:
      :no_caption:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    ``0`` enables apps access to your tasks.

    .. wregedit:: Disable apps to access your tasks
      :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
      :names:     LetAppsAccessTasks
      :types:     DWORD
      :data:      2
      :no_section:
      :no_caption:

  `Reference <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1819-tasks>`__

Choose which apps can access your tasks
***************************************
See :ref:`w10-20h2-settings-privacy-tasks-apps`.
