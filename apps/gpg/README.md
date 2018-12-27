Using GPG with multiple Yubikeys.

Great detailed step-by-step [security-focused instructions are here][1]. These
instructions are an abbreviated version, which also includes a photo for your
GPG master key. See [instructions above][1] for detailed walkthrough.

Required Materials
------------------
1. Tails Live USB [Setup instructions][5].
1. Hardware-backed Encrypted USB drive [Ironkey][6] (preferred), or USB drive
   with software encryption [using VeraCrypt][7] (less-preferred).
1. Yubikey (or other hardware security key support 4096bit RSA certificates)
   [nano][8] or [5][9].
1. Copy of these instructions or secondary device Internet access.
1. A photo to associate with your GPG master key.

This assumes usage of an Ironkey with Yubikeys.

Tails Setup
-----------
GPG generation should be done on a air-gapped, temporal, encrypted OS to
minimize secret key exposure.

1. On login, click `+`, setup temporary _root_ password.
1. Ensure wifi is disabled (upper-right).
1. Open browser, click on `IRONKEY` to automount to `/media/amnesia/IRONKEY`.

### Reset Ironkey
Do this if fresh Ironkey, or creating a new master key. **Data destructive**.

Initalize Device
```bash
/media/amnesia/IRONKEY/linux/linux64/ikd300_initalize
```
* Only needed on first use.

Reset Device
```bash
/media/amnesia/IRONKEY/linux/linux64/ikd300_reset
```
* Max 16 character password.

### Unlock Ironkey
```bash
sudo /media/amnesia/IRONKEY/linux/linux64/ikd300_login
```
* Open browser, click on `KINGSTON` to automount to `/media/amnesia/KINGSTON`.
* This is your hardware-backed encrypted storage.

GnuPG Configuration
-------------------
Setup GPG to store configuration on encrypted storage and setup secure
cross-platform preferences.

### Create Base Directory Structure
```bash
mkdir /media/amnesia/KINGSTON/gnupghome
mkdir /media/amnesia/KINGSTON/gnupgbackup
export GNUPGHOME=/media/amnesia/KINGSTON/gnupghome
export GPGBACKUP=/media/amnesia/KINGSTON/gnupgbackup
```

/media/amnesia/KINGSTON/gnupghome/gpg.conf
```bash
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
* Require cipher AES 256, 192, 128.
* Require digest SHA 512, 384, 256.
* Public preferences for cipher/digest, compression.
* Force our digest creation to SHA512.
* Force our cipher to AES256.
* Enable UTF-8 support (for cross platform usage).
* Fixed list - use unixtimestamps for all timestamps and do not merge id/key.
* Do not include comments in signature.
* Do not include version in signature.
* Require long hexidecimal keys.
* Show UID validity for listing and verification options.
* List fingerprints with keys.
* Ensure cross certification on subkey is present and valid (prevents attack).
* Enable smartcard use.

### Ensure Entropy is High & Generate password
Generate a strongly-random password for use with the GPG master key.

Ensure entropy pool is larger than 3000.
```bash
cat /proc/sys/kernel/random/entropy_avail
```
* Doing actions on the system will increase this.

```bash
gpg --gen-random -a 0 64
```
* Generate a random 64 bit sequence to use for password.
* `--armor` will make the binary ASCII safe.

Generate Master Key
-------------------
Create your GPG master key. GPG 2.1 and higher will automatically create a
revocation certificate in `$GNUPGHOME/openpgp-revocs.d`; using the revocation
certificate is better mechanism than an expiry date for [protecting the master
key][11].

```bash
gpg --full-generate-key
```
1. Select `4` "(4) RSA (sign only)".
1. `4096` bit keysize.
1. Select `0` "0 = key does not expire".
1. Select `y` to Confirm correct values.
1. name: `first last`.
1. email: `email`.
1. comment: [`BLANK`][10].
1. Select `o` "(O)kay" to confirm identity.

Export the master key ID for easier manipulations
* `Revocation Certificate` will be listed in output.
* Master Key ID will be listed under `pub  rsa4096/0x################`.

```bash
export KEYID=0x################
```

### Add Photo to Master Key
Typically a headshot photo to help confirm your identity; this is added to your
GPG key for additional verification.

Create a **240x288 JPEG** photo (max **6144** bytes) with metadata information
removed, [instructions here.][3]

```bash
gpg --edit-key $KEYID
```
1. `addphoto`.
1. Enter filename `photo.jpg` (may not be displayed if no program installed).
1. Select `y` for correct photo.
1. `save`.

### Add Additional Identities
Useful if you have multiple emails used, etc.

