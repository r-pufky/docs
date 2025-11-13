# Export to Yubikey
Exports GPG subkeys to Yubikey so master key can remain offline while still
using GPG keys.


## Understanding How Yubikeys Work
Read the [technical manual][a] to understand how Yubikeys work. This will setup
the Yubikey to use the **CCID** interface to setup **openpgp** on the key.

[Yubikey manager][b] is an application that is used to manage the Yubikey
itself (**ykman**) and sets *how* applets are used on the key. The
configuration of the applets themselves are managed by respective apps, in this
case **GPG**.

![Yubikey Concept](yubikey_concept.png)

**ykman** will set preferences like number of applet PIN attempts, PINs, and
touch preferences.

**gpg --edit-card** will set openpgp configuration, like PGP name, login, url.


## Export Subkeys to Yubikeys
!!! danger
    Exporting keys to Yubikey will **destroy** the local key. Ensure a backup
    has been made so original state can be restored. See [Backup](backup.md)
    and [Restore Original GPG State](#restore-original-gpg-state) respectively.

!!! tip
    Key selection is a toggle, ensure to only export *one* key at a time; this
    is denoted by a *.

    First Password: GPG private key password.

    Second Password: Yubikey user [PIN][c].

### Load signing key to Yubikey
``` bash
gpg --edit-key $KEYID
gpg> key 1

> sec  rsa4096/################
>      created: 2019-01-01  expires: never       usage: C
>      trust: ultimate      validity: ultimate
> ssb* rsa4096/################
>      created: 2019-01-01  expires: never       usage: S
> ssb  rsa4096/################
>      created: 2019-01-01  expires: never       usage: E
> ssb  rsa4096/################
>      created: 2019-01-01  expires: never       usage: A
> [ultimate] (1). FIRST LAST <EMAIL>

gpg> keytocard

> Please select where to store the key:
>    (1) Signature key
>    (3) Authentication key

Your selection? 1

> You need a passphrase to unlock the secret key for user: "FIRST LAST <EMAIL>"
> 4096-bit RSA key, ID ################, created 2019-01-01

gpg> save
```

### Load encryption key to Yubikey
``` bash
gpg --edit-key $KEYID
gpg> key 2

> sec  rsa4096/################
>      created: 2019-01-01  expires: never       usage: C
>      trust: ultimate      validity: ultimate
> ssb  rsa4096/################
>      created: 2019-01-01  expires: never       usage: S
> ssb* rsa4096/################
>      created: 2019-01-01  expires: never       usage: E
> ssb  rsa4096/################
>      created: 2019-01-01  expires: never       usage: A
> [ultimate] (1). FIRST LAST <EMAIL>

gpg> keytocard

> Please select where to store the key:
>    (2) Encryption key

Your selection? 2

> You need a passphrase to unlock the secret key for user: "FIRST LAST <EMAIL>"
> 4096-bit RSA key, ID ################, created 2019-01-01

gpg> save
```

### Load authentication key to Yubikey
``` bash
gpg --edit-key $KEYID
gpg> key 3

> sec  rsa4096/################
>      created: 2019-01-01  expires: never       usage: C
>      trust: ultimate      validity: ultimate
> ssb  rsa4096/################
>      created: 2019-01-01  expires: never       usage: S
> ssb  rsa4096/################
>      created: 2019-01-01  expires: never       usage: E
> ssb* rsa4096/################
>      created: 2019-01-01  expires: never       usage: A
> [ultimate] (1). FIRST LAST <EMAIL>

gpg> keytocard

> Please select where to store the key:
>    (3) Authentication key

Your selection? 3

> You need a passphrase to unlock the secret key for user: "FIRST LAST <EMAIL>"
> 4096-bit RSA key, ID ################, created 2019-01-01

gpg> save
```


## Verify subkeys are Offloaded
``` bash
gpg --list-secret-keys

# > - Offloaded keys will have > next to the key (key is on card).
```


## Restore Original GPG State
The original GPG state needs to be reloaded to export Subkeys to additional
Yubikeys, or to keep a pristine copy of GPG key data on encrypted storage.

``` bash
cp -avi $GPGBACKUP/* $GNUPGHOME
```

[a]: https://support.yubico.com/hc/en-us/articles/360016614900-YubiKey-5-Series-Technical-Manual
[b]: https://developers.yubico.com/yubikey-manager
[c]: ../../../glossary/yubikey.md#yubikey-passwordpin