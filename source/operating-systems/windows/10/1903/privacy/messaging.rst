.. _w10-1903-reasonable-privacy-messaging:

Messaging
#########
:cmdmenu:`⌘ + r --> ms-settings:privacy-messaging`

.. rubric:: Allow access to messaging on this device

.. note::
  This disables all email options. See
  :ref:`w10-1903-privacy-messaging` to manage access on a per app basis.

.. wregedit:: Disable access to messaging on this device via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
              CapabilityAccessManager\ConsentStore\chat
  :names:     Value
  :types:     SZ
  :data:      Deny
  :no_section:

.. _w10-1903-privacy-messaging:

.. rubric:: Allow apps to read or send messages

.. wregedit:: Disable apps to access your messaging via Registry
  :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
  :names:     LetAppsAccessMessaging
  :types:     DWORD
  :data:      2
  :no_section:

    .. note::
      See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more
      fine grained control of app access.

.. wgpolicy:: Disable apps access your messaging via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              App Privacy -->
              Let Windows apps access messaging
  :option:    ☑,
              Default for all apps
  :setting:   Enabled,
              Force Deny
  :no_section:

    .. note::
      See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more
      fine grained control of app access.

.. rubric:: Turn off message sync

.. note::
  This is not available in the GUI.

.. wregedit:: Disable message sync via Registry
  :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\Messaging
  :names:     AllowMessageSync
  :types:     DWORD
  :data:      0
  :no_section:


.. wgpolicy:: Disable message sync via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Messaging -->
              Allow Message Service Cloud Sync
  :option:    ☑
  :setting:   Disabled
  :no_section:

.. rubric:: Rreferences

#. `Messaging Windows Management Settings <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1812-messaging>`_