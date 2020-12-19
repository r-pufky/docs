.. _w10-1903-reasonable-privacy-phone-calls:

Phone Calls
###########
:cmdmenu:`⌘ + r --> ms-settings:privacy-phonecalls`

.. note::
  Only displayed in GUI if phone device is present. Can still be disabled.

.. dropdown:: Allow phone calls on this device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more fine
  grained control of app access.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    ``0`` enable apps to make phone calls.

    .. wregedit:: Disable apps make phone calls
      :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
      :names:     LetAppsAccessPhone
      :types:     DWORD
      :data:      2
      :no_section:
      :no_caption:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

    .. wgpolicy:: Disable apps make phone calls
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
      :no_caption:

.. dropdown:: Allow consent for phone calls.
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more fine
  grained control of app access.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    ``Allow`` enable consent for phone calls.

    .. wregedit:: Disable consent for phone calls
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
                  CapabilityAccessManager\ConsentStore\phoneCall
      :names:     Value
      :types:     SZ
      :data:      Deny
      :no_section:
      :no_caption:

.. rubric:: Rreferences

#. `Phone Call Windows Management Settings <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1813-phone-calls>`_
