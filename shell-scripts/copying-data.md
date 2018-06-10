Copying Data
------------
Securely delete data.

### Install md5deep and Archive Copy Data
```bash
sudo aptitude install md5deep rsync
cd /X/
sudo rsync -avxhHAX <DIRECTORY> /Y
```
 * -a archive (-rlptgoD)
 * -v verbose
 * -x don't cross FS boundaries
 * -h human readable
 * -H preserve hard links
 * -A preserve ACL's
 * -X preserve extended attributes

### Creating a Hashfile of All Original Files and Sort
```bash
cd /X/
sudo md5deep -l -r -e <DIRECTORY> | sort > /tmp/<DIRECTORY>.md5
```
 * -l use relative file paths
 * -r recursive
 * -e display progress indicator (not written to hashfile)

### Verifying Copied Files
Rsync verifies copied files, this is a manual verification.

```bash
cd /Y/
sudo md5deep -l -r -e <DIRECTORY> | sort > /tmp/<DIRECTORY>2.md5
md5sum /tmp/<DIRECTORY>.md5 /tmp/<DIRECTORY>2.md5
diff /tmp/<DIRECTORY>.md5 /tmp/<DIRECTORY>2.md5
```
 * This basically verifies that both hashfiles are the same (and therefore all
   files are the same)
 * md5sum will tell you if there is a difference in the hashfiles
 * diff will list the files that are actually changed

### Verifying Copied Files Across OS’s are Accurate
This removes path differences, and only compares source hashes to destination
hashes.

```bash
cut -f 1 -d ‘ ‘ <source>.md5 > <source>-hash-only.md5
grep -v -f <source>-hash-only.md5 <target>.md5
```
 * Only non-matching lines (e.g. those hashes that don’t match) should be
   printed

References
----------
[md5deep usage tricks][1]

[md5deep validating moved files between directories][2]

[Using rsync to backup hard drives][3]

[rsync common commands][4]

[1]: http://md5deep.sourceforge.net/start-md5deep.html#basic
[2]: http://stackoverflow.com/questions/606739/comparison-between-two-big-directories
[3]: http://superuser.com/questions/307541/copy-entire-file-system-hierarchy-from-one-drive-to-another
[4]: http://www.evbackup.com/support-commonly-used-rsync-arguments/