.. _windows-10-reasonable-privacy-microphone:

Microphone
##########
:cmdmenu:`⌘ + r --> ms-settings:privacy-microphone`

Leave Microphone enabled, but disable all apps. This will allow mumble to use
the microphone. See `1803 update breaks microphone`_.

.. rubric:: Allow access to the microphone on this device

.. wregedit:: Enable access to the microphone on this device via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
              CapabilityAccessManager\ConsentStore\microphone
  :names:     Value
  :types:     SZ
  :data:      Allow
  :no_section:

    .. note::
      Valid options are ``Allow`` and ``Deny``.

.. rubric:: Allow apps to access your microphone

.. wregedit:: Enable apps access to your microphone via Registry
  :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
  :names:     LetAppsAccessMicrophone
  :types:     DWORD
  :data:      0
  :no_section:

.. gtable::   Disable specific apps access to your microphone via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
              CapabilityAccessManager\ConsentStore\microphone
  :header: Key,
           Name,
           Type,
           Data
  :c0:     Microsoft.WindowsCamera_8wekyb3d8bbwe,
           Microsoft.Windows.Cortana_cw5n1h2txyewy,
           Microsoft.Win32WebViewHost_cw5n1h2txyewy,
           Microsoft.WindowsFeedbackHub_8wekyb3d8bbwe,
           Microsoft.XboxGamingOverlay_8wekyb3d8bbwe,
           Microsoft.Messaging_8wekyb3d8bbwe,
           Microsoft.MicrosoftEdge_8wekyb3d8bbwe,
           Microsoft.WindowsStore_8wekyb3d8bbwe,
           Microsoft.MixedReality.Portal_8wekyb3d8bbwe,
           Microsoft.Microsoft3DViewer_8wekyb3d8bbwe,
           Microsoft.Windows.Photos_8wekyb3d8bbwe,
           Microsoft.Windows.SecureAssessmentBrowser_cw5n1h2txyewy,
           Microsoft.WindowsSoundRecorder_8wekyb3d8bbwe,
           Microsoft.XboxApp_8wekyb3d8bbwe
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
           Deny
  :no_section:
  :no_launch:

    .. note::
      See :ref:`windows-10-privacy-app-list` to generate a list of apps for more
      fine grained control of app access.

.. wgpolicy:: Disable apps access to your microphone via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              App Privacy -->
              Let Windows access the microphone
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
              ›
  :setting:   Enabled,
              User is in control,
              Microsoft.WindowsCamera_8wekyb3d8bbwe,
              Microsoft.Windows.Cortana_cw5n1h2txyewy,
              Microsoft.Win32WebViewHost_cw5n1h2txyewy,
              Microsoft.WindowsFeedbackHub_8wekyb3d8bbwe,
              Microsoft.XboxGamingOverlay_8wekyb3d8bbwe,
              Microsoft.Messaging_8wekyb3d8bbwe,
              Microsoft.MicrosoftEdge_8wekyb3d8bbwe,
              Microsoft.WindowsStore_8wekyb3d8bbwe,
              Microsoft.MixedReality.Portal_8wekyb3d8bbwe,
              Microsoft.Microsoft3DViewer_8wekyb3d8bbwe,
              Microsoft.Windows.Photos_8wekyb3d8bbwe,
              Microsoft.Windows.SecureAssessmentBrowser_cw5n1h2txyewy,
              Microsoft.WindowsSoundRecorder_8wekyb3d8bbwe,
              Microsoft.XboxApp_8wekyb3d8bbwe
  :no_section:

    .. note::
      See :ref:`windows-10-privacy-app-list` to generate a list of apps for more
      fine grained control of app access.

.. rubric:: Rreferences

#. `Microphone Windows Management Settings <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#184-microphone>`_
#. `Microphone access via Registry <https://www.kapilarya.com/allow-prevent-apps-access-to-microphone-in-windows-10>`_

.. _1803 update breaks microphone: https://www.ghacks.net/2018/05/01/all-the-issues-of-windows-10-version-1803-you-may-run-into/