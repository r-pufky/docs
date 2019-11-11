Export GPG Subkeys to Yubikey
-----------------------------
This documents details loading the GPG Subkeys to a Yubikey. See [reference
documentation above][1] to create GPG keys and setup operating systems to use
Yubikeys for GPG key material.

1. [Creating GPG Keys][1]
1. [Windows GPG Yubikey Setup](windows.md)
1. [Ubuntu GPG Yubikey Setup](ubuntu.md)

Required Materials
------------------
1. Live USB OS, with persistent storage to setup additional packages. Tails Live
   USB [Setup instructions][2] is preferred (most secure), other [live USB][3]
   will work but be less secure. Instructions assume Debian-based system.
1. Hardware-backed Encrypted USB drive [Ironkey][4] (most secure), or USB drive
   with software encryption [using VeraCrypt][5] (less secure) containing your
   GPG Master Keys.
1. Yubikey (or other hardware security key support 4096bit RSA certificates)
   [nano][6] or [2][7].
1. Copy of these instructions or secondary device Internet access.

This assumes usage of an Ironkey with Yubikeys on a Debian-base system for
configuration; and that you've already created your [GPG Master Keys][1].

Understanding How Yubikeys Work
-------------------------------
Read the [technical manual][8] to understand how yubikeys work. This will setup
the yubikey to use the `CCID` interface to setup `openpgp` on the key.

[Yubikey-manager][9] is an application that is used to manage the yubikey
itself (`ykman`) and sets _how_ applets are used on the key. The configuration
of the applets themselves are managed by respective apps, in this case `GPG`.
![Yubikey Organization](yubikey-concept.png)
* `ykman` will set preferences like number of applet PIN attempts, PINs, and
  touch preferences.
* `gpg --edit-card` will set openpgp configuration, like PGP name, login, url.

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
* Ubuntu **18.04+** needs to add `universe multiverse` to all apt sources first
  `/etc/apt/sources.list`.

Export Subkeys to Yubikeys
--------------------------
**Ensure machine is air-gapped (no transmission devices on) during this step.**

### Initalize Yubikey
Confirm Yubikey status.

Default `PIN` is **123456** and default `admin PIN` is **12345678**. PINs may be
up to 127 ASCII characters long.

If the device is not new follow [these instructions][17] (alternative
[here][10]) to wipe the device and start new.
```bash
gpg --card-status
```
* If not found, re-insert the key. There is a known race condition that may
  occur with older GPG libraries.
* Ensure firmware version `3.1.8` or later using [Yubikey manager][9] or
  [commandline tool][11].
* Ensure device has `CCID` mode enabled using [Yubikey manager][9] or
  [commandline tool][11].

Reset Yubikey -- this will destory any openpgp material on the key and reset to
the default key state.
```bash
ykman openpgp reset
```

```bash
gpg --card-edit
```
1. `admin` to enter administration mode.
1. `passwd` to enter PIN password change mode.
1. `3` to change admin PIN. Be sure to enter the _initial_ **12345678** pin
   first. This is the `Admin Password` and can be up to 127 ASCII characters.
1. `1` to change PIN. Be sure to enter the _initial_ **123456** pin first.
   This is the `User Password` and can be up to 127 ASCII characters.
1. `q` to return to main menu.
1. `name` to set owners first and last name.
1. surname: `last`.
1. given name: `first`.
1. `lang`.
1. `en` to set the preferred language.
1. `url` to set public key retrival url, can upload gpg public key to
   [keybase][12] and enter that URL, or provide your own.
1. `login` to set account name.
1. account name: `email`.
1. `forcesig` to force PIN to be entered for every [GPG operation][16].
1. Press `enter` to see updated information.
1. `quit`.

Require touch each [time authentication, encryption or sign request occurs][13].
```bash
ykman openpgp set-touch aut fixed
ykman openpgp set-touch sig fixed
ykman openpgp set-touch enc fixed
```
* `Fixed` is the same as `on` but requires a [new certificate to be loaded][14]
  if this option is disabled.

### Load Subkeys to Yubikey
This is **data destructive** for local subkeys. Ensure a backup has been made
before doing this. See [Export GPG Keys & Backup][15].

```bash
gpg --edit-key $KEYID
```
* Key selection is a toggle action, ensure to only export _one_ key at a time.
* Remember to `save` and `quit` when done.

#### Load Signing Key
1. `key 1` (ensure _*_ only appears next to signing key).
1. `keytocard` to export key.
   1. First Password: GPG private key password.
   1. Second Password: Yubikey user password.
1. Select `1` "(1) Signature key".
1. `key 1` to deselect key.

#### Load Encryption Key
1. 'key 2' (ensure _*_ only appears next to encryption key).
1. `keytocard` to export key.
   1. First Password: GPG private key password.
   1. Second Password: Yubikey user password.
1. Select `2` "(2) Encryption key".
1. `key 2` to deselect key.

#### Load Authentication Key
1. 'key 3' (ensure _*_ only appears next to authentication key).
1. `keytocard` to export key.
   1. First Password: GPG private key password.
   1. Second Password: Yubikey user password.
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

Cleanup
-------
Just reboot if using live image, otherwise securely delete private data.
```bash
sudo srm -r $GNUPGHOME || sudo rm -rf $GNUPGHOME
sudo srm -r $GPGBACKUP || sudo rm -rf $GPGBACKUP
gpg --delete-secret-key $KEYID
```
* Your GPG data is backed up on an encryped medium, right?

[1]: README.md
[2]: https://tails.boum.org/install/win/usb-download/index.en.html
[3]: https://www.ubuntu.com/#download
[4]: https://www.kingston.com/us/usb/encrypted_security/IKD300
[5]: https://github.com/drduh/YubiKey-Guide#backup-keys
[6]: https://www.yubico.com/product/Yubikey-5-nano/#Yubikey-5-nano
[7]: https://www.yubico.com/product/Yubikey-5-nfc/#Yubikey-5-nfc
[8]: https://support.yubico.com/support/solutions/articles/15000014219-yubikey-5-series-technical-manual
[9]: https://developers.yubico.com/yubikey-manager/
[10]: https://developers.yubico.com/PIV/Guides/Device_setup.html
[11]: https://developers.yubico.com/Yubikey-personalization/
[12]: https://www.forgesi.net/gpg-smartcard/
[13]: https://suchsecurity.com/gpg-and-ssh-with-yubikey-on-windows.html
[14]: https://developers.yubico.com/PGP/Card_edit.html
[15]: README.md#export-gpg-Keys--backup
[16]: https://www.gnupg.org/howtos/card-howto/en/ch03.html
[17]: https://support.yubico.com/support/solutions/articles/15000006421-resetting-the-openpgp-applet-on-the-yubikey