```bash
gpg --edit-key $KEYID
```
1. `adduid`.
1. name: `first last`.
1. email: `email`.
1. comment: [`BLANK`][10].
1. Select `o` `(O)kay` to confirm identity.
1. `uid 1` to select the first identity.
1. `primary` to set _uid 1_ as primary identity.
1. `save`.

### Create Signing, Encryption & Authentication Subkeys
Subkeys are issued from the master key and are used for specific actions
essentially 'on behalf of' the master identity. These subkeys are loaded onto
Yubukeys for everyday use. As they are subkeys, these can be revoked as needed
or the master key can be revoked/changed to invalidate all subkeys at once.

Only export **one** key at a time. GPG uses a toggling system to select which
key to export.

```bash
gpg --expert --edit-key $KEYID
```
* Remember to `save` and `quit` when done.

#### Signing Key
Cryptographically sign your data.

1. `addkey`.
1. Select `4` "(4) RSA (sign only)".
1. `4096` bit keysize.
1. Select `0` "0 = key does not expire".
1. Select `y` to Confirm correct values.

#### Encryption Key
Encrypt your data.

1. `addkey`.
1. Select `6` "(6) RSA (encrypt only)".
1. `4096` bit keysize.
1. Select `0` "0 = key does not expire".
1. Select `y` to Confirm correct values.

#### Authentication Key
Authenicate to systems (e.g. SSH).

1. `addkey`.
1. Select `8` "(8) RSA (set your own capabilities)".
1. Select `s e a` to toggle signing/encryption off and authentication on.
1. Select `q` after confirming this is only set to "authentication".
1. `4096` bit keysize.
1. Select `0` "0 = key does not expire".
1. Select `y` to Confirm correct values.

### Verify Key
This will verify the key format is correct and highlight any potential issues.

```bash
gpg --export $KEYID | hokey lint
```
* _Red_ text indicates potential problems. Non-expiring keys will be marked as
  red; setting expiry is based on your security decisions.
* _Orange_ text indicates warnings. This is typically seen for
  cross-certification for the authentication key. GPG subkey does not sign and
  so does not need to be cross-certified.

Export GPG Keys & Backup
------------------------
Exporting subkeys to a Yubukey device will delete the key locally. Backing up
`$GNUPGHOME` before exporting will allow the creation of multiple Yubukeys with
the same subkeys. Make your own determination on if this security practice is
acceptable to you.

**Store on a (hardware) encrypted device.**

### Confirm Key State on Keyring
Ensure master and subkeys are created and locally stored before exporting.

```bash
gpg --list-keys $GNUPGHOME/pubring.gpg
gpg --list-secret-keys $GNUPGHOME/secring.gpg
```
* `>` indicates a key is exported to card already (e.g. 'ssb>').
* `sec#` indicates only stubs created, not subkeys.
* The master and subkeys should be listed if properly setup.

### Export Keys
The Master and sub-keys will be encrypted with your passphrase when exported.
```bash
mkdir /media/amnesia/KINGSTON/gnupghome/backup
export KEYBACKUP=/media/amnesia/KINGSTON/gnupghome/backup
gpg --armor --export-secret-keys $KEYID > $KEYBACKUP/master.key
gpg --armor --export-secret-subkeys $KEYID > $KEYBACKUP/sub.key
```

### Backup GNUPG
Backup GNUPG state for multiple Yubukey initalizations.
```bash
mkdir /media/amnesia/KINGSTON/gnupgbackup
export GPGBACKUP=/media/amnesia/KINGSTON/gnupgbackup
sudo cp -avi $GNUPGHOME $GPGBACKUP
```

Export Subkeys to Yubikeys
--------------------------

### Initalize Yubikey
Confirm Yubukey status.

Default `PIN` is **123456** and default `admin PIN` is **12345678**. PINs may be
up to 127 ASCII characters long.

If the device is not new follow [these instructions][15] to wipe the device and
start new.

```bash
gpg --card-status
```
* If not found, re-insert the key. There is a known race condition that may
  occur with older gpg libraries.
* Ensure firmware version `3.1.8` or later using [Yubukey manager][14] or
  [commandline tool][13].
* Ensure device is in `OTP/CCID` or `CCID` mode  using [Yubukey manager][14] or
  [commandline tool][13].

The PINs may be changed after loading the keys to card to make it quicker, if
not concerned about default PINs when loading.
```bash
gpg --card-edit
```
1. `admin` to enter administration mode.
1. `passwd` to enter PIN password change mode.
1. `3` to change admin PIN. Be sure to enter the _initial_ **12345678** pin
   first.
