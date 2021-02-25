.. _w10-20h2-settings-privacy-background-apps:

Background Apps
###############
:cmdmenu:`⌘ + r --> ms-settings:privacy-backgroundapps`

Leave background service **enabled**, but **disable** all apps. This will
prevent the start menu search from breaking.

See :ref:`w10-determining-app-list` to generate a list of apps for more fine
grained control of app access.

.. important::
  If start menu searches start to fail, it is because background apps
  service has been disabled. See :ref:`w10-background-apps`.

Let apps run in the background
******************************
.. dropdown:: Enable Let apps run in the background
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in
  :open:

  .. gpo::    Enable Let apps run in the background
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              App Privacy -->
              Let Windows apps run in the background
    :value0:  ☑, {ENABLED}
    :value1:  Default for all apps, User is in control
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1817-background-apps
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Enable Let apps run in the background
    :path:     HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
    :value0:   LetAppsRunInBackground, {DWORD}, 0
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1817-background-apps
    :update:  2021-02-19
    :generic:
    :open:

    ``2`` disables apps running in the background.

Choose which apps can run in the background
*******************************************
See :ref:`w10-20h2-settings-privacy-background-apps`.
