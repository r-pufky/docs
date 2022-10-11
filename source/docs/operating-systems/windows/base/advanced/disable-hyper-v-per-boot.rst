.. _wbase-specific-windows-fixes-disable-hyper-v-per-boot:

Disable Hyper-V Per Boot
************************
Some applications and games detect Hyper-V virtualization and refuse to start.
Disable Hyper-V on Windows boot instead of through the BIOS. This removes the
hypervisor kernel modules which prevents this from happening without needing to
turn it off.

.. code-block:: powershell
  :caption: powershell (as admin).

  bcdedit --% /copy {current} /d "No Hyper-V"

  bcdedit --%  /set {GUID} hypervisorlaunchtype off

Restart holding :cmdmenu:`shift` to show boot options. Select ``No Hyper-V``.

`Reference <https://www.hanselman.com/blog/switch-easily-between-virtualbox-and-hyperv-with-a-bcdedit-boot-entry-in-windows-81>`__
