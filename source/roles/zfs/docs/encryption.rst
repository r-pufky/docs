.. _service-zfs-encryption:

Encryption
##########
Best practice is to encrypt all datasets but not the pool. Encryption works by
generating a master encrpytion key for the dataset (which the user does not
access). Password or keyfiles are used to unlock the master encryption key. By
isolating data to smaller datasets, exposure of the master key is constrained.
See `ArchLinux ZFS Native Encryption <https://wiki.archlinux.org/title/ZFS#Native_encryption>`_
for detailed CLI usage with examples.

Do not `encrypt root ZFS pool <https://old.reddit.com/r/zfs/comments/bnvdco/zol_080_encryption_dont_encrypt_the_pool_root/>`_.
Encrypting the pool will result in difficulty later on when migrating/managing
the pool:

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
***********************
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

.. hint::
  Set mountpoint to immutable without the ZFS dataset mounted. This prevents
  writes when the dataset is not ready: ``chattr +i {MOUNTPOINT}``

Change Encryption Keys/Method
*****************************
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

`Reference <http://manpages.ubuntu.com/manpages/impish/man8/zfs-change-key.8.html>`__

.. rubric:: References

#. `ZFS Native Encryption <https://arstechnica.com/gadgets/2021/06/a-quick-start-guide-to-openzfs-native-encryption/>`_
#. `ZFS Encryption at Rest <https://blog.heckel.io/2017/01/08/zfs-encryption-openzfs-zfs-on-linux/>`_
