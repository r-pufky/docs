.. _w10-1903-reasonable-privacy-camera:

Camera
######
:cmdmenu:`⌘ + r --> ms-settings:privacy-webcam`

.. dropdown:: Allow access to the camera on this device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Enable Camera access and disable specific apps.
  
  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    See :ref:`Allow apps to access your camera <w10-1903-privacy-app-list>` to
    generate a list of apps for more fine grained control of app access.

    ``0`` to disable camera, ``Deny`` to dney constent for camera access.

    .. wregedit:: Disable access to camera on this device
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Camera
      :names:     AllowCamera
      :types:     DWORD
      :data:      1
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

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

    This disables hardware access. See :ref:`Allow apps to access your camera
    <w10-1903-privacy-camera>` to manage access on a per app basis.

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

.. _w10-1903-privacy-camera:

.. dropdown:: Allow apps to access your camera
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more fine 
  grained control of app access.

  ``0`` enables apps access to camera.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Disable apps access to your camera
      :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
      :names:     LetAppsAccessCamera
      :types:     DWORD
      :data:      2
      :no_section:
      :no_caption:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

    .. wgpolicy:: Disable apps access to your camera
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  App Privacy -->
                  Let Windows apps access the camera
      :option:    ☑,
                  Default for all apps
      :setting:   Enabled,
                  Force Deny
      :no_section:
      :no_caption:

.. rubric:: Rreferences

#. `Camera Windows Management Settings <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#183-camera>`_
