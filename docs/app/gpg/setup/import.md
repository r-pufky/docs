# Import Public Key
This will set ultimate trust for the [GPG Master Public
Key](https://stackoverflow.com/questions/31784368/how-to-give-highest-trust-level-to-an-openpgp-certificate-in-kleopatra)
certificate you created when backing up GPG state. Any of one these options
below can be used.

!!! tip
    Besides the locally exported public key file option, both other options
    assume that the public key has been published to key servers. Yubikey can
    [automatically import](https://withinboredom.info/blog/2017/11/18/signing-commits-ssh-with-yubikey-and-windows/)
    the correct certificate assuming the key was setup correctly. See [GPG
    Publish Key](backup.md#publish-public-key).

## GPG Public Key from File
``` bash
gpg --import YOUR_PUBLIC_GPG_KEY.asc

> gpg: key 0x################: public key "FIRST LAST <EMAIL>" imported
> gpg: Total number processed: 1
> gpg:               imported: 1

GPG Public Key from Keyserver.
``` bash
gpg --receive-keys $KEYID  --keyserver hkps://keys.openpgp.org

> gpg: requesting key 0x################ from hkps server pgp.mit.edu
> [...]
> gpg: key 0x################: public key "FIRST LAST <EMAIL>" imported
> gpg: Total number processed: 1
> gpg:               imported: 1
```

## GPG Public Key from Yubikey URL
``` bash
gpg --card-edit
gpg/card> fetch

> gpg: requesting key from 'https://keys.openpgp.org/vks/v1/by-fingerprint/{KEYID}'
> gpg: key ################: public key "FIRST LAST <EMAIL>" imported
> gpg: Total number processed: 1
> gpg:               imported: 1
```

## Trust GPG Public Key Locally
Each machine on which the signing, encryption and authentication certificates
are used must trust the GPG Master Public key to prevent errors.

Set Ultimate Trust for GPG Master Public Key.
``` bash
gpg --edit-key $KEYID  # Use imported public key ID.
gpg> trust

> pub# rsa4096/################
>      created: 2019-01-01  expires: never       usage: C
>      trust: unknown       validity: unknown
> sub> rsa4096/################
>      created: 2019-01-01  expires: never       usage: S
> sub> rsa4096/################
>      created: 2019-01-01  expires: never       usage: E
> sub> rsa4096/################
>      created: 2019-01-01  expires: never       usage: A
>
> Please decide how far you trust this user to correctly verify other users keys
> (by looking at passports, checking fingerprints from different sources, etc.)
>
>   1 = I don't know or won't say
>   2 = I do NOT trust
>   3 = I trust marginally
>   4 = I trust fully
>   5 = I trust ultimately
>   m = back to the main menu

Your decision? 5
Do you really want to set this key to ultimate trust? (y/N) y

> pub# rsa4096/################
>      created: 2019-01-01  expires: never       usage: C
>      trust: ultimate      validity: ultimate
> sub> rsa4096/################
>      created: 2019-01-01  expires: never       usage: S
> sub> rsa4096/################
>      created: 2019-01-01  expires: never       usage: E
> sub> rsa4096/################
>      created: 2019-01-01  expires: never       usage: A

gpg> save

# # - Certificate not on machine.
# > - Certificate on Yubikey.
gpg --list-secret-keys

> /home/{USER}/.gnupg/pubring.kbx
> -------------------------------
> sec#  rsa4096 2019-01-01 [C]
>       ########################################
> uid           [ultimate] FIRST LAST <EMAIL>
> uid           [ultimate] [jpeg image of size 5877]
> ssb>  rsa4096 2019-01-01 [S]
> ssb>  rsa4096 2019-01-01 [E]
> ssb>  rsa4096 2019-01-01 [A]
```
