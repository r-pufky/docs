.. _w10-20h2-standalone-biometrics:

Biometrics
##########
Facial recognition (Hello-Face) and Fingerprint ID are used to automatically
unlock your computer with your camera/fingerprint reader. Disable this.

.. danger::
  After every major windows update, verify these settings.

.. dropdown:: Disable Biometrics
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in
  :open:

  .. dropdown:: Delete Hello-Face
    :title: font-weight-bold
    :animate: fade-in

    .. code-block:: powershell
      :caption: Remove facial recognition package powershell (as admin)

      Get-WindowsPackage -Online | Where PackageName -like *Hello-Face* | Remove-WindowsPackage -Online -NoRestart

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Disable Biometrics
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Biometrics
      :names:     Enabled
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

    .. wgpolicy:: Allow the use of Biometrics
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Biometrics
      :option:    ☑
      :setting:   Disabled
      :no_section:
      :no_caption:

  .. dropdown:: Scheduled Tasks
    :title: font-weight-bold
    :animate: fade-in

    .. wtschedule:: Disable facial recognition schedule tasks
      :key_title:   Microsoft --> Windows --> HelloFace --> FODCleanupTask -->
                    RMB --> Disable
      :option:      Name
      :setting:     FODCleanupTask
      :no_section:
      :no_caption:

  `Reference <https://github.com/adolfintel/Windows10-Privacy#hello-face>`__
  `Reference <https://www.top-password.com/blog/disable-windows-10-face-recognition-or-fingerprint-login>`__
