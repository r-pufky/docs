# SSH Client


## Create Certificates
Use a [Yubikey GPG Key (Linux)][a] or [Yubikey GPG Key (Windows)][b].

Alternatively use a strong password on keys that is not your login password.

### [Generate 4096 bit RSA certificates & add user to SSH group][c]
``` bash
# Always use a strong password that is not a login password.
ssh-keygen -b 4096 -t rsa -f /home/{USER}/.ssh/{KEY_NAME}

# Add public key to any authorized_keys on any host to enable login.
# This is the published GPG identity for Yubikeys.
cat /home/{USER}/.ssh/{KEY_NAME}.pub >> home/{USER}/.ssh/authorized_keys

chmod 0600 /home/{USER}/.ssh/*
chmod 0640 /home/{USER}/.ssh/*.pub
addgroup {USER} _ssh
```

!!! note
    The private key **{KEY_NAME}** needs to be used to SSH into this host. Copy
    the public key **{KEY_NAME}.pub** to the **authorized_keys** on other hosts
    to be able to login to those hosts.

### Importing RSA Keys for Putty/WinSCP (Windows)

1. Copy RSA private key to windows computer.
2. ⌘ + r ➔ puttygen ➔ Conversions ➔ Import Key (Select Private Key)
3. Rename Key Comment to **user@server**.
4. Save private key in a **.ppk** file to local machine.
5. Delete RSA keys (use [sdelete64][d]).
6. Update public key in **authorized_keys** file with comment about key being
   used.


## Restricting SSH Tunneling
Restrict what local ports and IP's can be accessed via SSH tunneling.

!!! abstract "~/.ssh/authorized_keys"
    0600 {USER}:{USER}

    ``` bash
    # All on one line, comma separated with the public key cert afterwards.
    no-X11-forwarding,permitopen="localhost:80",permitopen="localhost:4243",permitopen="10.10.10.10:32400" {PUBKEY}
    # no-port-forwarding: Disable all port forwarding.
    # no-X11-forwarding: Disable X11 forwarding.
    # no-agent-forwarding: Disable agent forwarding.
    # permitopen: Explicitly allow port to be opened.
    #
    # Disable X11 forwarding but allow ports 80, 4243, 32400 to be forwarded.
    ```


## Forward ports through SSH connection
Useful for accessing services inside another network. May be specified multiple
times.

``` bash
# -L 1000:10.10.10.10:8888 - client: localhost:1000 -> host: 10.10.10.10:8888
ssl -L {LOCAL_PORT}:{INTERNAL_HOST}:{INTERNAL_PORT} user@example -p {PORT}
```


## [SSH Host Configuration][e]
Setup SSH to automatically select correct options when using hosts/shortcuts.

!!! abstract "~/.ssh/config"
    0600 {USER}:{USER}

    ``` bash
    # Autoselect github keys
    Host *.github.com github.com
      User {GITHUB_USERNAME}
      HostName *.github.com github.com
      Port 443
      PreferredAuthentications publickey
      IdentityFile ~/.ssh/github

    Host {CUSTOM_NAME}
      HostName {IP_OR_DNS}
      User {AUTH_USER}
      IdentityFile ~/.ssh/{CERT}
      BatchMode yes
      CheckHostIP no
      PasswordAuthentication no
      KbdInteractiveAuthentication no
      PreferredAuthentications publickey
      StrictHostKeyChecking no
      Port {PORT}
    ```

[a]: ../../app/gpg/os/linux.md#configure-sshgpg-agent
[b]: ../../app/gpg/os/windows.md#configure-gpg-agent
[c]: https://help.ubuntu.com/community/SSH/OpenSSH/Keys
[d]: https://docs.microsoft.com/en-us/sysinternals/downloads/sdelete
[e]: https://nerderati.com/2011/03/17/simplify-your-life-with-an-ssh-config-file
