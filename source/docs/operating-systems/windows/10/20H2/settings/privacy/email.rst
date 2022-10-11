.. _w10-20h2-settings-privacy-email:

Email
#####
:cmdmenu:`⌘ + r --> ms-settings:privacy-email`

See :ref:`wbase-determining-app-list` to generate a list of apps for more fine
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

  .. gpo::    Disable Allow access to email on this device
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              App Privacy -->
              Let Windows apps access email
    :value0:  ☑, {ENABLED}
    :value1:  Default for all apps, Force Deny
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1811-email
    :update:  2021-02-19
    :generic:
    :open:

    ``Allow`` enables access to email on this device.

  .. regedit:: Disable Allow access to email on this device
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
               CapabilityAccessManager\ConsentStore\email
    :value0:   Value, {SZ}, Deny
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1811-email
    :update:  2021-02-19
    :generic:
    :open:

.. _w10-20h2-settings-privacy-email-apps:

Allow apps to access your email
*******************************
.. dropdown:: Allow apps to access your email
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. gpo::    Disable Allow apps access your email
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              App Privacy -->
              Let Windows apps access email
    :value0:  ☑, {ENABLED}
    :value1:  Default for all apps, Force Deny
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1811-email
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable Allow apps to access your email
    :path:     HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
    :value0:   LetAppsAccessEmail, {DWORD}, 2
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1811-email
    :update:   2021-02-19
    :generic:
    :open:

    ``0`` enables apps access to email.

Choose which apps can access your email
***************************************
See :ref:`w10-20h2-settings-privacy-email-apps`.
