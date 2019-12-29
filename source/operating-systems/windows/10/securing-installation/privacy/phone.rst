.. _windows-10-reasonable-privacy-phone:

Phone Calls
###########
:cmdmenu:`⌘ + r --> ms-settings:privacy-phonecalls`

.. note::
  Only displayed in GUI if phone device is present. Can still be disabled.

.. rubric:: Let apps make phone calls

.. wregedit:: Disable apps make phone calls via Registry
  :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
  :names:     LetAppsAccessPhone
  :types:     DWORD
  :data:      2
  :no_section:

.. wgpolicy:: Disable apps make phone calls via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              App Privacy -->
              Let Windows apps make phone calls
  :option:    ☑,
              Default for all apps
  :setting:   Enabled,
              Force Deny
  :no_section:

.. rubric:: Rreferences

#. `Phone Call Windows Management Settings <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1813-phone-calls>`_