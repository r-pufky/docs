.. _service-zfs-manual-install:

ZFS Install
###########
Installation and creation of a new ZFS pool.

.. code-block:: bash
  :caption: Install ZFS tools.

  apt install zfsutils-linux

.. code-block:: bash
  :caption: Install RAM FS tools if ZFS is to be used for the **root** filesystem as well.

  apt install zfs-initramfs

.. note::
  The ``HWE`` kernel currently does not build properly for Ubuntu, you need to
  use the generic kernel `until this bug is resolved <https://bugs.launchpad.net/ubuntu/+source/linux/+bug/1693757>`_.

.. _service-zfs-create-new-pool:

Creating New ZFS Pool
*********************
Best practice from years of ZFS use are:

* Use an unecrypted ZFS pool.
* Create datasets to handle specific data needs/types/etc. Keep massive files
  in one dataset (e.g. videos), versus one for running services.
* Set dataset options based on those needs (encryption, compression, etc). This
  isolates master encryption keys and makes data management easy years later.
* Set mountpoints immutable ``chattr +i {MOUNTPOINT}`` when dataset is not
  mounted. This prevents writing to those mountpoints when the pool/dataset is
  not mounted or unlocked.

See :ref:`service-zfs-encryption`.

.. code-block:: bash
  :caption: Determine disks to add to ZFS pool.

  lsblk
  ls -l /dev/disk/by-id

.. note::
  ZFS will handle the paritioning of raw disks automatically. There is no need
  to explicitly partition your disks beforehand.

  Do not encrypt the root pool, or mount it. Encrypt and mount datasets instead.
  See :ref:`service-zfs-encryption`.

.. code-block:: bash
  :caption: Create a ZFS pool.

  zpool create -o autoexpand=on -o ashift=12 -O mountpoint=none {POOL} raidz2 /dev/disk/by-id/wwn-*
  zpool list
  zpool status {POOL}
  zdb -C {POOL}

* ``autoexpand=on`` enables auto-expanding of ZFS pool when new disks are
  added.
* ``ashift=12`` `Enables 4K sectors <https://forums.freebsd.org/threads/zfs-replacing-512b-drives-by-4k-drives.29539/>`_.
  **All > 2011** drives should have 4K sectors. This **cannot** be changed once
  set in the pool, and will lead to severe performance degradation if
  mis-matched for FS/drives. Cannot hotswap/replace ``512`` with ``4K`` drives
  in pool.
* ``-O mountpoint=none`` the unencrypted pool will not be mounted; mount
  datasets instead.
* ``raidz2`` preferred for 6+ disk arrays. ``raidz`` for <6.
* ``www-*`` replace with bash expansion to match drives to use. Can specify
  multiple block devices explicitly.
* With ``-C`` option, ensure ``ashift=12`` is enabled.
