.. _base-vm-template:

Base VM Template
################
Standard VM Template used for server setup and configuration.

Ubuntu
******
.. gtable:: Ubuntu Base VM Specifications
  :header: Type,
           Value
  :c0:     CPU,
           Memory,
           Disk
  :c1:     1 (1 socket; 1 core),
           1 GB,
           10 GB
  :no_key_title:
  :no_caption:
  :no_launch:

.. gtable:: Ubuntu Base VM Configuration
  :header: Type,
           Value
  :c0:     BIOS,
           Memory,
           CPU,
           Disk,
           Ethernet,
           Partitioning,
           Hostname,
           Full Name,
           Username,
           Password,
           Homedirectory,
           Partitioning,
           Updates,
           Packages
  :c1:     Copy BIOS strings to VM,
           8 GB,
           1 (1 sockets; 1 cores),
           10 GB,
           1 GB Ethernet bridged,
           Default Windows Scheme,
           Ubuntu,
           None,
           template,
           template,
           Not Encrypted,
           Guided; Full; Max,
           Automatic Security Updates,
           Standard System Utilities
  :no_key_title:
  :no_caption:
  :no_launch:

    .. note::
      Ubuntu VM's are managed with saltstack, see :ref:`salt-saltstack`.

Windows 10
**********
.. gtable:: Windows Base VM Specifications
  :header: Type,
           Value
  :c0:     BIOS,
           Memory,
           CPU,
           Disk,
           Ethernet,
           Partitioning,
           Hostname
  :c1:     Copy BIOS strings to VM,
           8 GB,
           8 (4 sockets; 2 cores),
           60 GB,
           1 GB Ethernet bridged,
           Default Windows Scheme,
           Windows
  :no_key_title:
  :no_caption:
  :no_launch:

    .. note::
      Copy BIOS strings over to keep activation for base hardware. Generally,
      follow :ref:`windows-10-pro-setup`.

Activating Windows
==================
You'll need a VM license for activating windows 10 on a VM. Homegamers can
probably get away with running one windows VM at a time. YMMV, I am not a
lawyer. Act in good faith.

* Ensure system is fully update to date.
* Applied :ref:`meltdown-spectre-patch`.

:cmdmenu:`⌘ --> Settings --> Update & Security --> Activation`

Install Virtualization Tools
============================
#. Mount the virtualization toolset for specific hypervisor:

   * ``guest-tools.iso`` on XenServer default repository.
   * `Install packages`_ for KVM.

#. Install tool packages and reboot VM.
#. Check and apply new updates.

Default Applications
====================
Add the base applications used by all VM's:

   * :ref:`apps-chrome`.
   * :ref:`apps-putty`.
   * `WinSCP`_.
   * :ref:`apps-sublime-text`.
   * :ref:`enabling-ssh-access`. (just download, don't install service).

Adding Custom Fonts
===================
Fonts must be imported for use in applications, such as sublime text.

Copy font files to system. Select all fonts then :cmdmenu:`RMB --> Install`.

.. note::
  Installed fonts can be deleted. These are now installed in the font directory.

.. _WinSCP: https://winscp.net/eng/download.php
.. _Install packages: http://www.linux-kvm.org/page/WindowsGuestDrivers