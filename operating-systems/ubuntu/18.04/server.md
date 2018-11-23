Ubuntu 18.04 Server
-------------------
Ubuntu 18.04 server configuration notes.

1. [Base Install](#base-install)
1. [Manual Crypt/LUKS Commands](#manual-cryptluks-commands)
1. [Enabling Secure SSH Config](#enabling-secure-ssh-config)
1. [Creating an Encrypted Volume](#creating-an-encrypted-volume)
1. [Adding Custom Fonts](#adding-custom-fonts)
1. [Update UFW Rules](#update-ufw-rules)
1. [NXDOMAIN Errors in Syslog](#nxdomain-errors-in-syslog)
1. [References](#references)

### Base Install
* Hostname: ubuntu
* Full Name: None
* Username: template
* Password: template
* No encrypted home directory
* Partitioning: Guided, Full disk, no encryption
* Set default encryption passphrase: template
* Size: max
* Automatic security updates
* Packages: Standard system utilities

### Change apt repository
sudo vim /etc/apt/sources.list
```vim
%s/us\.archive\.ubuntu\.com/mirrors\.mit\.edu/g
```

### Install base packages
```bash
sudo apt update && sudo apt upgrade
sudo apt install python-software-properties inotify-tools curl unattended-upgrades sysstat nmon screen ssh ffpmeg
```

### Set base sshd_config
* Copy the 'secure' sshd config to the machine. This just enforces cert-based
auth only. [LINK.](https://raw.githubusercontent.com/r-pufky/docs/master/operating-systems/ubuntu/etc/ssh/sshd_config.secure).
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
Unattended-Upgrade::Automatic-Reboot "true";
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
* Disable [documentation listing][12]
```bash
sudo chmod a-x /etc/update-motd.d/10-help-text
sudo chmod a-x /etc/update-motd.d/50-landscape-info
sudo chmod a-x /etc/update-motd.d/50-motd-news
sudo chmod a-x /etc/update-motd.d/50-landscape-sysinfo
sudo chmod a-x /etc/update-motd.d/80-livepatch
```

* Add uptime reboot warning message. [LINK.](https://raw.githubusercontent.com/r-pufky/docs/master/operating-systems/ubuntu/etc/update-motd.d/98-reboot-required)

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

if [ -x /usr/lib/update-notifier/update-motd-reboot-required ]; then
  exec /usr/lib/update-notifier/update-motd-reboot-required
fi
```
```bash
sudo chmod a+x /etc/update-motd.d/98-reboot-required
```

### Disable mdadm array
* Add at end of file to ignore software raid detection at boot

sudo vim /etc/mdadm/mdadm.conf
```vim
ARRAY <ignore> devices=/dev/null
```

### Setup skeleton user profile
* Copy the following configuration files to system, these are
  preconfigured preferences.

| File                    | Perm | Link                                                                                     |
|-------------------------|------|------------------------------------------------------------------------------------------|
| .bashrc                 | 0600 | [LINK](https://raw.githubusercontent.com/r-pufky/docs/master/operating-systems/ubuntu/etc/skel/.bashrc)       |
| .bash_profile           | 0600 | [LINK](https://raw.githubusercontent.com/r-pufky/docs/master/operating-systems/ubuntu/etc/skel/.bash_profile) |
| .bash_logout            | 0600 | [LINK](https://raw.githubusercontent.com/r-pufky/docs/master/operating-systems/ubuntu/etc/skel/.bash_logout)  |
| .vimrc                  | 0600 | [LINK](https://raw.githubusercontent.com/r-pufky/docs/master/operating-systems/ubuntu/etc/skel/.vimrc)        |
| .screenrc               | 0600 | [LINK](https://raw.githubusercontent.com/r-pufky/docs/master/operating-systems/ubuntu/etc/skel/.screenrc)     |
| README                  | 0600 | [LINK](https://raw.githubusercontent.com/r-pufky/docs/master/operating-systems/ubuntu/etc/skel/README)        |

* Create ssh and bin directories, secure
```bash
sudo rm /etc/skel/.profile
sudo mkdir /etc/skel/.ssh /etc/skel/bin
sudo chmod 0700 /etc/skel/.ssh /etc/skel/bin
sudo chmod -Rv go-rwx /etc/skel/
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
| .bashrc                         | 0600 | [LINK](https://raw.githubusercontent.com//r-pufky/docs/master/operating-systems/ubuntu/root/.bashrc)                         |
| .bash_profile                   | 0600 | [LINK](https://raw.githubusercontent.com//r-pufky/docs/master/operating-systems/ubuntu/root/.bash_profile)                   |
| .bash_logout                    | 0600 | [LINK](https://raw.githubusercontent.com//r-pufky/docs/master/operating-systems/ubuntu/root/.bash_logout)                    |
| .vimrc                          | 0600 | [LINK](https://raw.githubusercontent.com//r-pufky/docs/master/operating-systems/ubuntu/root/.vimrc)                          |
| .screenrc                       | 0600 | [LINK](https://raw.githubusercontent.com//r-pufky/docs/master/operating-systems/ubuntu/root/.screenrc)                       |
| bin/server-user                 | 0700 | [LINK](https://raw.githubusercontent.com//r-pufky/docs/master/operating-systems/ubuntu/root/bin/server-user)                 |
| bin/server-hostname             | 0700 | [LINK](https://raw.githubusercontent.com//r-pufky/docs/master/operating-systems/ubuntu/root/bin/server-hostname)             |
| bin/server-encryption-primary   | 0700 | [LINK](https://raw.githubusercontent.com//r-pufky/docs/master/operating-systems/ubuntu/root/bin/server-encryption-primary)   |
| bin/server-encryption-secondary | 0700 | [LINK](https://raw.githubusercontent.com//r-pufky/docs/master/operating-systems/ubuntu/root/bin/server-encryption-secondary) |

* Delete .profile

* Secure root directory
```bash
chmod 0700 /root
chmod -Rv go-rwx /root
```

Manual Crypt/LUKS commands
--------------------------
### Manually determining crypt block device
* List encrypted disks that are mounted through crypt. The root block device is
prepended to \_crypt
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

#### Bug in debian/ubuntu using keyscript
There is currently an open issue with all latest releases of debian/ubuntu,
where systemd does not respect the keyscript option in crypttab. This breaks
any easy use for automatic unlocking through USB keys.

https://news.ycombinator.com/item?id=8477913

https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=618862

https://askubuntu.com/questions/906870/luks-keyscript-being-ignored-asks-for-password

https://github.com/systemd/systemd/pull/3007/


Potential manual solution using ubuntu 16.04 with systemd workaround, though
seems to be very hacky:
https://www.len.ro/work/luks-disk-encryption-with-usb-key-on-ubuntu-14-04/

Enabling Secure SSH Config
--------------------------
The secure config requires that users are added to the `ssh` group before
publickey auth will work; as well as enabling the secure config.

Longstanding SSH options have been [removed in this release and your SSH config
will not carry over unchanged.][14]

Create /etc/ssh/<username> directories
```bash
mkdir /etc/ssh/<username>
chown <username>:<username> /etc/ssh/<username>
chmod 0700 /etc/ssh/<username>
```

Move user's ssh directory and generate certs for use.
```bash
mv ~/.ssh/* /etc/ssh/<username>
ln -s /etc/ssh/<username> /home/<username>/.ssh
cd .ssh
ssh-keygen -b 4096 -t rsa -f <intended-certificate-name>
cat <intended-certificate-name>.pub >> ~/.ssh/authorized_keys
chmod 0600 ~/.ssh/*
chmod 0640 ~/.ssh/*.pub
```

Enable ssh for the user and the secure ssh config
```bash
usermod -a -G ssh <username>
rm /etc/ssh/sshd_config
ln -s /etc/ssh/sshd_config.secure /etc/ssh/sshd_config
service sshd restart
```

_remember to copy private key to intended system to use it on._

Creating an Encrypted Volume
----------------------------
This assumes that an additional virtual disk has already been attached to the
VM, and resides at /dev/xvdb

### Find the new block device and setup encrpytion
```bash
lsblk
sudo cryptsetup luksFormat --hash=sha256 --key-size=512 --cipher=aes-xts-plain64 --verify-passphrase /dev/xvdb
```
* This is not the most secure encryption, however, it's the default settings
that ubuntu uses when it installs; use stronger encryption if desired.

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
* Generally, using discard for SSD's is preferred, even though there are
security issues related with it. See reference.

### Add to fstab
sudo vim /etc/fstab
```vim
/dev/mapper/data-data /data ext4 defaults 0 2
```

Adding Custom Fonts
-------------------
Fonts must be imported for use in applications, such as sublime text.

```bash
sudo apt install fontconfig
```

Copy font files to /usr/local/share/fonts/<font> and set appropriate permissions
```bash
sudo find /usr/local/share/fonts -type f -exec chown root:staff {} \;
sudo find /usr/local/share/fonts -type d -exec chmod o+rx {} \;
```

Refresh the font cache and list loaded fonts, you should see your new fonts.
```bash
fc-cache -f -v
fc-list
```

Update UFW Rules
----------------
Uncomplicated FireWall is setup by default in 18.04. Consideration should be
made on whether to keep this or disable this

### Allow a well-know service
```bash
ufw allow ssh
```

### Get current status
```base
ufw status
ufw status verbose
```

### Disable UFW
```bash
ufw disable
```

NXDOMAIN Errors in Syslog
-------------------------
This is caused by the systemd resolver not properly resolving local DNS. This
has been [resolved in `systemd - 239-7ubuntu4`][15], but it is currently not
avaliable to install.

### Workaround
Redirect the systemd resolver to the resolver specified from DHCP.

```
mv /etc/resolv.conf /etc/resolv.conf.broken
ls -s /etc/run/systemd/resolve/resolv.conf resolv.conf
```

References
----------
[Expanding a LVM after expanding virtual machine disk][1]

[Manually changing a password on a dmcrypt / LUKS volume][2]

[Reseting a password on an encrypted FS][3]

[Howto change LUKS passphrase][4]

[Full encryption with LVM and LUKS][5]

[Mounting LVM partitions][6]

[Mounting LVM logical volumes][7]

[Mounting encrypted LUKS drive at boot][8]

[Data Exposure when using 'discard' option with SSD's on dm-crypt][9]

[Adding custom fonts to ubuntu][10]

[Automatic Security Updates][11]

[Configuring UFW in Ubuntu 18.04][13]

[1]: https://www.rootusers.com/how-to-increase-the-size-of-a-linux-lvm-by-expanding-the-virtual-machine-disk/
[2]: https://unix.stackexchange.com/questions/185390/list-open-dm-crypt-luks-volumes
[3]: https://unix.stackexchange.com/questions/126180/how-to-reset-password-on-an-encrypted-fs
[4]: https://askubuntu.com/questions/95137/how-to-change-luks-passphrase
[5]: https://www.linux.com/blog/how-full-encrypt-your-linux-system-lvm-luks
[6]: http://ask.xmodulo.com/mount-lvm-partition-linux.html
[7]: https://blog.sleeplessbeastie.eu/2015/11/16/how-to-mount-encrypted-lvm-logical-volume/
[8]: https://askubuntu.com/questions/450895/mount-luks-encrypted-hard-drive-at-boot
[9]: http://asalor.blogspot.de/2011/08/trim-dm-crypt-problems.html
[10]: https://askubuntu.com/questions/3697/how-do-i-install-fonts
[11]: https://help.ubuntu.com/community/AutomaticSecurityUpdates
[12]: https://www.cyberciti.biz/faq/how-to-disable-ssh-motd-welcome-message-on-ubuntu-linux/
[13]: https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu-18-04
[14]: https://www.openssh.com/releasenotes.html
[15]: https://bugs.launchpad.net/ubuntu/+source/systemd/+bug/1766969