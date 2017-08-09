Xen Server Template
-------------------
Ubuntu 16.04 base Xen template.

1. [Base Install](#base-install)
2. [Manual Crypt/LUKS commands](#manual-cryptluks-commands)
3. [Enabling Secure SSH Config](#enabling-secure-ssh-config)
4. [Modifying a VM Template](#modifying-a-vm-template)
5. [Manually Creating New VM from Template](#manually-creating-new-vm-from-template)
6. [Creating an Encrypted Volume](#creating-an-encrypted-volume)
7. [References](#references)


Base Install
------------
* Template: ubuntu 16.04
* 10GB default disk
* All ethernet devices
* Hostname: ubuntu
* Full Name: None
* Username: template
* Password: template
* No encrypted home directory
* Partitioning: Guided, Full with Encrypted LVM
* Set default encryption passphrase: template
* Size: max
* Automatic security updates
* Packages: Standard system utilities

### Change apt repository
sudo vim /etc/apt/sources.list
```vim
%s/us\.archive\.ubuntu\.com/ubuntu\.media\.mit\.edu/g
```

### Install base packages
```bash
sudo apt update && sudo apt upgrade
sudo apt install python-software-properties inotify-tools curl unattended-upgrades sysstat  nmon screen ssh
```

### Set base sshd_config
* Copy the 'secure' sshd config to the machine. This just enforces cert-based auth only. [LINK.](https://raw.githubusercontent.com/r-pufky/docs/master/xen/etc/ssh/sshd_config.secure).
```bash
sudo mv /etc/ssh/sshd_config /etc/ssh/sshd_config.insecure
sudo ln -s /etc/ssh/sshd_config.insecure /etc/ssh/sshd_config
sudo chown root:root /etc/ssh/sshd_config*
```

### Install XenServer tools
* Mount guest-tools.iso on VM in XenCenter
* Install the package
```bash
sudo mount /dev/dvd /mnt
sudo /mnt/Linux/install.sh
```

### Configure Unattended Upgrades
sudo vim /etc/apt/apt.conf.d/50unattended-upgrades
```vim
Unattended-Upgrade::Allowed-Origins {
  "${distro_id}:${distro_codename}";
  "${distro_id}:${distro_codename}-security";
  "${distro_id}ESM:${distro_codename}";
  "${distro_id}:${distro_codename}-updates";
};

Unattended-Upgrade::Mail "root";
Unattended-Upgrade::Remove-Unused-Dependencies "true";
Unattended-Upgrade::Automatic-Rebot "true";
Unattended-Upgrade::Automatic-Reboot-Time "05:00";
```

sudo vim /etc/apt/apt.conf.d/10periodic
```vim
APT::Periodic::Update-Package-Lists "1";
APT::Periodic::Download-Upgradeable-Packages "1";
APT::Periodic::AutocleanInterval "7";
APT::Periodic::Unattended-Upgrade "1";
```

```bash
sudo service unattended-upgrades restart
```

### Setup Message of the Day
* Disable documentation listing
```bash
sudo chmod a-x /etc/update-motd.d/10-help-text
```

* Add uptime reboot warning message. [LINK.](https://raw.githubusercontent.com/r-pufky/docs/master/xen/etc/update-motd.d/98-reboot-required)

sudo vim /etc/update-motd.d/98-reboot-required
```vim
#!/bin/bash
DAYS_BEFORE_PROMPT=21
uptime=$(</proc/uptime)
uptime=${uptime%%.*}
days=$(( uptime/60/60/24 ))

if [ ${days} -gt ${DAYS_BEFORE_PROMPT} ]; then
  echo "System up for ${days} days. Perhaps a manual update, upgrade & reboot is in order?"
fi

fi [ -x /usr/lib/update-notifier/update-motd-reboot-required ]; then
  exec /usr/lib/update-notifier/update-motd-reboot-required
fi
```

### Setup skeleton user profile
* Copy the following configuration files to system, these are
  preconfigured preferences.

| File                    | Perm | Link                                                                                     |
|-------------------------|------|------------------------------------------------------------------------------------------|
| .bashrc                 | 0600 | [LINK](https://raw.githubusercontent.com/r-pufky/docs/master/xen/etc/skel/.bashrc)       |
| .bash_profile           | 0600 | [LINK](https://raw.githubusercontent.com/r-pufky/docs/master/xen/etc/skel/.bash_profile) |
| .bash_logout            | 0600 | [LINK](https://raw.githubusercontent.com/r-pufky/docs/master/xen/etc/skel/.bash_logout)  |
| .vimrc                  | 0600 | [LINK](https://raw.githubusercontent.com/r-pufky/docs/master/xen/etc/skel/.vimrc)        |
| .screenrc               | 0600 | [LINK](https://raw.githubusercontent.com/r-pufky/docs/master/xen/etc/skel/.screenrc)     |
| README                  | 0600 | [LINK](https://raw.githubusercontent.com/r-pufky/docs/master/xen/etc/skel/README)        |

* Create ssh and bin directories, secure
```bash
sudo rm /etc/skel/.profile
sudo mkdir /etc/skel/.ssh /etc/skel/bin
sudo chmod 0700 /etc/skel/.ssh /etc/skel/bin
sudo chmod go-rwx /etc/skel/{*,.*}
```

* Secure user directory
```bash
chmod go-rwx -Rv ~
```

### Setup root user profile
* Create ssh and bin directories, secure
```bash
mkdir ~/.ssh ~/bin
chmod 0700 ~/.ssh ~/bin
```

* Copy the following configuration files to system, these are
  preconfigured preferences.

| File                            | Perm | Link                                                                                                   |
|---------------------------------|------|--------------------------------------------------------------------------------------------------------|
| .bashrc                         | 0600 | [LINK](https://raw.githubusercontent.com/r-pufky/docs/master/xen/root/.bashrc)                         |
| .bash_profile                   | 0600 | [LINK](https://raw.githubusercontent.com/r-pufky/docs/master/xen/root/.bash_profile)                   |
| .bash_logout                    | 0600 | [LINK](https://raw.githubusercontent.com/r-pufky/docs/master/xen/root/.bash_logout)                    |
| .vimrc                          | 0600 | [LINK](https://raw.githubusercontent.com/r-pufky/docs/master/xen/root/.vimrc)                          |
| .screenrc                       | 0600 | [LINK](https://raw.githubusercontent.com/r-pufky/docs/master/xen/root/.screenrc)                       |
| bin/server-user                 | 0700 | [LINK](https://raw.githubusercontent.com/r-pufky/docs/master/xen/root/bin/server-user)                 |
| bin/server-hostname             | 0700 | [LINK](https://raw.githubusercontent.com/r-pufky/docs/master/xen/root/bin/server-hostname)             |
| bin/server-encryption-primary   | 0700 | [LINK](https://raw.githubusercontent.com/r-pufky/docs/master/xen/root/bin/server-encryption-primary)   |
| bin/server-encryption-secondary | 0700 | [LINK](https://raw.githubusercontent.com/r-pufky/docs/master/xen/root/bin/server-encrpytion-secondary) |

* Delete .profile

* Secure root directory
```bash
chmod 0700 /root
chmod -Rv go-rwx /root
```

### Convert VM to Template
* Clear command history from root/user
* shutdown cleanly
* VM: set vCPU priority to lowest
* VM: set Memory to dynamic, 512-1024MB
* VM: right-click > Convert to Template
* Template: Custom Fields: Final Setup = setup-server-setup; configure-server; setup-server-finish


Manual Crypt/LUKS commands
--------------------------
### Manually determining crypt block device
* List encrypted disks that are mounted through crypt. The root block device is prepended to \_crypt
```bash
dmsetup ls --target crypt
```
* /var/log/syslog will show crypt block device during boot as well
* Generally LUKS containers are on partition 5 if auto created

### Manually dumping LUKS container on crypt device
This will show all the current slots and usage.
```bash
cryptsetup luksDump /dev/xvda5
```
* Default key is usually in slot 0

### Manually changing existing passphrase in LUKS
```bash
cryptsetup --verify-passphrase luksChangeKey /dev/xvda5 --key-slot 0
```


Enabling Secure SSH Config
--------------------------
The secure config requires that users are added to the `ssh` group before publickey auth will work; as well as enabling the secure config
```bash
usermod -a -G ssh <username>
rm /etc/ssh/sshd_config
ln -s /etc/ssh/sshd_config.secure /etc/ssh/sshd_config
service sshd restart
```

Then generate certs for use.
```bash
cd .ssh
ssh-keygen -b 4096 -t rsa -f <intended-certificate-name>
cat <intended-certificate-name>.pub >> ~/.ssh/authorized_keys
chmod 0600 ~/.ssh/*
chmod 0640 ~/.ssh/*.pub
```
_remember to copy private key to intended system to use it on._


Modifying a VM Template
-----------------------
* Copy the UUID from the template image `General > Properties > UUID`
* SSH to the XenServer, change to root
* Convert template to VM and start it
```bash
xe vm-param-set uuid=<UUID> is-a-template=false
xe vm-start uuid=<UUID>
```
* After changes, convert back to a template in the GUI.


Manually Creating New VM from Template
--------------------------------------
Determine the template name, and create a new VM from that template, start it.
```bash
xe template-list
xe vm-install template="<template name>" new-name-label="<vm name>"
xe vm-start uuid=<new VM>
```

Creating an Encrypted Volume
----------------------------
This assumes that an additional virtual disk has already been attached to the VM, and resides at /dev/xvdb

### Find the new block device and setup encrpytion
```bash
lsblk
sudo cryptsetup luksFormat --hash=sha256 --key-size=512 --cipher=aes-xts-plain64 --verify-passphrase /dev/xvdb
```
* This is not the most secure encryption, however, it's the default settings that ubuntu uses when it installs; use stronger encryption if desired.

### Create the LVM physical volume, volume group and logical volume
```bash
sudo cryptsetup luksOpen /dev/xvdb xvdb_crypt
sudo pvcreate /dev/mapper/xvdb_crypt
sudo vgcreate data /dev/mapper/xvdb_crypt
sudo lvcreate -n data -l +100%FREE data
```

### Format and mount the encrypted volume to /data
```bash
sudo mkfs.ext4 -m 0 /dev/data/data
sudo mkdir /data
sudo mount /dev/data/data /data
```

### Add volume to crypttab
* Find the *ROOT* device UUID (/dev/xvdb)
```bash
sudo blkid
```

sudo vim /etc/crypttab
```vim
xvdb_crypt UUID=<UUID from xvdb> none luks,discard
```
* Generally, using discard for SSD's is preferred, even though there are security issues related with it. See reference.

### Add to fstab
sudo vim /etc/fstab
```vim
/dev/mapper/data-data /data ext4 defaults 0 2
```


References
----------
[Expanding a LVM after expanding virtual machine disk](https://www.rootusers.com/how-to-increase-the-size-of-a-linux-lvm-by-expanding-the-virtual-machine-disk/)

[Manually changing a password on a dmcrypt / LUKS volume](https://unix.stackexchange.com/questions/185390/list-open-dm-crypt-luks-volumes)

[Reseting a password on an encrypted FS](https://unix.stackexchange.com/questions/126180/how-to-reset-password-on-an-encrypted-fs)

[Howto change LUKS passphrase](https://askubuntu.com/questions/95137/how-to-change-luks-passphrase)

[Converting template to a VM on XenServer](https://discussions.citrix.com/topic/241867-guest-best-pratice-copy-vm-or-convert-to-template/)

[Full encryption with LVM and LUKS](https://www.linux.com/blog/how-full-encrypt-your-linux-system-lvm-luks)

[Mounting LVM partitions](http://ask.xmodulo.com/mount-lvm-partition-linux.html)

[Mounting LVM logical volumes](https://blog.sleeplessbeastie.eu/2015/11/16/how-to-mount-encrypted-lvm-logical-volume/)

[Mounting encrypted LUKS drive at boot](https://askubuntu.com/questions/450895/mount-luks-encrypted-hard-drive-at-boot)

[Data Exposure when using 'discard' option with SSD's on dm-crypt](http://asalor.blogspot.de/2011/08/trim-dm-crypt-problems.html)
