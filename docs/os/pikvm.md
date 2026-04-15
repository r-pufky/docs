# PiKVM
Raspberry Pi KVM with multi-port extenders based on Arch linux.

## Setup
!!! tip
    All commands are executed from an SSH session or launching Terminal after
    WebUI login.

    The filesystem **must** be set using **rw** before executing writes and
    using **ro** or rebooting after changes are made.

### Set Root Passwords
!!! danger
    The **root** user and the **WebUI** use different passwords. Change both.

    root: **root**/**root**.
    WebUI: **admin**/**admin**.

``` bash
# Terminal at WebUI login or SSH.
su -
passwd root  # Update root user password.
kvmd-htpasswd set admin  # Update WebUI admin password.
```

### Enable Certificate Authentication
See [SSHD](../network/ssh/README.md).

``` bash
cp {SSH KEYS} /root/.ssh/authorized_keys
```

!!! abstract "/etc/ssh/sshd_config"
    0644 root:root
    ``` bash
    PasswordAuthentication no
    ```

``` bash
systemctl restart ssh
```

### Update
``` bash
pikvm-update
```

### Enable Two-Factor Authentication (2FA)
``` bash
kvmd-totp init
```

### Disable Web Terminal
``` bash
# Be sure SSH connections work.
systemctl disable --now kvmd-webterm
```

### Disable Switch Lights
!!! example "Switch ➔ Color scheme"
    Drag all sliders to the left.

## Remote ISO Mount
Mount ISO image remotely for connected machine to use.

1. Obtain ISO to use
2. Drive ➔ Select image to upload
3. Drive ➔ Image select
4. Drive ➔ Drive mode: Flash
5. Drive ➔ Connect drive to server
6. Connect to local console and reboot

## Reference[^1]
[^1]: https://docs.pikvm.org/v4
