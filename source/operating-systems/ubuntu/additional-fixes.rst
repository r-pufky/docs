.. _additional-ubuntu-fixes:

Additional Ubuntu Fixes
#######################

Grub OS Prober
**************
Grub will throw the following error on 4.9+ Kernels running VM's on block
devices or ZFS during normal upgrades:

.. pull-quote::
  *device-mapper reload ioctl on osprober-linux*

These devices are attempted to be unmounted while in use to detect other OS's on
those partitions. This may be `safely disabled if you are only running one OS`_.

.. code-block:: bash
  :caption: **0644 root root** ``/etc/default/grub``
  :lineno-start: 12
  :emphasize-lines: 1

  GRUB_DISABLE_OS_PROBER=true

.. code-block:: bash
  :caption: Update GRUB to apply changes and restart apt updates.

  update-grub
  apt update && apt upgrade

NXDOMAIN Errors in Syslog
*************************
This is caused by the systemd resolver not properly resolving local DNS.
Resolved in `systemd - 239-7ubuntu4`_, but it is currently not avaliable to
install.



.. code-block:: bash
  :caption: The workaround is to redirect the systemd resolver to the resolver
            specified from DHCP.

  mv /etc/resolv.conf /etc/resolv.conf.broken
  ls -s /etc/run/systemd/resolve/resolv.conf resolv.conf

.. _safely disabled if you are only running one OS: https://unix.stackexchange.com/questions/347466/debian-new-error-message-upgrading-kernel-to-4-9-reload-ioctl-error
.. _systemd - 239-7ubuntu4: https://bugs.launchpad.net/ubuntu/+source/systemd/+bug/1766969