.. _w10-20h2-settings-privacy-microphone:

Microphone
##########
:cmdmenu:`⌘ + r --> ms-settings:privacy-microphone`

Leave Microphone enabled. See `1803 update breaks microphone`_.

See :ref:`w10-determining-app-list` to generate a list of apps for more fine
grained control of app access.

.. dropdown:: Allow access to the microphone on this device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Enable access to the microphone on this device
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
                  CapabilityAccessManager\ConsentStore\microphone
      :names:     Value
      :types:     SZ
      :data:      Allow
      :no_section:
      :no_caption:

.. _w10-20h2-settings-privacy-microphone-hardware:

Allow apps to access your microphone
************************************
.. dropdown:: Allow apps to access your microphone
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Enable apps access to your microphone
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  App Privacy -->
                  Let Windows access the microphone
      :option:    ☑,
                  Default for all apps
      :setting:   Enabled,
                  User is in control
      :no_section:
      :no_caption:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    ``2`` disables app access to microphone.

    .. wregedit:: Enable apps access to your microphone
      :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
      :names:     LetAppsAccessMicrophone
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

  `Reference <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#184-microphone>`__

Choose which Microsoft Store apps can access your microphone
************************************************************
See :ref:`w10-20h2-settings-privacy-microphone-hardware`.

Allow desktop apps to access your microphone
********************************************
See :ref:`w10-20h2-settings-privacy-microphone-hardware`.

.. _1803 update breaks microphone: https://www.ghacks.net/2018/05/01/all-the-issues-of-windows-10-version-1803-you-may-run-into/
