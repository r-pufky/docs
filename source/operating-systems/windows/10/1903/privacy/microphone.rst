.. _w10-1903-reasonable-privacy-microphone:

Microphone
##########
:cmdmenu:`⌘ + r --> ms-settings:privacy-microphone`

Leave Microphone enabled, but disable all apps. This will allow mumble to use
the microphone. See `1803 update breaks microphone`_.

.. regedit:: Allow access to the microphone on this device
  :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
             CapabilityAccessManager\ConsentStore\microphone
  :value0:   Value, {SZ}, Allow
  :update:   2021-02-19

.. dropdown:: Allow apps to access your microphone
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more fine
  grained control of app access.

  .. regedit:: Enable apps access to your microphone
    :path:     HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
    :value0:   LetAppsAccessMicrophone, {DWORD}, 0
    :update:   2021-02-19
    :generic:
    :open:

    ``2`` disables app access to microphone.

    Disable specific apps access to your microphone

    ``HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\microphone``

    +---------------------------------------------------------------+-------------+-----------+-----------+
    | Key                                                           | Name        | Type      | Data      |
    +===============================================================+=============+===========+===========+
    | Microsoft.WindowsCamera_8wekyb3d8bbwe                         | Value       | SZ        | Deny      |
    +---------------------------------------------------------------+-------------+-----------+-----------+
    | Microsoft.Windows.Cortana_cw5n1h2txyewy                       | Value       | SZ        | Deny      |
    +---------------------------------------------------------------+-------------+-----------+-----------+
    | Microsoft.Win32WebViewHost_cw5n1h2txyewy                      | Value       | SZ        | Deny      |
    +---------------------------------------------------------------+-------------+-----------+-----------+
    | Microsoft.WindowsFeedbackHub_8wekyb3d8bbwe                    | Value       | SZ        | Deny      |
    +---------------------------------------------------------------+-------------+-----------+-----------+
    | Microsoft.XboxGamingOverlay_8wekyb3d8bbwe                     | Value       | SZ        | Deny      |
    +---------------------------------------------------------------+-------------+-----------+-----------+
    | Microsoft.Messaging_8wekyb3d8bbwe                             | Value       | SZ        | Deny      |
    +---------------------------------------------------------------+-------------+-----------+-----------+
    | Microsoft.MicrosoftEdge_8wekyb3d8bbwe                         | Value       | SZ        | Deny      |
    +---------------------------------------------------------------+-------------+-----------+-----------+
    | Microsoft.WindowsStore_8wekyb3d8bbwe                          | Value       | SZ        | Deny      |
    +---------------------------------------------------------------+-------------+-----------+-----------+
    | Microsoft.MixedReality.Portal_8wekyb3d8bbwe                   | Value       | SZ        | Deny      |
    +---------------------------------------------------------------+-------------+-----------+-----------+
    | Microsoft.Microsoft3DViewer_8wekyb3d8bbwe                     | Value       | SZ        | Deny      |
    +---------------------------------------------------------------+-------------+-----------+-----------+
    | Microsoft.Windows.Photos_8wekyb3d8bbwe                        | Value       | SZ        | Deny      |
    +---------------------------------------------------------------+-------------+-----------+-----------+
    | Microsoft.Windows.SecureAssessmentBrowser_cw5n1h2txyewy       | Value       | SZ        | Deny      |
    +---------------------------------------------------------------+-------------+-----------+-----------+
    | Microsoft.WindowsSoundRecorder_8wekyb3d8bbwe                  | Value       | SZ        | Deny      |
    +---------------------------------------------------------------+-------------+-----------+-----------+
    | Microsoft.XboxApp_8wekyb3d8bbwe                               | Value       | SZ        | Deny      |
    +---------------------------------------------------------------+-------------+-----------+-----------+

  .. gpo::    Disable apps access to your microphone
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              App Privacy -->
              Let Windows access the microphone
    :value0:  ☑, {ENABLED}
    :value1:  Default for all apps, User is in control
    :value2:  Force deny these specific apps (use Package Family Names):,
    :value3:  ›, Microsoft.WindowsCamera_8wekyb3d8bbwe
    :value4:  ›, Microsoft.Windows.Cortana_cw5n1h2txyewy
    :value5:  ›, Microsoft.Win32WebViewHost_cw5n1h2txyewy
    :value6:  ›, Microsoft.WindowsFeedbackHub_8wekyb3d8bbwe
    :value7:  ›, Microsoft.XboxGamingOverlay_8wekyb3d8bbwe
    :value8:  ›, Microsoft.Messaging_8wekyb3d8bbwe
    :value9:  ›, Microsoft.MicrosoftEdge_8wekyb3d8bbwe
    :value10: ›, Microsoft.WindowsStore_8wekyb3d8bbwe
    :value11: ›, Microsoft.MixedReality.Portal_8wekyb3d8bbwe
    :value12: ›, Microsoft.Microsoft3DViewer_8wekyb3d8bbwe
    :value13: ›, Microsoft.Windows.Photos_8wekyb3d8bbwe
    :value14: ›, Microsoft.Windows.SecureAssessmentBrowser_cw5n1h2txyewy
    :value15: ›, Microsoft.WindowsSoundRecorder_8wekyb3d8bbwe
    :value16: ›, Microsoft.XboxApp_8wekyb3d8bbwe
    :update:   2021-02-19
    :generic:
    :open:

.. rubric:: Rreferences

#. `Microphone Windows Management Settings <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#184-microphone>`_
#. `Microphone access <https://www.kapilarya.com/allow-prevent-apps-access-to-microphone-in-windows-10>`_

.. _1803 update breaks microphone: https://www.ghacks.net/2018/05/01/all-the-issues-of-windows-10-version-1803-you-may-run-into/
