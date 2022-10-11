.. _preseed-fully-automatic-efi-install:

Fully Automatic Installation
############################
Use this option to boot an ISO image that immediately starts the install
process. This will immediately drop into the debian installer with required
options pre-selected using EFI/UEFI.

Alternative Configurations:

* :ref:`preseed-grub-efi-boot-menu`
* :ref:`preseed-grub-non-efi-boot-menu`

.. code-block:: bash
  :caption: **0644 root root** ``custom-iso/isolinux/isolinux.cfg``
  :lineno-start: 10

  default custom-saltstack
  label custom-saltstack
    menu label ^Install Ubuntu Server w/ Saltstack minion
    kernel /install/vmlinuz
    append file=/cdrom/preseed/ubuntu-saltstack.seed vga=768 debian-installer/language=en debian-installer/country=US console-setup/ask_detect=false keyboard-configuration/layoutcode=us debian-installer/locale=en_US.UTF-8 localechooser/preferred-locale=en_US.UTF8 initrd=/install/initrd.gz quiet ---

.. note::
  This correctly seeds the default isolinux boot image to automatically drop
  into the preseed installation, with required options.

Proceed to :ref:`preseed-create-installation-file`