imapsync setup
---------------------
Syncing from gmail to local imap server

ubuntu 16.04

### clone imapsync from [github][1]
```bash
git clone https://github.com/imapsync/imapsync
```

### Install [perl dependencies][2]
```bash
  sudo apt-get install libio-tee-perl libmail-imapclient-perl
  libterm-readkey-perl libunicode-string-perl libcrypt-openssl-rsa-perl
  libdata-uniqid-perl libjson-perl liblwp-online-perl libreadonly-perl
```

### Create secured password files, enter passwords
```bash
  touch .ssh/imapsync_{local,remote}
  chmod 0600 .ssh/imapsync_{local,remote}
```
  * Remote server is gmail, uses application specific password. [Setup here.][4]
  * Local server is your personal IMAP server. Use IMAP password.
  * We use .ssh directory here since it's already secured.

### Set password files readonly
```bash
  chmod 0400 .ssh/imapsync_{local,remote}
```

### Test sync to ensure connecting properly
```bash
  ./imapsync --dry --host1 imap.gmail.com --port1 993 --user1 
  **GMAIL_EMAIL_USER** --passfile1 ~/.ssh/imapsync_remote --ssl1 --host2
  **YOUR_IMAP_SERVER** --port2 993 --user2
  **LOCAL_IMAP_USER** --passfile2 ~/.ssh/imapsync_local --sslargs2
  SSL_verify_mode=0 --ssl2 --subfolder2 gmail-archive --minage
  30 --exitwhenover 2500000000 --delete --expunge1
```
  * This will sync mail older than 30 days, and remove it from [gmail][3]
  * Gmail has a download limit of 2.5GB's a day, this will safetly exit when 
    reached
  * SSL Verification is disabled for local IMAP (assuming self-signed cert) -
    this will allow for MITM attacks, you should get a [letsencrypt cert][5] 
	and	remove this
  * Ensure connections work, folders are identified, and local folder is set
    properly

### Install imapsync to /opt/imapsync
```bash
  sudo git checkout-index -a -f --prefix=/opt/imapsync/
```
  * Set /opt/imapsync permissions according to your system, ensure imapsync 
    is executable

### Create bash script using /opt/imapsync, typically in ~/bin
```bash
  #!/bin/bash

  /opt/imapsync/imapsync --host1 imap.gmail.com --port1 993 --user1 \
  **GMAIL_EMAIL_USER** --passfile1 ~/.ssh/imapsync_remote --ssl1 --host2 \
  **YOUR_IMAP_SERVER --port2 993 --user2 **YOUR_IMAP_USER** --passfile2 \
  ~/.ssh/imapsync_local --sslargs2 SSL_verify_mode=0 --ssl2 --subfolder2 \
  gmail-archive --minage 30 --exitwhenover 2500000000 --delete --expunge1 \
  --nolog &>/dev/null
```

### Add to [local crontab][6] to run nightly
```crontab
  * 3 * * * ~/bin/gmail_to_imap_sync
```

[1]: https://github.com/imapsync/imapsync
[2]: http://askubuntu.com/questions/539102/error-install-imapsync
[3]: http://imapsync.lamiral.info/FAQ.d/FAQ.Gmail.txt
[4]: https://security.google.com/settings/security/apppasswords
[5]: https://letsencrypt.org/
[6]: https://en.wikipedia.org/wiki/Cron