.. _wiping-data:

Wiping Data
###########
Securely delete data.

shred
*****
Tool to overwrite single file contents and optionall delete file.

.. code-block:: bash
  :caption: 35 pass random data, zero then remove file.

  shred --iterations=35 --verbose --zero --remove {FILE}

.. code-block:: bash
  :caption: Recursively overwrite file data.

  find . -type f -exec shred --iterations=35 --verbose --zero --remove {} \;

wipe
****
Tool to securely delete files and block devices.

.. code-block:: bash

  apt install wipe

.. code-block:: bash
  :caption: Recursively delete files, 35 pass random data.

  wipe -r -c -f -Q 35 {FILE OR DIR}

.. code-block:: bash
  :caption: Wipe a block device, 35 pass random data.

  wipe -k -Q 35 {BLOCK DEVICE}

dd
**
Using dd to zero disks. Good for testing/setup of new drives.

.. code-block:: bash
  :caption: Writing all Zero’s to Drive (quick).

  dd if=/dev/zero of=/dev/sdX bs=1M &

.. note::
  ~3-4 hours @ 1.5TB

.. code-block:: bash
  :caption: Writing all One’s to Drive (quick).

  tr '\000' '\377' < /dev/zero | dd of=/dev/sdX bs=1M &

.. note::
  ~4-5hours @ 1.5TB

.. code-block:: bash
  :caption: Checking Status on DD.

  ps -ef | grep dd
  kill -USR1 {PID}

DBAN
****
Download `DBAN boot & nuke`_ then run *DoD 3 pass*.

.. rubric:: References

#. `Basics on wiping a drive in linux <http://how-to.wikia.com/wiki/How_to_wipe_a_hard_drive_clean_in_Linux>`_
#. `Wiping a drive with ones <http://www.commandlinefu.com/commands/view/6483/fill-a-hard-drive-with-ones-like-zero-fill-but-the-opposite->`_
#. `What really needs to be done to destroy HD data <http://www.vidarholen.net/~vidar/overwriting_hard_drive_data.pdf>`_

.. _DBAN boot & nuke: http://sourceforge.net/projects/dban/
