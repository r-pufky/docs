SSH Configurations
------------------
End-user SSH typically SSH configuration needs. If you need to setup an SSH
service, see [SSH Service](#ssh-service.md)

1. [Generate RSA Keys](#generate-rsa-keys)
1. [Add Public Key to Authorized Keys for Use](#add-public-key-to-authorized-keys-for-use)
1. [Restricting SSH Tunneling](#restricting-ssh-tunneling)
1. [SSH Host Configuration](#ssh-host-configuration)
1. [Importing RSA keys for Putty/WinSCP on Windows](#Importing-rsa-keys-for-putty-winscp-on-Windows)
1. [References](#references)

Generate RSA Keys
-----------------
Always use a strong password on keys, that isn't your login password.

```bash
ssh-keygen -b 4096 -t rsa -f <keyname>
chmod 0600 <keyname>
chmod 0640 <keyname>.pub
```

Add Public Key to Authorized Keys for Use
-----------------------------------------

```bash
cat <keyname>.pub >> ~/.ssh/authorized_keys
```

Restricting SSH Tunneling
-------------------------
Restrict what local ports and IP's can be accessed via SSH tunneling.

All on one line, comma separated with the public key cert afterwards.

 * `no-port-forwarding`: disable all port forwarding
 * `no-X11-forwarding`: disable X11 forwarding
 * `no-agent-forwarding`: disable agent forwarding
 * `permitopen`: explicitly allow port to be opened

Disable X11 forwarding but allow ports 80,4243,32400 to be forwarded.
~/.ssh/authorized_keys
```bash
no-X11-forwarding,permitopen="localhost:80",permitopen="localhost:4243",permitopen="10.10.10.10:32400" <PUBKEY DUMP>
```

Allow connection, disable all forwarding.
~/ssh/authorized_keys
```bash
no-port-forwarding <PUBKEY DUMP>
```

SSH Host Configuration
----------------------
Setup SSH to automatically select correct options when using hosts/shortcuts.
See [detailed explanation][3] on `config` file.

~/.ssh/config
```bash
# Autoselect github keys
Host *.github.com github.com
  User <github username>
  HostName *.github.com github.com
  Port 443
  PreferredAuthentications publickey
  IdentityFile ~/.ssh/github

Host <CUSTOM_NAME>
  HostName <HOST_IP_OR_DNS>
  User <USER_TO_AUTH_AS>
  IdentityFile ~/.ssh/<CERT_TO_USE>
  BatchMode yes
  CheckHostIP no
  PasswordAuthentication no
  KbdInteractiveAuthentication no
  PreferredAuthentications publickey
  StrictHostKeyChecking no
  Port <SSH_SERVER_PORT>
```

Importing RSA keys for Putty/WinSCP on Windows
----------------------------------------------
 * Copy RSA private key to windows computer
 * ```win + r > puttygen```
 * ```File > Load Private Key (Select RSA Private Key)```
 * Rename Key Comment to user@server
 * Save private key as `RSA 4096` in a `.ppk` to local machine
 * Delete RSA keys (use [`sdelete64`][1])
 * Update public key in `authorized_keys` file with comment about key being used

References
----------
[Using puttygen to convert RSA public keys for WinSCP authentication][2]

[1]: https://docs.microsoft.com/en-us/sysinternals/downloads/sdelete
[2]: http://winscp.net/eng/docs/ui_puttygen
[3]: https://nerderati.com/2011/03/17/simplify-your-life-with-an-ssh-config-file/