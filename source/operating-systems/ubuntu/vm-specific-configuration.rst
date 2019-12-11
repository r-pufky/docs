.. _ubuntu-vm-specific-configuration:

Ubuntu VM Configuration
#######################

Installing XenServer / XCP Tools
================================
Only for VM systems. This enables better VM management.

Mount ``guest-tools.iso`` on VM management console:

.. code-block:: bash
  :caption: On VM system.

  sudo mount /dev/dvd /mnt
  sudo /mnt/Linux/install.sh

.. rubric:: References

#. `Expanding a LVM after expanding virtual machine disk <https://www.rootusers.com/how-to-increase-the-size-of-a-linux-lvm-by-expanding-the-virtual-machine-disk/>`_