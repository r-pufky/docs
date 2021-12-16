.. _w10-1903-reasonable-privacy-email:

Email
#####
:cmdmenu:`⌘ + r --> ms-settings:privacy-email`

.. dropdown:: Allow access to email on this device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  This disables all email value0s. See
  :ref:`Allow apps to access your email <w10-1903-privacy-email>` to manage
  access on a per app basis.

  .. gpo::   Disable apps access your email
    :path:   Computer Configuration -->
             Administrative Templates -->
             Windows Components -->
             App Privacy -->
             Let Windows apps access email
    :value0: ☑, {ENABLED}
    :value1: Default for all apps, Force Deny
    :ref:    https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1811-email
    :update: 2021-02-19
    :generic:
    :open:

  .. regedit:: Disable access to email on this device
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
               CapabilityAccessManager\ConsentStore\email
    :value0:   Value, {SZ}, Deny
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1811-email
    :update:   2021-02-19
    :generic:
    :open:

    ``Allow`` enables access to email on this device.

.. _w10-1903-privacy-email:

.. dropdown:: Allow apps to access your email
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more fine
  grained control of app access.

  .. gpo::    Disable apps access your email
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

  .. regedit:: Disable apps to access your email
    :path:     HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
    :value0:   LetAppsAccessEmail, {DWORD}, 2
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1811-email
    :update:   2021-02-19
    :generic:
    :open:

    ``0`` enables apps access to email.
