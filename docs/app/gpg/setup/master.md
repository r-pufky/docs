# Master Key
The GPG Master Key is your digital identity and should be kept **offline** and
**encrypted** per [setup](README.md).

!!! danger
    Ensure machine is **air-gapped** (no transmission devices on) during this
    setup.


## Prepare Environment
Setup GPG to store configuration on encrypted storage and setup secure
cross-platform preferences.

Create directories on encrypted drive and setup environment variables.
``` bash
mkdir /media/user/KINGSTON/gnupghome

# Store respective key material in these folders.
mkdir -p /media/user/KINGSTON/backup/public /media/user/KINGSTON/backup/private

# Directs GPG where to find material.
export GNUPGHOME=/media/user/KINGSTON/gnupghome

# Directs GPG where to backup material.
export GPGBACKUP=/media/user/KINGSTON/backup
```

??? abstract "/media/user/KINGSTON/gnupghome/gpg.conf"
    0600 {USER}:{USER}

    ``` bash
    personal-cipher-preferences AES256 AES192 AES
    personal-digest-preferences SHA512 SHA384 SHA256
    default-preference-list SHA512 SHA384 SHA256 AES256 AES192 AES ZLIB BZIP2 ZIP Uncompressed
    cert-digest-algo SHA512
    s2k-digest-algo SHA512
    s2k-cipher-algo AES256
    charset utf-8
    fixed-list-mode
    no-comments
    no-emit-version
    keyid-format 0xlong
    list-options show-uid-validity
    verify-options show-uid-validity
    with-fingerprint
    require-cross-certification
    use-agent
    ```

??? info "gpg.conf explanation"
    * Require cipher AES 256, 192, 128.
    * Require digest SHA 512, 384, 256.
    * Public preferences for cipher/digest, compression.
    * Force our digest creation to SHA512.
    * Force our cipher to AES256.
    * Enable UTF-8 support (for cross platform usage).
    * Fixed list - use unixtimestamps for all timestamps and do not merge
      id/key.
    * Do not include comments in signature.
    * Do not include version in signature.
    * Require long hexidecimal keys.
    * Show UID validity for listing and verification options.
    * List fingerprints with keys.
    * Ensure cross certification on subkey is present and valid (prevents
      attack).
    * Enable smartcard use.


## Generate Strong Password
Generate a strong random password for use with the GPG master key. Doing
actions on the system will slowly increase the entropy pool.

!!! warning
    Use this password when generating the Master GPG Key below. Store it in a
    physically separate location from where the offline Master Key is stored.
    This **protects your digital identity**.

``` bash
# Ensure entropy pool is larger than 3000.
cat /proc/sys/kernel/random/entropy_avail

# Generate a random 64 bit ACSII safe sequence for GPG password.
gpg --gen-random --armor 0 64
```


## Create Master Key
Master key will **only** certify subkeys - it is **not** used directly to deal
with encryption material. This enables subkeys to be replaced when compromised
without needing to regenerate an entire GPG identity. Subkeys are for everyday
use.

!!! tip
    GPG 2.1 and higher will automatically create a revocation certificate in
    **$GNUPGHOME/openpgp-revocs.d**.

    Using the revocation certificate is better mechanism than an expiry date
    for [protecting the master key][a].

!!! warning "Comments are considered harmful"
    [Explicitly leave key comments blank][b]. All required information is
    included within the key itself and muddles the human readability of the
    key.

