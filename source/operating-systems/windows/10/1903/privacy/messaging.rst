.. _w10-1903-reasonable-privacy-messaging:

Messaging
#########
:cmdmenu:`⌘ + r --> ms-settings:privacy-messaging`

.. rubric:: Allow access to messaging on this device

.. dropdown:: Allow access to messaging on this device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  This disables all messaging options. See
  :ref:`Allow apps to read or send messages <w10-1903-privacy-messaging>` to
  manage access on a per app basis.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    ``Allow`` enables access to messaging on this device.

    .. wregedit:: Disable access to messaging on this device
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
                  CapabilityAccessManager\ConsentStore\chat
      :names:     Value
      :types:     SZ
      :data:      Deny
      :no_section:
      :no_caption:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

    .. wgpolicy:: Disable apps access your messaging
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
      :no_caption:

.. _w10-1903-privacy-messaging:

.. dropdown:: Allow apps to read or send messages
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more fine
  grained control of app access.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    ``0`` enabels apps access to messaging.

    .. wregedit:: Disable apps to access your messaging
      :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
      :names:     LetAppsAccessMessaging
      :types:     DWORD
      :data:      2
      :no_section:
      :no_caption:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

    .. wgpolicy:: Disable apps access your messaging
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
      :no_caption:

.. dropdown:: Turn off message sync
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  This is not available in the GUI.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    ``1`` enable message sync.

    .. wregedit:: Disable message sync
      :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\Messaging
      :names:     AllowMessageSync
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

    .. wgpolicy:: Disable message sync
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Messaging -->
                  Allow Message Service Cloud Sync
      :option:    ☑
      :setting:   Disabled
      :no_section:
      :no_caption:

.. rubric:: Rreferences

#. `Messaging Windows Management Settings <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1812-messaging>`_
