.. _w10-20h2-settings-privacy-calendar:

Calendar
########
:cmdmenu:`⌘ + r --> ms-settings:privacy-calendar`

See :ref:`w10-determining-app-list` to generate a list of apps for more fine
grained control of app access.

Allow access to calendar on this device
***************************************
.. dropdown:: Disable Allow access to calendar on this device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  This disables all calendar options. See
  :ref:`w10-20h2-settings-privacy-calendar-apps` to manage access on a per app
  basis.

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Disable apps access your contacts
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  App Privacy -->
                  Let Windows apps access the calendar
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

    ``Allow`` to enable access to calednar on this device.

    .. wregedit:: Disable access to calendar on this device
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
                  CapabilityAccessManager\ConsentStore\appointments
      :names:     Value
      :types:     SZ
      :data:      Deny
      :no_section:
      :no_caption:

  `Reference <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#189-calendar>`__

.. _w10-20h2-settings-privacy-calendar-apps:

Allow apps to access your contacts
**********************************
.. dropdown:: Disable Allow apps to access your contacts
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Disable apps access your contacts
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  App Privacy -->
                  Let Windows apps access the calendar
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

    ``0`` to enable apps access to contacts.

    .. wregedit:: Disable apps to access your contacts
      :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
      :names:     LetAppsAccessCalendar
      :types:     DWORD
      :data:      2
      :no_section:
      :no_caption:

  `Reference <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#189-calendar>`__

Choose which apps can access your calendar
******************************************
See :ref:`w10-20h2-settings-privacy-calendar-apps`.
