Xen Server Setup
-------------------
Basic XenServer 7.2 Setup & lockdown.

1. [Console Setup](#console-setup)
1. [Creating a Local ISO Repository](#creating-a-local-iso-repository)
1. [Convert VM to a Template](#convert-vm-to-a-template)
1. [Modifying a VM Template](#modifying-a-vm-template)
1. [Manually Creating New VM from Template](#manually-creating-new-vm-from-template)
1. [PCI Passthrough for Direct Hardware Access](#pci-passthrough-for-direct-hardware-access)
1. [References](#references)

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

### Refresh ISO library contents
```bash
xe sr-list
xe sr-scan uuid=<UUID of ISO repository>
```

Convert VM to a Template
------------------------
* Clear command history from root/user
* shutdown cleanly
* VM: set vCPU priority to lowest (if reasonable)
* VM: set Memory to dynamic, 512-1024MB (if reasonable)
* VM: right-click > Convert to Template
* Template: Custom Fields: add custom fields as needed

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

PCI Passthrough for Direct Hardware Access
------------------------------------------
Used for direct hardware access needs, like disks for ZFS and GPU's for 
plex.

### Find Device IDs
On XenServer as root, list PCI devices and determine the device ID's that
you want. They are in the format B:D.f (beginging of line)
```bash
lspci
```

### Prevent dom0 driver binding
This prevents dom0 from binding to hardware and presenting via a meta-layer.

```bash
/opt/xensource/libexec/xen-cmdline --set-dom0 "xen-pciback.hide=(04:00.0)"
```

Note: for multiple devices
```bash
/opt/xensource/libexec/xen-cmdline --set-dom0 "xen-pciback.hide=(04:00.0)(00:02.0)"
```
**Reboot XenServer**

### Add PCI device passthrough
With target VM off, determine UUID of vm with `xe vm-list`, then passthrough
PCI devices. You only have to do this once.

```bash
xe vm-param-set other-config:pci=0/0000:<B:D.f> uuid=<vm uuid>
```

Note: for multiple devices
```bash
xe vm-param-set other-config:pci=0/0000:<B:D.f>,0/0000:<B:D.f> uuid=<vm uuid>
```

References
----------
[Basic XenServer Security Tips][1]

[Adding new usergroups to XenServer][2]

[XenServer 7.0 release notes][3]

[Modifying XenServer logging][4]

[Creating A Local ISO Repository][5]

[Converting template to a VM on XenServer][6]

[PCI Passthrough][7]

[Multiple PCI Passthrough][8]

[PCI Passthrough Reference][9]

[1]: http://burm.net/2012/01/29/xenserver-basic-security-tips-how-do-you-secure-your-xenserver/
[2]: https://discussions.citrix.com/topic/154063-add-new-usersgroup-to-xenserver/
[3]: http://docs.citrix.com/content/dam/docs/en-us/xenserver/xenserver-7-0/downloads/xenserver-7-0-release-notes.pdf
[4]: https://discussions.citrix.com/topic/299016-how-to-disable-xenserver-logging/
[5]: https://xen-orchestra.com/blog/creating-a-local-iso-repository-in-xenserver/
[6]: https://discussions.citrix.com/topic/241867-guest-best-pratice-copy-vm-or-convert-to-template/
[7]: https://xenserver.org/blog/entry/pci-pass-through-on-xenserver-7-0.html
[8]: https://discussions.citrix.com/topic/355675-xenserver-pci-passthrough-pv-hvm-multiple-devices/
[9]: https://wiki.xen.org/wiki/Xen_PCI_Passthrough
