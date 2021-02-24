.. _w10-1903-reasonable-privacy-call-history:

Call History
############
:cmdmenu:`⌘ + r --> ms-settings:privacy-callhistory`

.. dropdown:: Allow access to call history on this device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  This disables all call history value0s. See
  :ref:`Allow apps to access your call history <w10-1903-privacy-call-history>`
  to manage access on a per app basis.

  .. gpo::    Disable apps access your call history
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              App Privacy -->
              Let Windows apps access call history
    :value0:  ☑, {ENABLED}
    :value1:  Default for all apps, Force Deny
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1810-call-history
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable access to call history on this device
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
               CapabilityAccessManager\ConsentStore\phoneCallHistory
    :value0:   Value, {SZ}, Deny
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1810-call-history
    :update:   2021-02-19
    :generic:
    :open:

    ``Allow`` to enable call history.

.. _w10-1903-privacy-call-history:

.. dropdown:: Allow apps to access your call history
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more fine
  grained control of app access.

  .. gpo::    Disable apps access your call history
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              App Privacy -->
              Let Windows apps access call history
    :value0:  ☑, {ENABLED}
    :value1:  Default for all apps, Force Deny
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1810-call-history
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable apps to access your call history
    :path:     HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
    :value0:   LetAppsAccessCallHistory, {DWORD}, 2
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1810-call-history
    :update:   2021-02-19
    :generic:
    :open:

    ``0`` to enable app access to call history.
