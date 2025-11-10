# Setup
Carefully follow these instructions before setting up GPG and Yubikeys to
remain in a secure state. Failure to follow these instructions may expose
private key material to bad actors.

## Required Materials

1. Live USB OS, with persistent storage to setup additional packages. Tails
   Live USB [setup
   instructions](https://tails.boum.org/install/win/usb-download/index.en.html)
   is preferred (most secure), other [live USB](https://ubuntu.com/#download)
   will work but be less secure. Instructions assume Debian-based system.
2. Hardware-backed Encrypted USB drive [Ironkey](https://www.kingston.com/unitedstates/us/usb-flash-drives/ironkey-d300-encrypted-usb-flash-drive)
   (most secure), or USB drive with software encryption [using VeraCrypt](https://github.com/drduh/YubiKey-Guide#backup)
   (less secure).
3. [Yubikey 5](https://www.yubico.com/products/yubikey-5-overview/) (or other
   hardware security key support 4096bit RSA certificates).
4. A complete copy of these instructions or secondary device Internet access.
5. A photo to associate with your GPG master key.

This assumes usage of an Ironkey with Yubikeys on a Debian-base system for
configuration.

Reference:

* https://developers.yubico.com/PIV/Guides/Device_setup.html
* https://zeos.ca/post/2018/gpg-yubikey5/
* https://www.gnupg.org/howtos/card-howto/en/ch03.html

## Prep Live USB
GPG generation should be done on a air-gapped, temporal, encrypted OS to
minimize secret key exposure. Persistent disk should be created so that
packages may be installed / updated as needed (e.g. Yubikey manager). All GPG
operations should be done **offline** with the exception of uploading public
keys to services.

Set a **root** password.

!!! danger
    Do **not** store secret material directly on live USB filesystems.

    Network is required for this step. **Disable** after packages are
    installed.

``` bash
# Update and install Yubikey management.
apt update && apt upgrade
apt-add-repository ppa:yubico/stable
apt update
apt install software-properties-common scdaemon hopenpgp-tools gpg
apt install yubikey-manager yubikey-manager-qt
```

!!! note
    **yubikey-manager-qt** is a GUI frontend which has limited functionality
    but does provide easy ways to ensure specific applets are enabled.
    **scdaemon** enables smartcard support for GPG.

## Prep Ironkey
!!! tip
    Max **16** character password. Ironkey will wipe device after **10** failed
    attempts and force physical re-insertion after every **3** failed attempts.

### Initialize Ironkey
For a new Ironkey or creating a new master key.

!!! danger
    This is **data destructive**.

    ``` bash
    /media/user/IRONKEY/linux/linux64/ikd300_initalize
    ```

### Reset Ironkey
Wipes a working Ironkey to a default state.

!!! danger
    This is **data destructive**.

    ``` bash
    /media/user/IRONKEY/linux/linux64/ikd300_resetdevice
    ```

### Unlock Ironkey
``` bash
sudo /media/user/IRONKEY/linux/linux64/ikd300_login
```

* Run **KINGSTON** from file browser to mount to **/media/user/KINGSTON**.

!!! success "Safe for Secrete Key Material"
    The Ironkey is the only **safe** location to store secret key material.

## Prep Yubikey
!!! note "Default Yubikey Passwords"
    * Default User Pin: **123456**
    * Default Admin Pin: **12345678**

    [Yubikey Password/PINs](../../../glossary/yubikey.md#yubikey-passwordpin)
    may be up to **127 ASCII characters** long.

### Verify Genuine Yubikey
Ensure Yubikey is genuine and has not been tampered with during any step of the
supply chain.

1. https://www.yubico.com/genuine
2. Verify Device.
3. Touch Yubikey when prompted.

!!! note
    Yubico must be able to see the make and model of the device during the
    verification process.

**Verification Complete** is displayed for genuine keys. Failure means
potential compromise and should be thrown out after it is confirmed to fail
again.

### Reset Yubikey
This will [destroy any openpgp material](https://support.yubico.com/hc/en-us/articles/360013761339-Resetting-the-OpenPGP-Applet-on-the-YubiKey)
on the key and reset to the default key state.

!!! warning "Do this even if the Yubikey is new"
    ``` bash
    ykman openpgp reset
    ```

    Existing 2FA configurations will be deleted.

Alternatively using the [Yubikey Personalization Tool](https://www.yubico.com/products/services-software/download/yubikey-personalization-tools/)
will provide options to do this via a GUI.

``` bash
### Show current Yubikey card shows with default values.
gpg --card-status
```

* If not found, re-insert the key. There is a known race condition that may
  occur with older GPG libraries.
* Ensure latest firmware version using [Yubikey
  Manager](../../../glossary/yubikey.md#yubikey-manager).
* Ensure device has **CCID** mode enabled using [Yubikey
  Manager](../../../glossary/yubikey.md#yubikey-manager). Most
  firmware past **3.1.8** will have this permanently enabled and not listed.

### Configure Yubikey
Configure behavior of Yubikey so short touches will provide GPG material, while
long touches will provide Yubico OTP. This prevents accidental touches spewing
keystrokes into whatever is open. NFC is also disabled to force physical touch
to use key.

#### Swap slots
1. Yubikey Manager ➔ Applications ➔ OTP
2. Delete **Slot 1**.
3. Configure **Slot 2** to use **Yubico OTP**.

![OTP](yubikey_otp.png)

!!! tip
    Newer keys can just use the **swap** button.

#### Disable NFC
1. Yubikey Manager ➔ Interfaces ➔ NFC ➔ Disable All
2. **Save Interfaces**.

![NFC](yubikey_nfc.png)

!!! tip
    All NFC options are disabled to require physical presence.

## Setup OpenPGP on Yubikey
Prepare Yubikey to load GPG key material.

``` bash
# Edit openpgp application on Yubikey.
gpg --card-edit
> Reader ...........: Yubico YubiKey OTP FIDO CCID 0
> Application ID ...: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
> Version ..........: 3.4
> Manufacturer .....: Yubico
> Serial number ....: XXXXXXXXXX
> Name of cardholder: [not set]
> Language prefs ...: [not set]
> Sex ..............: unspecified
> URL of public key : [not set]
> Login data .......: [not set]
> Signature PIN ....: forced
> Key attributes ...: rsa4096 rsa4096 rsa4096
> Max. PIN lengths .: 127 127 127
> PIN retry counter : 3 3 3
> Signature counter : 0

# Set admin password (Remember to use the Default PIN if needed).
gpg/card> admin
> Admin commands are allowed

gpg/card> passwd
> gpg: OpenPGP card no. XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX detected
>
> 1 - change PIN
> 2 - unblock PIN
> 3 - change Admin PIN
> 4 - set the Reset Code
> Q - quit

Your selection? 3
> PIN changed.

Your selection? Q

# Set user password (Remember to use the Default PIN if needed).
gpg/card> admin
> Admin commands are allowed

gpg/card> passwd
> gpg: OpenPGP card no. XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX detected
>
> 1 - change PIN
> 2 - unblock PIN
> 3 - change Admin PIN
> 4 - set the Reset Code
> Q - quit

Your selection? 1
> PIN changed.

Your selection? Q

# Set name used in the GPG credentials to load.
gpg/card> name
Cardholders surname: {USER LAST NAME}
Cardholders given name: {USER FIRST NAME}

# Set language for GPG user.
gpg/card> lang
Language preferences: en

#  Set URL to location of user's GPG public key.
gpg/card> url
URL to retrieve public key: https://keys.openpgp.org/vks/v1/by-fingerprint/{KEYID}

# Set login to GPG email account used.
gpg/card> login
Login data (account name): {GPG USER EMAIL ADDRESS}

# Set forcesig to always require PIN to access GPG key material.
gpg/card> forcesig

# Verify configuration and quit to save.
gpg/card> {PRESS ENTER}
> Reader ...........: Yubico YubiKey OTP FIDO CCID 0
> Application ID ...: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
> Version ..........: 3.4
> Manufacturer .....: Yubico
> Serial number ....: XXXXXXXXXX
> Name of cardholder: {USER FIRST NAME} {USER LAST NAME}
> Language prefs ...: en
> Sex ..............: unspecified
> URL of public key : https://keys.openpgp.org/vks/v1/by-fingerprint/{KEYID}
> Login data .......: {GPG USER EMAIL ADDRESS}
> Signature PIN ....: forced
> Key attributes ...: rsa4096 rsa4096 rsa4096
> Max. PIN lengths .: 127 127 127
> PIN retry counter : 3 3 3
> Signature counter : 0

gpg/card> quit
```

## Require touch for each Authentication, Encryption, or Signing Request
``` bash
ykman openpgp set-touch aut fixed
ykman openpgp set-touch sig fixed
ykman openpgp set-touch enc fixed
```
!!! tip
    **Fixed** is the same as **on** but requires a new certificate to be loaded
    if this option is ever disabled.

Reference:

* https://developers.yubico.com/PGP/Card_edit.html
* https://suchsecurity.com/gpg-and-ssh-with-yubikey-on-windows.html
