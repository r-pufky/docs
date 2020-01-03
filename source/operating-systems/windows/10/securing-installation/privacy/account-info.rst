.. _windows-10-reasonable-privacy-account-info:

Account Info
############
:cmdmenu:`⌘ + r --> ms-settings:privacy-accountinfo`

.. rubric:: Allow access to account info on this device

.. note::
  This disables all account info options. See
  :ref:`windows-10-privacy-account-info` to manage access on a per app basis.

.. wregedit:: Disable access to account info on this device via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
              CapabilityAccessManager\ConsentStore\userAccountInformation
  :names:     Value
  :types:     SZ
  :data:      Deny
  :no_section:

.. _windows-10-privacy-account-info:

.. rubric:: Allow apps to access your account info

.. wregedit:: Disable apps to access your account info via Registry
  :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
  :names:     LetAppsAccessAccountInfo
  :types:     DWORD
  :data:      2
  :no_section:

    .. note::
      See :ref:`windows-10-privacy-app-list` to generate a list of apps for more
      fine grained control of app access.

.. wgpolicy:: Disable apps access your account info via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              App Privacy -->
              Let Windows apps access account information
  :option:    ☑,
              Default for all apps
  :setting:   Enabled,
              Force Deny
  :no_section:

    .. note::
      See :ref:`windows-10-privacy-app-list` to generate a list of apps for more
      fine grained control of app access.

.. rubric:: Rreferences

#. `Account Info Windows Management Settings <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#187-account-info>`_