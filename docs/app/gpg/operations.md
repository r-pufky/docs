# [Operations][a]
!!! note
    If you are encrypting files for yourself, use your email address associated
    with your public key as the recipient.


## Import
If the public key is not your own and cannot be found on key servers, it must
be manually imported.

``` bash
#Import a public key from a file.
gpg --import {KEY FILE}

# Import a public key from a key server.
gpg --recv {KEYID}
```


## Export
The public key can be exported as well for others to encrypt data for you.

Export public key for signing data.
``` bash
gpg --homedir /some/custom/.gnupg --armor --export > my_public_key.gpg
```


## Encrypt
Encrypt a file for a given recipient.
``` bash
# Trust model always prevents GPG warnings about untrusted key recipients.
gpg --armor --batch --trust-model always --encrypt --recipient {GPGID} {FILE}

# Encrypt some text
echo -n "super_secret_server_stuff" | gpg --armor --batch --trust-model always --encrypt --recipient {GPGID}
```


## Create a Detached Signature
This is used to validate that the GPG encrypted file has not been changed.

Create a detached signature for a given file.
``` bash
gpg --detach-sign {FILE}.gpg
```


## Validate File Using Detached Signature
``` bash
# Import the public key if needed.
gpg --import {PUBLIC KEY}

# Verify the GPG encrypted file.
gpg --verify {FILE}.sig
```

[a]: https://gnupg.org/documentation/manpage.html
