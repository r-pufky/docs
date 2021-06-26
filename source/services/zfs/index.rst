.. _service-zfs:

ZFS
###
ZFS (Zettabyte FileSystem) storage pool. See `ZFS Tutorial`_ (outdated, but good for
concepts).

ZFS Install
***********

.. code-block:: bash
  :caption: Install ZFS tools.

  apt install zfsutils-linux

.. code-block:: bash
  :caption: Install RAM FS tools if ZFS is to be used for the **root** filesystem as well.

  apt install zfs-initramfs

.. note::
  The ``HWE`` kernel currently does not build properly for Ubuntu, you need to
  use the generic kernel `until this bug is resolved`_.

Mounting Existing ZFS Pool
**************************
.. code-block:: bash

  zpool import {POOL}
  zpool status {POOL}
  zpool scrub {POOL}

.. note::
  * A pool name does not need to be used to identify a ZFS container, it
    will be detected automatically. ``zpool import -a``.
  * Search for the pool, then mount it, use ``-f`` if it wasn't exported.
    Scrub.

.. _service-zfs-create-new-pool:

Creating New ZFS Pool
*********************
Best practice from years of ZFS use are:

* Use an unecrypted ZFS pool.
* Create datasets to handle specific data needs/types/etc. Keep massive files in
  one dataset (e.g. videos), versus one for running services.
* Set dataset options based on those needs (encryption, compression, etc). This
  isolates master encryption keys and makes data management easy years later.
* Set mountpoints immutable ``chattr +i {ZFS MOUNT POINT}`` when dataset is not
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
* ``ashift=12`` `Enables 4K sectors`_. **All > 2011** drives should have 4K
  sectors. This **cannot** be changed once set in the pool, and will lead to
  severe performance degradation if mis-matched for FS/drives. Cannot
  hotswap/replace ``512`` with ``4K`` drives in pool.
* ``-O mountpoint=none`` the unencrypted pool will not be mounted; mount
  datasets instead.
* ``raidz2`` preferred for 6+ disk arrays. ``raidz`` for <6.
* ``www-*`` replace with bash expansion to match drives to use. Can specify
  multiple block devices explicitly.
* With ``-C`` option, ensure ``ashift=12`` is enabled.

.. _service-zfs-encryption:

`Encryption`_
*************
Best practice is to encrypt all datasets but not the pool. Encryption works by
generating a master encrpytion key for the dataset (which the user does not
access). Password or keyfiles are used to unlock the master encryption key. By
isolating data to smaller datasets, exposure of the master key is constrained.
See `ArchLinux ZFS Native Encryption`_ for detailed CLI usage with examples.

Do not `encrypt root ZFS pool`_. Encrypting the pool will result in difficulty
later on when migrating/managing the pool:

* Datasets on the pool can still be **encrypted** regardless. Store data in
  datasets and not on the root pool. Do not mount the root pool.
* Pool will mount on boot (encrypted datasets are not unless specifically
  automated).
* **All contents** of the root pool need to be removed to change encryption.
  This is quite literally days-to-weeks even for modest 6-disk (100T) pools.
* Metadata on datasets is unencrypted even with encryption. Encrypting the
  root drive offers no additional protection or data leakage from dataset
  metadata.
* Master key scope is reduced. Using a password or keyfile to unlock ZFS only
  unlocks the master key, it does not change it. By creating separate
  datasets (and not encrypting the entire pool), a different underlying master
  key is used for each, limiting breach scope.

.. code-block:: bash
  :caption: Create encrypted dataset on ZFS pool using 1 million pbkdf2 iterations.

  zfs create -o encryption=aes-256-gcm -o keyformat=passphrase -o keylocation=prompt -o pbkdf2iters=1000000 -o mountpoint=/d/media {POOL}/media

.. note::
  Pools created before ``ZoL 0.8.0`` (pool versions <= ``28``) must be upgraded
  before encryption is supported.

  .. code-block:: bash
    :caption: Upgrade ZFS pool to latest version.
    
    zpool upgrade -v
    zpool upgrade -a

.. danger::
  Always **confirm** key works before loading data.

  This means: unmount, unload encryption key, and remount before proceeding.
  
  This checks **you** and confirms you are using the password intended for the
  dataset; preventing dataloss on a missing key/password.

Mount Encrypted Dataset
=======================
.. code-block:: bash
  :caption: Mount encrypted dataset.

  zfs mount -l {POOL}/{DATASET}
  zfs mount -l -a

Once a key is loaded unmounting and remounting will not require re-entry of
the password or file.

Use ``zfs unload-key {POOL}/{DATASET}`` after unmounting to remove the key
from memory.

Use ``zfs load-key {POOL/DATASET}`` to prelod a dataset encryption key or
``zfs load-key -a`` to preload all keys in a pool; before mounting
(preventing prompts).

`Change Encryption`_ Keys/Method
================================
Change password, keyfile, or swap between the two methods. This does **not**
change the user-inaccessible master key (to do that you must create a new
dataset).

