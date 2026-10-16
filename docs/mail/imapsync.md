# [imapsync][a]
Sync gmail to local imap server.

## Setup

=== "[Arch][b]"
    ``` bash
    git clone https://github.com/imapsync/imapsync

    paru -Ss cpanminus
    sudo pkgfile --update
    ./INSTALL.d/prerequisities_imapsync

    paru -S perl-cgi \
       perl-crypt-openssl-rsa \
       perl-data-uniqid \
       perl-digest-hmac \
       perl-dist-checkconflicts \
       perl-file-copy-recursive \
       perl-io-socket-inet6 \
       perl-io-socket-ssl \
       perl-io-tee \
       perl-json \
       perl-html-parser \
       perl-libwww \
       perl-module-implementation \
       perl-module-runtime \
       perl-module-scandeps \
       perl-net-ssleay \
       perl-net-dns \
       perl-package-stash \
       perl-package-stash-xs \
       perl-parse-recdescent \
       perl-readonly \
       perl-regexp-common \
       perl-term-readkey \
       perl-test-fatal \
       perl-test-mockobject \
       perl-test-pod \
       perl-test-requires \
       perl-test-nowarnings \
       perl-test-deep \
       perl-try-tiny \
       perl-uri \
       perl-file-tail

    sudo /usr/bin/vendor_perl/cpanm Mail::IMAPClient Unicode::String Sys::MemInfo

    ./imapsync  # should display help if installed correctly.
    ```

=== "[Debian][c]"
    ``` bash
    git clone https://github.com/imapsync/imapsync

    # Dependency / Pre-requisite list.
    ./INSTALL.d/prerequisities_imapsync

    # Perl dependencies
    apt install libio-tee-perl \
       libmail-imapclient-perl \
       libterm-readkey-perl \
       libunicode-string-perl \
       libcrypt-openssl-rsa-perl \
       libdata-uniqid-perl \
       libjson-perl \
       liblwp-online-perl \
       libreadonly-perl \
       libfile-copy-recursive-perl \
       libio-socket-inet6-perl \
       libsys-meminfo-perl \
       libregexp-common-perl \
       libfile-tail-perl \
       libauthen-ntlm-perl \
       libcgi-pm-perl \
       libclass-load-perl \
       libcrypt-ssleay-perl \
       libdigest-hmac-perl \
       libdist-checkconflicts-perl \
       libencode-imaputf7-perl \
       libio-compress-perl \
       libio-socket-ssl-perl \
       libmodule-scandeps-perl \
       libnet-dbus-perl \
       libnet-ssleay-perl \
       libpar-packer-perl \
       libtest-fatal-perl \
       libtest-mock-guard-perl \
       libtest-mockobject-perl \
       libtest-pod-perl \
       libtest-requires-perl \
       libtest-simple-perl \
       liburi-perl \
       libtest-nowarnings-perl \
       libtest-deep-perl \
       libtest-warn-perl \
       libjson-webtoken-perl \
       cpanminus \
       make

    ./imapsync  # should display help if installed correctly.
    ```

### Create password files.
``` bash
# Create a security imapsync config directory.
mkdir -p ~/.config/imapsync && chmod 0700 ~/.config/imapsync
vim .config/imapsync/{gmail,personal}

# Set gmail Application password and lockdown file.
# https://myaccount.google.com/apppasswords
chmod 0400 ~/.config/imapsync/gmail

# Set personal mail server password and lock file.
chmod 0400 ~/.config/imapsync/personal
```

## Test Sync
``` bash
./imapsync --dry \
  --host1 imap.gmail.com --port1 993 --user1 {USER}@gmail.com \
    --passfile1 ~/.config/imapsync/gmail --ssl1 \
  --host2 {YOUR IMAP SERVER} --port2 993 --user2 {USER}@example.com \
    --passfile2 ~/.config/imapsync/personal --ssl2 \
  --subfolder2 gmail-archive --minage 30 --exitwhenover 2500000000 \
  --delete --expunge1
```

* This will sync mail older than 30 days, and remove it from [gmail][d].
* Gmail has a download limit of 2.5GB a day. Will safely exit when reached.
* Ensure connections work, folders are identified, and local folder is set
  properly.

## Install Service
``` bash
mkdir -p ~/.config/systemd/user
```

!!! abstract "~/.config/systemd/user/gmail-sync.service"
    0644 {USER}:{USER}

    ``` toml
    [Unit]
    Description=Gmail to IMAP Sync Service
    After=network.target

    [Service]
    Type=oneshot
    # Use full paths and remove --dry.
    ExecStart=/opt/imapsync/imapsync \
        --host1 imap.gmail.com --port1 993 --user1 {USER}@gmail.com \
        --passfile1 /home/{USER}/.config/imapsync/gmail --ssl1 \
        --host2 {IMAP SERVER} --port2 993 --user2 {USER}@example.com \
        --passfile2 /home/{USER}/.config/imapsync/personal --ssl2 \
        --subfolder2 gmail-archive --minage 30 --exitwhenover 2500000000 \
        --delete --expunge1 \
        --nolog

    # Disable logging.
    # StandardOutput=null
    # StandardError=null
    ```

!!! abstract "~/.config/systemd/user/gmail-sync.timer"
    0644 {USER}:{USER}

    ``` toml
    [Unit]
    Description=Daily Gmail to IMAP Sync Timer

    [Timer]
    OnCalendar=*-*-* 03:00:00
    Persistent=true

    [Install]
    WantedBy=timers.target
    ```

``` bash
# Enable user gmail sync.
systemctl --user daemon-reload
systemctl --user enable --now gmail-sync.timer
```

## Reference[^1][^2]
[^1]: https://askubuntu.com/questions/539102/error-install-imapsync
[^2]: https://blog.christosoft.de/2015/03/maildir-remove-duplicates

[a]: https://github.com/imapsync/imapsync
[b]: https://imapsync.lamiral.info/INSTALL.d/INSTALL.ArchLinux.txt
[c]: https://imapsync.lamiral.info/INSTALL.d/INSTALL.Debian.txt
[d]: https://imapsync.lamiral.info/FAQ.d/FAQ.Gmail.txt