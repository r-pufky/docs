# [CachyOS][a].

!!! warning "[Disable Secure Boot and CSM][b]"
    Secure boot and CSM must be disabled during UEFI installations. It can be
    configured afterwards.


## Install
Use [USB Boot Disk][c].

1. Boot into Live Installer
2. Click on **Launch Installer** on Welcome screen.
    * Language: **American English**.
    * Region: **US**.
    * Zone: **Los Angeles**.
    * Keyboard Layout: **English (US)**.
    * Keyboard Language: **Default**.
    * Bootloader: **systemd-boot**.

        !!! info "GRUB is a second class citizen"
            CachyOS will create an encrypted LUKS2 partition with Argon2id, but
            deploy a version of GRUB without Agron2id support. This will cause
            boot password unlocks to fail but appear successful on live media.

            GRUB may still be used but requires re-encrypting the partition,
            updating GRUB, rebuilding initramfs, and rebuilding GRUB. All in
            the live media. Use systemd-boot as a stable replacement with
            multiple OS selection via firmware boot options (**F12**).

            A ZRAM partition will automatically be created.

    * Disk: **Erase Disk**.
      * EXT4: ✔
      * Encryption: ✔


    * Desktop: **Plasma Desktop**.
    * Packages: **Defaults**.
    * User:
      * Login: **Username**.
      * Computer: **Hostname**.
      * Use the same password for the administrator account: ✔

        !!! warning "Root cannot be disabled during installation."

### [Disable root logins][d]
Most online advice warns against disabling root. Standard linux constructs
apply. Locking root does not affect the system, only being able to login as
root user with a password - e.g. instead use live media and chroot to fix
catastrophic problems.

``` bash
passwd --lock root
```

### Set desired shell
CachyOS users default to fish shell. Set desired shell.

``` bash
chsh {USER} -s /bin/bash
```

### [Secure SSH][e]
Require certificate based authentication and disable root logins. Open firewall
and enable service

!!! abstract "/etc/ssh/sshd_confg"
    0644 root:root

    ``` bash
    PermitRootLogin no
    PasswordAuthentication no
    KbdInteractiveAuthentication no
    ```

``` bash
ufw open ssh
systemctl enable sshd
sysyetctl start sshd
```

## Configure Updates

``` bash
pacman -S cachy-update
cachy-update --gen-config
cachy-update --edit-config
systemctl --user enable --now arch-update.timer
# Check on boot and every day
# OnUnitActiveSec=1d
systemctl --user edit --full arch-update.timer
```


## Optional Packages
``` bash
pacman -S paru  # AUR repository helper (install non-arch AUR packages).

pacman -S iptables-nft  # More performant IPTables drop-in.
```

[a]: https://cachyos.org/
[b]: https://wiki.archlinux.org/title/Unified_Extensible_Firmware_Interface/Secure_Boot#Implementing_Secure_Boot
[c]: ../windows/README.md#create-uefi-usb-boot-disk
[d]: https://wiki.archlinux.org/title/Security#Restricting_root
[e]: ../../service/ssh/sshd/linux.md
