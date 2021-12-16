.. _service-zfs-replacing-disks:

Replacing Disks
###############
Management of underlying block devices for ZFS.

ZFS will *automatically* partition the raw disk if it is not currently
partitioned. Only the root block device for disk needs to be known. Preference
is to use the WWN name (world-wide unique name) for the disk, which will be
consistent across systems. This is in ``/dev/disk/by-id/wwn-*``.

.. note::
  When issuing ZFS commands against devices in the pool, you **must** use those
  ID's.

  When issuing ZFS commands with devices **outside** the pool, you **must** use
  the full path, preferably with the WWN name.

.. _service-zfs-offline-replacement-bad-disk:

Offline Replacement Bad Disk
****************************
For non-server grade hardware where the server must be shutdown and disks
physically swapped. This also applies in cases where there is no additional
space and a drive must be removed to be replaced.

Determine the bad disk based on the status returned. This disk ID may be the WWN
or the full path to the disk. If it is the WWN, determine the block device.
Identify the drive serial number for easy hardware swapping when off.

.. code-block:: bash
  :caption: Identify block devices to minimize downtime

  zpool status {POOL}
  ls -l /dev/disk/by-id/{BAD DISK}
  smartctl -i /dev/disk/by-id/{BAD DISK}

.. code-block:: bash
  :caption: Identify the ZFS GUID for the bad disk

  zdb

.. code-block:: bash
  :caption: The ZFS GUID would be 13942365352362146142

  $ zdb
    ...
    children[1]:
        type: 'disk'
        id: 1
        guid: 13942365352362146142
        path: '/dev/disk/by-id/wwn-0xXXXXXXXXXXXXXXXX-part1'
        whole_disk: 0
        DTL: 403
        create_txg: 4
        com.delphix:vdev_zap_leaf: 131

.. code-block:: bash
  :caption: Offline the bad disk in the pool

  zpool status {POOL}
  zpool offline {POOL} {BAD DISK}
  shutdown -h now

Replace the pyhsical disk with the new disk and reboot. Find the new block
device to replace the old drive.

.. code-block:: bash
  :caption: Find the new disk to add to ZFS pool

  lsblk
  smartctl -i /dev/disk/by-id/{NEW DISK}

.. code-block:: bash
  :caption: Replace the old disk using the ZFS GUID and the new disk WWN name

  zpool replace {POOL} {BAD DISK GUID} /dev/disk/by-id/{NEW DISK WWN}

This will initiate a disk replacement, partitioning the new disk if needed and
start the resilvering process. Immediately after this command ZFS will scan the
pool, which will look like:

.. code-block:: bash

  $ zpool status
     pool: tank
    state: DEGRADED
   status: One or more devices is currently being resilvered.  The pool will
           continue to function, possibly in a degraded state.
   action: Wait for the resilver to complete.
     scan: resilver in progress since Tue Sep 21 11:08:12 2021
           4.15T scanned at 26.4G/s, 3.55G issued at 22.6M/s, 45.7T total
           0B resilvered, 0.01% done, 24 days 13:33:50 to go
   config:

           NAME                                STATE     READ WRITE CKSUM
           hundo                               DEGRADED     0     0     0
             raidz2-0                          DEGRADED     0     0     0
               wwn-0xXXXXXXXXXXXXXXXX-part1    ONLINE       0     0     0
               wwn-0xXXXXXXXXXXXXXXXX-part1    ONLINE       0     0     0
               replacing-2                     DEGRADED     0     0     0
                 wwn-0xXXXXXXXXXXXXXXXX-part1  OFFLINE      0     0     0
                 wwn-0xXXXXXXXXXXXXXXXX        ONLINE       0     0     0
               wwn-0xXXXXXXXXXXXXXXXX-part1    ONLINE       0     0     0
               wwn-0xXXXXXXXXXXXXXXXX-part1    ONLINE       0     0     0
               wwn-0xXXXXXXXXXXXXXXXX-part1    ONLINE       0     0     0

.. code-block:: bash
  :caption: After the initial scan, resilvering should kickoff

  $ zpool status
    pool: tank
   state: DEGRADED
  status: One or more devices is currently being resilvered.  The pool will
          continue to function, possibly in a degraded state.
  action: Wait for the resilver to complete.
    scan: resilver in progress since Tue Sep 21 11:08:12 2021
          9.07T scanned at 10.1G/s, 570G issued at 636M/s, 45.7T total
          93.7G resilvered, 1.22% done, 20:40:40 to go
  config:

          NAME                                STATE     READ WRITE CKSUM
          hundo                               DEGRADED     0     0     0
            raidz2-0                          DEGRADED     0     0     0
              wwn-0xXXXXXXXXXXXXXXXX-part1    ONLINE       0     0     0
              wwn-0xXXXXXXXXXXXXXXXX-part1    ONLINE       0     0     0
              replacing-2                     DEGRADED     0     0     0
                wwn-0xXXXXXXXXXXXXXXXX-part1  OFFLINE      0     0     0
                wwn-0xXXXXXXXXXXXXXXXX        ONLINE       0     0     0  (resilvering)
              wwn-0xXXXXXXXXXXXXXXXX-part1    ONLINE       0     0     0
              wwn-0xXXXXXXXXXXXXXXXX-part1    ONLINE       0     0     0
              wwn-0xXXXXXXXXXXXXXXXX-part1    ONLINE       0     0     0

`Reference <https://askubuntu.com/questions/305830/replacing-a-dead-disk-in-a-zpool>`__

Hotswap Bad Disk
****************
Hotswap disks if your hardware supports it. See
:ref:`service-zfs-offline-replacement-bad-disk` for manual instructions.

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

Combination of Raw Disks and Partitions in Pool
***********************************************
This is **normal**; though unnerving if used to traditional disk management. ZFS
manages all disk hardware and depending on how the pool was created, when disks
were added, removed, or replaced. You may end up with some devices showing
partitions versus raw disks. This is **OK**. The zpool listing is just the ID
used to represent the disk.

Using ``zdb`` on the pool will show the details of the underlying hardware. Raw
disks will show a mapping to ``-part1`` if automatically created as well as a
reference to the underlying block device.


.. code-block:: bash
  :caption: Show the underlying hardware configuration for a ZFS pool

  $ zdb
    ...
  children[2]:
      type: 'disk'
      id: 2
      guid: 149i73844241267554311
      path: '/dev/disk/by-id/wwn-0xXXXXXXXXXXXXXXXX-part1'
      devid: 'ata-WDC_XXXXXXXXX-XXXXXXX_XXXXXXXX-part1'
      phys_path: 'pci-0000:01:00.1-ata-5.0'
      whole_disk: 1
      DTL: 272
      create_txg: 4
      com.delphix:vdev_zap_leaf: 262

This may also be confirmed by checking the block device itself. ZFS formatted
drives will have two partitions (part1, part9).

.. code-block:: bash

  ls -l /dev/disk/by-id/{DISK}*

  lrwxrwxrwx 1 root root  9 Sep 22 09:37 /dev/disk/by-id/wwn-0xXXXXXXXXXXXXXXXX -> ../../sde
  lrwxrwxrwx 1 root root 10 Sep 22 09:37 /dev/disk/by-id/wwn-0xXXXXXXXXXXXXXXXX-part1 -> ../../sde1
  lrwxrwxrwx 1 root root 10 Sep 22 09:37 /dev/disk/by-id/wwn-0xXXXXXXXXXXXXXXXX-part9 -> ../../sde9
