.. _xenserver:

XenServer (XCP-NG)
##################
XenServer Setup & Lockdown (XCP-NG, Citrix XenServer).

`Securing Xenserver`_
*********************
Basic steps to harden an out of box installation of xenserver. Required.

Console non-root User Setup
===========================
Create a non-root user account with sudo access.

.. code-block:: bash
  :caption: Add a non-root account.

  useradd {USER}
  passwd {PASS}
  visudo

.. code-block:: bash
  :caption: ``visudo``

  {USER}  ALL=(ALL)  ALL

.. code-block:: bash
  :caption: Confirm sudo works as new user.

  sudo su -

:ref:`ubuntu-generate-certificates` for the new user.

Enforce cert-only SSH logins:

.. code-block:: bash
  :caption: **0644 root root** ``/etc/ssh/sshd_config``

  permitrootlogin no
  allowusers {USER}
  MaxAuthTries 3
  PasswordAuthentication no
  AuthorizedKeysFile %h/.ssh/authorized_keys

.. code-block:: bash
  :caption: Restart SSHD to apply changes.

  service sshd restart

Disable Utils Webpage
=====================

.. code-block:: bash
  :caption: Set index.html to empty file.

  cp /opt/xensource/www/Citrix-index.html /home/{USER}/original-index.html
  echo '' > /opt/xensource/www/Citrix-index.html

Restrict XAPI to Pre-defined Hosts
==================================
Only allow explicit hosts access to the API.

.. code-block:: bash
  :caption: **0644 root root** ``/etc/hosts.deny``

  xapi:ALL

.. code-block:: bash
  :caption: **0644 root root** ``/etc/hosts.allow``

  xapi:{IP} {IP}

Disable TLS < 1.2 for SSL Connections
=====================================

.. code-block:: bash
  :caption: Disable TLS < 1.2 via CLI.

  xe pool-disable-ssl-legacy

.. note::
  This can be done in the GUI via
  :cmdmenu:`XenPool --> Properties --> Security --> TLS 1.2 only`.

Only `Keep 2 Days of Logs`_
===========================
Keep 2 days of log rotations, instead of 31 by default.

.. code-block:: bash
  :caption: **0644 root root** ``/etc/logrotate.conf``

  rotate 2

Creating A `Local ISO Repository`_
**********************************
This will allow the use of ISO's on ``dom0`` to be used during VM creation. From
an SSH session, create a directory and create a Storage Repository on top of it.

.. code-block:: bash
  :caption: Create Local ISO repository.

  mkdir -p /var/opt/xen/iso_import
  xe sr-create name-label=LocalISO type=iso device-config:location=/var/opt/xen/isos device-config:legacy_mode=true content-type=iso

.. code-block:: bash
  :caption: Refresh ISO library contents.

  xe sr-list
  xe sr-scan uuid={UUID OF ISO REPOSITORY}

Convert VM to a Template
************************
* Clear command history from root/user.
* shutdown cleanly.
* VM: set vCPU priority to lowest (if reasonable).
* VM: set Memory to dynamic, 512-1024MB (if reasonable).
* VM: :cmdmenu:`RMB --> Convert to Template`.
* Template: Custom Fields: add custom fields as needed.

Modifying a `VM Template`_
**************************
* Copy the UUID from the template image :cmdmenu:`General --> Properties --> UUID`
* SSH to the XenServer, change to root.
* Convert template to VM and start it.

  .. code-block:: bash
    :caption: Start a Template VM.

    xe vm-param-set uuid={UUID} is-a-template=false
    xe vm-start uuid={UUID}

* After changes, convert back to a template in the GUI.

Manually Creating New VM from Template
**************************************
Determine the template name, and create a new VM from that template, start it.

.. code-block:: bash
  :caption: Create a new VM from Template.

  xe template-list
  xe vm-install template="{TEMPLATE NAME}" new-name-label="{NEW VM}"
  xe vm-start uuid={NEW VM}

