.. _w10-1903-reasonable-privacy-email:

Email
#####
:cmdmenu:`⌘ + r --> ms-settings:privacy-email`

.. rubric:: Allow access to email on this device

.. note::
  This disables all email options. See
  :ref:`w10-1903-privacy-email` to manage access on a per app basis.

.. wregedit:: Disable access to email on this device via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
              CapabilityAccessManager\ConsentStore\email
  :names:     Value
  :types:     SZ
  :data:      Deny
  :no_section:

.. _w10-1903-privacy-email:

.. rubric:: Allow apps to access your email

.. wregedit:: Disable apps to access your email via Registry
  :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
  :names:     LetAppsAccessEmail
  :types:     DWORD
  :data:      2
  :no_section:

    .. note::
      See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more
      fine grained control of app access.

.. wgpolicy:: Disable apps access your email via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              App Privacy -->
              Let Windows apps access email
  :option:    ☑,
              Default for all apps
  :setting:   Enabled,
              Force Deny
  :no_section:

    .. note::
      See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more
      fine grained control of app access.

.. rubric:: Rreferences

#. `Email Windows Management Settings <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1811-email>`_