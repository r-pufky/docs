.. _preseed-create-installation-file:

Create Preseed Installation File
################################
This provides answers for the debconf installer during installation. Providing
these answers enables the installation to complete without interaction. Most of
the options here are required for automated installation.

Reading the `the preseed manual`_ is recommended. See the complete example
file here: :download:`ubuntu-template.seed <../source/ubuntu-template.seed>`.

.. code-block:: bash
  :caption: To get avaliable parameters for a section:

  debconf-get-selections | grep <option>

.. literalinclude:: ../source/ubuntu-template.seed
  :caption: Localization Section.
  :lineno-start: 1
  :lines: 1-2

.. note::
  Set the installer's locale.

.. literalinclude:: ../source/ubuntu-template.seed
  :caption: Keyboard Section.
  :lineno-start: 4
  :lines: 4-7

.. note::
  Set keyboard to US and remove detection prompt.

.. literalinclude:: ../source/ubuntu-template.seed
  :caption: Network Section.
  :lineno-start: 9
  :lines: 9-20

.. note::
  Grab the first active network connection, quick fail DHCPv6 and wait 10
  seconds for a link. Hostname is automatically set via DHCP, so just set a
  template hostname for initial installation. Disable WEP dialog.

.. literalinclude:: ../source/ubuntu-template.seed
  :caption: Firmware Section.
  :lineno-start: 22
  :lines: 22-23

.. note::
  Enable installation of close-sourced firmware updates for hardware.

.. literalinclude:: ../source/ubuntu-template.seed
  :caption: Apt Mirror Section.
  :lineno-start: 25
  :lines: 25-30

.. note::
  This is for the main OS installation, *NOT* package installation. Set a custom
  ubuntu mirror, and enable all for components.

.. literalinclude:: ../source/ubuntu-template.seed
  :caption: Accounts Section.
  :lineno-start: 32
  :lines: 32-42

.. code-block:: bash
  :caption: Creating {PRE HASHED PASSWORD}.

  mkpasswd -m sha-512

.. note::
  Disables root login, creating an initial {USER}, with a sha512 password
  hash. Give {USER} sudo and ssh access, and `default groups to function`_.

  The password used should be an **installation password** and not a real one.

.. literalinclude:: ../source/ubuntu-template.seed
  :caption: Clock & Time Section.
  :lineno-start: 44
  :lines: 44-47

.. note::
  Read hardware clock as non-UTC, set timezone and enable NTP.

.. literalinclude:: ../source/ubuntu-template.seed
  :caption: Partition Section.
  :lineno-start: 49
  :lines: 49-75

.. note::
  Automatically delete and remove LVM and RAID partitions. Umount any partitions
  that may have autmounted to ``/media``. Create a `single partition`_ with no
  swap, EXT4, on block device ``/dev/{BLOCK DEVICE}``.

.. important::
  This can fail because there was no pre-existing partitions to umount. You can
  *ignore* this message or remove the umount command if you are sure you will
  not run into systems requiring to unmount ``/media``.

  See `fix unmount problem in preseed`_ and `disks have mounted partitions`_
  which explains why these cause automated partitioning to fail.

.. literalinclude:: ../source/ubuntu-template.seed
  :caption: Kernel Section.
  :lineno-start: 77
  :lines: 77-78

.. note::
  Install the generic kernel. Use ``linux-server`` for server kernel.

.. literalinclude:: ../source/ubuntu-template.seed
  :caption: Apt Setup Section.
  :lineno-start: 80
  :lines: 80-84

.. note::
  Set system to use all four standard repos.

.. literalinclude:: ../source/ubuntu-template.seed
  :caption: Package Selection Section.
  :lineno-start: 80
  :lines: 86-97

.. note::
  Install the server and openssh-server tasks as well as other ubuntu packages.
  Upgrade all packages to latest version -- `this is currently broken in
  ubuntu`_ and needs to be `done manually in late_command`_.

