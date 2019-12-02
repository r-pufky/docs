.. _preseed-grub-efi-boot-menu:

GRUB EFI Boot Menu
##################
Use this option to add an additional menu item in the boot menu for the ISO,
which will allow you to do an automated install after setting your preferences
and potentially using any utilities on the standard boot menu.

This is for modern (EFI/UEFI) systems.

Alternative Configurations:

* :ref:`preseed-fully-automatic-efi-install`
* :ref:`preseed-grub-non-efi-boot-menu`

.. code-block:: bash
  :caption: **0644 root root** ``custom-iso/boot/grub/grub.cfg``
  :lineno-start: 15

  set default 0
  menuentry "Install Ubuntu Server w/ Saltstack minion" {
    set gfxpayload=keep
    linux /install/vmlinuz file=/cdrom/preseed/ubuntu-saltstack.seed debian-installer/language=en debian-installer/country=US console-setup/ask_detect=false keyboard-configuration/layoutcode=us debian-installer/locale=en_US.UTF-8 localechooser/preferred-locale=en_US.UTF8 quiet ---
    initrd /install/initrd.gz
  }

.. note::
  This assumes you place the custom entry first. Adjust default accordingly.

Proceed to :ref:`preseed-create-installation-file`