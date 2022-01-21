.. _wbase-remove-preinstalled-packages:

Remove Preinstalled Packages
############################
Certain packages (and windows store applications) cannot be removed with
`programs and applications <https://www.makeuseof.com/tag/3-clever-powershell-functions-upgrading-windows-10>`__.
This removes applications using Windows the built-in package manager.

Default applications are updated with each major update to windows 10, so
manually removing applications is preferred over a script.

   * ``Remove-AppxProvisionedPackage`` will remove packages for newly
     provisioned accounts.
   * ``Remove-AppxPackage`` removes for the current user.
   * ``Get-AppxPackage -AllUsers`` will return results for all users on system.

:download:`Remove packages script. <source/remove-crapware.ps1>`
