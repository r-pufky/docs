.. _w10-20h2-settings-privacy-microphone:

Microphone
##########
:cmdmenu:`⌘ + r --> ms-settings:privacy-microphone`

Leave Microphone enabled. See `1803 update breaks microphone`_.

See :ref:`w10-determining-app-list` to generate a list of apps for more fine
grained control of app access.

.. regedit:: Allow access to the microphone on this device
  :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
             CapabilityAccessManager\ConsentStore\microphone
  :value0:   Value, {SZ}, Allow
  :update:   2021-02-19

.. _w10-20h2-settings-privacy-microphone-hardware:

Allow apps to access your microphone
************************************
.. dropdown:: Allow apps to access your microphone
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. gpo::    Enable apps access to your microphone
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              App Privacy -->
              Let Windows access the microphone
    :value0:  ☑, {ENABLED}
    :value1:  Default for all apps, User is in control
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#184-microphone
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Enable apps access to your microphone
    :path:     HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
    :value0:   LetAppsAccessMicrophone, {DWORD}, 0
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#184-microphone
    :update:   2021-02-19
    :generic:
    :open:

    ``2`` disables app access to microphone.

Choose which Microsoft Store apps can access your microphone
************************************************************
See :ref:`w10-20h2-settings-privacy-microphone-hardware`.

Allow desktop apps to access your microphone
********************************************
See :ref:`w10-20h2-settings-privacy-microphone-hardware`.

.. _1803 update breaks microphone: https://www.ghacks.net/2018/05/01/all-the-issues-of-windows-10-version-1803-you-may-run-into/
