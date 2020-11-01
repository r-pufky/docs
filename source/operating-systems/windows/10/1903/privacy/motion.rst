.. _w10-1903-reasonable-privacy-motion:

Motion
######
:cmdmenu:`⌘ + r --> ms-settings:privacy-motion`

.. note::
  Only displayed in GUI if motion detection device is present (e.g. phone,
  pedometer, etc.). Can still be disabled.

.. rubric:: Let Windows and your apps use your motion data and collect motion
            history

.. wregedit:: Disable apps use your motion data and collect motion history via
              Registry
  :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
  :names:     LetAppsAccessMotion
  :types:     DWORD
  :data:      2
  :no_section:

.. wgpolicy:: Disable apps use your motion data and collect motion history via
              machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              App Privacy -->
              Let Windows apps access motion
  :option:    ☑,
              Default for all apps
  :setting:   Enabled,
              Force Deny
  :no_section:
  :no_launch:

.. rubric:: Rreferences

#. `Motion Windows Management Settings <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1818-motion>`_