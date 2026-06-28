# Troubleshooting

!!! danger "Never use pool until root issue is resolved and understood"
    Look at the failure. If spread across all devices it likely represents a
    **common** failure across the system and not a disk itself. Memory,
    controller cards, power are all suspect here.

    Individual disk failures will be evident.

## ZFS-9000-8A One or more devices has experienced an error
ZFS has detected data corruption in the pool.

!!! danger ""
    status: One or more devices has experienced an error resulting in data
    	corruption.  Applications may be affected.
    action: Restore the file in question if possible.  Otherwise restore the
    	entire pool from backup.
       see: https://openzfs.github.io/openzfs-docs/msg/ZFS-8000-8A

### Check SMART status
``` bash
# Always run smartctl to verify disk health of pool. Look at the attributes and
# determine if anything is close to, or over, thresholds. Also compare to
# similar disks in the pool.
lsblk
smartctl -a /dev/{DEVICE}
> ...
> === START OF READ SMART DATA SECTION ===
> SMART overall-health self-assessment test result: PASSED
> ...
> SMART Error Log Version: 1
> No Errors Logged
```

### Run [Memtest86][a]
Run memtest from USB disk and stress test memory. Errors should be immediately
apparent (either freezing or reported errors). Complete at least one full test
cycle in the conditions that created the error.

### Run [mprime][b]
Run mprime from [StresKit][c] USB disk. mprime is headless prime95. Tests will
explicitly say completed and should not freeze.

### Rollback updates
Updates containing microcode updates, AGESA changes, etc. may cause issues.
Rollback updates and re-test to confirm they do not cause issues.

[Run through Crash troubleshootin](../../os/windows/crashes.md).

### [Resolve ZFS error][d]

#### Determine what files are affected
Either delete or restore these files from backup or previous snapshots.

!!! tip "Encrypted pools must be mounted for files to be shown"

``` bash
zpool status
>   pool: tank
>  state: ONLINE
> status: One or more devices has experienced an error resulting in data
> 	corruption.  Applications may be affected.
> action: Restore the file in question if possible.  Otherwise restore the
> 	entire pool from backup.
>    see: https://openzfs.github.io/openzfs-docs/msg/ZFS-8000-8A
> ...
> errors: 2 data errors, use '-v' for a list

# Encrypted pools require unlocking.
$ zpool status -v
> ...
> errors: List of errors unavailable: permission denied

zfs mount -a -l

zpool status -v
> ...
> errors: Permanent errors have been detected in the following files:
>
>         /hundo/some_file

rm /hundo/some_file
```

See [syncing datasets](sync_backup.md#syncing-datasets) to restore dataset to a
previous snapshot.

### Re-scrub ZFS pool.

!!! danger "Never use pool until root issue is resolved and understood"

``` bash
# Run the scrub and verify no additional errors are found.
zpool clear hundo
zpool scrub hundo

# If clean and root issued resolve, remount the pool.
zfs mount -a -l
```

## Cannot destroy snapshots
Snapshot user does not have **mount,destroy** permissions on the dataset to
manage snapshots.

!!! danger ""
    cannot destroy snapshots: permission denied

``` bash
# Check current permissions for a dataset.
zfs allow tank/example

# Add mount,destroy permissions
zfs allow -d zfs_snapshot mount,destroy tank/example
```

[a]: https://www.memtest86.com
[b]: https://www.mersenne.org/download
[c]: https://github.com/valleyofdoom/StresKit
[d]: https://openzfs.github.io/openzfs-docs/msg/ZFS-8000-8A