# Copying Data

## Copy data with verification
``` bash
apt install md5deep rsync

# -a archive (-rlptgoD).
# -v verbose.
# -x don't cross FS boundaries.
# -h human readable.
# -H preserve hard links.
# -A preserve ACL's.
# -X preserve extended attributes.
rsync -avxhHAX {DIR} /Y
```

## Create Hashfile of All Original Files and Sort
``` bash
# -l use relative file paths.
# -r recursive.
# -e display progress indicator (not written to hashfile).
md5deep -l -r -e {DIR} | sort > /tmp/{DIR}.md5
```

## Verify copied files with rsync
``` bash
# Use MD5 sums to detect file differences.
md5deep -l -r -e {DIR} | sort > /tmp/{DIR}2.md5
md5sum /tmp/{DIR}.md5 /tmp/{DIR}2.md5
diff /tmp/{DIR}.md5 /tmp/{DIR}2.md5
```

## Verifying Copied Files Across OS’s are Accurate
``` bash
# This removes path differences and only compares source hashes to destination
# hashes. Only non-matching lines (e.g. those hashes that don’t match) should
# be printed.
cut -f 1 -d ‘ ‘ {SOURCE}.md5 > {SOURCE}-hash-only.md5
grep -v -f {SOURCE}-hash-only.md5 {TARGET}.md5
```

## Reference

* http://md5deep.sourceforge.net/start-md5deep.html#basic
* https://stackoverflow.com/questions/606739/comparison-between-two-big-directories
* https://superuser.com/questions/307541/copy-entire-file-system-hierarchy-from-one-drive-to-another
* https://www.evbackup.com/support/rsync-arguments