PCI Passthrough for Direct Hardware Access
******************************************
Used for direct hardware access needs, like disks for ZFS and GPU's for plex.

Find Device IDs
===============
On XenServer as ``root``, list PCI devices and determine the device ID's that
you want. They are in the format **B:D.f** (beginning of line). You can see
current drives attached to these PCI devices by `listing system block devices`_.

.. code-block:: bash
  :caption: List block devices.

  lspci
  ls -a /sys/block

Prevent dom0 Driver Binding
===========================
This prevents dom0 from binding to hardware and presenting via a meta-layer.

.. code-block:: bash
  :caption: Prevent dom0 from binding to specific PCI hardware.

  /opt/xensource/libexec/xen-cmdline --set-dom0 "xen-pciback.hide=(04:00.0)"

.. note::
  .. code-block:: bash
    :caption: For multiple devices.

    /opt/xensource/libexec/xen-cmdline --set-dom0 "xen-pciback.hide=(04:00.0)(00:02.0)"

**Reboot** XenServer.

Add `PCI Device Passthrough`_
*****************************
With target VM off, determine UUID of vm with ``xe vm-list``, then `passthrough
PCI devices`. You only have to do this once.

.. code-block:: bash
  :caption: Add PCI device passthrough to a specific VM.

  xe vm-param-set other-config:pci=0/0000:{B:D.f} uuid={VM UUID}

.. note::
  .. code-block:: bash
    :caption: For `multiple PCI devices`_.

    xe vm-param-set other-config:pci=0/0000:{B:D.f},0/0000:{B:D.f} uuid={VM UUID}

Fix `Missing OS Templates`_
***************************
If there are missing OS templates when creating a VM, it generally means that
the ``create-guest-templates`` script hasn't been run. Running it manually as
root on the server will add/update all OS templates and populate the dropdown.

.. code-block:: bash
  :caption: Re-create guest templates.

  /usr/bin/create-guest-templates

Auto Start VM on `Boot`_
************************
Start VM when Hypervisor is booted.

.. code-block:: bash
  :caption: Both the pool that the VM is in and the VM need to be enabled.

  xe pool-list
  xe vm-param-set uuid={POOL} other-config:auto_poweron=true
  xe vm-list
  xe vm-param-set uuid={VM} other-config:auto_poweron=true

.. rubric:: References

#. `Adding new usergroups to XenServer <https://discussions.citrix.com/topic/154063-add-new-usersgroup-to-xenserver/>`_
#. `XenServer 7.0 release notes <https://docs.citrix.com/en-us/xenserver/7-0/downloads/release-notes.pdf>`_

.. _Securing Xenserver: http://burm.net/2012/01/29/xenserver-basic-security-tips-how-do-you-secure-your-xenserver/
.. _Missing OS Templates: https://www.reddit.com/r/XenServer/comments/607pbi/my_xenserver_is_missing_templates/
.. _VM Template: https://discussions.citrix.com/topic/241867-guest-best-pratice-copy-vm-or-convert-to-template/
.. _Local ISO Repository: https://xen-orchestra.com/blog/creating-a-local-iso-repository-in-xenserver/
.. _passthrough PCI devices: https://wiki.xen.org/wiki/Xen_PCI_Passthrough
.. _multiple PCI devices: https://discussions.citrix.com/topic/355675-xenserver-pci-passthrough-pv-hvm-multiple-devices/
.. _PCI Device Passthrough: https://github.com/xcp-ng/xcp/wiki/PCI-Passtrough
.. _Keep 2 Days of Logs: https://discussions.citrix.com/topic/299016-how-to-disable-xenserver-logging/
.. _listing system block devices: https://willhaley.com/blog/find-correspond-disk-belongs-which-hard-drive-controller-linux/
.. _Boot: https://xen-orchestra.com/blog/auto-start-vm-on-xenserver-boot/
