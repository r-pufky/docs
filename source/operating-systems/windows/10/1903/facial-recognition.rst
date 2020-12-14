.. _w10-1903-disable-facial-recognition:

`Disable Facial Recognition`_
#############################
Facial recognition is used to automatically unlock your computer with your
camera. Disable this.

.. danger::
  After every major windows update, verify these settings.

.. code-block:: powershell
  :caption: Remove facial recognition package powershell (as admin)

  Get-WindowsPackage -Online | Where PackageName -like *Hello-Face* | Remove-WindowsPackage -Online -NoRestart

.. wtschedule:: Disable schedule task for System Restore.
  :key_title:   Microsoft --> Windows --> HelloFace --> FODCleanupTask --> RMB --> Disable
  :option:      Name
  :setting:     FODCleanupTask
  :no_section:

:term:`Registry` Machine
************************
.. wregedit:: Disable Biometrics via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Biometrics
  :names:     Enabled
  :types:     DWORD
  :data:      0
  :no_section:

:term:`GPO` Computer
********************
.. wgpolicy:: Allow the use of Biometrics
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Biometrics
  :option:    ☑
  :setting:   Disabled
  :no_section:


.. rubric:: References

#. `Remove Hello Face <https://github.com/adolfintel/Windows10-Privacy#hello-face>`_

.. _Disable Facial Recognition: https://www.top-password.com/blog/disable-windows-10-face-recognition-or-fingerprint-login
