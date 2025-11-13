# Encryption
Best practice is to encrypt all datasets but not the pool. Encryption works by
generating a master encryption key for the dataset (which the user does not
access). Password or keyfiles are used to unlock the master encryption key.

By isolating data to smaller datasets, exposure of the master key is
constrained. See [ZFS Native Encryption][a] for detailed CLI usage with
examples.


## [Do NOT Encrypt ZFS Pool][b]
Do not encrypt root ZFS pool
Encrypting the pool will result in difficulty later on when migrating and
managing the pool:

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


## Encrypt a Dataset
!!! warning
    Pools created before **ZoL 0.8.0** (pool versions <= **28**) must be
    upgraded before encryption is supported.

    ``` bash
    # Upgrade ZFS pool to latest version.
    zpool upgrade -v
    zpool upgrade -a
    ```

!!! danger
    Always **confirm** key works before loading data.

    This means: unmount, unload encryption key, and remount before proceeding.

    This checks **you** and confirms you are using the password intended for
    the dataset; preventing data loss on a missing key/password.

``` bash
# Create encrypted dataset on ZFS pool using 1 million pbkdf2 iterations.
zfs create -o encryption=aes-256-gcm -o keyformat=passphrase -o keylocation=prompt -o pbkdf2iters=1000000 -o mountpoint=/d/media {POOL}/media
```


## Mount Encrypted Dataset
!!! tip
    Set mountpoint to immutable without the ZFS dataset mounted. This prevents
    writes when the dataset is not ready: **chattr +i {MOUNTPOINT}**

``` bash
zfs mount -l {POOL}/{DATASET}
zfs mount -l -a
```

Once a key is loaded unmounting and remounting will not require re-entry of
the password or file.


## Unload Encryption KEy
``` bash
# Use after unmounting to remove the key from memory.
zfs unload-key {POOL}/{DATASET}
```


## Preload Dataset Encryption Key
``` bash
zfs load-key {POOL/DATASET}  # Preload one key.
zfs load-key -a  # Preload all keys.
```


## [Change Encryption Keys/Method][c]
!!! danger
    Always **confirm** key works before loading data. Do not overwrite or
    delete the old key until the new key is in place.

    This means: unmount, unload encryption key, and remount before proceeding.

    This checks **you** and confirms you are using the password intended for
    the dataset; preventing data loss on a missing key/password.

Change password, keyfile, or swap between the two methods. This does **not**
change the user-inaccessible master key (to do that you must create a new
dataset).

Always use full path for key. Ideally store on removable USB key for booting
where the mounted path will always be known. Otherwise store on encrypted boot
drive. Use a password if key would be stored on an unencrypted disk.

``` bash
# Change password for dataset.
zfs change-key -l -o keyformat=passphrase -o keylocation=prompt -o pbkdf2iters=1000000 {POOL}/{DATASET}

# Use keyfile for encryption key.
dd if=/dev/urandom of=/root/zfs.key bs=1 count=32
zfs change-key -l -o keyformat=raw -o keylocation=file:///root/zfs.key {POOL}/{DATASET}
```


## Reference[^1][^2]

[^1]: https://arstechnica.com/gadgets/2021/06/a-quick-start-guide-to-openzfs-native-encryption
[^2]: https://blog.heckel.io/2017/01/08/zfs-encryption-openzfs-zfs-on-linux

[a]: https://wiki.archlinux.org/title/ZFS#Native_encryption
[b]: https://old.reddit.com/r/zfs/comments/bnvdco/zol_080_encryption_dont_encrypt_the_pool_root
[c]: http://manpages.ubuntu.com/manpages/impish/man8/zfs-change-key.8.html
