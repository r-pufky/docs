.. _service-zfs:

ZFS
###
Set up and maintain a ZFS pool.

Uses :ref:`1804-server-base-install`. See `ZFS Tutorial`_.

ZFS Install
***********
This is now in the default repositories for Ubuntu. The `old PPA archive is
here`_.

.. note::
  The ``HWE`` kernel currently does not build properly, you need to use the
  generic kernel `until this bug is resolved`_.

`Ubuntu 16.04+ has native ZFS kernel`_ level support built in. Only user tools
need to be installed.

.. code-block:: bash
  :caption: Install ZFS tools.

  apt install zfsutils-linux

.. code-block:: bash
  :caption: Install RAM FS tools if ZFS is to be used for the **root** filesystem as well.

  apt install zfs-initramfs

Mounting Existing ZFS Pool
**************************
.. code-block:: bash

  sudo zpool import {CONTAINER}
  sudo zpool status {CONTAINER}
  sudo zpool scrub {CONTAINER}

.. note::
  * A container name does not need to be used to identify a ZFS container, it will
    be detected automatically. ``sudo zpool import``.
  * Ensure low-level disks are setup properly. See
    :ref:`service-zfs-create-new-pool`.
  * Search for the pool, then mount it, use ``-f`` if it wasn't exported before.
    Scrub.

.. _service-zfs-create-new-pool:

Creating New ZFS Pool
*********************
.. code-block:: bash
  :caption: Create a GPT partition for each disk to be used.

  ls -l /dev/disk/by-id
  for x in `ls -1 /dev/disk/by-id/ata-*`; do
    sudo parted /dev/disk/by-id/${x} mklabel gpt quit;
  done

.. note::
  * by-id is the easiest to use as it identifies drives by the WWN (World Wide
    Name) or a composite of the model and serial number.
  * Use ``GPT`` partitions for `2TB+ disk support`_.
  * Use ``smartctl -i {DEVICE}`` to get `detailed information on disk`_.

.. code-block:: bash
  :caption: Create a ZFS container.

  sudo zpool create -o autoexpand=on -o ashift=12 -m /data {CONTAINER} raidz /dev/disk/by-id/ata-*
  sudo zpool list
  sudo zpool status {CONTAINER}
  sudo zdb -C {CONTAINER}

.. note::
  * ``autoexpand=on`` enables auto-expanding of ZFS pool when new disks are
    added.
  * ``ashift=12`` `Enables 4K sectors`_. **All > 2011** drives should have 4K
    sectors. This **cannot** be changed once set in the pool, and will lead to
    severe performance degradation if mis-matched for FS/drives. Cannot
    hotswap/replace ``512`` with ``4K`` drives in pool.
  * With ``-C`` option, ensure ``ashift=12`` is enabled.
  * ``ata-*`` should be replaced with a filter to match drives to use. Can
    specify multiple drives explicitly.
  * ZFS will automatically create partitions on drives.

`Upgrading ZFS with Larger Disks`_
**********************************

.. code-block:: bash

  sudo zpool scrub {CONTAINER}
  sudo zpool status {CONTAINER}
  ls -l /dev/disk/by-id
  ls -l /dev/disk/by-vdev
  sudo parted /dev/disk/by-id/{DISK}
  mklabel gpt
  quit
  sudo zpool replace {CONTAINER} sdb

.. warning::
  **Data destructive**. Verify the correct drive is selected.

`Setup Monthly ZFS Scrub`_
**************************
Scrubbing verifies all blocks can be read, and marks then bad if not. This is
done while the filesystem is online, but may slightly impact performance.

.. code-block:: bash
  :caption: **0750 root root** ``/root/bin/scrub-zpool-monthly``

  #!/bin/bash
  #
  # Scrubs zpool set at the beginning of the month.
  # Note: cronjob should run set to run on a day of the week.
  if [ $(date +\%d) -le 07 ]; then
    /sbin/zpool scrub CONTAINER
  fi

.. code-block:: bash
  :caption: Add to `root crontab`_ to run monthly.

  @weekly /root/bin/scrub-zpool-monthly

.. _old PPA archive is here: https://launchpad.net/~zfs-native/+archive/ubuntu/stable
.. _2TB+ disk support: https://www.cyberciti.biz/tips/fdisk-unable-to-create-partition-greater-2tb.html
.. _ZFS Tutorial: http://kbdone.com/zfs-basics/
.. _Upgrading ZFS with Larger Disks: http://www.itsacon.net/computers/unix/growing-a-zfs-pool/
.. _Enables 4K sectors: https://forums.freebsd.org/threads/zfs-replacing-512b-drives-by-4k-drives.29539/
.. _Setup Monthly ZFS Scrub: https://docs.oracle.com/cd/E23823_01/html/819-5461/gbbwa.html
.. _root crontab: https://en.wikipedia.org/wiki/Cron
.. _until this bug is resolved: https://bugs.launchpad.net/ubuntu/+source/linux/+bug/1693757
.. _Ubuntu 16.04+ has native ZFS kernel: https://wiki.ubuntu.com/ZFS
.. _detailed information on disk: https://www.thomas-krenn.com/en/wiki/Analyzing_a_Faulty_Hard_Disk_using_Smartctl