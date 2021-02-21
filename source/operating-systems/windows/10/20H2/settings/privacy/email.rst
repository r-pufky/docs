.. _w10-20h2-settings-privacy-email:

Email
#####
:cmdmenu:`⌘ + r --> ms-settings:privacy-email`
  
See :ref:`w10-determining-app-list` to generate a list of apps for more fine
grained control of app access.

Allow access to email on this device
************************************
.. dropdown:: Disable Allow access to email on this device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in
  
  This disables all email options. See
  :ref:`w10-20h2-settings-privacy-email-apps` to manage access on a per app
  basis.

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Disable Allow access to email on this device
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
      :no_caption:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    ``Allow`` enables access to email on this device.

    .. wregedit:: Disable Allow access to email on this device
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
                  CapabilityAccessManager\ConsentStore\email
      :names:     Value
      :types:     SZ
      :data:      Deny
      :no_section:
      :no_caption:

  `References <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1811-email>`__

.. _w10-20h2-settings-privacy-email-apps:

Allow apps to access your email
*******************************
.. dropdown:: Allow apps to access your email
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Disable Allow apps access your email
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
      :no_caption:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    ``0`` enables apps access to email.

    .. wregedit:: Disable Allow apps to access your email
      :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
      :names:     LetAppsAccessEmail
      :types:     DWORD
      :data:      2
      :no_section:
      :no_caption:

  `References <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1811-email>`__

Choose which apps can access your email
***************************************
See :ref:`w10-20h2-settings-privacy-email-apps`.
