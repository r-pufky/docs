# Troubleshooting


## [SSH pubkey authentication with locked accounts does not work][a]
Locked accounts cannot SSH pubkey auth.  SSH now distinguishes between ! and *
password locking.

*: Lock password - allow SSH pubkey auth.

!: Lock password - deny SSH pubkey auth.

Any other means to lock the password will result in SSH pubkey failures.

!!! danger
    [Do NOT set **UsePam=yes**][b] as this leads to security vulnerabilities.


## Debian ssh group no longer works

### [ssh group now _ssh][c]
**ssh** group migrated to **_ssh** in Trixie.

**ssh** group must be manually managed if used with existing users and groups,
or migrate users to **_ssh**.


## Enable Debug Mode
Print verbose messages to **/var/log/syslog** to help in debugging issues.

!!! abstract "/etc/default/ssh"
    0644 root:root

    ``` bash
    SSHD_OPTS=-ddd
    ```

``` bash
systemctl daemon-reload
service ssh restart
```

!!! note
    After a login attempt, the service may need to be restarted to test again.

    Check `**/var/log/syslog** for debug information.


## Could not open authorized keys: Permission denied
The keyfile could not be accessed. This generally happens when SSHD drops
privileges to the user when logging in and the user cannot access the keyfile.

1. Directory containing keyfile is **readable** and **executable** by the user.
2. Keyfile is **0600**.


## [GPG pinentry not redirecting to correct terminal][d]
GPG connect agent must be informed when on a new terminal.

Manually
``` bash
gpg-connect-agent updatestartuptty /bye
```

!!! abstract "~/.ssh/config"
    0640 {USER}:{USER}

    ``` bash
    Match host * exec "gpg-connect-agent updatestartuptty /bye"
    ```

[a]: https://unix.stackexchange.com/questions/193066/how-to-unlock-account-for-public-key-ssh-authorization-but-not-for-password-aut
[b]: https://arlimus.github.io/articles/usepam
[c]: https://salsa.debian.org/ssh-team/openssh/-/commit/18da782ebe789d0cf107a550e474ba6352e68911
[d]: https://unix.stackexchange.com/questions/280879/how-to-get-pinentry-curses-to-start-on-the-correct-tty
