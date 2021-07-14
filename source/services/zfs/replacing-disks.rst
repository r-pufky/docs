.. _service-zfs-replacing-disks:

Replacing Disks
###############
Management of underlying block devices for ZFS.

Hotswap Bad Disk
****************
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
****************
Offine replacement of a bad disk. Bring server down, replace the broken disk
with the new one and boot.

.. code-block:: bash
  :caption: Replace disk.

  zpool status {POOL}
  lsblk
  zpool replace {POOL} {BAD DISK} {NEW DISK}
  zpool status {POOL}

`Upgrade with Larger Disks <http://www.itsacon.net/computers/unix/growing-a-zfs-pool/>`_
****************************************************************************************
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
