.. _windows-10-disable-facial-recognition:

Disable Facial Recognition
##########################
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

.. rubric:: References

#. `Remove Hello Face <https://github.com/adolfintel/Windows10-Privacy#hello-face>`_