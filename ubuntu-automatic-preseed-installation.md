Ubuntu Automatic (Preseed) Installation
---------------------------------------
[Preseeding][4] allows you to install debian/ubuntu from an ISO image with
selections already made, setting up specific base packages so that it can be
automatically installed on boot and immediately used afterwards. This is great
for VM's and pre-setup of configuration management agents.

1. [Install pre-req packages](#install-package-pre-reqs)
2. [Extract ISO for modification](#extract-iso-for-modification-to-custom-iso)
3. [Setup auto-install on boot](#setup-auto-installation-preseed-preferences)
4. [Setup preseed file](#create-preseed-installation-file)
5. [Write ISO](#build-custom-iso)
6. [Build commands](#build-testing-commands)
7. [Gotchas](#gotchas)


## Install package pre-reqs
These include a utility to manipulate ISO images, debconf utilities and a
password hash utility for /etc/shadow.
```bash
apt install debconf-utils whois xorriso
```

## Extract ISO for modification to custom-iso
```bash
xorriso -osirrox on -indev <ubuntu>.iso -extract / custom-iso
```

## Setup auto-installation (preseed) preferences
Depending on how you would like to preseed the automatic install:

 * [Fully Automatic Installation](#isolinux.cfg)
 * [Grub (non-EFI) boot menu, manual selection for auto install](#grub-non-efi-boot-menu)
 * [Grub (EFI) boot menu, manual selection for auto install](#grub-efi-boot-menu)

You can create a single disk that supports both EFI and non-EFI machines. Ensure
that your labels and configs are changes accordingly.

### isolinux.cfg
Use this option if you want a booted ISO image to immediately start the install
process. This will immediately drop you into the debian installer with required
options pre-selected.

custom-iso/isolinux/isolinux.cfg
```bash
default custom-saltstack
label custom-saltstack
  menu label ^Install Ubuntu Server w/ Saltstack minion
  kernel /install/vmlinuz
  append file=/cdrom/preseed/ubuntu-saltstack.seed vga=768 debian-installer/language=en debian-installer/country=US console-setup/ask_detect=false keyboard-configuration/layoutcode=us debian-installer/locale=en_US.UTF-8 localechooser/preferred-locale=en_US.UTF8 initrd=/install/initrd.gz quiet ---
```
 * This correctly seeds the default isolinux boot image to automatically drop
   into the preseed installation, with required options.

### Grub (non-EFI) boot menu
Use this option to add an additional menu item in the boot menu for the ISO,
which will allow you to do an automated install after setting your preferences
and potentially using any utilities on the standard boot menu.

This is for legacy (non-EFI/BIOS) systems.

custom-iso/isolinux/txt.cfg
```bash
default custom-saltstack
label custom-saltstack
  menu label ^Install Ubuntu Server w/ Saltstack minion
  kernel /install/vmlinuz
  append file=/cdrom/preseed/ubuntu-saltstack.seed vga=768 debian-installer/language=en debian-installer/country=US console-setup/ask_detect=false keyboard-configuration/layoutcode=us debian-installer/locale=en_US.UTF-8 localechooser/preferred-locale=en_US.UTF8 initrd=/install/initrd.gz quiet ---
```
 * If you only want an automatic install, modify [isolinux.cfg](#isolinux.cfg)
   instead.

### Grub (EFI) boot menu
Use this option to add an additional menu item in the boot menu for the ISO,
which will allow you to do an automated install after setting your preferences
and potentially using any utilities on the standard boot menu.

This is for modern (EFI/UEFI) systems.

custom-iso/boot/grub/grub.cfg
```bash
set default 0
menuentry "Install Ubuntu Server w/ Saltstack minion" {
  set gfxpayload=keep
  linux /install/vmlinuz file=/cdrom/preseed/ubuntu-saltstack.seed debian-installer/language=en debian-installer/country=US console-setup/ask_detect=false keyboard-configuration/layoutcode=us debian-installer/locale=en_US.UTF-8 localechooser/preferred-locale=en_US.UTF8 quiet ---
  initrd /install/initrd.gz
}
```
 * This assumes you place the custom entry first. Adjust default accordingly.
 * If you only want an automatic install, modify [isolinux.cfg](#isolinux.cfg)
   instead.

## Create preseed installation file.
This provides answers for the debconf installer during installation. Providing
these answers enables the installation to complete without interaction. Most of
the options here are required for automated installation.

See [ubuntu-preseed.seed](#ubuntu-preseed.seed) for a complete example file, or
read [the preseed manual][4].

To get avaliable parameters for a section, use:
```bash
debconf-get-selections | grep <option>
```


### Localization
```
# -------- Localization --------
d-i debian-installer/locale string en_US.UTF-8
```
Set the installer's locale

### Keyboard
```
# -------- Keyboard --------
d-i console-setup/ask_detect boolean false
d-i console-setup/layoutcode string us
d-i keyboard-configuration/xkb-keymap select us
```
Set keyboard to us and remove detection prompt.

### Network
```
# -------- Network --------
d-i netcfg/choose_interface select auto
d-i netcfg/link_wait_timeout string 10
d-i netcfg/dhcp_timeout string 10
d-i netcfg/dhcpv6_timeout string 1

# Set default names to prevent prompts, overwritten by DHCP names.
d-i netcfg/get_hostname string unassigned-hostname
d-i netcfg/get_domain string unassigned-domain

# Disable that annoying WEP key dialog.
d-i netcfg/wireless_wep string

```
Grab the first active network connection, quick fail DHCPv6 and wait 10 seconds
for a link. Hostname is automatically set via DHCP, so just set a template
hostname for initial installation. Disable WEP dialog.

### Hardware
```
# -------- Hardware Firmware --------
d-i hw-detect/load_firmware boolean true
```
Enable installation of close-sourced firmware updates for hardware.

### Apt
```
# -------- Apt Mirror --------
d-i mirror/country string manual
d-i mirror/http/hostname string mirrors.mit.edu
d-i mirror/http/directory string /ubuntu
d-i mirror/http/proxy string
d-i mirror/udeb/components multiselect main, restricted, multiverse, universe
```
Note: This is for the main OS installation, *NOT* package installation. Set a
custom ubuntu mirror, and enable all for components.

### Accounts
```
# -------- Accounts --------
# disable root user
d-i passwd/root-login boolean false

# base user for system
d-i passwd/user-fullname string
d-i passwd/username string <username>
d-i passwd/user-password-crypted password <mkpasswd -m sha-512>
d-i passwd/user-uid string 1000
d-i passwd/user-default-groups string cdrom video sudo ssh plugdev
d-i user-setup/encrypt-home boolean false
```
 * Disable root login
 * Create an initial user, with a sha512 password hash `mkpasswd -m sha-512`
   copy the resulting hash into the password field. *NOTE* This should be an
   _installation_ password, not your real one. You can change that later with
   configuration management tools.
 * Give that user sudo and ssh access, and [default groups to function][11].

### Time
```
# -------- Clock and Timezone --------
d-i clock-setup/utc boolean false
d-i time/zone string America/Los_Angeles
d-i clock-setup/ntp boolean true
```
Read hardware clock as non-UTC, set timezone and enable NTP.

### Paritioning
```
# -------- Partitioning --------
# Auto remove existing LVM/RAID partitions on disk
d-i partman-lvm/device_remove_lvm boolean true
d-i partman-lvm/confirm boolean true
d-i partman-lvm/confirm_nooverwrite boolean true
d-i partman-md/device_remove_md boolean true
d-i partman-md/confirm boolean true

# Unmount auto-mounted existing partitions on disks, if any
d-i preseed/early_command string umount /media

# Disable no-swap warning, create / with at least 1GB for entire disk.
d-i partman-auto/disk string /dev/xvda
d-i partman-auto/method string regular
d-i partman-basicfilesystems/no_swap boolean false
d-i partman-auto/expert_recipe string root :: 1000 50 -1 ext4 \
     $primary{ } $bootable{ } method{ format } \
     format{ } use_filesystem{ } filesystem{ ext4 } \
     mountpoint{ / } \
    .
d-i partman-auto/choose_recipe select root

# Apply partitioning info with confirmation
d-i partman-partitioning/confirm_write_new_label boolean true
d-i partman/choose_partition select finish
d-i partman/confirm boolean true
d-i partman/confirm_nooverwrite boolean true
```
 * Automatically delete and remove LVM and RAID partitions.
 * Umount any partitions that may have autmounted to media. See [here][13] and
   [here][14] which explains why these cause automated partitioning to fail.
 * Create a [single partition][12] with no swap, EXT4, on block device
   /dev/xvda.
 * See [umount /media fails!](#execution-of-umount-on-media-failed)

### Kernel
```
# -------- Base System Installation --------
d-i base-installer/kernel/image string linux-generic
```
Install the generic kernel. Use `linux-server` for server kernel.

### Apt Packages
```
# -------- Apt Setup -------
d-i apt-setup/restricted boolean true
d-i apt-setup/universe boolean true
d-i apt-setup/multiverse boolean true
d-i apt-setup/backports boolean true

# -------- Package Selection --------
# Main tasksel server packages
tasksel tasksel/first multiselect server, openssh-server

# Additional packages to install
d-i pkgsel/include string openssh-server python-software-properties inotify-tools curl unattended-upgrades sysstat nmon screen ssh vim haveged

# Upgrade packages after bootstrap
d-i pkgsel/upgrade select full-upgrade

# Install security updates automatically
d-i pkgsel/update-policy select unattended-upgrades
```
 * Setup apt package install to use all four components
 * Install server and openssh-server tasks
 * Install other default ubuntu packages
 * Upgrade all packages to latest version [this is currently broken in ubuntu
   and needs to be done manually in late_command](#post-install)

#### Tasksel
Tasksel installs meta-packages for common setups.

List all avaliable tasks
```bash
tasksel --list-task
```
These can be used in the `tasksel/first` line.

The packages installed in these meta packages can be found with
```bash
tasksel --task-packages <package>
apt --dry-run install <task>
```
 * the task includes ^, e.g. `server^`
 * From ubuntu 16.04, `--task-packages` returns the meta-package name, not the
   list of packages. Other versions you can just use `--task-packages`.
 * Can also see [task packages from the germinate templates here][15].

### Console
```
# Verbose startup output, drop to console (text) login by default.
d-i debian-installer/quiet  boolean false
d-i debian-installer/splash boolean false
```
Disable the GUI boot login prompt, use console. Enable verbose logging on boot.

### Boot Loader
```
# -------- Boot Loader Installation --------
# Assume one OS, install to default device, add other OS's if found.
d-i grub-installer/only_debian boolean true
d-i grub-installer/with_other_os boolean true
d-i grub-installer/bootdev  string default
d-i grub-installer/timeout  string 2
```
Install grub to MBR with this OS as default. Detect other OS's and add if
needed. default boot this OS in 2 seconds.

### Post Install
```
# After system is setup (before reboot), run post-install script.
d-i preseed/late_command string cp -R /cdrom/post-install/* /target/tmp; in-target /tmp/post-preseed-complete
```
 * Copy post-install directory from ISO to installed OS's /tmp, and execute
   post-install script.
 * NOTE: commands *must* be executed with `in-target` command, otherwise your
   scripts will [run on the isolinux image and fail][17], and not the target OS
   install.
 * Using `in-target` behaves as a chroot to that system, meaning _copy over your
   files to that system to find them_.
 * You can [pull your scripts and files using curl or wget.][18]

### Finish Installation
```
# -------- Finish Installation --------
d-i cdrom-detect/eject boolean true
d-i finish-install/reboot_in_progress note
```
Eject the CD before booting, don't prompt for reboot.


## Build custom ISO

### Copy custom files
```bash
cp ubuntu-saltstack.seed custom-iso/preseed/ubuntu-saltstack.seed
cp -av post-install custom-iso/
```
 * Ensure to copy modified boot menus, if not edited directly.

### Extract existing isohdpfx.bin for multi-boot (EFI/non-EFI) ISO image
Take the existing multi-boot (EFI/non-EFI) image from the iso and reuse it to
create the new ISO image.
```bash
sudo dd if=<ubuntu>.iso bs=512 count=1 of=custom-iso/isolinux/isohdpfx.bin
```

### Rehash MD5 sums for file integrity checks
```bash
cd custom-iso
md5sum $(find -type f) > md5sum.txt
```

### Make new ISO image / checksum it
```bash
cd custom-iso
sudo xorriso -as mkisofs -isohybrid-mbr isolinux/isohdpfx.bin -c isolinux/boot.cat -b isolinux/isolinux.bin -no-emul-boot -boot-load-size 4 -boot-info-table -eltorito-alt-boot -e boot/grub/efi.img -no-emul-boot -isohybrid-gpt-basdat -o ../custom-ubuntu.iso .
cd ..
sha512sum custom-ubuntu.iso > custom-ubuntu.sha512sum
sha512sum -c custom-ubuntu.sha512sum
```

### Ensure both non-EFI and EFI partitions show
```bash
fdisk -l custom-ubuntu.iso

...

Device             Boot Start     End Sectors  Size Id Type
custom-ubuntu.iso1 *        0 1763327 1763328  861M  0 Empty
custom-ubuntu.iso2       4028    8763    4736  2.3M ef EFI (FAT-12/16/32)
```
This will confirm that there's an EFI and non-EFI ISO in the image.


## Build / Testing commands

Checksum, build and push the latest image to xen:
```bash
sudo md5sum $(find -type f) > md5sum.txt; sudo xorriso -as mkisofs -isohybrid-mbr isolinux/isohdpfx.bin -c isolinux/boot.cat -b isolinux/isolinux.bin -no-emul-boot -boot-load-size 4 -boot-info-table -eltorito-alt-boot -e boot/grub/efi.img -no-emul-boot -isohybrid-gpt-basdat -o ../custom-ubuntu.iso .; scp ../custom-ubuntu.iso Xen:~
```

Refresh the ISO image in Storage Repository on Xen:
```bash
xe sr-list
rm -f custom-ubuntu.iso; mv /home/<xenuser>/custom-ubuntu.iso /var/opt/xen/iso_import; chown root:root custom-ubuntu.iso; chmod o+r custom-ubuntu.iso; xe sr-scan uuid=<UUID from sr-list for ISO Repository>
```
 * Assumes root user.


## Gotchas

### Blank screen on reboot
Everything works fine, but [blank screen on boot?][16] You need to setup a
proper GUI login (e.g. probable need to install `desktop` task) or enable the
console. See [Console Section](#console) for setting no splash.

You can still `ctrl-alt-F1` to get to the console from the blank screen.

### pkgsel/upgrade string full-upgrade not working
This is [broken in ubuntu 16.04][17]. You need to manually run late_command
tasks to update the packages.

### Execution of umount on /media failed!
This fails because there was no pre-existing partitions to umount. You can
ignore this message or remove the umount command if you are sure you will not
run into systems requiring to unmount /media.

[10]: https://github.com/dsgnr/Ubuntu-16.04-Unattended-Install/blob/master/README.md
[1]: https://askubuntu.com/questions/813058/preseed-ubuntu-16-04-not-working-preseed-file-not-found
[2]: https://searchitchannel.techtarget.com/feature/Performing-an-automated-Ubuntu-install-using-preseeding
[3]: https://askubuntu.com/questions/806820/how-do-i-create-a-completely-unattended-install-of-ubuntu-desktop-16-04-1-lts
[4]: https://help.ubuntu.com/16.04/installation-guide/amd64/apb.html
[5]: https://help.ubuntu.com/16.04/installation-guide/amd64/apbs01.html
[6]: https://help.ubuntu.com/16.04/installation-guide/amd64/apbs04.html
[7]: https://help.ubuntu.com/16.04/installation-guide/example-preseed.txt
[8]: https://github.com/dsgnr/Ubuntu-16.04-Unattended-Install/blob/master/preseed.cfg
[9]: https://github.com/dsgnr/Ubuntu-16.04-Unattended-Install/blob/master/post-install.sh
[11]: https://wiki.ubuntu.com/Security/Privileges#Use_CD-ROM_drives
[12]: https://superuser.com/questions/458672/ubuntu-preseed-use-whole-disk-space-but-no-swap
[13]: https://ubuntuforums.org/showthread.php?t=2215103
[14]: https://bugs.launchpad.net/ubuntu/+source/debian-installer/+bug/1347726
[15]: http://people.canonical.com/~ubuntu-archive/germinate-output/ubuntu.xenial/
[16]: https://askubuntu.com/questions/837007/ubuntu-server-16-04-1-lts-installed-with-preseed-file-taking-to-black-screen
[17]: https://github.com/tylert/packer-build/issues/7
[17]: https://www.linuxquestions.org/questions/programming-9/how-to-use-late_command-in-preseed-file-852603/
[18]: https://askubuntu.com/questions/557933/copy-package-to-a-specific-directory-with-customized-iso
[19]: https://askubuntu.com/questions/409607/how-to-create-a-customized-ubuntu-server-iso
