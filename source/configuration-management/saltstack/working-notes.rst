.. _salt-working-notes:

Working Notes
#############

.. warning::
  Working notes have not been folded into the standard documentation yet. These
  change frequently and are not to be used as instructions.

Using Chocolately for Windows
*****************************
This will use ``iexplore`` to download *chocolatey* and install it via a
powershell command

.. code-block:: powershell
  :caption: Install chocolatey from powershell remotely (Salt Master).

  powershell salt {WINDOWS MINION} cmd.run "iex ((new-object new.webclient).DownloadString('https://chocolatey.org/install.ps1'))" shell=powershell
  salt {WINDOWS MINION} cmd.run 'choco install sublimetext3' shell=powershell