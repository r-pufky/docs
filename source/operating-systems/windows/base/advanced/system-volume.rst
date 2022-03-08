.. _wbase-specific-windows-fixes-system-volume:

Fix Undeletable System Volumes
##############################
System Volume information can be accidently copied to other volumes (e.g. USB
drives) using `robocopy` and copying the entire drive. This will lead to
directories that cannot be deleted even if they are not needed.

Take ownership and grant full privileges for everyone to remove the directory.

.. code-block:: powershell

  takeown /f ".\System Volume Information" /a /r /d y
  icacls ".\System Volume Information" /t /c /grant administrators:F System:F everyone:F
  rd ".\System Volume Information"