Generate a 4096bit RSA with authenticate (**certify**) abilities only.
``` bash
gpg --expert --full-generate-key
>
> Please select what kind of key you want:
>    (1) RSA and RSA (default)
>    (2) DSA and Elgamal
>    (3) DSA (sign only)
>    (4) RSA (sign only)
>    (7) DSA (set your own capabilities)
>    (8) RSA (set your own capabilities)
>    (9) ECC and ECC
>   (10) ECC (sign only)
>   (11) ECC (set your own capabilities)
>   (13) Existing key

Your selection? 8  # Create RSA 2096 bit key.

> Possible actions for a RSA key: Sign Certify Encrypt Authenticate
> Current allowed actions: Sign Certify Encrypt
>
>   (S) Toggle the sign capability
>   (E) Toggle the encrypt capability
>   (A) Toggle the authenticate capability
>   (Q) Finished

Your selection? =c  # Force certify only.

> RSA keys may be between 1024 and 4096 bits long.

What keysize do you want? (2048) 4096

> Requested keysize is 4096 bits
> Please specify how long the key should be valid.
>          0 = key does not expire
>       <n>  = key expires in n days
>       <n>w = key expires in n weeks
>       <n>m = key expires in n months
>       <n>y = key expires in n years

Key is valid for? (0) 0  # Do not expire.

> Key does not expire at all

Is this correct? (y/N) y

# Set GPG identity.
> GnuPG needs to construct a user ID to identify your key.

Real name: {USER FIRST NAME} {USER LAST NAME}
Email address: {GPG USER EMAIL ADDRESS}
Comment: {PRESS ENTER}

> You selected this USER-ID:
>     "FIRST LAST <EMAIL>"

Change (N)ame, (C)omment, (E)mail or (O)kay/(Q)uit? o

# Password generated above.
> You need a Passphrase to protect your secret key.

Enter passphrase: {GPG PASSWORD}
Repeat passphrase: {GPG PASSWORD}

> We need to generate a lot of random bytes. It is a good idea to perform
> some other action (type on the keyboard, move the mouse, utilize the
> disks) during the prime generation; this gives the random number
> generator a better chance to gain enough entropy.
>
> gpg: /media/user/KINGSTON/gnupghome/trustdb.gpg: trustdb created
> gpg: key ################ marked as ultimately trusted
> gpg: directory '/media/user/KINGSTON/gnupghome/openpgp-revocs.d' created
> gpg: revocation certificate stored as '/media/user/KINGSTON/gnupghome/openpgp-revocs.d/########################################.rev'
> public and secret key created and signed.
>
> pub   rsa4096/################ 2019-01-01 [C]
>       Key fingerprint = #### #### #### #### ####  #### #### #### #### ####
> uid                              FIRST LAST <EMAIL>

# Revocation certificate will be listed in output.
# Master Key ID will be listed under 'pub  rsa4096/################'.
```
  * See [Troubleshooting](../troubleshooting.md) if an error occurs.

Export master key ID to bash environment for easy reference later.
``` bash
export KEYID=################
```


## Add [Photo to Master Key (Optional)][c]
A photo to help confirm your identity (typically a head shot); this is added to
your GPG key for additional verification in person.

Create a **240x288 JPEG** photo (max **6144 bytes**) with metadata information
removed.

``` bash
gpg --edit-key $KEYID
gpg> addphoto

> Pick an image to use for your photo ID. The image must be a JPEG file.
> Remember that the image is stored within your public key. If you use a very
> large picture, your key will become very large as well! Keeping the image
> close to 240x288 is a good size to use.

Enter JPEG filename for photo ID: photo.jpg
Is this correct? (y/N) y

gpg> save
```


## Add Additional Identities (Optional)
Associate additional metadata to GPG key, useful if you have multiple emails,
etc. The **primary** ID is the main identity used for the GPG key. This can be
any identity that has been configured, in this case **1**.

!!! warning "Comments are considered harmful"
    [Explicitly leave key comments blank][b]. All required information is included
    within the key itself and muddles the human readability of the key.

``` bash
$ gpg --edit-key $KEYID
gpg> adduid

Real name: {USER FIRST NAME} {USER LAST NAME}
Email address: {GPG USER EMAIL ADDRESS}
Comment: {PRESS ENTER}

> You selected this USER-ID:
>     "FIRST LAST <EMAIL>"

Change (N)ame, (C)omment, (E)mail or (O)kay/(Q)uit? o

gpg> uid 1
gpg> primary
gpg> save
```


## Sign New Key with Existing Key (Optional)
This will extend the chain of trust and prove that the new key is controlled by
your original key (you). Useful for when the master key is compromised or
expired.

The new key is exported and signed by the old key, then published.
``` bash
gpg --export-secret-keys --armor --output /tmp/new-gpg-key.asc
gpg --default-key $OLDKEY --sign-key $KEYID
```

[a]: https://security.stackexchange.com/questions/14718/does-openpgp-key-expiration-add-to-security/79386
[b]: https://web.archive.org/web/20130730162915/https://debian-administration.org/users/dkg/weblog/97
[c]: https://blog.josefsson.org/2014/06/19/creating-a-small-jpeg-photo-for-your-openpgp-key
