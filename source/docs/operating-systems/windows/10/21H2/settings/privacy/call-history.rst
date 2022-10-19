.. _w10-21h2-settings-privacy-call-history:

Call History
############
:cmdmenu:`⌘ + r --> ms-settings:privacy-callhistory`

See :ref:`wbase-determining-app-list` to generate a list of apps for more fine
grained control of app access.

Allow access to call history on this device
*******************************************
.. dropdown:: Disable Allow access to call history on this device
  :color: primary
  :icon: shield-lock
  :animate: fade-in
  :class-container: sd-shadow-sm

  This disables all call history options.

  .. gpo::    Disable apps access your call history on this device
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
