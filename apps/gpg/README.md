Using GPG with multiple Yubikeys
--------------------------------
1. [Windows GPG Yubikey Setup](windows.md)

This document details setting up a GPG Master Key with a photo, and
sub-documents detail Yubikey conifguration and platform setups.

Core (out of date) [instructions are here][1]. Additional step-by-step
walkthrough instructions for configuring [multi-platform GPG/Yubikey SSH usage
are here][16].

Required Materials
------------------
1. Live USB OS, with persistent storage to setup additional packages. Tails Live
   USB [Setup instructions][5] is preferred (most secure), other [live USB][22]
   will work but be less secure. Instructions assume Debian-based system.
1. Hardware-backed Encrypted USB drive [Ironkey][6] (most secure), or USB drive
   with software encryption [using VeraCrypt][7] (less secure).
1. Yubikey (or other hardware security key support 4096bit RSA certificates)
   [nano][8] or [5][9].
1. Copy of these instructions or secondary device Internet access.
1. A photo to associate with your GPG master key.

This assumes usage of an Ironkey with Yubikeys on a Debian-base system for
configuration.

Live USB Setup
--------------
GPG generation should be done on a air-gapped, temporal, encrypted OS to
minimize secret key exposure. Persistent disk should be created so that packages
may be installed / updated as needed (e.g. yubikey manager). All GPG operations
should be done offline with the exception of uploading public keys to services.

* Enusre a _root_ password is set to install additional software.

### Configure Persistent Disk
This will enable the installation of packages (e.g. Yubikey Manager) to manage
physical keys. Do **not** store secret material on this.

**Network is required for this step. Disable after packages are installed.**

Configure a Persistent volume then install yubikey management.
```bash
apt update && apt upgrade
apt-add-repository ppa:yubico/stable
apt update
apt install software-properties-common yubikey-manager yubikey-manager-qt scdaemon
```
* `yubikey-manager-qt` is a GUI frontend which has limited functionality but
  does provide easy ways to ensure specific applets are enabled.
* `scdaemon` enables smartcard support for gpg.

### Reset Ironkey
Do this if fresh Ironkey, or creating a new master key. **Data destructive**.

Initalize Device
```bash
/media/user/IRONKEY/linux/linux64/ikd300_initalize
```
* Only needed on first use.

Reset Device
```bash
/media/user/IRONKEY/linux/linux64/ikd300_resetdevice
```
* Max 16 character password. Ironkey will wipe device after 10 failed attempts
  and force phsyical re-insertion after every 3 failed attempts.

### Unlock Ironkey
```bash
sudo /media/user/IRONKEY/linux/linux64/ikd300_login
```
* Open browser, click on `KINGSTON` to automount to `/media/user/KINGSTON`.
* This is your hardware-backed encrypted storage.
* **Store secret material here**.

GnuPG Configuration
-------------------
Setup GPG to store configuration on encrypted storage and setup secure
cross-platform preferences.

**Ensure machine is air-gapped (no transmission devices on) during this step.**

### Environment Variables & Base Directory Structure
```bash
mkdir /media/user/KINGSTON/gnupghome
mkdir -p /media/user/KINGSTON/backup/public /media/user/KINGSTON/backup/private
export GNUPGHOME=/media/user/KINGSTON/gnupghome
export GPGBACKUP=/media/user/KINGSTON/backup
```
* `GNUPGHOME` directs gpg where to find key material.
* `GPGBACKUP` will be used to direct backups of key material.
* `public` and `private` will be used to store respective key and cert material.

/media/user/KINGSTON/gnupghome/gpg.conf
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
* If "No agent running error" occurs, restart gpg-agent with `gpg-agent
  --daemon`

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
Yubikeys for everyday use. As they are subkeys, these can be revoked as needed
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
1. Enter `=a` to set only authentication capability, this will auto-advance.
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
Exporting subkeys to a Yubikey device will delete the key locally. Backing up
`$GNUPGHOME` before exporting will allow the creation of multiple Yubikeys with
the same subkeys. Make your own determination on if this security practice is
acceptable to you.

**Ensure machine is air-gapped (no transmission devices on) during this step.**
**Store on a (hardware) encrypted device.**

### Confirm Key State on Keyring
Ensure master and subkeys are created and locally stored before exporting.

```bash
gpg --list-keys
```
* `>` indicates a key is exported to card already (e.g. 'ssb>').
* `sec#` indicates only stubs created (e.g. private cert on different machine).
* The master and subkeys should be listed with no modifiers if properly setup to
  export to key.

### Export GPG Keys
Master and Subkeys will be encrypted with your passphrase when exported.
```bash
gpg --armor --export-secret-keys $KEYID > $GPGBACKUP/private/$KEYID.master.asc
gpg --armor --export-secret-subkeys $KEYID > $GPGBACKUP/private/$KEYID.subkey.asc
gpg --armor --export $KEYID > $GPGBACKUP/public/$KEYID.asc
```
* The exported public key may be used in keybase.io, and manually imported into
  other GPG programs.
* GPG Public key export can be used to manually import into other GPG clients if
  you do not want to use keyservers.

### Export SSH RSA Public Key
Generate and export the [RSA Public Key][18] used for SSH.
```bash
gpg --export-ssh-key $KEYID > $GPGBACKUP/public/$KEYID.ssh.pub
```
* The SSH key comment will use the authentication short key ID (e.g.
  `openpgp:0x2C518E44`).

