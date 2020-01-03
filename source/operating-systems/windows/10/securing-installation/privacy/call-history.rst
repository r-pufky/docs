.. _windows-10-reasonable-privacy-call-history:

Call History
############
:cmdmenu:`⌘ + r --> ms-settings:privacy-callhistory`

.. rubric:: Allow access to call history on this device

.. note::
  This disables all call history options. See
  :ref:`windows-10-privacy-call-history` to manage access on a per app basis.

.. wregedit:: Disable access to call history on this device via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
              CapabilityAccessManager\ConsentStore\phoneCallHistory
  :names:     Value
  :types:     SZ
  :data:      Deny
  :no_section:

.. _windows-10-privacy-call-history:

.. rubric:: Allow apps to access your call history

.. wregedit:: Disable apps to access your call history via Registry
  :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
  :names:     LetAppsAccessCallHistory
  :types:     DWORD
  :data:      2
  :no_section:

    .. note::
      See :ref:`windows-10-privacy-app-list` to generate a list of apps for more
      fine grained control of app access.

.. wgpolicy:: Disable apps access your call history via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              App Privacy -->
              Let Windows apps access call history
  :option:    ☑,
              Default for all apps
  :setting:   Enabled,
              Force Deny
  :no_section:

    .. note::
      See :ref:`windows-10-privacy-app-list` to generate a list of apps for more
      fine grained control of app access.

.. rubric:: Rreferences

#. `Call History Windows Management Settings <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1810-call-history>`_