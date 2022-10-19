.. _service-zfs:

ZFS
###
ZFS (Zettabyte FileSystem) storage pool. See
`ZFS Tutorial <http://kbdone.com/zfs-basics/>`_ (outdated, but good for
concepts).

.. toctree::
   :hidden:
   :maxdepth: -1

   manual-install
   operations
   encryption
   sync-backup
   replacing-disks

.. role:: zfs
  :service_doc: https://openzfs.org/wiki/Main_Page
  :private:
  :update:      2022-10-09

  Import ZFS datasets and setup ZFS incremental snapshots on system.

Defaults
********
.. literalinclude:: ../defaults/main.yml
