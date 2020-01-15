.. _windows-10:

Windows 10
##########
Standard Windows setup used for gaming. Removes known tracking & bloatware.

Working assumptions:

* Windows 10 pro (64 bit).
* Execution Policy: **Unrestricted** (see: :ref:`setting-execution-policy`).
* Assumes Admin Rights.

Related Material:

* :ref:`windows-10-pro-setup` for base installation.
* :ref:`windows-10-pro-securing-install` for securing a base install.
* :ref:`troubleshooting-pc-hardware` for diagnosing problems.
* :ref:`additional-windows-10-fixes` for uncommon Windows 10 fixes.
* :ref:`reinstalling-windows-10` for common backups before reinstalling.
* :ref:`scheduled-tasks-inconsistencies` for inconsistencies in scheduling
  service.

.. rubric:: References

#. `Windows Command Reference <https://ss64.com/nt/run.html>`_
#. `Group Policy Administrative Templates Catalog <https://getadmx.com/>`_
#. `Windows Launch Command Shortcuts <https://docs.microsoft.com/en-us/windows/uwp/launch-resume/launch-settings-app>`_
#. `Windows Management Options for Each Component Setting (UI, Reg, GPO) <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services>`_
#. `Windows Group Policy Reference <https://www.windows-security.org/group-policy-setting/3813-windows-group-policy-encyclopedia>`_
#. `Windows Management Options for Each Setting <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services>`_
#. `Registry Data Types <https://docs.microsoft.com/en-us/windows/win32/shell/hkey-type>`_
#. `Windows Tweaking Scripts <https://github.com/Disassembler0/Win10-Initial-Setup-Script>`_
#. `Deploying Regsitry Keys via GPO <https://thesolving.com/server-room/how-to-deploy-a-registry-key-via-group-policy/>`_
#. `Well Known Windows SIDs (Security Identifiers) <https://support.microsoft.com/en-us/help/243330/well-known-security-identifiers-in-windows-operating-systems>`_

.. toctree::
   :hidden:
   :maxdepth: -1

   setup/index
   securing-installation/index
   wsl
   troubleshooting-pc-hardware
   reinstalling
   additional-fixes
   scheduled-tasks-inconsistencies
