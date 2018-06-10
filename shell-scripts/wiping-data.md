Wiping Data
-----------
Securely delete data.

1. [shred](#shred)
1. [wipe](#wipe)
1. [dd](#dd)
1. [DBAN](#dban)
1. [References](#references)

shred
-----
Tool to overwrite single file contents and optionall delete file.

### 35 pass random data, zero then remove file
```bash
shred --iterations=35 --verbose --zero --remove <FILE>
```

### Recursively overwrite file data.
```bash
find . -type f -exec shred --iterations=35 --verbose --zero --remove {} \;
```

wipe
----
Tool to securely delete files and block devices.

```bash
apt install wipe
```

### Recursively delete files, 35 pass random data.
```bash
wipe -r -c -f -Q 35 <FILE_OR_DIR>
```

### Wipe a block device, 35 pass random data.
```bash
wipe -k -Q 35 <BLOCK_DEVICE>
```

dd
--
Using dd to zero disks. Good for testing/setup of new drives.

### Writing all Zero’s to Drive (quick)
```bash
dd if=/dev/zero of=/dev/sdX bs=1M &
```
 * ~3-4 hours @ 1.5TB

### Writing all One’s to Drive (quick)
```bash
tr '\000' '\377' < /dev/zero | dd of=/dev/sdX bs=1M &
```
 * ~4-5hours @ 1.5TB

### Checking Status on DD
```bash
ps -ef | grep dd
kill -USR1 <pid>
```

DBAN
----
Download [DBAN boot & nuke][3]

Run DoD 3 pass

References
----------
[Basics on wiping a drive in linux][1]

[Wiping a drive with ones][2]

[DBAN - Boot and Nuke live CD][3]

[What really needs to be done to destroy HD data][4]

[1]: http://how-to.wikia.com/wiki/How_to_wipe_a_hard_drive_clean_in_Linux
[2]: http://www.commandlinefu.com/commands/view/6483/fill-a-hard-drive-with-ones-like-zero-fill-but-the-opposite-
[3]: http://sourceforge.net/projects/dban/
[4]: http://www.vidarholen.net/~vidar/overwriting_hard_drive_data.pdf

