.. _w10-20h2-settings-privacy-call-history:

Call History
############
:cmdmenu:`⌘ + r --> ms-settings:privacy-callhistory`

See :ref:`w10-determining-app-list` to generate a list of apps for more fine
grained control of app access.

Allow access to call history on this device
*******************************************
.. dropdown:: Disable Allow access to call history on this device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  This disables all call history options. See
  :ref:`_w10-20h2-settings-privacy-call-history-apps` to manage access on a per
  app basis.

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Disable apps access your call history on this device
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
      :no_caption:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    ``Allow`` to enable call history.

    .. wregedit:: Disable access to call history on this device
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
                  CapabilityAccessManager\ConsentStore\phoneCallHistory
      :names:     Value
      :types:     SZ
      :data:      Deny
      :no_section:
      :no_caption:

  `Reference <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1810-call-history>`__

.. _w10-20h2-settings-privacy-call-history-apps:

Allow apps to access your call history
**************************************
.. dropdown:: Disable Allow apps to access your call history
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Disable apps access your call history
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
      :no_caption:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    ``0`` to enable app access to call history.

    .. wregedit:: Disable apps to access your call history
      :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
      :names:     LetAppsAccessCallHistory
      :types:     DWORD
      :data:      2
      :no_section:
      :no_caption:

  `Reference <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1810-call-history>`__

Choose which apps can access your call history
**********************************************
See :ref:`w10-20h2-settings-privacy-call-history-apps`.
