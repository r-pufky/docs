.. _additional-ubuntu-fixes:

Additional Ubuntu Fixes
#######################

Make RAW Disk Image of Physical Disk
************************************
DD can be used to make a RAW image of a disk, and can be mounted in other linux
systems for use.

.. code-block:: bash
  :caption: `Copy disk block device`_ to a file.

  dd if=/dev/{BLOCK} of=/some/filesystem/{IMAGE}.raw bs=1M conv=noerror,sync status=progress

.. code-block:: bash
  :caption: `Mount RAW disk`_ image for use.

  losetup -f -P /some/filesystem/{IMAGE}.raw
  losetup -l
  mount /dev/loop0p1 /mnt/test/
  umount /dev/loop0p1
  losetup -d /dev/loop0

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

.. _additional-ubuntu-fixes-disable-ipv6:

`Disable IPv6`_
***************
Disable if IPv6 is not being actively used to prevent any IPv6 misconfiguration
attacks.

.. code-block:: bash
  :caption: **0644 root root** ``/etc/sysctl.conf``

  net.ipv6.conf.all.disable_ipv6 = 1
  net.ipv6.conf.default.disable_ipv6 = 1
  net.ipv6.conf.lo.disable_ipv6 = 1

.. code-block:: bash

  sysctl -p
  reboot

Shadow Passwords
****************
linux hash *sha512*. Use either the ``mkpasswd`` tool or the `python script`_
below to generate a *salted, sha512 hash* in the correct format for consumption
in ``/etc/shadow``. GPG encrypt this data if storing in configuration
management tools.

.. code-block:: bash
  :caption: Using ``mkpasswd``.

  apt install whois
  mkpasswd -m sha-512

.. code-block:: bash
  :caption: Python 3 version.

  python3 -c "import crypt, getpass; print(crypt.crypt(getpass.getpass('password to hash: '), crypt.mksalt(crypt.METHOD_SHA512)))"

.. _safely disabled if you are only running one OS: https://unix.stackexchange.com/questions/347466/debian-new-error-message-upgrading-kernel-to-4-9-reload-ioctl-error
.. _systemd - 239-7ubuntu4: https://bugs.launchpad.net/ubuntu/+source/systemd/+bug/1766969
.. _Mount RAW disk: https://blog.tinned-software.net/mount-raw-image-of-entire-disc/
.. _Copy disk block device: https://blog.tinned-software.net/mount-raw-image-of-entire-disc/
.. _Disable IPv6: https://www.linuxbabe.com/ubuntu/disable-ipv6-on-ubuntu
