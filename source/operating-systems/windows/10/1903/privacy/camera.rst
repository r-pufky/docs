.. _w10-1903-reasonable-privacy-camera:

Camera
######
:cmdmenu:`⌘ + r --> ms-settings:privacy-webcam`

.. dropdown:: Allow access to the camera on this device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Enable Camera access and disable specific apps.

  .. gpo::    Disable access to camera on this device
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Camera -->
              Allow Use of Camera
    :value0:  ☑, {ENABLED}
    :update:  2021-02-19
    :generic:
    :open:

    This disables hardware access. See :ref:`Allow apps to access your camera
    <w10-1903-privacy-camera>` to manage access on a per app basis.

  .. regedit:: Disable access to camera on this device
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Camera
    :value0:   AllowCamera, {DWORD}, 1
    :update:   2021-02-19
    :generic:
    :open:

    See :ref:`Allow apps to access your camera <w10-1903-privacy-app-list>` to
    generate a list of apps for more fine grained control of app access.

    ``0`` to disable camera, ``Deny`` to dney constent for camera access.

  .. regedit:: Disable apps access to your camera consentstore
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
               CapabilityAccessManager\ConsentStore\webcam
    :value0:   Value, {SZ}, Allow
    :update:   2021-02-19
    :generic:
    :open:

    See :ref:`Allow apps to access your camera <w10-1903-privacy-app-list>` to
    generate a list of apps for more fine grained control of app access.

    ``0`` to disable camera, ``Deny`` to dney constent for camera access.

.. _w10-1903-privacy-camera:

.. dropdown:: Allow apps to access your camera
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more fine
  grained control of app access.

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

  .. regedit:: Disable apps access to your camera
    :path:     HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppPrivacy
    :value0:   LetAppsAccessCamera, {DWORD}, 2
    :update:   2021-02-19
    :generic:
    :open:

    ``0`` enables apps access to camera.
