.. _w10-1903-reasonable-privacy-calendar:

Calendar
########
:cmdmenu:`⌘ + r --> ms-settings:privacy-calendar`

.. dropdown:: Allow access to calendar on this device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  This disables all calendar value0s. See
  :ref:`Allow apps to access your contacts <w10-1903-privacy-calendar>` to
  manage access on a per app basis.

  .. gpo::    Disable apps access your contacts
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              App Privacy -->
              Let Windows apps access the calendar
    :value0:  ☑, {ENABLED}
              Default for all apps, Force Deny
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#189-calendar
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable access to calendar on this device
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
               CapabilityAccessManager\ConsentStore\appointments
    :value0:   Value, {SZ}, Deny
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#189-calendar
    :update:   2021-02-19
    :generic:
    :open:

    ``Allow`` to enable access to calednar on this device.

.. _w10-1903-privacy-calendar:

.. dropdown:: Allow apps to access your contacts
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more fine
  grained control of app access.

  .. gpo::    Disable apps access your contacts
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              App Privacy -->
              Let Windows apps access the calendar
    :value0:  ☑, {ENABLED}
              Default for all apps, Force Deny
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#189-calendar
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable apps to access your contacts
    :path:     HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
    :value0:   LetAppsAccessCalendar, {DWORD}, 2
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#189-calendar
    :update:   2021-02-19
    :generic:
    :open:

    ``0`` to enable apps access to contacts.
