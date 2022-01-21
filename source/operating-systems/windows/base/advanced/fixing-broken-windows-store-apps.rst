.. _wbase-specific-windows-fixes-fixing-broken-windows-store-apps:

Fixing Broken Windows Store apps / 'Trial Expired' Apps
#######################################################
Default windows 10 applications may stop working if you remove dependent apps
from the system. Symptoms include apps like xbox controller config never
loading, or calculator prompting with trial expired. This resets the system to
the default app installation state for windows 10.

.. code-block:: powershell
  :caption: Reinstall default Windows applications (powershell as admin).

  Get-AppXPackage -AllUsers | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}

`Reference <https://community.spiceworks.com/how_to/122006-windows-10-your-trial-period-for-this-app-has-expired-visit-the-windows-store-to-purchase-the-full-app-problem>`__
