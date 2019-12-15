.. _os-windows-wsl:

Windows Subsystem for Linux (`WSL`_)
####################################
Windows Subsystem for Linux (:term:`WSL`) enables the ability to install a
pseudo distribution of linux on windows using a fully suppported (Microsoft
built) kernel; replaces the need for Cygwin.

See :ref:`apps-putty-x-windows` to setup a Windows 10 X server to display WSL
applications on the Windows desktop.

.. _os-windows-wsl-enable:

Enable WSL in Windows 10
************************
This will enable the feature and install additional packages to support it. WSL
is **not** suppport in ``S`` (secure) Windows mode.

.. code-block:: powershell
  :caption: Enable WSL and reboot (powershell as admin).

  Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux

Installing Linux Distros
************************
Only custom linux distros built for the Windows Linux Kernel are supported.

Manual Install
==============
See `Manual Install`_ for list of available pre-built distros.

.. code-block:: powershell
  :caption: Download Appstore package and install (powershell as admin).

  curl.exe -L -o {DISTRO}.appx https://aka.ms/wsl-{DISTRO}
  Add-AppxPackage .\{DISTRO}.appx

Launch the distro to complete installation.

Windows Store Install
=====================
This automatically installs a given distro but requires login to the Microsoft
Store.

:cmdmenu:`⌘ --> Microsoft Store --> Search --> {DISTRO}`

Launch the distro to complete installation.

Troubleshooting
***************
See main `Troubleshooting`_ page for additional fixes.

Installation failed with error 0x80070003
=========================================
WSL is only intended to run on the system drive (usually ``c:\``). WSL was
installed to a different drive.

.. ggui:: WSL Storage Settings
  :key_title: ⌘ -->  Settings --> Storage --> More Storage Settings
  :option:  New apps will save to
  :setting: c:\
  :no_caption:
  :no_launch:

Then reinstall your distro.

WslRegisterDistribution failed with error 0x8007019e
====================================================
WSL is not enabled. See :ref:`os-windows-wsl-enable`

.. _WSL: https://docs.microsoft.com/en-us/windows/wsl/install-win10
.. _Manual Install: https://docs.microsoft.com/en-us/windows/wsl/install-manual
.. _Initialize: https://docs.microsoft.com/en-us/windows/wsl/initialize-distro
.. _Troubleshooting: https://docs.microsoft.com/en-us/windows/wsl/troubleshooting