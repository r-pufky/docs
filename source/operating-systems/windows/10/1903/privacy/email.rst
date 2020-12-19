.. _w10-1903-reasonable-privacy-email:

Email
#####
:cmdmenu:`⌘ + r --> ms-settings:privacy-email`

.. dropdown:: Allow access to email on this device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in
  
  This disables all email options. See
  :ref:`Allow apps to access your email <w10-1903-privacy-email>` to manage
  access on a per app basis.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    ``Allow`` enables access to email on this device.

    .. wregedit:: Disable access to email on this device
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
                  CapabilityAccessManager\ConsentStore\email
      :names:     Value
      :types:     SZ
      :data:      Deny
      :no_section:
      :no_caption:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

    .. wgpolicy:: Disable apps access your email
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

.. _w10-1903-privacy-email:

.. dropdown:: Allow apps to access your email
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in
  
  See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more fine
  grained control of app access.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    ``0`` enables apps access to email.

    .. wregedit:: Disable apps to access your email
      :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
      :names:     LetAppsAccessEmail
      :types:     DWORD
      :data:      2
      :no_section:
      :no_caption:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

    .. wgpolicy:: Disable apps access your email
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

.. rubric:: Rreferences

#. `Email Windows Management Settings <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1811-email>`_
