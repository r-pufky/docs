.. _w10-1903-reasonable-privacy-camera:

Camera
######
:cmdmenu:`⌘ + r --> ms-settings:privacy-webcam`

.. rubric:: Allow access to the camera on this device

.. wregedit:: Disable access to camera on this device via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Camera
  :names:     AllowCamera
  :types:     DWORD
  :data:      0
  :no_section:

.. wregedit:: Disable apps access to your camera consentstore via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
              CapabilityAccessManager\ConsentStore\webcam
  :names:     Value
  :types:     SZ
  :data:      Deny
  :no_section:
  :no_launch:

    .. note::
      See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more
      fine grained control of app access.

.. wgpolicy:: Disable access to camera on this device via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Camera -->
              Allow Use of Camera
  :option:    ☑
  :setting:   Disabled
  :no_section:

    .. note::
      This disables hardware access. See :ref:`w10-1903-privacy-camera` to
      manage access on a per app basis.

.. _w10-1903-privacy-camera:

.. rubric:: Allow apps to access your camera

.. wregedit:: Disable apps access to your camera via Registry
  :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
  :names:     LetAppsAccessCamera
  :types:     DWORD
  :data:      2
  :no_section:

    .. note::
      See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more
      fine grained control of app access.

.. wgpolicy:: Disable apps access to your camera via machine GPO
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
  :no_launch:

    .. note::
      See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more
      fine grained control of app access.

.. rubric:: Rreferences

#. `Camera Windows Management Settings <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#183-camera>`_
