# Wiping Data
Securely delete data.


## shred
Tool to overwrite single file contents and optionally delete files.

``` bash
# 35 pass random data, zero then remove file.
shred --iterations=35 --verbose --zero --remove {FILE}

# Recursively overwrite file data.
find . -type f -exec shred --iterations=35 --verbose --zero --remove {} \;
```


## wipe
Tool to securely delete files and block devices.

``` bash
apt install wipe

# Recursively delete files, 35 pass random data.
wipe -r -c -f -Q 35 {FILE OR DIR}

# Wipe a block device, 35 pass random data.
wipe -k -Q 35 {BLOCK DEVICE}
```


## dd
Using dd to zero disks. Good for testing/setup of new drives.

``` bash
# Writing all Zero’s to Drive.
dd if=/dev/zero of=/dev/sdX bs=1M &

# Writing all One’s to Drive.
tr '\000' '\377' < /dev/zero | dd of=/dev/sdX bs=1M &

# Checking Status on DD.
ps -ef | grep dd
kill -USR1 {PID}
```


## DBAN Boot & Nuke
Live ISO image specifically for data destruction.

[Download][a] and run *DoD 3 pass*.


## Reference[^1][^2][^3]

[^1]: https://how-to.fandom.com/wiki/How_to_wipe_a_hard_drive_clean_in_Linux
[^2]: https://www.commandlinefu.com/commands/view/6483/fill-a-hard-drive-with-ones-like-zero-fill-but-the-opposite-
[^3]: https://www.vidarholen.net/~vidar/overwriting_hard_drive_data.pdf

[a]: https://sourceforge.net/projects/dban