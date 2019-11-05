.. _preseed-grub-non-efi-boot-menu:

GRUB non-EFI Boot Menu
######################
Use this option to add an additional menu item in the boot menu for the ISO,
which will allow an automated install after setting preferences and potentially
using any utilities on the standard boot menu.

This is for legacy (non-EFI/BIOS) systems.

Alternative Configurations:

* :ref:`preseed-fully-automatic-efi-install`
* :ref:`preseed-grub-efi-boot-menu`

.. code-block:: bash
  :caption: **0644 root root** ``custom-iso/isolinux/txt.cfg``
  :lineno-start: 6

  default custom-saltstack
  label custom-saltstack
    menu label ^Install Ubuntu Server w/ Saltstack minion
    kernel /install/vmlinuz
    append file=/cdrom/preseed/ubuntu-saltstack.seed vga=768 debian-installer/language=en debian-installer/country=US console-setup/ask_detect=false keyboard-configuration/layoutcode=us debian-installer/locale=en_US.UTF-8 localechooser/preferred-locale=en_US.UTF8 initrd=/install/initrd.gz quiet ---

.. note::
  This assumes you place the custom entry first. Adjust default accordingly.

Proceed to :ref:`preseed-create-installation-file`