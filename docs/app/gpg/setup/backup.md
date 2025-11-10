# Backup
Exporting subkeys will delete the key locally. Backing up **$GNUPGHOME** before
exporting enables exporting subkeys to multiple Yubikeys. Make your own
determination on if this security practice is acceptable to you.

!!! danger
    Ensure machine is **air-gapped** (no transmission devices on) during this
    step.

    Store on a (hardware) encrypted device.

## Confirm Key State
Ensure master and subkeys are created and locally stored before exporting.

!!! info
    The master and subkeys should be listed with no modifiers if properly setup
    to export to a key.

``` bash
gpg --list-keys

# > - indicates a key is exported to card already (ssb>).
# sec# - indicates only stubs created (a private cert on different machine).
```

## Export GPG Keys
Master and Subkeys will be encrypted with your passphrase when exported.

GPG Public key export can be used to manually import into other GPG clients if
you do not want to use key servers.

Export master, subkeys, and public key.
``` bash
gpg --armor --export-secret-keys $KEYID > $GPGBACKUP/private/$KEYID.master.asc
gpg --armor --export-secret-subkeys $KEYID > $GPGBACKUP/private/$KEYID.subkeys.asc
gpg --armor --export $KEYID > $GPGBACKUP/public/$KEYID.asc
cp $GNUPGHOME/openpgp-revocs.d/* $GPGBACKUP/private
```

Export SSH RSA public key.
``` bash
gpg --export-ssh-key $KEYID > $GPGBACKUP/public/$KEYID.ssh.pub
```

!!! note
    The SSH RSA Public Key comment will use the authentication short key ID
    (**openpgp:0xXXXXXXXX**). See [Linux](../os/linux.md) or
    [Windows](../os/windows.md) for importing keys.

    Reference:

    * https://lists.gnupg.org/pipermail/gnupg-devel/2016-January/030682.html

Backup GNUPG state for multiple Yubikey initializations.
``` bash
sudo cp -avi $GNUPGHOME $GPGBACKUP
```

## Publish Public Key
Export the public key to public key servers for GPG encrypt/decrypt/signing.
Without publishing you can still use SSH.

!!! danger
    Network is required for this step. Disable network immediately afterwards.

Export public key to https://keys.openpgp.org.
``` bash
gpg --keyserver hkps://keys.openpgp.org --send-key $KEYID
```

Reference:

* https://superuser.com/questions/227991/where-to-upload-pgp-public-key-are-keyservers-still-surviving
