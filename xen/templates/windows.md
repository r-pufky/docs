Windows 10 Template
-------------------
Windows 10 base Xen template.

1. [Base Install](#base-install)
2. [Default Applications](#default-applications)
5. [Adding Custom Fonts](#adding-custom-fonts)
6. [References](#references)

Base Install
------------
* Template: Windows 10
* Copy BIOS Strings to VM
* Memory: 8GB
* Disk: 60GB
* All ethernet devices
* Hostname: windows
* Partitioning: Default
* Otherwise, follow [windows-gaming build documentation][1]

### Activating Windows
Generally, you'll need a VM license for activating windows 10 on a VM. 
Homegamers can probably get away with running one windows VM at a time. YMMV, I
am not a lawyer. Act in good faith.

* Ensure system is fully update to date
* meltdown/spectre [patches are applied][2]
* Activate Windows

```
start > settings > update & security > activation
```

### Install XenServer tools
* Mount guest-tools.iso on VM in XenCenter
* Tools should install automatically when drive is clicked. If not:

If not, goto drive
```
right click drive > open
double click Setup.exe
```

* Reboot VM
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
[1]: ../../windows-gaming.md
[2]: ../../windows-gaming.md#securing-windows-installation
[3]: ../../windows-gaming.md#enabling-ssh-access