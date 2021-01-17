.. _w10-20h2-settings-privacy-camera:

Camera
######
:cmdmenu:`⌘ + r --> ms-settings:privacy-webcam`

See :ref:`w10-determining-app-list` to generate a list of apps for more fine
grained control of app access.

Allow access to the camera on this device
*****************************************
.. dropdown:: Allow access to the camera on this device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  This disables hardware access. See
  :ref:`w10-20h2-settings-privacy-camera-apps` to manage access on a per app
  basis.
  
  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Disable access to camera on this device
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Camera -->
                  Allow Use of Camera
      :option:    ☑
      :setting:   Enabled
      :no_section:
      :no_caption:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    ``0`` to disable camera
    
    .. wregedit:: Disable access to camera on this device
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Camera
      :names:     AllowCamera
      :types:     DWORD
      :data:      1
      :no_section:
      :no_caption:

  `Reference <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#183-camera>`__

.. _w10-20h2-settings-privacy-camera-apps:

Allow apps to access your camera
********************************
.. dropdown:: Allow apps to access your camera
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Disable apps access to your camera
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  App Privacy -->
                  Let Windows apps access the camera
      :option:    ☑,
                  Default for all apps
      :setting:   Enabled,
                  Force Allow
      :no_section:
      :no_caption:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    ``2`` disables apps access to camera. ``Deny`` to deny constent for camera
    access.

    .. wregedit:: Disable apps access to your camera
      :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
      :names:     LetAppsAccessCamera
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

    .. wregedit:: Disable apps access to your camera consentstore
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
                  CapabilityAccessManager\ConsentStore\webcam
      :names:     Value
      :types:     SZ
      :data:      Allow
      :no_section:
      :no_caption:
      :no_launch:

  `Reference <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#183-camera>`__

Choose which Microsoft Store apps can access your camera
********************************************************
See :ref:`w10-20h2-settings-privacy-camera-apps`.

Allow desktop apps to access your camera
****************************************
.. dropdown:: Allow desktop apps to access your camera
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    ``Deny`` disables desktop app camera access.

    .. wregedit:: Enable desktop apps to access your camera
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
                  CapabilityAccessManager\ConsentStore\webcam
      :names:     Value
      :types:     SZ
      :data:      Allow
      :no_section:
      :no_caption:
