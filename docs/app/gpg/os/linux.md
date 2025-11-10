# Linux

!!! tip
    See [Trust GPG Key
    Locally](../setup/import.md#trust-gpg-public-key-locally)
    for importing your public key and assigning ultimate trust for use.

    Requires **~/.ssh/authorized_keys** on target machine with your exported
    GPG SSH RSA Public Key. See [GPG Export
    Keys](../setup/backup.md#export-gpg-keys). See
    [SSH](../../../service/ssh/README.md) for remote SSH configuration.

## Install Packages

Install GPG and security card agents on machine.

=== "Manjaro"
    ``` bash
    sudo pacman -Syu gnupg pcsclite ccid hopenpgp-tools yubikey-personalization
    sudo systemctl enable pcscd.service
    sudo systemctl start pcscd.service
    ```

=== "Debian"
    ``` bash
    apt update && apt upgrade
    apt install wget gnupg2 gnupg-agent dirmngr cryptsetup scdaemon pcscd
    apt install secure-delete hopenpgp-tools yubikey-personalization

    # Optionally install yubikey manager to manage yubikeys.
    apt install python3-pip python3-pyscard
    pip3 install PyOpenSSL
    pip3 install yubikey-manager
    service pcscd start
    ~/.local/bin/ykman openpgp info
    ```

=== "Ubuntu"
    ``` bash
    # Requires universe multiverse APT sources.
    apt update && apt upgrade
    apt install wget gnupg2 gnupg-agent dirmngr cryptsetup scdaemon pcscd
    apt install secure-delete hopenpgp-tools yubikey-personalization

    apt install libssl-dev swig libpcsclite-dev
    ```

## Configure SSH/GPG Agent
This will enable SSH usage with the gpg-agent.

**~/.gnupg/gpg-agent.conf** (1)
{ .annotate }

1. 0600 {USER}:{USER}
``` bash
# https://github.com/drduh/config/blob/master/gpg-agent.conf
# https://www.gnupg.org/documentation/manuals/gnupg/Agent-Options.html
enable-ssh-support
ttyname $GPG_TTY
default-cache-ttl 60
max-cache-ttl 120
pinentry-program /usr/bin/pinentry-curses
#pinentry-program /usr/bin/pinentry-tty
#pinentry-program /usr/bin/pinentry-gtk-2
#pinentry-program /usr/bin/pinentry-x11
#pinentry-program /usr/bin/pinentry-gnome3
#pinentry-program /usr/local/bin/pinentry-curses
#pinentry-program /usr/local/bin/pinentry-mac
```

**~/.gnupg/gpg.conf** (1)
{ .annotate }

1. 0600 {USER}:{USER}
``` bash
# https://github.com/drduh/config/blob/master/gpg.conf
# https://www.gnupg.org/documentation/manuals/gnupg/GPG-Configuration-Options.html
# https://www.gnupg.org/documentation/manuals/gnupg/GPG-Esoteric-Options.html
# Use AES256, 192, or 128 as cipher
personal-cipher-preferences AES256 AES192 AES
# Use SHA512, 384, or 256 as digest
personal-digest-preferences SHA512 SHA384 SHA256
# Use ZLIB, BZIP2, ZIP, or no compression
personal-compress-preferences ZLIB BZIP2 ZIP Uncompressed
# Default preferences for new keys
default-preference-list SHA512 SHA384 SHA256 AES256 AES192 AES ZLIB BZIP2 ZIP Uncompressed
# SHA512 as digest to sign keys
cert-digest-algo SHA512
# SHA512 as digest for symmetric ops
s2k-digest-algo SHA512
# AES256 as cipher for symmetric ops
s2k-cipher-algo AES256
# UTF-8 support for compatibility
charset utf-8
# Show Unix timestamps
fixed-list-mode
# No comments in signature
no-comments
# No version in output
no-emit-version
# Disable banner
no-greeting
# Long hexidecimal key format
keyid-format 0xlong
# Display UID validity
list-options show-uid-validity
verify-options show-uid-validity
# Display all keys and their fingerprints
with-fingerprint
# Display key origins and updates
#with-key-origin
# Cross-certify subkeys are present and valid
require-cross-certification
# Disable caching of passphrase for symmetrical ops
no-symkey-cache
# Enable smartcard
use-agent
# Disable recipient key ID in messages
throw-keyids
# Default/trusted key ID to use (helpful with throw-keyids)
#default-key 0xFF3E7D88647EBCDB
#trusted-key 0xFF3E7D88647EBCDB
# Group recipient keys (preferred ID last)
#group keygroup = 0xFF00000000000001 0xFF00000000000002 0xFF3E7D88647EBCDB
# Keyserver URL
#keyserver hkps://keys.openpgp.org
#keyserver hkps://keyserver.ubuntu.com:443
#keyserver hkps://hkps.pool.sks-keyservers.net
#keyserver hkps://pgp.ocf.berkeley.edu
# Proxy to use for keyservers
#keyserver-options http-proxy=http://127.0.0.1:8118
#keyserver-options http-proxy=socks5-hostname://127.0.0.1:9050
# Verbose output
#verbose
# Show expired subkeys
#list-options show-unusable-subkeys
```

**~/.bashrc** (1)
{ .annotate }

1. 0644 {USER}:{USER}
``` bash
# Direct SSH to use GPG for authentication.
export GPG_TTY="$(tty)"
export SSH_AUTH_SOCK=$(gpgconf --list-dirs agent-ssh-socket)
gpgconf --launch gpg-agent
gpg-connect-agent updatestartuptty /bye > /dev/null
```

## Verify SSH Works
1. Connect with SSH as normal.
2. A **Pin Entry** pop-up window should appear. It may not be in focus. Enter
   your **user** [PIN](../../../glossary/yubikey.md#yubikey-passwordpin).
3. Touch key to confirm (key will blink during wait for password).

Reference:

* https://github.com/drduh/YubiKey-Guide

## SSH Through a Bastion
All latest versions of SCP and SSH support multiple jump proxies for transfers.
GPG agent will be forwarded automatically (two authentication touches) if agent
forwarding is enabled.

``` bash
# Modern SSH uses -J.
ssh -J {USER}@{BASTION} {STANDARD SSH COMMAND}

# Equivalent.
ssh -o ProxyJump={USER}@{BASTION} {STANDARD SCP COMMAND}
```

This may also be setup to auto proxy via the config file.

**~/.ssh/config** (1)
{ .annotate }

1. 0644 {USER}:{USER}
``` bash
Host {HOST}
User {USER}
HostName {HOST}
ProxyJump {USER}@{BASTION}
```

Reference:

* https://superuser.com/questions/456438/how-do-i-scp-a-file-through-an-intermediate-server
* https://superuser.com/questions/174160/scp-over-a-proxy-with-one-command-from-local-machine

## SCP Transfer File Through a Bastion
All latest versions of SCP and SSH support multiple jump proxies for transfers.
GPG agent will be forwarded automatically (two authentication touches) if agent
forwarding is enabled.

``` bash
# Modern SSH uses -J.
scp -J {USER}@{BASTION} {STANDARD SCP COMMAND}

# Equivalent.
scp -o ProxyJump={USER}@{BASTION} {STANDARD SCP COMMAND}
```

## Reference

* https://superuser.com/questions/456438/how-do-i-scp-a-file-through-an-intermediate-server
* https://superuser.com/questions/174160/scp-over-a-proxy-with-one-command-from-local-machine