Xen Server Setup
-------------------
Basic XenServer 7.2 Setup & lockdown.

1. [Console Setup](#console-setup)
2. [Creating a Local ISO Repository](#creating-a-local-iso-repository)
2. [References](#references)

Console Setup
-------------
### Add a non-root account
* Open SSH Console to XenServer instance
```bash
useradd <username>
passwd <username>
```

* Enable sudo access for new user

visudo
```bash
<username>  ALL=(ALL)  ALL
```

* Confirm sudo works.
```bash
sudo su -
```

### Generate pubkey cert for new user
* Copy private key to whatever system used to login
```bash
cd ~; mkdir .ssh; chmod 0700 .ssh; cd .ssh
ssh-keygen -b 4096 -t rsa -f <intended-certificate-name>
cat <intended-certificate-name>.pub >> ~/.ssh/authorized_keys
chmod 0600 ~/.ssh/*
chmod 0640 ~/.ssh/*.pub
```

### Enforce cert-only ssh logins
* Ensure certs are copied off server before restarting or you'll be locked out
* sudo vi /etc/ssh/sshd_config
```vim
permitrootlogin no
allowusers <username>
MaxAuthTries 3
PasswordAuthentication no
AuthorizedKeysFile %h/.ssh/authorized_keys
```

```bash
service sshd restart
```

### Disable utils webpage
```bash
cp /opt/xensource/www/Citrix-index.html /home/<username>/original-index.html
echo '' > /opt/xensource/www/Citrix-index.html
```

### Restrict XAPI to pre-defined hosts
* sudo vi /etc/hosts.deny
```bash
xapi:ALL
```

* sudo vi /etc/hosts.allow
```bash
xapi:<IP> <IP>
```

### Disable TLS < 1.2 for SSL connections
* This can be done in the GUI via `XenPool > Properties > Security > TLS 1.2 only`
```bash
xe pool-disable-ssl-legacy
```

### Only keep 2 days of logs
* Keep 2 days of log rotations, instead of 31 by default.
* sudo vi /etc/logrotate.conf
```
rotate 2
```

Creating A Local ISO Repository
-------------------------------
This will allow the use of ISO's on dom0 to be used during VM creation.

* From an SSH session, create a directory and create a Storage Repository on top of it

```bash
mkdir -p /var/opt/xen/iso_import
xe sr-create name-label=LocalISO type=iso device-config:location=/var/opt/xen/iso_import device-config:legacy_mode=true content-type=iso
```

References
----------
[Basic XenServer Security Tips](http://burm.net/2012/01/29/xenserver-basic-security-tips-how-do-you-secure-your-xenserver/)

[Adding new usergroups to XenServer](https://discussions.citrix.com/topic/154063-add-new-usersgroup-to-xenserver/)

[XenServer 7.0 release notes](http://docs.citrix.com/content/dam/docs/en-us/xenserver/xenserver-7-0/downloads/xenserver-7-0-release-notes.pdf)

[Modifying XenServer logging](https://discussions.citrix.com/topic/299016-how-to-disable-xenserver-logging/)

[Creating A Local ISO Repository](https://xen-orchestra.com/blog/creating-a-local-iso-repository-in-xenserver/)
