Dovecot Setup
-------------
Mail Delivery Agent (MDA) Setup.

Ubunutu 16.04

1. [Standard Definitions](#standard-definitions)
1. [Base dovecot Installation](#base-dovecot-installation)
1. [Testing dovecot](#testing-dovecot)
1. [Adding a user/password for imap.passwd](#adding-a-userpassword-for-imappasswd)
1. [Setting Up Server-Side Mail Filtering (sieve)](#setting-up-server-side-mail-filtering-sieve)
1. [Migrating from Courier to Dovecot](#migrating-from-courier-to-dovecot)

Standard Definitions
--------------------
* MTA = Mail Transport Agent: handles mail server to server (e.g. other domains)
* MDA = Mail Delivery Agent: handles user access to email (e.g. IMAP)
* MUA = Mail User Agent: user client to check email (e.g. thunderbird/outlook)
* Disable ports **25/465/993** on firewall until configuration is final
  otherwise you may get email delivered while you are configuring server
* example.com = your primary domain
* example2.com = your secondary domain, if applicable
* X.X.X.X/24 = your server subnet (this is defaulting to a class C CIDR)
* user = a local linux user account
* alias@example.com = an email address (alias) for a given domain

Base [dovecot Installation][5]
-------------------------
This will configure dovecot as an IMAPS server, disabling POP and non-SSL
connections. Accounts are based off of local accounts, using non-local passwords
for authentication.

Sieve is used to do server-side mailbox filtering, in additional to what the MTA
already does. This allows for vacation messages as well as custom filtering and
responses.

Other templates for installations are [here][1] and [here][4]

```bash
sudo apt remove --purge dovecot-core dovecot-imapd
sudo rm -rfv /etc/dovecot
sudo apt install dovecot-core dovecot-imapd dovecot-sieve dovecot-managesieved
```

* Create SSL certificate
* Hostname: YOUR_HOSTNAME

#### /etc/postfix/main.cf
```config
mailbox_command = /usr/lib/dovecot/deliver
````

#### /etc/dovecot/conf.d/10-master.conf
```config
# Postfix smtp-auth
unix_listener /var/spool/postfix/private/auth {
  mode = 0666
}

service imap-login {
  inet_listener imap {
    port = 0
  }
  inet_listener imaps {
    port = 993
    ssl = yes
  }
}

service pop3-login {
  inet_listener pop3 {
    port = 0
  }
  inet_listener pop3s {
    port = 0
    ssl = yes
  }
}
```

#### /etc/dovecot/conf.d/10-auth.conf
```config
auth_mechanisms = plain login
#!include auth-system.conf.ext
!include auth-passwdfile.conf.ext
```

#### /etc/dovecot/conf.d/10-mail.conf
```config
mail_location: maildir:/home/%u/Maildir
```

#### /etc/dovecot/conf.d/10-ssl.conf
```config
ssl = required
ssl_cert = </etc/dovecot/dovecot.pem
ssl_key = </etc/dovecot/private/dovecot.pem
```

*	These certs can be the same as postfix, useful when you get valid certs
* The </ is not a mistake, it is required to specify file location

#### /etc/dovecot/conf.d/15-lda.conf
```config
postmaster_address = postmaster@%d
Protocol lda {
  mail_plugins = $mail_plugins
}
```

#### /etc/dovecot/conf.d/20-imap.conf
```config
protocol imap {
  imap_client_workarounds = tb-extra-mailbox-sep
}
```

#### [/etc/dovecot/conf.d/auth-passwdfile.conf.ext][7]
```config
passdb {
  driver = passwd-file
  args = scheme=SHA512-CRYPT username_format=%u /etc/imap.passwd
}

userdb {
  driver = passwd-file
  args = username_format=%u /etc/imap.passwd
}
```

```bash
sudo touch /etc/imap.passwd
sudo chown dovecot:dovecot /etc/imap.passwd
sudo chmod 0400 /etc/imap.passwd
sudo postconf -e 'smtpd_sasl_type = dovecot'
sudo postconf -e 'smtpd_sasl_auth_enable = yes'
sudo postconf -e 'smtpd_recipient_restrictions = permit_sasl_authenticated,permit_mynetworks,reject_unauth_destination'
sudo postconf -e 'smtpd_sasl_path = private/auth'
sudo service postfix restart
sudo service dovecot restart
```
*	Restarting postfix will pickup dovecot as the MDA instead of postfix/maildir (dovecot still delivers to maildir)
*	LDA (local delivery agent) is what dovecot uses for it’s MDA; it also provides imaps
*	Tailing mail.log and watching for incoming message delivery, should be sent to /usr/lib/dovecot/deliver and appear in your maildir

Testing dovecot
---------------
These are basic tests to ensure dovecot is working properly as an IMAPS MDA.

```bash
telnet localhost 25
ehlo localhost
```

* Should see a 250 auth plain login, if so then SASL dovecot setup for postfix properly

```bash
telnet localhost imap2
C logout
```

*	Should get a * OK [list of capabilities] Dovecot (ubuntu) ready.
*	C logout to quit

```bash
telnet localhost 143
telnet localhost 110
telnet localhost 995
openssl s_client -connect localhost:993
openssl s_client -starttls smtp -crlf -connect localhost:465
```

*	telnet (non-encrypted) logins should fail (imap, pop3, pop3s)
*	openssl logins should present certificate, connection (imaps)
*	C logout to quit

Adding a [user/password for imap.passwd][9]
-------------------------------------------
This will add a separate IMAP password for a [given user][6], instead of using
their main account password. This [file is formatted exactly like
[/etc/passwd][8], but password is included and no login shell is required. The
IMAP password created should be different from the login password for that user.

```bash
doveadm pw -s SHA512-CRYPT
```
*	Copy full hash, including hashtype

#### /etc/imap.passwd
```config
<username>:<passwordhash>:UID from /etc/passwd:GID from /etc/passwd::<home directory>
```

Setting Up [Server-Side Mail Filtering (sieve)][10]
---------------------------------------------------
This will enable users to setup server-side per-mailbox filters that are applied
automatically when email is [delivered by the MDA][11], which removes the need
for the user to setup a filtering on each MUA they use. This is in addition to
any filtering already applied at the MTA level.

Sieve filtering uses a [standard mail filtering language][12] and is [fairly
easy to learn][13].

#### /etc/dovecot/conf.d/15-lda.conf
```config
postmaster_address = postmaster@%d
Protocol lda {
  mail_plugins = $mail_plugins sieve
}
```

#### /etc/dovecot/conf.d/90-sieve.conf
```config
Plugin {
  sieve = file:~/sieve;active=~/.dovecot.sieve
  sieve_default = /var/lib/dovecot/sieve/default.sieve
  # Disable implicit recipient validation before responding to vacation messages
  # otherwise, vacation messages are not sent, as there are multiple emails to
  # a given email account in this example. You should have this disabled unless
  # needed.
  sieve_vacation_dont_check_recipient = yes
}
```

```bash
sudo mkdir -p /var/lib/dovecot/sieve
sudo chown -R dovecot:dovecot /var/lib/dovecot
sudo chmod 755 /var/lib/dovecot /var/lib/dovecot/sieve
```

### [/var/lib/dovecot/sieve/default.sieve](default.sieve)

* This is an example sieve filter that will allow certain emails through to that
  user, and reject all others with an autoresponder. Any emails not sent to a
  specific email address are filtering into an alternative inbox.
*	Run sievec to compile script for sieve to use (will expose any errors in script)

```bash
sudo sievec /var/lib/dovecot/sieve/default.sieve
```

* You should see sieve entries on incoming mail in the /var/log/mail.log

Migrating from [Courier to Dovecot][3]
--------------------------------------
This will convert Courier IMAP states to Dovecot IMAP states. An alternative
script is located [here][2]

[1]: https://help.ubuntu.com/community/PostfixDovecotSASL
[2]: https://pario.no/2007/05/17/courier-imap-to-dovecot-migration-script/
[3]: http://wiki.dovecot.org/Migration/Courier
[4]: http://www.townx.org/index.php?q=blog/elliot/simple_spamassassin_setup_with_postfix_and_dovecot_on_ubuntu_breezy
[5]: http://www.binarytides.com/install-postfix-dovecot-debian/
[6]: http://wiki.dovecot.org/VirtualUsers
[7]: http://wiki.dovecot.org/Authentication/PasswordSchemes
[8]: http://wiki.dovecot.org/AuthDatabase/PasswdFile
[9]: http://wiki.dovecot.org/HowTo/SimpleVirtualInstall
[10]: http://dikant.de/2012/05/21/setting-up-server-side-mail-filtering/
[11]: http://wiki2.dovecot.org/Pigeonhole
[12]: https://easyengine.io/tutorials/mail/server/sieve-filtering/
[13]: https://tty1.net/blog/2011/sieve-tutorial_en.html