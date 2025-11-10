# GPG with Yubikey
Details creating a GPG Master Key & subkeys, with an embedded photo and
exporting subkeys to multiple Yubikeys. Additional documents provide setup for
using Yubikeys for SSH authentication on different client operating systems.

Subkeys are issued from the master key and are used for specific actions
essentially 'on behalf of' the master identity. These subkeys are loaded onto
Yubikeys for everyday use. As they are subkeys, these can be revoked as needed
or the master key can be revoked/changed to invalidate all subkeys at once. The
master key should be kept offline and encrypted and **only** the subkeys used in
day to day usage.


## Reference

* https://github.com/drduh/YubiKey-Guide
* https://zacharyvoase.com/2009/08/20/openpgp/
* https://zeos.ca/post/2015/gpg-smartcard/
* https://support.yubico.com/hc/en-us/articles/360013790259-Using-Your-YubiKey-with-OpenPGP
* https://www.linode.com/docs/guides/gpg-key-for-ssh-authentication/