.. tip::
  Tasksel installs meta-packages for common setups.

  .. code-block:: bash
    :caption: List all avaliable tasks.

    tasksel --list-task

  These can be used in the ``tasksel/first`` line.

  The packages installed in these meta packages can be found with:

  .. code-block:: bash

    tasksel --task-packages {PACKAGE}
    apt --dry-run install {TASK}

  * The task includes ``^``, e.g. ``server^``.
  * From ubuntu 16.04, ``--task-packages`` returns the meta-package name, not
    the list of packages. Other versions you can just use ``--task-packages``.
  * See task packages from the `germinate output`_ templates here.

.. literalinclude:: ../source/ubuntu-template.seed
  :caption: Console Setup Section.
  :lineno-start: 99
  :lines: 99-102

.. note::
  Disable the GUI boot login prompt, use console. Enable verbose logging on
  boot.

.. tip::
  Everything works fine, but `black screen on boot`_? You need to setup a proper
  GUI login (e.g. probably need to install ``desktop`` task) or enable the
  console.

  You can still ``ctrl-alt-F1`` to get to the console from the blank screen.

.. literalinclude:: ../source/ubuntu-template.seed
  :caption: Boot Loader Installation Section.
  :lineno-start: 104
  :lines: 104-109

.. note::
  Install grub to MBR with this OS as default. Detect other OS's and add if
  needed. Default boot this OS in 2 seconds.

.. literalinclude:: ../source/ubuntu-template.seed
  :caption: Finish Installation Section.
  :lineno-start: 111
  :lines: 111-113

.. note::
  Eject the CD before booting, don't prompt for reboot.

.. literalinclude:: ../source/ubuntu-template.seed
  :caption: Post Installation Section.
  :lineno-start: 115
  :lines: 115-122

.. note::
  Copy post-install directory from ISO to installed OS's /tmp, and execute
  post-install script.

  Commands *must* be `done manually in late_command`_ with ``in-target``
  command to target the OS install, otherwise your scripts will fail. Using
  ``in-target`` behaves as a chroot to that system, meaning
  *copy over your files to that system to find them*.

  You can `pull your scripts and files using curl or wget`_.

.. rubric:: References

#. `Contents of the Preseed file <https://help.ubuntu.com/16.04/installation-guide/amd64/apbs04.html>`_
#. `Example preseed file <https://help.ubuntu.com/16.04/installation-guide/example-preseed.txt>`_
#. `Preseed config <https://github.com/dsgnr/Ubuntu-16.04-Unattended-Install/blob/master/preseed.cfg>`_
#. `Post install <https://github.com/dsgnr/Ubuntu-16.04-Unattended-Install/blob/master/post-install.sh>`_
#. `UEFI pressed install <https://github.com/dsgnr/Ubuntu-16.04-Unattended-Install/blob/master/README.md>`_

.. _the preseed manual: https://help.ubuntu.com/16.04/installation-guide/amd64/apb.html
.. _default groups to function: https://wiki.ubuntu.com/Security/Privileges#Use_CD-ROM_drives
.. _single partition: https://superuser.com/questions/458672/ubuntu-preseed-use-whole-disk-space-but-no-swap
.. _fix unmount problem in preseed: https://ubuntuforums.org/showthread.php?t=2215103
.. _disks have mounted partitions: https://bugs.launchpad.net/ubuntu/+source/debian-installer/+bug/1347726
.. _this is currently broken in ubuntu: https://github.com/tylert/packer-build/issues/7
.. _done manually in late_command: https://www.linuxquestions.org/questions/programming-9/how-to-use-late_command-in-preseed-file-852603/
.. _pull your scripts and files using curl or wget: https://askubuntu.com/questions/557933/copy-package-to-a-specific-directory-with-customized-iso
.. _germinate output:  https://people.canonical.com/~ubuntu-archive/germinate-output/ubuntu.xenial/
.. _black screen on boot: https://askubuntu.com/questions/837007/ubuntu-server-16-04-1-lts-installed-with-preseed-file-taking-to-black-screen