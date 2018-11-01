VM Templates
------------
Standard VM Templates used for server setup and configuration.

1. [Ubuntu](#ubuntu)
2. [Windows 10](#windows-10)

Ubuntu
------
| Type   | Value                |
|--------|----------------------|
| CPU    | 1 (1 socket, 1 core) |
| Memory | 1 GB                 |
| Disk   | 10 GB                |


Xen Server Template
-------------------
Ubuntu base VM template.

Base Configuration
------------------
| Type          | Value                      |
|---------------|----------------------------|
| BIOS          | Copy BIOS strings to VM    |
| Memory        | 8 GB                       |
| CPU           | 1 (1 sockets, 1 cores)     |
| Disk          | 10 GB                      |
| Ethernet      | 1 GB Ethernet bridged      |
| Partitioning  | Default Windows Scheme     |
| Hostname      | Ubuntu                     |
| Full Name     | None                       |
| Username      | template                   |
| Password      | template                   |
| Homedirectory | Not Encrypted              |
| Partitioning  | Guided, Full, Max          |
| Updates       | Automatic Security Updates |
| Packages      | Standard System Utilities  |
 * Ubuntu VM's are managed with saltstack
 * Follow [documentation here][../../operating-systems/ubuntu] for manual system
   configuration (all of these steps are automatically applied with saltstack).


Windows 10
----------
Windows 10 base VM template.

1. [Base Configuration](#base-configuration)
1. [Default Applications](#default-applications)
1. [Adding Custom Fonts](#adding-custom-fonts)
1. [References](#references)

Base Configuration
------------------
| Type         | Value                   |
|--------------|-------------------------|
| BIOS         | Copy BIOS strings to VM |
| Memory       | 8 GB                    |
| CPU          | 8 (4 sockets, 2 cores)  |
| Disk         | 60 GB                   |
| Ethernet     | 1 GB Ethernet bridged   |
| Partitioning | Default Windows Scheme  |
| Hostname     | Windows                 |
 * Copy BIOS strings over to keep activation for base hardware.
 * Generally, follow [windows-gaming build documentation][1]

### Activating Windows
You'll need a VM license for activating windows 10 on a VM.
Homegamers can probably get away with running one windows VM at a time. YMMV, I
am not a lawyer. Act in good faith.

* Ensure system is fully update to date
* meltdown/spectre [patches are applied][2]
* Activate Windows

```
start > settings > update & security > activation
```

### Install Virtualization Tools
 * Mount the virtualization toolset for specific hypervisor
   * guest-tools.iso on XenServer default repository
   * [Install packages][4] for KVM
 * Install tool packages and reboot VM
 * Check and apply new updates

Default Applications
--------------------
Add the base applications used by all VM's

 * [Chrome](https://www.google.com/chrome/)
 * [Putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)
 * [Winscp](https://winscp.net/eng/download.php)
 * [Sublime Text 3](https://www.sublimetext.com/3)
 * [OpenSSH Server][3] (just download, don't install service on template VM)

Adding Custom Fonts
-------------------
Fonts must be imported for use in applications, such as sublime text.

Copy font files to system
```
select all fonts
right click > install
```
 * Delete fonts copied over. These are now installed in the font directory.

References
----------
[1]: ../../operating-systems/windows/10/README.md
[2]: ../../operating-systems/windows/10/README.md#securing-windows-installation
[3]: ../../operating-systems/windows/10/windows-issues.md#enabling-ssh-access
[4]: http://www.linux-kvm.org/page/WindowsGuestDrivers