### Backup GNUPG
Backup GNUPG state for multiple Yubikey initalizations.
```bash
sudo cp -avi $GNUPGHOME $GPGBACKUP
```

Export Subkeys to Yubikeys
--------------------------
Read the [technical manual][19] to understand how yubikeys work. This will setup
the yubikey to use the `CCID` interface to setup `openpgp` on the key.

Understand conceptually how Yubikeys are managed. [Yubikey-manager][14] is an
application that is used to manage the yubikey itself (`ykman`) and sets _how_
applets are used on the key. The configuration of the applets themselves are
managed by respective apps, in this case `GPG`.
![Yubikey Organization](yubikey-concept.png)
* `ykman` will set preferences like number of applet PIN attempts, PINs, and
  touch preferences.
* `gpg --edit-card` will set openpgp configuration, like PGP name, login, url.

**Ensure machine is air-gapped (no transmission devices on) during this step.**

### Initalize Yubikey
Confirm Yubikey status.

Default `PIN` is **123456** and default `admin PIN` is **12345678**. PINs may be
up to 127 ASCII characters long.

If the device is not new follow [these instructions][15] to wipe the device and
start new.
```bash
gpg --card-status
```
* If not found, re-insert the key. There is a known race condition that may
  occur with older gpg libraries.
* Ensure firmware version `3.1.8` or later using [Yubikey manager][14] or
  [commandline tool][13].
* Ensure device has `CCID` mode enabled using [Yubikey manager][14] or
  [commandline tool][13].

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
1. `url` to set public key retrival url, can upload gpg public key to
   [keybase][16] and enter that URL, or provide your own.
1. `login` to set account name.
1. account name: `email`.
1. Optionally `forcesig` to force PIN to be entered for every [GPG
   operation][20]. Otherwise it will prompt once and only reprompt when the
   cache expires.
1. Press `enter` to see updated information.
1. `quit`.

Require touch each [time authentication, encryption or sign request occurs][21].
```bash
ykman openpgp touch aut fixed
ykman openpgp touch sig fixed
ykman openpgp touch enc fixed
```
* `Fixed` is the same as `on` but requires a new certificate to be loaded if
  this option or PINs are changed.

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
Ensure keys are offloaded to the Yubikey. Offloaded keys will have `>` next to
the key, showing that the key is on the card.

```bash
gpg --list-secret-keys
```

### Multiple Yubikeys
The original GPG state needs to be reloaded to export subkeys to additional
Yuibkeys. If not exporting to additional keys, this step may be skipped.

```bash
cp -avi $GPGBACKUP/* $GNUPGHOME
```
* Repeat the steps in this section to export to another key.

Publish Public Key
------------------
Export the public key to public keyservers for GPG encrypt/decrypt/signing.
Without publishing you can still use SSH.

**Network is required for this step.**

Export to [SKS keyservers][4]
```bash
gpg --keyserver hkp://pgp.mit.edu --send-key $KEYID
```
* This will export to major keyservers. These are all syncronized so only a
  single server is needed.
* Also consider exporting public key to [keybase.io](http://keybase.io).
* The default gpg server is `hkps://hkps.pool.sks-keyservers.net`

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

Just reboot if using live image.

Otherwise securely delete private data
```bash
sudo srm -r $GNUPGHOME || sudo rm -rf $GNUPGHOME
sudo srm -r $GPGBACKUP || sudo rm -rf $GPGBACKUP
gpg --delete-secret-key $KEYID
```

[1]: https://github.com/drduh/YubiKey-Guide
[2]: https://codingnest.com/how-to-use-gpg-with-Yubikey-wsl/
[3]: http://blog.josefsson.org/2014/06/19/creating-a-small-jpeg-photo-for-your-openpgp-key/
[4]: https://superuser.com/questions/227991/where-to-upload-pgp-public-key-are-keyservers-still-surviving
[5]: https://tails.boum.org/install/win/usb-download/index.en.html
[6]: https://www.kingston.com/us/usb/encrypted_security/IKD300
[7]: https://github.com/drduh/YubiKey-Guide#backup-keys
[8]: https://www.yubico.com/product/Yubikey-5-nano/#Yubikey-5-nano
[9]: https://www.yubico.com/product/Yubikey-5-nfc/#Yubikey-5-nfc
[10]: https://debian-administration.org/users/dkg/weblog/97
[11]: https://security.stackexchange.com/questions/14718/does-openpgp-key-expiration-add-to-security/79386
[12]: https://support.yubico.com/support/solutions/articles/15000006420-using-your-Yubikey-with-openpgp
[13]: https://developers.yubico.com/Yubikey-personalization/
[14]: https://developers.yubico.com/yubikey-manager/
[15]: https://developers.yubico.com/PIV/Guides/Device_setup.html
[16]: https://www.forgesi.net/gpg-smartcard/
[17]: https://www.linode.com/docs/security/authentication/gpg-key-for-ssh-authentication/
[18]: https://lists.gnupg.org/pipermail/gnupg-devel/2016-January/030682.html
[19]: https://support.yubico.com/support/solutions/articles/15000014219-yubikey-5-series-technical-manual
[20]: https://www.gnupg.org/howtos/card-howto/en/ch03.html
[21]: https://suchsecurity.com/gpg-and-ssh-with-yubikey-on-windows.html
[22]: https://www.ubuntu.com/#download