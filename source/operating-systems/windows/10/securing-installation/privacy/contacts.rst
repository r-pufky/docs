.. _windows-10-reasonable-privacy-contacts:

Contacts
########
:cmdmenu:`⌘ + r --> ms-settings:privacy-contacts`

.. rubric:: Allow access to contacts on this device

.. note::
  This disables all contacts options. See
  :ref:`windows-10-privacy-contacts` to manage access on a per app basis.

.. wregedit:: Disable access to user notifications on this device via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
              CapabilityAccessManager\ConsentStore\contacts
  :names:     Value
  :types:     SZ
  :data:      Deny
  :no_section:

.. _windows-10-privacy-contacts:

.. rubric:: Allow apps to access your contacts

.. wregedit:: Disable apps to access your contacts via Registry
  :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
  :names:     LetAppsAccessContacts
  :types:     DWORD
  :data:      2
  :no_section:

    .. note::
      See :ref:`windows-10-privacy-app-list` to generate a list of apps for more
      fine grained control of app access.

.. wgpolicy:: Disable apps access your contacts via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              App Privacy -->
              Let Windows apps access contacts
  :option:    ☑,
              Default for all apps
  :setting:   Enabled,
              Force Deny
  :no_section:

    .. note::
      See :ref:`windows-10-privacy-app-list` to generate a list of apps for more
      fine grained control of app access.

.. rubric:: Rreferences

#. `Contacts Windows Management Settings <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#188-contacts>`_