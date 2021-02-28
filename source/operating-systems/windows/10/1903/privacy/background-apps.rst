.. _w10-1903-reasonable-privacy-background-apps:

Background Apps
###############
:cmdmenu:`⌘ + r --> ms-settings:privacy-backgroundapps`

Leave background service enable, but disable all apps. This will prevent the
start menu search from breaking.

.. important::
  If start menu searches start to fail, it is because background apps
  service has been disabled. See :ref:`w10-background-apps`.

.. dropdown:: Let apps run in the background
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in
  :open:

  See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more fine
  grained control of app access.

  .. regedit:: Enable apps run in the background
    :path:     HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
    :value0:   LetAppsRunInBackground, {DWORD}, 0
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1817-background-apps
    :update:   2021-02-19
    :generic:
    :open:

    ``2`` disables apps running in the background.

    ``HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy\LetAppsRunInBackground``

    +------------------------------------------------------+----------+---------+--------+
    | Key                                                  | Name     | Type    | Data   |
    +======================================================+==========+=========+========+
    | Microsoft.WindowsAlarms_8wekyb3d8bbwe                | Value    | SZ      | Deny   |
    +------------------------------------------------------+----------+---------+--------+
    | Microsoft.WindowsCalculator_8wekyb3d8bbwe            | Value    | SZ      | Deny   |
    +------------------------------------------------------+----------+---------+--------+
    | Microsoft.WindowsCamera_8wekyb3d8bbwe                | Value    | SZ      | Deny   |
    +------------------------------------------------------+----------+---------+--------+
    | Microsoft.PPIProjection_cw5n1h2txyewy                | Value    | SZ      | Deny   |
    +------------------------------------------------------+----------+---------+--------+
    | Microsoft.WindowsFeedbackHub_8wekyb3d8bbwe           | Value    | SZ      | Deny   |
    +------------------------------------------------------+----------+---------+--------+
    | Microsoft.XboxGamingOverlay_8wekyb3d8bbwe            | Value    | SZ      | Deny   |
    +------------------------------------------------------+----------+---------+--------+
    | Microsoft.GetHelp_8wekyb3d8bbwe                      | Value    | SZ      | Deny   |
    +------------------------------------------------------+----------+---------+--------+
    | Microsoft.ZuneMusic_8wekyb3d8bbwe                    | Value    | SZ      | Deny   |
    +------------------------------------------------------+----------+---------+--------+
    | microsoft.windowscommunicationsapps_8wekyb3d8bbwe    | Value    | SZ      | Deny   |
    +------------------------------------------------------+----------+---------+--------+
    | Microsoft.WindowsMaps_8wekyb3d8bbwe                  | Value    | SZ      | Deny   |
    +------------------------------------------------------+----------+---------+--------+
    | Microsoft.Messaging_8wekyb3d8bbwe                    | Value    | SZ      | Deny   |
    +------------------------------------------------------+----------+---------+--------+
    | Microsoft.MicrosoftEdge_8wekyb3d8bbwe                | Value    | SZ      | Deny   |
    +------------------------------------------------------+----------+---------+--------+
    | Microsoft.WindowsStore_8wekyb3d8bbwe                 | Value    | SZ      | Deny   |
    +------------------------------------------------------+----------+---------+--------+
    | Microsoft.MixedReality.Portal_8wekyb3d8bbwe          | Value    | SZ      | Deny   |
    +------------------------------------------------------+----------+---------+--------+
    | Microsoft.Microsoft3DViewer_8wekyb3d8bbwe            | Value    | SZ      | Deny   |
    +------------------------------------------------------+----------+---------+--------+
    | Microsoft.ZuneVideo_8wekyb3d8bbwe                    | Value    | SZ      | Deny   |
    +------------------------------------------------------+----------+---------+--------+
    | Microsoft.MSPaint_8wekyb3d8bbwe                      | Value    | SZ      | Deny   |
    +------------------------------------------------------+----------+---------+--------+
    | Microsoft.Windows.Photos_8wekyb3d8bbwe               | Value    | SZ      | Deny   |
    +------------------------------------------------------+----------+---------+--------+
    | windows.immersivecontrolpanel_cw5n1h2txyewy          | Value    | SZ      | Deny   |
    +------------------------------------------------------+----------+---------+--------+
    | Microsoft.ScreenSketch_8wekyb3d8bbwe                 | Value    | SZ      | Deny   |
    +------------------------------------------------------+----------+---------+--------+
    | Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe         | Value    | SZ      | Deny   |
    +------------------------------------------------------+----------+---------+--------+
    | Microsoft.WindowsSoundRecorder_8wekyb3d8bbwe         | Value    | SZ      | Deny   |
    +------------------------------------------------------+----------+---------+--------+
    | Microsoft.Windows.SecHealthUI_cw5n1h2txyewy          | Value    | SZ      | Deny   |
    +------------------------------------------------------+----------+---------+--------+
    | Microsoft.XboxApp_8wekyb3d8bbwe                      | Value    | SZ      | Deny   |
    +------------------------------------------------------+----------+---------+--------+
    | Microsoft.YourPhone_8wekyb3d8bbwe                    | Value    | SZ      | Deny   |
    +------------------------------------------------------+----------+---------+--------+
    | Microsoft.XboxDevices_8wekyb3d8bbwe                  | Value    | SZ      | Deny   |
    +------------------------------------------------------+----------+---------+--------+

    .. gpo:: Disable Background apps access
      :path: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  App Privacy -->
                  Let Windows apps run in the background
      :value0:  ☑, {ENABLED}
      :value1:  Default for all apps, User is in control
      :value2:  Force deny these specific apps (use Package Family value0):,
      :value3:  ›, Microsoft.WindowsAlarms_8wekyb3d8bbwe
      :value4:  ›, Microsoft.WindowsCalculator_8wekyb3d8bbwe
      :value5:  ›, Microsoft.WindowsCamera_8wekyb3d8bbwe
      :value6:  ›, Microsoft.PPIProjection_cw5n1h2txyewy
      :value7:  ›, Microsoft.WindowsFeedbackHub_8wekyb3d8bbwe
      :value8:  ›, Microsoft.XboxGamingOverlay_8wekyb3d8bbwe
      :value9:  ›, Microsoft.GetHelp_8wekyb3d8bbwe
      :value10: ›, Microsoft.ZuneMusic_8wekyb3d8bbwe
      :value11: ›, microsoft.windowscommunicationsapps_8wekyb3d8bbwe
      :value12: ›, Microsoft.WindowsMaps_8wekyb3d8bbwe
      :value13: ›, Microsoft.Messaging_8wekyb3d8bbwe
      :value14: ›, Microsoft.MicrosoftEdge_8wekyb3d8bbwe
      :value15: ›, Microsoft.WindowsStore_8wekyb3d8bbwe
      :value16: ›, Microsoft.MixedReality.Portal_8wekyb3d8bbwe
      :value17: ›, Microsoft.Microsoft3DViewer_8wekyb3d8bbwe
      :value18: ›, Microsoft.ZuneVideo_8wekyb3d8bbwe
      :value19: ›, Microsoft.MSPaint_8wekyb3d8bbwe
      :value20: ›, Microsoft.Windows.Photos_8wekyb3d8bbwe
      :value21: ›, windows.immersivecontrolpanel_cw5n1h2txyewy
      :value22: ›, Microsoft.ScreenSketch_8wekyb3d8bbwe
      :value23: ›, Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe
      :value24: ›, Microsoft.WindowsSoundRecorder_8wekyb3d8bbwe
      :value25: ›, Microsoft.Windows.SecHealthUI_cw5n1h2txyewy
      :value26: ›, Microsoft.XboxApp_8wekyb3d8bbwe
      :value27: ›, Microsoft.YourPhone_8wekyb3d8bbwe
      :value28: ›, Microsoft.XboxDevices_8wekyb3d8bbwe
      :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1817-background-apps
      :update:  2021-02-19
      :generic:
      :open:
