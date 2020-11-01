.. _w10-1903-reasonable-privacy-calendar:

Calendar
########
:cmdmenu:`⌘ + r --> ms-settings:privacy-calendar`

.. rubric:: Allow access to calendar on this device

.. note::
  This disables all calendar options. See
  :ref:`w10-1903-privacy-calendar` to manage access on a per app basis.

.. wregedit:: Disable access to calendar on this device via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
              CapabilityAccessManager\ConsentStore\appointments
  :names:     Value
  :types:     SZ
  :data:      Deny
  :no_section:

.. _w10-1903-privacy-calendar:

.. rubric:: Allow apps to access your contacts

.. wregedit:: Disable apps to access your contacts via Registry
  :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
  :names:     LetAppsAccessCalendar
  :types:     DWORD
  :data:      2
  :no_section:

    .. note::
      See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more
      fine grained control of app access.

.. wgpolicy:: Disable apps access your contacts via machine GPO
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

    .. note::
      See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more
      fine grained control of app access.

.. rubric:: Rreferences

#. `Calendar Windows Management Settings <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#189-calendar>`_