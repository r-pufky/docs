.. _w10-1903-reasonable-privacy-background-apps:

Background Apps
###############
:cmdmenu:`⌘ + r --> ms-settings:privacy-backgroundapps`

Leave background service enable, but disable all apps. This will prevent
the start menu search from breaking.

.. note::
  If start menu searches start to fail, it is because background apps
  service has been disabled. See :ref:`w10-background-apps`.

.. rubric:: Let apps run in the background

.. wregedit:: Enable apps run in the background via Registry
  :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
  :names:     LetAppsRunInBackground
  :types:     DWORD
  :data:      0
  :no_section:

.. gtable::   Disable specific apps access to your microphone via Registry
  :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy\
              LetAppsRunInBackground
  :header: Key,
           Name,
           Type,
           Data
  :c0:     Microsoft.WindowsAlarms_8wekyb3d8bbwe,
           Microsoft.WindowsCalculator_8wekyb3d8bbwe,
           Microsoft.WindowsCamera_8wekyb3d8bbwe,
           Microsoft.PPIProjection_cw5n1h2txyewy,
           Microsoft.WindowsFeedbackHub_8wekyb3d8bbwe,
           Microsoft.XboxGamingOverlay_8wekyb3d8bbwe,
           Microsoft.GetHelp_8wekyb3d8bbwe,
           Microsoft.ZuneMusic_8wekyb3d8bbwe,
           microsoft.windowscommunicationsapps_8wekyb3d8bbwe,
           Microsoft.WindowsMaps_8wekyb3d8bbwe,
           Microsoft.Messaging_8wekyb3d8bbwe,
           Microsoft.MicrosoftEdge_8wekyb3d8bbwe,
           Microsoft.WindowsStore_8wekyb3d8bbwe,
           Microsoft.MixedReality.Portal_8wekyb3d8bbwe,
           Microsoft.Microsoft3DViewer_8wekyb3d8bbwe,
           Microsoft.ZuneVideo_8wekyb3d8bbwe,
           Microsoft.MSPaint_8wekyb3d8bbwe,
           Microsoft.Windows.Photos_8wekyb3d8bbwe,
           windows.immersivecontrolpanel_cw5n1h2txyewy,
           Microsoft.ScreenSketch_8wekyb3d8bbwe,
           Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe,
           Microsoft.WindowsSoundRecorder_8wekyb3d8bbwe,
           Microsoft.Windows.SecHealthUI_cw5n1h2txyewy,
           Microsoft.XboxApp_8wekyb3d8bbwe,
           Microsoft.YourPhone_8wekyb3d8bbwe,
           Microsoft.XboxDevices_8wekyb3d8bbwe
  :c1:     Value,
           Value,
           Value,
           Value,
           Value,
           Value,
           Value,
           Value,
           Value,
           Value,
           Value,
           Value,
           Value,
           Value,
           Value,
           Value,
           Value,
           Value,
           Value,
           Value,
           Value,
           Value,
           Value,
           Value,
           Value,
           Value
  :c2:     SZ,
           SZ,
           SZ,
           SZ,
           SZ,
           SZ,
           SZ,
           SZ,
           SZ,
           SZ,
           SZ,
           SZ,
           SZ,
           SZ,
           SZ,
           SZ,
           SZ,
           SZ,
           SZ,
           SZ,
           SZ,
           SZ,
           SZ,
           SZ,
           SZ,
           SZ
  :c3:     Deny,
           Deny,
           Deny,
           Deny,
           Deny,
           Deny,
           Deny,
           Deny,
           Deny,
           Deny,
           Deny,
           Deny,
           Deny,
           Deny,
           Deny,
           Deny,
           Deny,
           Deny,
           Deny,
           Deny,
           Deny,
           Deny,
           Deny,
           Deny,
           Deny,
           Deny
  :no_section:
  :no_launch:

    .. note::
      See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more
      fine grained control of app access.

.. wgpolicy:: Disable Background apps access via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              App Privacy -->
              Let Windows apps run in the background
  :option:    ☑,
              Default for all apps,
              Force deny these specific apps (use Package Family Names):,
              ›,
              ›,
              ›,
              ›,
              ›,
              ›,
              ›,
              ›,
              ›,
              ›,
              ›,
              ›,
              ›,
              ›,
              ›,
              ›,
              ›,
              ›,
              ›,
              ›,
              ›,
              ›,
              ›,
              ›,
              ›
  :setting:   Enabled,
              User is in control,
              Microsoft.WindowsAlarms_8wekyb3d8bbwe,
              Microsoft.WindowsCalculator_8wekyb3d8bbwe,
              Microsoft.WindowsCamera_8wekyb3d8bbwe,
              Microsoft.PPIProjection_cw5n1h2txyewy,
              Microsoft.WindowsFeedbackHub_8wekyb3d8bbwe,
              Microsoft.XboxGamingOverlay_8wekyb3d8bbwe,
              Microsoft.GetHelp_8wekyb3d8bbwe,
              Microsoft.ZuneMusic_8wekyb3d8bbwe,
              microsoft.windowscommunicationsapps_8wekyb3d8bbwe,
              Microsoft.WindowsMaps_8wekyb3d8bbwe,
              Microsoft.Messaging_8wekyb3d8bbwe,
              Microsoft.MicrosoftEdge_8wekyb3d8bbwe,
              Microsoft.WindowsStore_8wekyb3d8bbwe,
              Microsoft.MixedReality.Portal_8wekyb3d8bbwe,
              Microsoft.Microsoft3DViewer_8wekyb3d8bbwe,
              Microsoft.ZuneVideo_8wekyb3d8bbwe,
              Microsoft.MSPaint_8wekyb3d8bbwe,
              Microsoft.Windows.Photos_8wekyb3d8bbwe,
              windows.immersivecontrolpanel_cw5n1h2txyewy,
              Microsoft.ScreenSketch_8wekyb3d8bbwe,
              Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe,
              Microsoft.WindowsSoundRecorder_8wekyb3d8bbwe,
              Microsoft.Windows.SecHealthUI_cw5n1h2txyewy,
              Microsoft.XboxApp_8wekyb3d8bbwe,
              Microsoft.YourPhone_8wekyb3d8bbwe,
              Microsoft.XboxDevices_8wekyb3d8bbwe
  :no_section:

    .. note::
      See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more
      fine grained control of app access.

.. rubric:: Rreferences

#. `Background Apps Windows Management Settings <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1817-background-apps>`_
