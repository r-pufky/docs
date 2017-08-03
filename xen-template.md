Xen Server Template
-------------------
Ubuntu 16.04 base Xen template.

### Base Install
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

### Disable sshd and set sshd_config
* Copy the 'secure' sshd config to the machine. This just enforces cert-based auth only. [LINK.](https://raw.githubusercontent.com/r-pufky/docs/master/xen/etc/ssh/sshd_config.secure)
```bash
sudo systemctl disable ssh.service
sudo mv /etc/ssh/sshd_config /etc/ssh/sshd_config.insecure
sudo ln -s /etc/ssh/sshd_config.secure /etc/ssh/sshd_config
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

* Add uptime reboot warning message
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

### Setup base user profile
* Create ssh and bin directories, secure
```bash
mkdir ~/.ssh ~/bin
chmod 0700 ~/.ssh ~/bin
```

* Copy the following configuration files to system, these are
  preconfigured preferences.

| File                    | Perm | Link                    |
|-------------------------|------|-------------------------|
| .bashrc                 | 0600 | [LINK](https://raw.githubusercontent.com/r-pufky/docs/master/xen/home/.bashrc) |
| .bash_profile           | 0600 | [LINK](https://raw.githubusercontent.com/r-pufky/docs/master/xen/home/.bash_profile) |
| .bash_logout            | 0600 | [LINK](https://raw.githubusercontent.com/r-pufky/docs/master/xen/home/.bash_logout) |
| .vimrc                  | 0600 | [LINK](https://raw.githubusercontent.com/r-pufky/docs/master/xen/home/.vimrc) |
| .screenrc               | 0600 | [LINK](https://raw.githubusercontent.com/r-pufky/docs/master/xen/home/.screenrc) |
| bin/setup-server-start  | 0700 | [LINK](https://raw.githubusercontent.com/r-pufky/docs/master/xen/home/bin/setup-server-start) |
| bin/setup-server-finish | 0700 | [LINK](https://raw.githubusercontent.com/r-pufky/docs/master/xen/home/bin/setup-server-finish) |

* Delete .profile

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

| File                 | Perm | Link                    |
|----------------------|------|-------------------------|
| .bashrc              | 0600 | [LINK](https://raw.githubusercontent.com/r-pufky/docs/master/xen/root/.bashrc) |
| .bash_profile        | 0600 | [LINK](https://raw.githubusercontent.com/r-pufky/docs/master/xen/root/.bash_profile) |
| .bash_logout         | 0600 | [LINK](https://raw.githubusercontent.com/r-pufky/docs/master/xen/root/.bash_logout) |
| .vimrc               | 0600 | [LINK](https://raw.githubusercontent.com/r-pufky/docs/master/xen/root/.vimrc) |
| .screenrc            | 0600 | [LINK](https://raw.githubusercontent.com/r-pufky/docs/master/xen/root/.screenrc) |
| bin/configure-server | 0700 | [LINK](https://raw.githubusercontent.com/r-pufky/docs/master/xen/root/bin/configure-server) |

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
