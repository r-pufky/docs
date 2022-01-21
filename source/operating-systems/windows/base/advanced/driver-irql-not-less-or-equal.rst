.. _wbase-specific-windows-fixes-driver-irql-not-less-or-equal:

DRIVER_IRQL_NOT_LESS_OR_EQUAL (Epfwwfp.sys)
###########################################
:cmdmenu:`shift + Reset --> Troubleshoot --> Advanced options --> Start-up Settings --> Restart --> 4 (Safe Mode)`
:cmdmenu:`Troubleshoot --> Command Prompt`

.. code-block:: powershell
  :caption: Remove ESET driver and reboot.

  del /F /S /Q /A "c:\Windows\System32\drivers\epfwwfp.sys"

Offending program should be reinstalled.

`Reference <https://ugetfix.com/ask/how-to-fix-driver_irql_not_less_or_equal-epfwwfp-sys-error-on-windows/>`__
