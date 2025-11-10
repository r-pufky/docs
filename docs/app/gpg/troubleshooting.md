# Troubleshooting

## No agent running error
gpg-agent can sometimes die in the background, just restart it.

``` bash
gpg-agent --daemon
```

## agent_genkey failed: permission denied
Security measure; this means that the terminal you are using is not owned by you
and therefore GPG has aborted instead of continuing. Frequently happens if
running over SSH.

Set proper terminal ownership.
``` bash
ls -la $(tty)
> crw-rw----. 1 otheruser tty 4, 1 Jan 19 18:47 /dev/pts/9

sudo chown {USER} /dev/pts/9
```

Reference:

* https://blog.ijun.org/2017/05/gpg-agentgenkey-failed-permission-denied.html

## Yubikey Not Appearing
gpg-agent can lose the key if the daemon was restarted in the background or if
the Yubikey is not seated properly.

``` bash
# Re-insert the Yubikey, then run command to verify key returns data.
gpg --card-status
```

## SSH connection failed, Server sent: publickey
SSH public key not provided or was not matched on the server.

1. SSH public key is not loaded on the SSH server. Confirm your GPG public SSH
   key (see [GPG Export Keys](setup/export_to_yubikey.md)) is added to
   **~/.ssh/authorized_keys** for the user you are attempting to login with.
2. GPG agent configuration is not reloaded. Ensure SSH and Putty support in
   configuration is set, **gpg-agent**, and **gpg-connect-agent** are both
   restarted. See [Configure GPG Agent](os/windows.md#configure-gpg-agent).

## Please insert card with serial number
Original key used for authentication is not the key being used now.

![Pinentry Wrong Key](pinentry_wrong_key.png)

GPG Agent caches the serial number of the card for the KeyStub used. This just
needs to be removed.

``` bash
# Show all keygrips in GPG, these will be used to match cache in private store.
gpg --with-keygrip --list-keys

# Identify keygrip in private-keys-v1.d and delete it, or you can just remove
# all keys in that directory.
rm %appdata%\gnupg\private-keys-v1.d\{KEY}  # Windows.
rm ~/.gnupg/private-keys-v1.d  # Linux.
```

Reference:

* https://security.stackexchange.com/questions/165286/how-to-use-multiple-smart-cards-with-gnupg
