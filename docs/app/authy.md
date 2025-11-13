# Authy TOTP Migration
Authy actively tries to lock in users, which is only made worse by some sites
only allowing Authy usage (such at twitch.tv). This is not ideal, especially if
you have other TOTP solutions that already work for you.

This will guide you how to remove dependence on Authy.

[Original step-by-step here][a]. [Github repo with Script][b].


## Setup
Ensure Two Factor is setup for those sites which require Authy.

* Install [Authy App][c].
* Install [Authy Chrome Extension][d].

!!! warning
    A phone number is needed. Set a master password as well, in case you ever
    need to come back and reset TOTP offloading. Both of these will be removed
    after setup.

### Authy TOTP Format
Authy uses a **7 digit**, **10 second** period for TOTP.

This is know to work with the following authenticators:

* [Google Authenticator][e].
* [Lastpass Authenticator][f].
* [1Password][g].
* KeePassXC.
* [Bitwarden][h].


## [Export TOTP from Authy][i]
Open chrome authy extension, navigate to Two Factor site to extract.

* chrome ➔ more tools ➔ extensions
  * Enable Developer Mode.
  * Navigate to Authy extension details.
    * Inspect Views ➔ main.html
    * Switch to **Console** tab.
    * Insert following code (not my work) and generate TOTP QR codes:

        ``` javascript
        function hex_to_b32(hex) {
          let alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567";
          let bytes = [];
          for (let i = 0; i < hex.length; i += 2) {
            bytes.push(parseInt(hex.substr(i, 2), 16));
          }
          let bits = 0;
          let value = 0;
          let output = '';
          for (let i = 0; i < bytes.length; i++) {
            value = (value << 8) | bytes[i];
            bits += 8;
            while (bits >= 5) {
              output += alphabet[(value >>> (bits - 5)) & 31];
              bits -= 5;
            }
          }
          if (bits > 0) {
            output += alphabet[(value << (5 - bits)) & 31];
          }
          return output;
        }
        // Based on https://github.com/adriancooney/console.image
        function console_image(url, size) {
          console.log("%c+", "font-size: 1px; padding: " + Math.floor(size / 2) + "px " + Math.floor(size / 2) + "px; line-height: " + size + "px; background: url(" + url + "); color: transparent;");
        }
        appManager.getModel().forEach(function(i) {
          let qr_size = 500;
          let secret = (i.markedForDeletion === false ? i.decryptedSeed : hex_to_b32(i.secretSeed));
          let period = (i.digits === 7 ? 10 : 30);
          let totp_uri = `otpauth://totp/${encodeURIComponent(i.name)}?secret=${secret}&digits=${i.digits}&period=${period}`;
          console.group(i.name);
            console.log('TOTP secret:', secret);
            console.log('TOTP URI:', totp_uri);
            let url = (new QRious({value: totp_uri, size: qr_size})).toDataURL();
            console_image(url, qr_size);
          console.groupEnd();
        });
        ```

* Scan the **TOTP URI** code. This will program your Two Factor app with
  the correct number of digits and period. The **TOTP secret** QR is the
  hash for manually entering data.

Confirm Two Factor works with a token from the new Two Factor device. It is
**OK** if tokens for Authy and new device do not line up. Confirm login works.


## Cleanup
* Remove Authy app.
* Remove Authy Extension.
* Chrome ➔ more tools ➔ extensions
    * Disable Developer Mode.

[a]: https://medium.com/@dubistkomisch/set-up-2fa-two-factor-authentication-for-twitch-with-google-authenticator-or-other-totp-client-f19af32df68a
[b]: https://gist.github.com/gboudreau/94bb0c11a6209c82418d01a59d958c93
[c]: https://play.google.com/store/apps/details?id=com.authy.authy
[d]: https://chrome.google.com/webstore/detail/authy/gaedmjdfmmahhbjefcbgaolhhanlaolb
[e]: https://gist.github.com/gboudreau/94bb0c11a6209c82418d01a59d958c93?source=post_page---------------------------#gistcomment-2176972
[f]: https://gist.github.com/gboudreau/94bb0c11a6209c82418d01a59d958c93?source=post_page---------------------------#gistcomment-2875862
[g]: https://gist.github.com/gboudreau/94bb0c11a6209c82418d01a59d958c93?source=post_page---------------------------#gistcomment-2318490
[h]: https://gist.github.com/gboudreau/94bb0c11a6209c82418d01a59d958c93?source=post_page---------------------------#gistcomment-2176972
[i]: https://gist.github.com/DuBistKomisch/a12160a0d1d6c31499497e15263c3db3#file-authy-extract-js
