# Troubleshooting

## SSH pubkey authentication with locked accounts does not work
Locked accounts cannot SSH pubkey auth.  SSH now distinguishes between ! and *
password locking.

*: Lock password - allow SSH pubkey auth.

!: Lock password - deny SSH pubkey auth.

Any other means to lock the password will result in SSH pubkey failures.

!!! danger
    Do NOT **UsePam=yes** as this leads to security vulnerabilities.

    Reference:

    * https://arlimus.github.io/articles/usepam

Reference:

* https://unix.stackexchange.com/questions/193066/how-to-unlock-account-for-public-key-ssh-authorization-but-not-for-password-aut

## Debian ssh group no longer works

### ssh group now _ssh
**ssh** group migrated to **_ssh** in Trixie.

**ssh** group must be manually managed if used with existing users and groups,
or migrate users to **_ssh**.

Reference:

* https://salsa.debian.org/ssh-team/openssh/-/commit/18da782ebe789d0cf107a550e474ba6352e68911

## Enable Debug Mode
Print verbose messages to **/var/log/syslog** to help in debugging issues.

**/etc/default/ssh** (1)
{ .annotate }

1. 0644 root:root

``` bash
SSHD_OPTS=-ddd
```

``` bash
systemctl daemon-reload
service ssh restart
```

## Could not open authorized keys: Permission denied
The keyfile could not be accessed. This generally happens when SSHD drops
privileges to the user when logging in and the user cannot access the keyfile.

1. Directory containing keyfile is **readable** and **executable** by the user.
2. Keyfile is **0600**.
