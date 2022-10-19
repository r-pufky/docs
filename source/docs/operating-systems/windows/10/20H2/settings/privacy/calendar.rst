.. _w10-20h2-settings-privacy-calendar:

Calendar
########
:cmdmenu:`⌘ + r --> ms-settings:privacy-calendar`

See :ref:`wbase-determining-app-list` to generate a list of apps for more fine
grained control of app access.

Allow access to calendar on this device
***************************************
.. dropdown:: Disable Allow access to calendar on this device
  :color: primary
  :icon: note
  :animate: fade-in
  :class-container: sd-shadow-sm

  This disables all calendar options. See
  :ref:`w10-20h2-settings-privacy-calendar-apps` to manage access on a per app
  basis.

  .. gpo::    Disable apps access your contacts
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              App Privacy -->
              Let Windows apps access the calendar
    :value0:  ☑, {ENABLED}
    :value1:  Default for all apps, Force Deny
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#189-calendar
    :update:  2021-02-19
    :generic:
    :open:

    ``Allow`` to enable access to calednar on this device.

  .. regedit:: Disable access to calendar on this device
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
               CapabilityAccessManager\ConsentStore\appointments
    :value0:   Value, {SZ}, Deny
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#189-calendar
    :update:   2021-02-19
    :generic:
    :open:

.. _w10-20h2-settings-privacy-calendar-apps:

Allow apps to access your contacts
**********************************
.. dropdown:: Disable Allow apps to access your contacts
  :color: primary
  :icon: note
  :animate: fade-in
  :class-container: sd-shadow-sm

  .. gpo::    Disable apps access your contacts
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              App Privacy -->
              Let Windows apps access the calendar
    :value0:  ☑, {ENABLED}
    :value1:  Default for all apps, Force Deny
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#189-calendar
    :update:  2021-02-19
    :generic:
    :open:

    ``0`` to enable apps access to contacts.

  .. regedit:: Disable apps to access your contacts
    :path:     HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
    :value0:   LetAppsAccessCalendar, {DWORD}, 2
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#189-calendar
    :update:   2021-02-19
    :generic:
    :open:

Choose which apps can access your calendar
******************************************
See :ref:`w10-20h2-settings-privacy-calendar-apps`.
