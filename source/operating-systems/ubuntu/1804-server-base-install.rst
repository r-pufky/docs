.. _1804-server-base-install:

Ubuntu 18.04 Server Base Install
################################
Ubuntu 18.04 server base configuration notes.

Base Install
************

* Hostname: {HOSTNAME}
* Full Name: {FULLNAME}
* Username: {USERNAME}
* Password: {PASSWORD}
* No encrypted home directory
* Partitioning: Guided, Full disk, no encryption
* Set default encryption passphrase: template
* Size: max
* Automatic security updates
* Packages: Standard system utilities


.. code-block:: bash
  :caption: Change to faster default apt repositories & install base packages.

  sed -i 's/us\.archive\.ubuntu\.com/mirrors\.mit\.edu/g' /etc/apt/sources.list
  apt update && apt upgrade
  apt install python-software-properties inotify-tools curl unattended-upgrades sysstat htop tmux ssh ffpmeg

.. code-block:: bash
  :caption: Disable software RAID 5 detection on boot by default.

  grep -qxF 'ARRAY <ignore> devices=/dev/null' /etc/mdadm/mdadm.conf || echo 'ARRAY <ignore> devices=/dev/null' >> /etc/mdadm/mdadm.conf

.. code-block:: bash
  :caption: Secure existing home directories & setup ssh/bin sub directories.

  find /home/ -maxdepth 1 -type d ! -path /home/ -exec mkdir {}/.ssh {}/bin && chmod 0700 {}/.ssh {}/bin \;
  mkdir /root.ssh /root/bin && chmod 0700 /root/.ssh /root/bin
  find /home -name '.profile' -exec rm -v {} \;
  rm /root/.profile
  chmod go-rwx -Rv /home/* /root

.. _secure-ssh-connections:

Secure SSH connections
======================
.. caution::
  Longstanding SSH options have been removed in 18.04 and your `SSH config will
  not carry over unchanged`_.

Basic changes here will lock down SSH connections to require public key
authentication, remove root user SSH logins, and disable password auth.

.. literalinclude:: source/sshd_config
  :caption: **0644 root root** /etc/ssh/sshd_config
  :linenos:
  :emphasize-lines: 12,15,22

.. code-block:: bash
  :caption: Restart SSH service.

  systemctl restart ssh

.. note::
  See :ref:`ubuntu-creating-ssh-certificates` for user certificate generation.

`Install TCP BBR Kernel Patches`_
=================================
TCP BBR is a new congestion controlling algorithm that is designed to respond to
actual congestion instead of packet loss. This results in a dramatic increase in
transfer speeds. This applies to *any* Linux distrubtion running Kernel **4.9+**
with BBR patches.

Ensure ``CONFIG_TCP_CONG_BBR`` and ``CONFIG_NET_SCH_FQ`` parameters are
supported in the Kernel and that the kernel version is **4.9+**.

.. code-block:: bash

  uname -r
  egrep 'CONFIG_TCP_CONG_BBR|CONFIG_NET_SCH_FQ' /boot/config-$(uname -r)

* Both parameters should be returned.
* Uname should return a kernel version **4.9** or higher.

Enable BBR Support:

.. code-block:: bash
  :caption: **0640 root root** ``/etc/sysctl.d/10-custom-kernel-bbr.conf``

  net.core.default_qdisc=fq
  net.ipv4.tcp_congestion_control=bbr

Reboot the system to apply changes.

.. note::
  Before and after performance may tested using ``iperf``

  On BBR Server: ``iperf -s``.

  On Client: ``iperf -c {SERVER} -i 2 -t 30``.

`Setup Automatic Updates & Upgrades`_
=====================================

.. literalinclude:: source/50unattended-upgrades
  :caption: **0644 root root** /etc/apt/apt.conf.d/50unattended-upgrades
  :emphasize-lines: 2-5,8,12,16-20

.. literalinclude:: source/10periodic
  :caption: **0644 root root** /etc/apt/apt.conf.d/10periodic

.. code-block:: bash
  :caption: Restart unattended upgrades.

  systemctl restart unattended-upgrades

Remove Extraneous MOTD's
========================
Default login messages do not add value to login. `Disable ubuntu login
messages`_.

.. code-block:: bash
  :caption: Disable MOTD's that do not add value on login.

  chmod a-x /etc/update-motd.d/10-help-text
  chmod a-x /etc/update-motd.d/50-landscape-info
  chmod a-x /etc/update-motd.d/50-motd-news
  chmod a-x /etc/update-motd.d/50-landscape-sysinfo
  chmod a-x /etc/update-motd.d/80-livepatch

Add MOTD to warn if the system has been up for a long period of time:

.. literalinclude:: source/98-reboot-required
  :caption: **0755 root root** /etc/update-motd.d/98-reboot-required
  :emphasize-lines: 2

Setup Skeleton User Profile
===========================
Copy the following configuration files to system, these are preconfigured
preferences.

.. code-block:: bash
  :caption: Setup ``/etc/skel`` directory and copy files.

  rm /etc/skel/.profile
  mkdir /etc/skel/.ssh /etc/skel/bin
  chmod 0700 /etc/skel/.ssh /etc/skel/bin
  chmod -Rv go-rwx /etc/skel/

.. note::
  Pre-configured user skeleton files are here:

   * :download:`.bashrc <source/.bashrc>`
   * :download:`.bash_profile <source/.bash_profile>`
   * :download:`.bash_logout <source/.bash_logout>`
   * :download:`.vimrc <source/.vimrc>`
   * :download:`.tmux.conf <source/.tmux.conf>`

  These will need to be manually added to pre-existing accounts (e.g. ``root``
  and the *initial user*).

`Update UFW Rules`_
===================
Uncomplicated FireWall is setup by default in 18.04. Consideration should be
made on whether to keep this or disable this.

.. code-block:: bash
  :caption: Allow a well-known service.

  ufw allow ssh

.. code-block:: bash
  :caption: Get current status.

  ufw status
  ufw status verbose

.. code-block:: bash
  :caption: Disable UFW.

  ufw disable

`Adding Custom Fonts`_
**********************
Fonts must be imported for use in applications, such as sublime text.

.. code-block:: bash
  :caption: Install font management tools.

  apt install fontconfig


.. code-block:: bash
  :caption: Copy fonts to ``/usr/local/share/fonts/``, set appropriate
            permissions, and refresh the font cache.

  find /usr/local/share/fonts -type f -exec chown root:staff {} \;
  find /usr/local/share/fonts -type d -exec chmod o+rx {} \;
  fc-cache -f -v
  fc-list

Creating an Encrypted Volume
****************************
The options specified here are the default encryption settings for ubuntu during
installation and not the most secure encryption. See
:ref:`1804-server-base-install-references`.

.. code-block:: bash
  :caption: Find the new block device and setup encryption.

  lsblk
  cryptsetup luksFormat --hash=sha256 --key-size=512 --cipher=aes-xts-plain64 --verify-passphrase /dev/{BLOCK DEVICE}

.. code-block:: bash
  :caption: Create the LVM physical volume, volume group and logical volume.

  cryptsetup luksOpen /dev/{BLOCK DEVICE} {BLOCK DEVICE}_crypt
  pvcreate /dev/mapper/{BLOCK DEVICE}_crypt
  vgcreate data_vol_group /dev/mapper/{BLOCK DEVICE}_crypt
  lvcreate -n encrypted_data -l +100%FREE data_vol_group

.. code-block:: bash
  :caption: Format and mount the encrypted volume to ``/data``.

  mkfs.ext4 -m 0 /dev/data_vol_group/encrypted_data
  mkdir /data
  mount /dev/data_vol_group/encrypted_data /data

.. code-block:: bash
  :caption: Find the *ROOT* device UUID (``/dev/{BLOCK DEVICE}``).

  blkid

Add device to ``crypttab`` and ``fstab``. System **will** require a password to
boot:

.. code-block:: bash
  :caption: **0644 root root** ``/etc/crypttab``

  xvdb_crypt UUID=<UUID from xvdb> none luks,discard

.. note::
  Even though there are `security issues related with using discard for SSD's`_,
  it is preferred for lifespan and performance.

.. code-block:: bash
  :caption: **0644 root root** ``/etc/fstab``

  /dev/mapper/data-data /data ext4 defaults 0 2

.. _1804-server-base-install-references:

.. rubric:: References

#. `Manually changing a password on a dmcrypt / LUKS volume <https://unix.stackexchange.com/questions/185390/list-open-dm-crypt-luks-volumes>`_
#. `Reseting a password on an encrypted FS <https://unix.stackexchange.com/questions/126180/how-to-reset-password-on-an-encrypted-fs>`_
#. `Howto change LUKS passphrase <https://askubuntu.com/questions/95137/how-to-change-luks-passphrase>`_
#. `Full encryption with LVM and LUKS <https://www.linux.com/tutorials/how-full-encrypt-your-linux-system-lvm-luks>`_
#. `Mounting LVM partitions <http://ask.xmodulo.com/mount-lvm-partition-linux.html>`_
#. `Mounting LVM logical volumes <https://blog.sleeplessbeastie.eu/2015/11/16/how-to-mount-encrypted-lvm-logical-volume/>`_
#. `Mounting encrypted LUKS drive at boot <https://askubuntu.com/questions/450895/mount-luks-encrypted-hard-drive-at-boot>`_

.. _security issues related with using discard for SSD's: http://asalor.blogspot.com/2011/08/trim-dm-crypt-problems.html
.. _Update UFW Rules: https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu-18-04
.. _Adding Custom Fonts: https://askubuntu.com/questions/3697/how-do-i-install-fonts
.. _Setup Automatic Updates & Upgrades: https://help.ubuntu.com/community/AutomaticSecurityUpdates
.. _Disable ubuntu login messages: https://www.cyberciti.biz/faq/how-to-disable-ssh-motd-welcome-message-on-ubuntu-linux/
.. _SSH config will not carry over unchanged: https://www.openssh.com/releasenotes.html
.. _Install TCP BBR Kernel Patches: https://cloud.google.com/blog/products/gcp/tcp-bbr-congestion-control-comes-to-gcp-your-internet-just-got-faster