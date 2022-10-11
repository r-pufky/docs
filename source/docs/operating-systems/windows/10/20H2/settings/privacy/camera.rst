.. _w10-20h2-settings-privacy-camera:

Camera
######
:cmdmenu:`⌘ + r --> ms-settings:privacy-webcam`

See :ref:`wbase-determining-app-list` to generate a list of apps for more fine
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

  .. gpo::    Disable access to camera on this device
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Camera -->
              Allow Use of Camera
    :value0:  ☑, {ENABLED}
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#183-camera
    :update:  2021-02-19
    :generic:
    :open:

    ``0`` to disable camera

  .. regedit:: Disable access to camera on this device
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Camera
    :value0:   AllowCamera, {DWORD}, 1
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#183-camera
    :update:   2021-02-19
    :generic:
    :open:

.. _w10-20h2-settings-privacy-camera-apps:

Allow apps to access your camera
********************************
.. dropdown:: Allow apps to access your camera
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. gpo::    Disable apps access to your camera
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              App Privacy -->
              Let Windows apps access the camera
    :value0:  ☑, {ENABLED}
    :value1:  Default for all apps, Force Deny
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#183-camera
    :update:  2021-02-19
    :generic:
    :open:

    ``2`` disables apps access to camera. ``Deny`` to deny constent for camera
    access.

  .. regedit:: Disable apps access to your camera
    :path:     HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
    :value0:   LetAppsAccessCamera, {DWORD}, 0
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#183-camera
    :update:   2021-02-19
    :generic:
    :open:

  .. regedit:: Disable apps access to your camera consentstore
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
               CapabilityAccessManager\ConsentStore\webcam
    :value0:   Value, {SZ}, Allow
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#183-camera
    :update:   2021-02-19
    :generic:
    :open:


Choose which Microsoft Store apps can access your camera
********************************************************
See :ref:`w10-20h2-settings-privacy-camera-apps`.

Allow desktop apps to access your camera
****************************************
.. regedit:: Allow desktop apps to access your camera
  :path: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
              CapabilityAccessManager\ConsentStore\webcam
  :value0:     Value, {SZ}, Allow
  :update:   2021-02-19

  ``Deny`` disables desktop app camera access.
