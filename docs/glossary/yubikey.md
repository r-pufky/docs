# Yubikey


## Yubikey Manager
Application that will manage Yubikey configuration. There is a
[GUI Yubikey Manager][a] and a [CLI Yubikey Manager][b].


## Yubikey Password/PIN
Password for **user** and **admin** accounts for a Yubikey. Can be up to
**127 ASCII characters** long.

The **user** password is used whenever GPG material needs to be accessed on the
card. Daily usage.

The **admin** password is used to reset the user password and perform
administrative functions on the Yubikey itself. Limited usage.

[a]: https://developers.yubico.com/yubikey-manager
[b]: https://www.yubico.com/products/services-software/download/yubikey-manager
