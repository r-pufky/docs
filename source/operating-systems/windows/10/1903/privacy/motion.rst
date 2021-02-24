.. _w10-1903-reasonable-privacy-motion:

Motion
######
:cmdmenu:`⌘ + r --> ms-settings:privacy-motion`

.. note::
  Only displayed in GUI if motion detection device is present (e.g. phone,
  pedometer, etc.). Can still be disabled.

.. dropdown:: Let Windows and your apps use your motion data and collect motion
              history
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in
  :open:

  Disable access to motion data.

  .. gpo::    Disable apps use your motion data and collect motion history
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              App Privacy -->
              Let Windows apps access motion
    :value0:  ☑, {ENABLED}
    :value1:  Default for all apps, Force Deny
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1818-motion
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable apps use your motion data and collect motion history
    :path:     HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
    :value0:   LetAppsAccessMotion, {DWORD}, 2
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1818-motion
    :update:   2021-02-19
    :generic:
    :open:

    ``0`` enable apps usage of motion data.
