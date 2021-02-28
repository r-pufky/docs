.. _w10-wsl:

Windows Subsystem for Linux (`WSL`_)
####################################
Windows Subsystem for Linux (:term:`WSL`) enables the ability to install a
pseudo distribution of linux on windows using a fully suppported (Microsoft
built) kernel; replaces the need for Cygwin.

WSL2 runs `a real linux`_ kernel which increases performance and compatiblity.
It is preferred over WSL1. WSL references the WSL2 installation.

See :ref:`apps-putty-x-windows` to setup a Windows 10 X server to display WSL
applications on the Windows desktop.

.. _w10-wsl-enable:

Enable WSL in Windows 10
************************

.. code-block:: powershell
  :caption: Enable WSL on Windows (powershell as admin).

  dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

.. note::
  Force update Windows after this step.
  
  Windows versions up to ``1909`` must install `KB4566116`_. :ref:`w10-version` if needed.

.. code-block:: powershell
  :caption: Enable WSL on Windows up to **1909** (powershell as admin).

  Enable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform -NoRestart

.. code-block:: powershell
  :caption: Enable WSL on Windows **2004+** (powershell as admin).

  dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

Install :download:`x64 kernel update for WSL2 <https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi>`.

.. code-block:: powershell
  :caption: Set WSL2 as default.

  wsl --set-default-version 2

Installing Linux Distros
************************
Only custom linux distros built for the Windows Linux Kernel are supported.

.. rubric:: Manual Install

See `Manual Install`_ for list of available pre-built distros.

.. code-block:: powershell
  :caption: Download Appstore package and install (powershell as admin).

  curl.exe -L -o {DISTRO}.appx https://aka.ms/wsl-{DISTRO}
  Add-AppxPackage .\{DISTRO}.appx

Launch the distro to complete installation.

.. rubric:: Windows Store Install

This automatically installs a given distro but requires login to the Microsoft
Store.

:cmdmenu:`⌘ --> Microsoft Store --> Search --> {DISTRO}`

Launch the distro to complete installation.

Troubleshooting
***************
See main `Troubleshooting`_ page for additional fixes.

.. rubric:: Installation failed with error 0x80070003

WSL is only intended to run on the system drive (usually ``c:\``). WSL was
installed to a different drive.

.. gui::   WSL Storage Settings
  :path:   ⌘ -->  Settings --> Storage --> More Storage Settings
  :value0: New apps will save to, c:\
  :ref:    https://docs.microsoft.com/en-us/windows/wsl/troubleshooting
  :update: 2021-02-19

Then reinstall your distro.

.. rubric:: WslRegisterDistribution failed with error 0x8007019e

WSL is not enabled. See :ref:`w10-wsl-enable`.

.. _KB4566116: https://support.microsoft.com/en-us/help/4566116/windows-10-update-kb4566116
.. _a real linux: https://www.omgubuntu.co.uk/how-to-install-wsl2-on-windows-10
.. _WSL: https://docs.microsoft.com/en-us/windows/wsl/install-win10
.. _Manual Install: https://docs.microsoft.com/en-us/windows/wsl/install-manual
.. _Initialize: https://docs.microsoft.com/en-us/windows/wsl/initialize-distro
