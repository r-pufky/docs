.. _ubuntu-preseed-installation:

`Ubuntu Automatic (Preseed) Installation`_
##########################################
Preseeding allows you to install debian/ubuntu from an ISO image with selections
already made, setting up specific base packages so that it can be automatically
installed on boot and immediately used afterwards. This is great for VM's and
pre-setup of configuration management agents.

.. code-block:: bash
  :caption: Install utitlities to manipulate ISO images, debconf utilities and a
            password hash utility for ``/etc/shadow``.

  apt install debconf-utils whois xorriso

.. code-block:: bash
  :caption: Extract ISO for preseed modification to ``custom-iso``.

  xorriso -osirrox on -indev {UBUNTU IMAGE}.iso -extract / custom-iso

Depending on how you would like to preseed the automatic install:

* :ref:`preseed-fully-automatic-efi-install`
* :ref:`preseed-grub-non-efi-boot-menu`
* :ref:`preseed-grub-efi-boot-menu`

You can create a single disk that supports both EFI and non-EFI machines, just
create all files required for each. Ensure that your labels and configs are
changed accordingly.

.. rubric:: References

#. `Preseed file not found <https://askubuntu.com/questions/813058/preseed-ubuntu-16-04-not-working-preseed-file-not-found>`_
#. `Automated install using preseed <https://searchitchannel.techtarget.com/feature/Performing-an-automated-Ubuntu-install-using-preseeding>`_
#. `Unattended installs of ubuntu desktop <https://askubuntu.com/questions/806820/how-do-i-create-a-completely-unattended-install-of-ubuntu-desktop-16-04-1-lts>`_
#. `Preseeding methods <https://help.ubuntu.com/16.04/installation-guide/amd64/apbs01.html>`_
#. `Create a customized ubuntu server iso <https://askubuntu.com/questions/409607/how-to-create-a-customized-ubuntu-server-iso>`_

.. _Ubuntu Automatic (Preseed) Installation: https://help.ubuntu.com/16.04/installation-guide/amd64/apb.html

.. toctree::
   :hidden:
   :maxdepth: -1

   fully-automated-install
   grub-efi-boot-menu
   grub-non-efi-boot-menu
   create-preseed-file
   build-custom-iso