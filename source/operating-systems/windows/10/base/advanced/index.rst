.. _w10-pro-advanced:

Advanced
########
.. danger:: Only apply these if you know what you are doing.

Advanced Windows configuration. Specific configuration for specific cases.

* :ref:`w10-specific-windows-fixes` for unique cases.
* :ref:`w10-wsl` to run Linux in Windows Kernel. 
* :ref:`w10-scheduled-tasks-inconsistencies` to remediate scheduling service issues.
* :ref:`w10-run-windows-on-usb` to run (not install) Windows on USB.

.. _w10-advanced-references:

.. rubric:: Advanced References

#. `Windows Command Reference <https://ss64.com/nt/run.html>`_
#. `Windows Launch Command Shortcuts <https://docs.microsoft.com/en-us/windows/uwp/launch-resume/launch-settings-app>`_

.. rubric:: Group Policy (GPO)

#. `Group Policy Administrative Templates Catalog <https://getadmx.com/>`_
#. `Windows Group Policy Reference <https://www.windows-security.org/group-policy-setting/3813-windows-group-policy-encyclopedia>`_
#. `Deploying Regsitry Keys via GPO <https://thesolving.com/server-room/how-to-deploy-a-registry-key-via-group-policy/>`_

.. rubric:: Windows Connections to Microsoft Services

#. `Windows Management Options for Each Component Setting (UI, Reg, GPO) <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services>`_

.. rubric:: Scripting

#. `Registry Data Types <https://docs.microsoft.com/en-us/windows/win32/shell/hkey-type>`_
#. `Windows Tweaking Scripts <https://github.com/Disassembler0/Win10-Initial-Setup-Script>`_
#. `Well Known Windows SIDs (Security Identifiers) <https://docs.microsoft.com/en-us/troubleshoot/windows-server/identity/security-identifiers-in-windows>`_

.. toctree::
   :hidden:
   :maxdepth: -1

   specific-windows-fixes
   windows-subsystem-for-linux-wsl
   scheduled-tasks-inconsistencies
   run-windows-on-usb