Always use full path for key. Ideally store on removable USB key for booting
where the mounted path will always be known. Otherwise store on encrypted boot
drive. Use a password if key would be stored on an unencrypted disk.

Always unmount, unload-key, and re-mount to confirm the expected key/password
works **before** loading data onto the dataset.

.. code-block:: bash
  :caption: Use (or change) password for dataset.

  zfs change-key -l -o keyformat=passphrase -o keylocation=prompt -o pbkdf2iters=1000000 {POOL}/{DATASET}

.. code-block:: bash
  :caption: Use (or change) keyfile for encrpytion key.

  dd if=/dev/urandom of=/root/zfs.key bs=1 count=32
  zfs change-key -l -o keyformat=raw -o keylocation=file:///root/zfs.key {POOL}/{DATASET}

.. danger::
  Do not overwrite or delete the old key until the new key is in place.

ZFS Filesystem Options
**********************
ZFS can be tweaked per dataset based on the data being used. ZFS only applies
new settings on newly written data; changing options for pre-existing data
requires export/re-import of that data to the dataset.

.. code-block:: bash
  :caption: Enable text compression and disable atime for Maildir datasets.

  zfs set atime=off {POOL}/{DATASET}
  zfs set compression=lz4 {POOL}/{DATASET}

.. code-block:: bash
  :caption: Enable high compression for backup datasets.

  zfs set compression=gzip {POOL}/{DATASET}

ZFS Disk Management
*******************
Management of underlying block devices for ZFS.

Hotswap Bad Disk
================
Hotswap disks if your hardware supports it.

.. code-block:: bash
  :caption: In-place replacement with no disk device ID change.

  zpool scrub {POOL}
  zpool status {POOL}
  lsblk
  zpool offline {POOL} {BAD DISK}
  {REPLACE DISK}
  zpool online {POOL} {NEW DISK}
  zpool replace {POOL} {NEW DISK}
  zpool status {POOL}

.. code-block:: bash
  :caption: Replacement with new disk device ID.

  {ADD NEW DISK}
  zpool scrub {POOL}
  zpool status {POOL}
  lsblk
  zpool replace {POOL} {BAD DISK} {NEW DISK}
  zpool status {POOL}
  {REMOVE BAD DISK}

Replace Bad Disk
================
Offine replacement of a bad disk. Bring server down, replace the broken disk
with the new one and boot.

.. code-block:: bash
  :caption: Replace disk.

  zpool status {POOL}
  lsblk
  zpool replace {POOL} {BAD DISK} {NEW DISK}
  zpool status {POOL}

`Upgrade with Larger Disks`_
============================
Capacity will automatically be expanded (``autoexpand=on``) when minimum disk
upgrade requirements have been met.

.. code-block:: bash
  :caption: Upgrade process for each disk in pool.

  zpool scrub {POOL}
  zpool status {POOL}
  lsblk
  zpool replace {POOL} {OLD DISK} {BIGGER DISK}
  zpool status {POOL}

.. warning::
  Repeat for each disk. Alternatively, the old disk can be offlined
  (``zpool offline {POOL} {OLD DISK}``), the new disk physically changed, and
  then replace (``zpool replace {POOL} {NEW DISK}``), if constrained by
  hardware.
  
  **Data destructive**. Verify the correct drive is selected.

`Setup Monthly ZFS Scrub`_
**************************
Scrubbing verifies all blocks can be read, and marks then bad if not. This is
done while the filesystem is online, but may slightly impact performance.

.. code-block:: bash
  :caption: **0750 root root** ``/root/bin/scrub-zpool-monthly``

  #!/bin/bash
  #
  # Scrubs zpool monthly.
  /sbin/zpool scrub {POOL}

.. code-block:: bash
  :caption: Add to `root crontab`_ to run monthly.

  @weekly /root/bin/scrub-zpool-monthly

.. _ZFS Tutorial: http://kbdone.com/zfs-basics/
.. _Upgradingw with Larger Disks: http://www.itsacon.net/computers/unix/growing-a-zfs-pool/
.. _Enables 4K sectors: https://forums.freebsd.org/threads/zfs-replacing-512b-drives-by-4k-drives.29539/
.. _Setup Monthly ZFS Scrub: https://docs.oracle.com/cd/E23823_01/html/819-5461/gbbwa.html
.. _root crontab: https://en.wikipedia.org/wiki/Cron
.. _until this bug is resolved: https://bugs.launchpad.net/ubuntu/+source/linux/+bug/1693757
.. _encrypt root ZFS pool: https://old.reddit.com/r/zfs/comments/bnvdco/zol_080_encryption_dont_encrypt_the_pool_root/
.. _ArchLinux ZFS Native Encryption: https://wiki.archlinux.org/title/ZFS#Native_encryption
.. _Change Encryption: http://manpages.ubuntu.com/manpages/impish/man8/zfs-change-key.8.html
