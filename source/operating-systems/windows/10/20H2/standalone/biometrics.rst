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
    :open:

    .. code-block:: powershell
      :caption: Remove facial recognition package powershell (as admin)

      Get-WindowsPackage -Online | Where PackageName -like *Hello-Face* | Remove-WindowsPackage -Online -NoRestart

  .. gpo::    Disable the use of Biometrics
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Biometrics
    :value0:  ☑, {DISABLED}
    :ref:     https://www.top-password.com/blog/disable-windows-10-face-recognition-or-fingerprint-login
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable the use of Biometrics
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Biometrics
    :value0:   Enabled, {DWORD}, 0
    :ref:      https://www.top-password.com/blog/disable-windows-10-face-recognition-or-fingerprint-login
    :update:   2021-02-19
    :generic:
    :open:

  .. gui::    Disable facial recognition schedule tasks
    :label:   Task Scheduler
    :nav:     ⌘ --> Task Scheduler --> Task Scheduler Library
    :path:    Microsoft --> Windows --> HelloFace --> FODCleanupTask -->
              {RMB} --> Disable
    :value0:  Name, FODCleanupTask
    :ref:     https://github.com/adolfintel/Windows10-Privacy#hello-face
    :update:  2021-02-19
    :generic:
    :open:
