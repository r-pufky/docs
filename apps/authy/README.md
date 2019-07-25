Moving Authy TOTP to Other Authenticators
=========================================
Lock in is unreal with Authy and some sites are only allowing Authy usage. This
is not ideal, especially if you have other TOTP solutions that work for you.

This will guide you how to remove dependence on Authy.

[Original step-by-step here][8f].
[Github repo with Script][x0].

This is _not_ my work; just abbreviated notes with sources to remove Authy
dependence.

1. [Setup Authy](#setup-authy)
1. [Export TOTP from Authy](#export-totp-from-authy)
1. [Cleanup](#cleanup)

Setup Authy
-----------
Ensure Two Factor is setup for those sites which require Authy.

* Install [Authy App][3o].
* Install [Authy Chrome Extension][hl].

> :warning:  
> A phone number is needed. Set a master password as well, in case you ever need
> to come back and reset TOTP offloading. Both of these will be removed after
> setup.

### Authy TOTP Format
Authy uses a **7 digit**, **10 second** period for TOTP.

This is know to work with the following authenticators:
* [Google Authenticator][9b]
* [Lastpass Authenticator][9d]
* [1Password][9f]
* KeePassXC

Export TOTP from Authy
----------------------

1. Open chrome authy extension, nagivate to Two Factor site to extract.
1. `chrome > more tools > extensions`
   1. Enable _Developer Mode_.
   1. Click `Details` on _Authy_ extension.
   1. Click `Inspect Views > main.html`.
   1. Switch to `Console` tab
   1. Insert following code (not my work) and generate TOTP QR codes:
      ```javascript
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
      * [source page here][8f], [source code here][2i]
   1. Scan the `TOTP URI` code. This will program your Two Factor app with the
      correct number of digits and period. The `TOTP secret` QR is the hash for
      manually entering data.
1. Confirm Two Factor works with a token from the new Two Factor device. It is
   OK if tokens for Authy and new device do not line up. Confirm login works.

Cleanup
-------
1. Remove Authy app.
1. Remove Authy Extension.
1. `chrome > more tools > extensions`
   1. Disable _Developer Mode_.

[8f]: https://medium.com/@dubistkomisch/set-up-2fa-two-factor-authentication-for-twitch-with-google-authenticator-or-other-totp-client-f19af32df68a
[x0]: https://gist.github.com/gboudreau/94bb0c11a6209c82418d01a59d958c93
[hl]: https://chrome.google.com/webstore/detail/authy/gaedmjdfmmahhbjefcbgaolhhanlaolb
[3o]: https://play.google.com/store/apps/details?id=com.authy.authy
[2i]: https://gist.github.com/DuBistKomisch/a12160a0d1d6c31499497e15263c3db3#file-authy-extract-js
[9d]: https://gist.github.com/gboudreau/94bb0c11a6209c82418d01a59d958c93?source=post_page---------------------------#gistcomment-2875862
[9f]: https://gist.github.com/gboudreau/94bb0c11a6209c82418d01a59d958c93?source=post_page---------------------------#gistcomment-2318490
[9b]: https://gist.github.com/gboudreau/94bb0c11a6209c82418d01a59d958c93?source=post_page---------------------------#gistcomment-2176972
