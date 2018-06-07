Postfix Setup
-------------
Mail Transport Agent (MTA) setup

Ubunutu 16.04


1. [Standard Definitions](#standard-definitions)
2. [Base postfix Setup](#base-postfix-setup)
3. [Configuring email Aliases for Users](#configuring-email-aliases-for-users)
4. [Testing Initial postfix Setup](#testing-initial-postfix-setup)
3. [Installing postgrey](#installing-postgrey)
4. [Installing Sender Policy Framework (SPF) Validation](#installing-sender-policy-framework-spf-validation)
5. [Installing spamassassin](#installing-spamassassin)
6. [Disable Login notifications for Email](#disable-login-notifications-for-email)

Standard Definitions
--------------------
* MTA = Mail Transport Agent: handles mail server to server (e.g. other domains)
* MDA = Mail Delivery Agent: handles user access to email (e.g. IMAP)
* MUA = Mail User Agent: user client to check email (e.g. thunderbird/outlook)
* Disable ports **25 (smtp)/587 (smtps)/993 (imaps)** on firewall until configuration is final 
  otherwise you may get email delivered while you are configuring server
* example.com = your primary domain
* example2.com = your secondary domain, if applicable
* X.X.X.X/24 = your server subnet (this is defaulting to a class C CIDR)
* user = a local linux user account
* alias@example.com = an email address (alias) for a given domain

[Base postfix Setup][1]
-----------------------
Remove existing email MTA's and start fresh.
### Install Postfix Dependencies
```bash
sudo apt remove --purge exim4 exim4-base exim4-config exim4-daemon-light postfix
sudo rm -rfv /etc/postfix
sudo apt install sasl2-bin postfix postgrey postfix-policyd-spf-python spamc spamassassin
```
* Internet site: example.com
* mynetworks: Add local server network in CIDR format X.X.X.X/24
* Defaults
* Accept mail for: localhost

#### /etc/default/saslauthd
```config
START=yes
```
```bash
sudo service saslauthd start
sudo postconf -e “myhostname = example.com”
sudo postconf -e “mydestination = localhost, mail.example.com, example.com, example2.com, mail.example2.com, localhost.localdomain”
sudo postconf -e “mynetworks = 127.0.0.0/8 [::ffff:127.0.0.0]/104 [::1]/128 X.X.X.X/24”
sudo postconf -X “alias_maps”
sudo postconf -e “virtual_alias_maps = hash:/etc/postfix/virtual”
sudo postconf -e “home_mailbox = Maildir/”
sudo postconf -e “mailbox_command = “
```

#### /etc/postfix/master.cf
```config
smtps  inet  n       -       -       -       -       smtpd
```
* Uncomment this line in the first section of the master.cf file; enables
  smtps/465 for MUA's
* On newer versions of postfix, you might get a chroot warning. This is because
  it was not specified originally. Set all of these to **n**, unless explicitly
  **y**

[Configuring email Aliases for Users][2]
----------------------------------------
#### /etc/postfix/virtual
```config
alias1@example.com user
alias2@example.com user
alias1@example2.com user
alias3@example.com blackhole@localhost
@example.com user
```
* blackhole@localhost will accept mail for specific address, and deliver locally
  to /dev/null
* *@example.com user* is a catchall for domains and delivers to user

#### [/etc/aliases][4]
```config
blackhole:/dev/null
```
* Added at end of file

```bash
sudo newaliases
sudo postmap /etc/postfix/virtual
sudo service postfix restart
```
* postmap creates a db from the virtual file used to process mail

[Testing Initial postfix Setup][5]
----------------------------------
```bash
telnet localhost 25
ehlo localhost
mail from: root@localhost
rcpt to: user@localhost
data
Subject: postfix text
testing mail from postfix
.
quit
```
* Should receive 220 from the server if working when initially connecting
* type . then newline then quit to send mail
* Verify email sent is received (mail command works here)
* Send email from another account (like gmail), verify received again. This
  should use one of the aliases created, also ensure ports are opened

[Installing postgrey][6]
------------------------
Postgrey will graylist senders (e.g. will initially reject non-certified MTA
senders and wait for them to reconnect). This will remove a bunch of spammers
that will only connect once and move on.

#### /etc/default/postgrey
```config
POSTGREY_OPTS="--inet=10023 --delay=60"
```
* Reduce default graylist from 300 seconds to 60
* Can verify ports by checking /var/log/mail.log

```bash
sudo postconf -e 'smtpd_recipient_restrictions = permit_sasl_authenticated,permit_mynetworks,reject_unauth_destination,check_policy_service inet:127.0.0.1:10023'
sudo service postfix reload
sudo service postgrey restart
sudo tail -F /var/log/mail.log
```
* Note ports should match port defined in /etc/default/postgrey
* Greylisting is logged in /var/log/mail.log

[Installing Sender Policy Framework (SPF) Validation][7]
--------------------------------------------------------
This will enable our MTA to verify that the sending MTA is from an authorized
host for that domain, via DNS.

```bash
sudo postconf -e “policy-spf_time_limit = 3600s”
```

#### /etc/postfix/master.cf
```config
# Enable SPF validation for receiving email
policy-spf  unix  -       n       n       -       -       spawn
     user=nobody argv=/usr/bin/policyd-spf
```
* Place this command in the first section of services near the bottom, before the
  _Interfaces to non-Postfix_ software section.
* Newline, two spaces for user= line.

```bash
sudo postconf -e 'smtpd_recipient_restrictions = permit_sasl_authenticated,permit_mynetworks,reject_unauth_destination,check_policy_service inet:127.0.0.1:10023,check_policy_service unix:private/policy-spf'
sudo service postfix reload
sudo tail -F /var/log/mail.log
```
* check_policy_service needs to appear after permit_mynetworks to enable local
  non-SPF validated local email to send
* Send a test mail to a hosted domain and from a hosted domain
* SPF validation will appear as “policyd-spf[PID]:” with pass, none or fail if
  working properly

[Installing spamassassin][8]
----------------------------
This will automatically filter detected spam and deal with it how you wish. In
this setup, it is sent to the users spam folder, which is used to train
spamassassin for better future accuracy.

Learning (training) is accomplished via the [sa-learn utility][9].

```bash
sudo groupadd spamd
sudo useradd -g spamd -s /bin/false -d /var/log/spamassassin spamd
mkdir /var/log/spamassassin
chown spamd:spamd /var/log/spamassassin
```

#### /etc/default/spamassassin
```config
# /etc/default/spamassassin
# Duncan Findlay

# WARNING: please read README.spamd before using.
# There may be security risks.

# Change to one to enable spamd
ENABLED=1

# Options
# See man spamd for possible options. The -d option is automatically added.

# SpamAssassin uses a preforking model, so be careful! You need to
# make sure --max-children is not set to anything higher than 5,
# unless you know what you're doing.

SAHOME="/var/log/spamassassin/"

#OPTIONS="--create-prefs --max-children 5 --helper-home-dir"
OPTIONS="--create-prefs --max-children 2 --username spamd -H ${SAHOME} -s ${SAHOME}spamd.log"

# Pid file
# Where should spamd write its PID to file? If you use the -u or
# --username option above, this needs to be writable by that user.
# Otherwise, the init script will not be able to shut spamd down.
PIDFILE="/var/run/spamd.pid"

# Set nice level of spamd
#NICE="--nicelevel 15"

# Cronjob
# Set to anything but 0 to enable the cron job to automatically update
# spamassassin's rules on a nightly basis
CRON=0
```

#### /etc/spamassassin/local.cf
```config
# Set the threshold at which a message is considered spam (default: 5.0)
#
required_score 3.0
```

* This is the only changed line in this file

```bash
sudo service spamassassin start
sudo systemctl enable spamassassin.service
```

#### /etc/postfix/master.cf
```config
smtp      inet  n       -       -       -       -       smtpd
        -o content_filter=spamassassin
```

* This is the first line in the master.cf configuration
* Newline, two spaces for -o line.

#### /etc/postfix/master.cf
```config
spamassassin unix -     n       n       -       -       pipe
        user=spamd argv=/usr/bin/spamc -f -e  
        /usr/sbin/sendmail -oi -f ${sender} ${recipient}
```

* This is the last line (EOF) in the master.cf configuration
* Newline, two spaces for additional lines.

```bash
sudo postfix reload
sudo sa-learn --spam -u spamd --dir /home/user/Maildir/.spam/* -D
sudo sa-learn --ham -u spamd --dir /home/user/Maildir/.some_valid_mails/* -D
sudo tail -f /var/log/mail.log
```

* --spam will do initial training for spamassassin on known spam mail
* --ham will do initial training for spamassassin on known good mail
* In the logs, you should see relay=spamassassin for messages coming in, which
  means it’s sending it to spamassassin correctly (sending a test mail from an
  external account works well)
* sa-learn --backup > backup.txt; sa-learn --restore backup.txt to backup
  database and restore it


Disable Login notifications for Email
-------------------------------------
#### /etc/pam.d/login
```config
session  optional  pam_mail.so nopen
```

#### /etc/pam.d/sshd
```config
session  optional  pam_mail.so nopen noenv # [1]
```

[1]: https://help.ubuntu.com/community/PostfixBasicSetupHowto
[2]: http://postfix.1071664.n5.nabble.com/How-to-delete-a-key-via-postconf-td3692.html
[3]: http://www.cyberciti.biz/faq/howto-setup-postfix-catch-all-email-accounts/
[4]: http://madphilosopher.ca/2006/09/how-to-send-an-entire-domain-to-dev-null-in-postfix/
[5]: https://qmail.jms1.net/test-auth.shtml
[6]: https://help.ubuntu.com/community/PostfixGreylisting
[7]: https://help.ubuntu.com/community/Postfix/SPF
[8]: http://www.debuntu.org/postfix-and-spamassassin-how-to-filter-spam/
[9]: https://spamassassin.apache.org/full/3.1.x/doc/sa-learn.html
