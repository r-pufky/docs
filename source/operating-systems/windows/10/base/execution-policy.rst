.. _w10-execution-policy:

.. _setting-execution-policy:

`Setting Execution Policy`_
###########################
Powershell scripts require unrestricted execution policy to be set to execute.
By default this is **disabled** and is the **correct choice**. Once you've
executed scripts, you **must** manually reset this to restricted or you leave
yourself open to bad things. This persists across sessions.

.. code-block:: powershell
  :caption: Check and set unrestricted policy (powershell as admin).

  Get-ExecutionPolicy
  Set-ExecutionPolicy -ExecutionPolicy unrestricted -Force

.. code-block:: powershell
  :caption: Set restricted policy (powershell as admin).

  Set-ExecutionPolicy -ExecutionPolicy restricted -force

Set Policy Via Script
*********************
Commands entered directly into powershell are executed. Scripts may be run
without setting execution policy by launching a sub-shell with ExecutionPolicy
bypassed.

.. code-block:: powershell
  :caption: Execute script without setting ExecutionPolicy.

  PowerShell.exe -ExecutionPolicy Bypass -File {SCRIPT}.ps1

.. rubric:: References

#. `Setting Execution Policy <https://blog.netspi.com/15-ways-to-bypass-the-powershell-execution-policy/>`_
#. `Powershell Scripts Disabled <https://stackoverflow.com/questions/4037939/powershell-says-execution-of-scripts-is-disabled-on-this-system>`_
