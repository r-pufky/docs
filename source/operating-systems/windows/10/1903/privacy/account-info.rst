.. _w10-1903-reasonable-privacy-account-info:

Account Info
############
:cmdmenu:`⌘ + r --> ms-settings:privacy-accountinfo`

.. dropdown:: Allow access to account info on this device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  This disables all account info options. See
  :ref:`Allow apps to access your account info <w10-1903-privacy-account-info>`
  to manage access on a per app basis.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    ``Allow`` to enable access to account info.

    .. wregedit:: Disable access to account info on this device
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
                  CapabilityAccessManager\ConsentStore\userAccountInformation
      :names:     Value
      :types:     SZ
      :data:      Deny
      :no_section:
      :no_caption:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

    .. wgpolicy:: Disable apps access your account info
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
      :no_caption:

.. _w10-1903-privacy-account-info:

.. dropdown:: Allow apps to access your account info
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more fine
  grained control of app access.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    ``0`` enables apps access to account info.

    .. wregedit:: Disable apps to access your account info
      :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
      :names:     LetAppsAccessAccountInfo
      :types:     DWORD
      :data:      2
      :no_section:
      :no_caption:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

    .. wgpolicy:: Disable apps access your account info
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
      :no_caption:

.. rubric:: Rreferences

#. `Account Info Windows Management Settings <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#187-account-info>`_
