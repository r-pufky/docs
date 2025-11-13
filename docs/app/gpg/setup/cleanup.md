# Cleanup
Manually verify this information to ensure you do not accidentally lose data or
access/control to your GPG identity.


## Verify

1. Encrypted Media has the following:
    * **$GPGBACKUP/private/$KEYID.master.asc**
    * **$GPGBACKUP/private/$KEYID.subkeys.asc**
    * **$GPGBACKUP/private/$KEYID.rev**
    * **$GPGBACKUP/public/$KEYID.asc**
    * **$GPGBACKUP/public/$KEYID.ssh.pub**

2. A backup of GPG Master Key (with all keys locally present):

    **$GPGBACKUP/gnupghome**

3. Your Master Key password is stored **away** from your encrypted media in a
   controlled space.
4. Your Encrypted Media password is stored **away** from your encrypted media
   in a controlled space.
5. **The encrypted media is stored offline in a controlled space.**
6. The public keys are stored or published and are readily accessible.

    **$GPGBACKUP/public/***

7. It is generally a good idea to print a copy of the revocation certificate and
   give it to a trusted third-party.

## Secure Delete Secret Material
Securely remove any secret GPG material.

If you are using a Live OS, just reboot. If you're paranoid, wipe the live OS
drive.

If not using a live OS, wipe private key material **after** you confirm it is
backed up.

``` bash
sudo srm -r $GNUPGHOME || sudo rm -rf $GNUPGHOME
sudo srm -r $GPGBACKUP || sudo rm -rf $GPGBACKUP
gpg --delete-secret-key $KEYID
```
