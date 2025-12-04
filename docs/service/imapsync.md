# [imapsync][a]
Sync gmail to local imap server.


## Setup
``` bash
git clone https://github.com/imapsync/imapsync

# Dependency / Pre-requisite list.
imapsync/INSTALL.d/prerequisities_imapsync

# Perl dependencies
apt install libio-tee-perl libmail-imapclient-perl libterm-readkey-perl libunicode-string-perl libcrypt-openssl-rsa-perl libdata-uniqid-perl libjson-perl liblwp-online-perl libreadonly-perl libfile-copy-recursive-perl libio-socket-inet6-perl libsys-meminfo-perl libregexp-common-perl libfile-tail-perl libauthen-ntlm-perl libcgi-pm-perl libclass-load-perl libcrypt-ssleay-perl libdigest-hmac-perl libdist-checkconflicts-perl libencode-imaputf7-perl libio-compress-perl libio-socket-ssl-perl libmodule-scandeps-perl libnet-dbus-perl libnet-ssleay-perl libpar-packer-perl libtest-fatal-perl libtest-mock-guard-perl libtest-mockobject-perl libtest-pod-perl libtest-requires-perl libtest-simple-perl liburi-perl libtest-nowarnings-perl libtest-deep-perl libtest-warn-perl libjson-webtoken-perl cpanminus make

# Create password files.
touch .ssh/imapsync_{gmail,personal}
chmod 0600 .ssh/imapsync_{gmail,personal}

# Set gmail Application password and lockdown file.
# https://security.google.com/settings/security/apppasswords
chmod 0400 .ssh/imapsync_gmail

# Set personal mail server password and lock file.
chmod 0400 .ssh/imapsync_personal
```


## Test Sync
``` bash
./imapsync --dry \
  --host1 imap.gmail.com --port1 993 --user1 {GMAIL EMAIL USER} \
    --passfile1 ~/.ssh/imapsync_gmail --ssl1 \
  --host2 {YOUR IMAP SERVER} --port2 993 --user2 {YOUR IMAP USER} \
    --passfile2 ~/.ssh/imapsync_personal --ssl2 \
  --subfolder2 gmail-archive --minage 30 --exitwhenover 2500000000 \
  --delete --expunge1
```

* This will sync mail older than 30 days, and remove it from
  [gmail](https://imapsync.lamiral.info/FAQ.d/FAQ.Gmail.txt).
* Gmail has a download limit of 2.5GB a day. Will safely exit when reached.
* Ensure connections work, folders are identified, and local folder is set
  properly.


## Install Service
``` bash
sudo git checkout-index -a -f --prefix=/opt/imapsync/
chmod +x /opt/imapsync/imapsync
```

!!! abstract "~/bin/gmail_to_imap_sync"
    0755 {USER}:{USER}

    ``` bash
    #!/bin/bash

    /opt/imapsync/imapsync \
    --host1 imap.gmail.com --port1 993 --user1 {GMAIL EMAIL USER} \
      --passfile1 ~/.ssh/imapsync_gmail --ssl1 \
    --host2 {YOUR IMAP SERVER} --port2 993 --user2 {YOUR IMAP USER} \
      --passfile2 ~/.ssh/imapsync_personal --ssl2 \
    --subfolder2 gmail-archive --minage 30 --exitwhenover 2500000000 \
    --delete --expunge1 \
    --nolog &>/dev/null
    ```

``` bash
# Add to local crontab to run nightly.
crontab -e
> * 3 * * * ~/bin/gmail_to_imap_sync
```


## Reference[^1][^2][^3]

[^1]: https://askubuntu.com/questions/539102/error-install-imapsync
[^2]: https://en.wikipedia.org/wiki/Cron
[^3]: https://blog.christosoft.de/2015/03/maildir-remove-duplicates

[a]: https://github.com/imapsync/imapsync