1. `1` to change PIN. Be sure to enter the _initial_ **123456** pin first.
1. `q` to return to main menu.
1. `name` to set owners first and last name.
1. surname: `last`.
1. given name: `first`.
1. `lang`.
1. `en` to set the preferred language.
1. `login` to set account name.
1. account name: `email`.
1. Press `enter` to see updated information.
1. `quit`.

### Load Subkeys to Yubikey
This is **data destructive** for local subkeys. Ensure a backup has been made
before doing this. See [Export GPG Keys & Backup](#export-gpg-Keys--backup).

```bash
gpg --edit-key $KEYID
```
* Key selection is a toggle action, ensure to only export _one_ key at a time.
* Remember to `save` and `quit` when done.

#### Load Signing Key
1. `key 1` (ensure _*_ only appears next to signing key).
1. `keytocard` to export key.
1. Select `1` "(1) Signature key".
1. `key 1` to deselect key.

#### Load Encryption Key
1. 'key 2' (ensure _*_ only appears next to encryption key).
1. `keytocard` to export key.
1. Select `2` "(2) Encryption key".
1. `key 2` to deselect key.

#### Load Authentication Key
1. 'key 3' (ensure _*_ only appears next to authentication key).
1. `keytocard` to export key.
1. Select `3` "(3) Authentication key".
1. `key 3` to deselect key.

### Verify Subkeys Loaded
Ensure keys are offloaded to the Yubukey. Offloaded keys will have `>` next to
the key, showing that the key is on the card.

```bash
gpg --list-secret-keys
```

### Multiple Yubikeys
The original GPG state needs to be reloaded to export subkeys to additional
Yuibkeys. If not exporting to additional keys, this step may be skipped.

```bash
cp -avi $GPGBACKUP $GNUPGHOME
```
* Repeat the steps in this section to export to another key.

Publish Public Key
------------------
Export the public key to public keyservers for GPG encrypt/decrypt/signing.
Without publishing you can still use SSH.

```bash
gpg --armor --export $KEYID > /media/UNENCRYPTED_USB_KEY/pubkey.gpg
```

Export to [SKS keyservers][4]
```bash
gpg --send-key $KEYID
gpg --send-key $KEYID --keyserver pgp.mit.edu
gpg --send-key $KEYID --keyserver keys.gnupg.net
```
* This will export to major keyservers. These are all syncronized however so
  only a single server is needed.
* Also consider exporting public key to [keybase.io](http://keybase.io).

### Cleanup
Make sure your private info remains private. Confirm that
* Yubikey has Encryption, Signing and Authentication subkeys.
* Yubikey PINs are **not default PINS**.
* Password for Master Key is safe.
* Master Key, Subkeys and revocation certificates are stored on **encrypted**
  device stored **offline**. **Do not access in unsecured environment.***
* Password for encryption device is saved, and stored in a **different**
  location.
* Public key is saved somewhere easily accessible.

Just reboot if using **tails** or a live image.

Otherwise securely delete private data
```bash
sudo srm -r $GNUPGHOME || sudo rm -rf $GNUPGHOME
sudo srm -r $GPGBACKUP || sudo rm -rf $GPGBACKUP
gpg --delete-secret-key $KEYID
```

[1]: https://github.com/drduh/YubiKey-Guide
[2]: https://codingnest.com/how-to-use-gpg-with-Yubukey-wsl/
[3]: http://blog.josefsson.org/2014/06/19/creating-a-small-jpeg-photo-for-your-openpgp-key/
[4]: https://superuser.com/questions/227991/where-to-upload-pgp-public-key-are-keyservers-still-surviving
[5]: https://tails.boum.org/install/win/usb-download/index.en.html
[6]: https://www.kingston.com/us/usb/encrypted_security/IKD300
[7]: https://github.com/drduh/YubiKey-Guide#backup-keys
[8]: https://www.yubico.com/product/Yubukey-5-nano/#Yubukey-5-nano
[9]: https://www.yubico.com/product/Yubukey-5-nfc/#Yubukey-5-nfc
[10]: https://debian-administration.org/users/dkg/weblog/97
[11]: https://security.stackexchange.com/questions/14718/does-openpgp-key-expiration-add-to-security/79386
[12]: https://support.yubico.com/support/solutions/articles/15000006420-using-your-Yubukey-with-openpgp
[13]: https://developers.yubico.com/Yubukey-personalization/
[14]: https://www.yubico.com/products/services-software/download/Yubukey-manager/
[15]: https://developers.yubico.com/PIV/Guides/Device_setup.html