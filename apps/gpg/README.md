Using GPG with multiple Yubikeys
--------------------------------
Details creating a GPG Master Key & Subkeys, with an embedded photo and
exporting sed Subkeys to Multiple Yubikeys. Additional documents provide setup
for using Yubikeys for SSH authentication on different client operating systems.

1. [Creating GPG Keys][1]
1. [Export GPG Subkeys to Yubikey][2]
1. [Windows GPG Yubikey Setup][3]
1. [Ubuntu GPG Yubikey Setup][4]

Core (out of date) [instructions are here][5]. Alternative step-by-step
walkthrough instructions for configuring [multi-platform GPG/Yubikey SSH usage
are here][16]. [OpenPGP for Beginners][6] is a good starting point if you have
no understanding of what this is.

Required Materials
------------------
1. Live USB OS, with persistent storage to setup additional packages. Tails Live
   USB [Setup instructions][7] is preferred (most secure), other [live USB][8]
   will work but be less secure. Instructions assume Debian-based system.
1. Hardware-backed Encrypted USB drive [Ironkey][9] (most secure), or USB drive
   with software encryption [using VeraCrypt][10] (less secure).
1. Yubikey (or other hardware security key support 4096bit RSA certificates)
   [nano][11] or [Yubikey 5][12].
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
key][15].

```bash
gpg --full-generate-key
```
1. Select `4` "(4) RSA (sign only)".
1. `4096` bit keysize.
1. Select `0` "0 = key does not expire".
1. Select `y` to Confirm correct values.
1. name: `first last`.
1. email: `email`.
1. comment: [`BLANK`][13].
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
removed, [instructions here.][14]

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
1. comment: [`BLANK`][13].
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
cp $GNUPGHOME/openpgp-revocs.d/* $GPGBACKUP/private
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

Publish Public Key
------------------
Export the public key to public keyservers for GPG encrypt/decrypt/signing.
Without publishing you can still use SSH.

**Network is required for this step.**

Export to [SKS keyservers][19]
```bash
gpg --keyserver hkp://pgp.mit.edu --send-key $KEYID
```
* This will export to major keyservers. These are all syncronized so only a
  single server is needed.
* Also consider exporting public key to [keybase.io](http://keybase.io).
* The default gpg server is `hkps://hkps.pool.sks-keyservers.net`

Cleanup
-------
### Critical Confirmations
Manually verify this information to ensure you do not accidently lose data or
access/control to your GPG identity.

1. Encrypted Media has the following
   * `$GPGBACKUP/private/$KEYID.master.asc`
   * `$GPGBACKUP/private/$KEYID.subkey.asc`
   * `$GPGBACKUP/private/$KEYID.rev`
   * `$GPGBACKUP/public/$KEYID.asc`
   * `$GPGBACKUP/public/$KEYID.ssh.pub`
1. A backup of GPG Master Key (with all keys locally present)
   * `$GPGBACKUP/gnupghome`
1. Your Master Key password is stored **away** from your encrypted media, in a
   controlled space.
1. Your Encrypted Media password is stored **away** from your encrypted media,
   in a controlled space.
1. **The encrypted media is stored offline, in a controlled space.**
1. The public keys are stored or published, and are readily accessible.
   * `$GPGBACKUP/public/*`
1. It is generally a good idea to print a copy of the revocation certificate and
   give it to a trusted third-party.

### Next Steps
1. [Export Keys to Yubikey][2].
1. Setup Yubikey on [windows][3] or [ubuntu][4].

### Cleaning Up
Securely remove any secret GPG material.

If you are using a Live OS, just reboot. If you're paranoid, wipe the live
drive.

If not using a live OS, wipe private key material _after you confirm it is
backed up_
```bash
sudo srm -r $GNUPGHOME || sudo rm -rf $GNUPGHOME
sudo srm -r $GPGBACKUP || sudo rm -rf $GPGBACKUP
gpg --delete-secret-key $KEYID
```

Cofirming GPG Password
----------------------
There is no built in method to confirm a GPG password is correct (e.g. if you
want to verify your password works without doing an operation). Verification of
passsword happens by checkin the exit code and printing 'Correct' if the command
succeeded.

```bash
echo '1234' | gpg --batch --passphrase-fd 1 -o /dev/null --local-user $KEYID -as - && echo 'Correct.'
```

[1]: README.md
[2]: yubikey.md
[3]: windows.md
[4]: ubuntu.md
[5]: https://github.com/drduh/YubiKey-Guide
[6]: https://zacharyvoase.com/2009/08/20/openpgp/
[7]: https://tails.boum.org/install/win/usb-download/index.en.html
[8]: https://www.ubuntu.com/#download
[9]: https://www.kingston.com/us/usb/encrypted_security/IKD300
[10]: https://github.com/drduh/YubiKey-Guide#backup-keys
[11]: https://www.yubico.com/product/Yubikey-5-nano/#Yubikey-5-nano
[12]: https://www.yubico.com/product/Yubikey-5-nfc/#Yubikey-5-nfc
[13]: https://debian-administration.org/users/dkg/weblog/97
[14]: http://blog.josefsson.org/2014/06/19/creating-a-small-jpeg-photo-for-your-openpgp-key/
[15]: https://security.stackexchange.com/questions/14718/does-openpgp-key-expiration-add-to-security/79386
[16]: https://www.forgesi.net/gpg-smartcard/
[18]: https://lists.gnupg.org/pipermail/gnupg-devel/2016-January/030682.html
[19]: https://superuser.com/questions/227991/where-to-upload-pgp-public-key-are-keyservers-still-surviving

[ref1]: https://support.yubico.com/support/solutions/articles/15000006420-using-your-Yubikey-with-openpgp
[ref2]: https://www.linode.com/docs/security/authentication/gpg-key-for-ssh-authentication/