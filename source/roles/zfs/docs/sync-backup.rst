.. _service-zfs-sync-backup:

Sync / Backup
#############
ZFS send & receive allows for a powerful syncronization and backup mechanism.
It should be used instead of typical ``rsync`` linux methods. ZFS will send only
block level changes with typically a lower throughput, while ``rsync`` sends
entire files with higher throughput.

``rsync`` tends to be faster for the inital sync, but in the long run loses to
ZFS due to effeciciency gains across multiple TBs.

Snapshotting creates a point-in-time state for a given ZFS dataset; as the
system is Copy On Write (COW), this enables any snapshot to be deleted at any
time without dataloss (as long as the dataset/pool is not deleted), as well as
snapshots essentially being 'free' until more data is written to the dataset.
Sync'ing snapshot remotely requires a reference snapshot and the snapshot to
sync to.

Sync'ing Datasets
*****************
Dataset may be sync'ed to remote ZFS pools as a method for backup. These are
basic tools for sync'ing datasets. See :ref:`service-zfs-sync-backup-automation`
to backup and manage snapshots automatically.

.. code-block:: bash
  :caption: Create the initial snapshot for the local system

  zfs snapshot tank/example@YYYYMMDD

.. code-block:: bash
  :caption: Send the ZFS snapshot to the remote machine

  zfs send -R -w -I tank/example@YYYYMMDD | ssh remote_host sudo zfs receive -F -u -v tank2/example

.. note::
  It is important to use the RAW flags for encrypted datasets to be transferred.
  Encrypted datasets do not need to mounted. Blocks are transferred encrypted,
  meaning the remote machine does not need the key to sync the data, but will
  require the key to mount and read/write the data.

  The remote rollback to the latest snapshot ensures the new snapshot is
  transferred correctly, otherwise a syncronization error will occur.

.. _service-zfs-sync-backup-automation:

Automation
**********
:download:`zfs_incremental_snapshot <source/zfs_incremental_snapshot>` or clone
the repository: https://github.com/r-pufky/zincrsend. Read comments in the
script to setup correct sync.

.. literalinclude:: source/zfs_incremental_snapshot
  :caption: **0750 root root** ``/etc/zfs_sync/zfs_incremental_snapshot``


.. code-block:: bash
  :caption: Add to `crontab <https://en.wikipedia.org/wiki/Cron>`_.

  @weekly /etc/zfs_sync/zfs_incremental_snapshot &> /etc/zfs_sync/zfs_sync.log

Removing Old Snapshots
**********************
Snapshots can be sorted by creation time and deleted based on the number to
keep.

.. code-block:: bash
  :caption: Keep the latest two snapshots

  zfs_latest=`/usr/sbin/zfs list -H -t snapshot -o name -S creation | grep ^tank/example@ | head -2`
  zfs_delete=`/usr/sbin/zfs list -H -t snapshot -o name -S creation | grep ^tank/example@`

  # Remove latest snapshots from all set.
  for keep_snap in ${zfs_latest[@]}; do
    zfs_delete=( "${zfs_delete[@]/${keep_snap}}" );
  done

  # Destroy old snapshots
  for snap in ${zfs_delete[@]}; do
    /usr/sbin/zfs destroy ${snap}
  done

.. rubric:: References

#. `Using Snapshots <https://ubuntu.com/tutorials/using-zfs-snapshots-clones#2-using-snapshots>`_
#. `Send ZFS snapshot to Remote Machine <https://askubuntu.com/questions/764416/send-zfs-snapshot-to-remote-machine>`_
#. `Sending and Receiving ZFS Data <https://docs.oracle.com/cd/E19253-01/819-5461/gbchx/index.html>`_
