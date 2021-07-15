.. _service-dropbear:

`Dropbear <https://linuxconfig.org/how-to-install-and-configure-dropbear-on-linux>`_
####################################################################################
Remote unlock encrypted root filesystems over SSH on boot. Note that most
systems do not encrypt ``/boot`` and therefore dropbear keys should be
considered compromised/untrusted; use separate keys when using dropbear!

See :ref:`service-wireguard-initramfs` to enable wireguard service on boot for
fully encrypted remote boot root FS unlock!

Dropbear Setup
**************
.. code-block:: bash
  :caption: Install dropbear package

  apt install dropbear-initramfs

Set dropbear options:

.. literalinclude:: source/config
  :caption: **0644 root root** ``/etc/dropbear-initramfs/config``

Dropbear uses a special binary format for host keys. Generate a new pair of host
keys to use, and remove all others:

.. code-block:: bash
  :caption: Generate new dropbear host keys (RSA 4096); remove unused.

  dropbearkey -t rsa -s 4096 -f /etc/dropbear-initramfs/dropbear_rsa_host_key
  rm /etc/dropbear-initramfs/dropbear_{dss,ecdsa,ed25519}_host_key

Create a set of SSH keys to use for dropbear explicitly. These should be
password protected. Add to authorized keys for dropbear.

.. code-block:: bash
  :caption: Create SSH keys and set authorized keys for dropbear.

  ssh-keygen -b 4096 -t rsa -f ~/.ssh/dropbear
  cp ~/.ssh/dropbear.pub /etc/dropbear-initramfs/authorized_keys

Update Kernel
*************
The kernel must be updated everytime the dropbear configuration is changed.

.. code-block:: bash
  :caption: Update Kernel with Dropbear configuration.

  update-initramfs -u
  update-grub
  reboot

Remote Unlock
*************
.. code-block:: bash
  :caption: Use the dropbear key and unlock the system remotely.

  ssh -i ~/.ssh/dropbear root@remote_host
  # cryptroot-unlock
