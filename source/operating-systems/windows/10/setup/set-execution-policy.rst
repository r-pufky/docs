.. _setting-execution-policy:

`Setting Execution Policy`_
###########################
Powershell scripts require unrestricted execution policy to be set to execute.
By default this is **disabled** and is the **correct choice**. Once you've
executed scripts, you **must** manually reset this to restricted or you leave
yourself open to bad things. This persists across sessions.

.. code-block:: powershell
  :caption: Check and set unrestricted policy (powershell as admin).
  :emphasize-lines: 3

  get-executionpolicy
  set-executionpolicy unrestricted
  Y

.. code-block:: powershell
  :caption: Set restricted policy (powershell as admin).
  :emphasize-lines: 2

  set-executionpolicy restricted
  Y

.. _Setting Execution Policy: https://stackoverflow.com/questions/4037939/powershell-says-execution-of-scripts-is-disabled-on-this-system