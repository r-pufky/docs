.. _salt-windows-manual-install:

`Windows Manual Install`_
#########################
:download:`Latest Windows Minion Installer <https://repo.saltstack.com/windows/>`.

Installer can be launched from the `CLI or GUI`_, dependencies are included with
the installer. The minion will be installed to ``c:\salt``.

.. code-block:: powershell
  :caption: The salt-minion can be managed like a normal windows service.

  sc start salt-minion
  net start salt-minion

Windows CLI Install
*******************
.. code-block:: powershell
  :caption: Installing Windows Minion from powershell (as admin).

  Salt-Minion-2019.2.0-Py3-AMD64-Setup.exe /S /master={SALT MASTER} /minion-name={MINION NAME} /start-minion-delayed

Windows GUI Install
*******************
* Specify the master name.
* Specify the minion name.
* Optionally provide a default configuration file.
* Enable delayed start (allows highstates requiring reboots to work).

.. _Windows Manual Install: https://repo.saltstack.com/#windows
.. _CLI or GUI: https://docs.saltstack.com/en/latest/topics/installation/windows.html