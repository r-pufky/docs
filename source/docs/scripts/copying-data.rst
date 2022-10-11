.. _copying-data:

Copying Data
############
Copy data with verification.

.. code-block:: bash
  :caption: Install Utilities.

  apt install md5deep rsync

.. code-block:: bash
  :caption: Archive Copying Data.

  cd /X/
  rsync -avxhHAX {DIRECTORY} /Y

.. note::
  * ``-a`` archive (-rlptgoD).
  * ``-v`` verbose.
  * ``-x`` don't cross FS boundaries.
  * ``-h`` human readable.
  * ``-H`` preserve hard links.
  * ``-A`` preserve ACL's.
  * ``-X`` preserve extended attributes.

.. code-block:: bash
  :caption: Create Hashfile of All Original Files and Sort.

  cd /X/
  md5deep -l -r -e {DIRECTORY} | sort > /tmp/{DIRECTORY}.md5

.. note::
  * ``-l`` use relative file paths.
  * ``-r`` recursive.
  * ``-e`` display progress indicator (not written to hashfile).

.. code-block:: bash
  :caption: Verify copied files with rsync.

  cd /Y/
  md5deep -l -r -e {DIRECTORY} | sort > /tmp/{DIRECTORY}2.md5
  md5sum /tmp/{DIRECTORY}.md5 /tmp/{DIRECTORY}2.md5
  diff /tmp/{DIRECTORY}.md5 /tmp/{DIRECTORY}2.md5

.. note::
  * This basically verifies that both hashfiles are the same (and therefore
    all files are the same).
  * md5sum will tell you if there is a difference in the hashfiles.
  * diff will list the files that are actually changed.

.. code-block:: bash
  :caption: Verifying Copied Files Across OS’s are Accurate.

  cut -f 1 -d ‘ ‘ {SOURCE}.md5 > {SOURCE}-hash-only.md5
  grep -v -f {SOURCE}-hash-only.md5 {TARGET}.md5

.. note::
  This removes path differences, and only compares source hashes to destination
  hashes. Only non-matching lines (e.g. those hashes that don’t match) should be
  printed.

.. rubric:: References

#. `md5deep usage tricks <http://md5deep.sourceforge.net/start-md5deep.html#basic>`_
#. `md5deep validating moved files between directories <https://stackoverflow.com/questions/606739/comparison-between-two-big-directories>`_
#. `Using rsync to backup hard drives <https://superuser.com/questions/307541/copy-entire-file-system-hierarchy-from-one-drive-to-another>`_
#. `rsync common commands <https://www.evbackup.com/support/rsync-arguments>`_
