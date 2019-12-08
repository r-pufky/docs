.. _service-postfix:

Postfix
#######
Mail Transport Agent (MTA) setup

Uses :ref:`debian-server-base-install`. See :ref:`service-dovecot-glossary` for
mail term definitions.

Standard Definitions
********************
* Disable ports **25 (smtp)/587 (smtps)/993 (imaps)** on firewall until
  configuration is final otherwise you may get email delivered while you are
  configuring server.
* example.com = your primary domain.
* example2.com = your secondary domain, if applicable.
* X.X.X.X/24 = your server subnet (this is defaulting to a class C CIDR).
* user = a local linux user account.
* alias@example.com = an email address (alias) for a given domain.

`Postfix Setup`_
****************
Remove existing email MTA's and start fresh.

.. code-block:: bash
  :caption: Install Postfix Dependencies.

  sudo apt remove --purge exim4 exim4-base exim4-config exim4-daemon-light postfix
  sudo rm -rfv /etc/postfix
  sudo apt install sasl2-bin postfix postgrey postfix-policyd-spf-python spamc spamassassin

.. ggui:: Configuration Options
  :option:  Internet site,
            mynetworks,
            Defaults,
            Accept mail for
  :setting: example.com,
            {Add local server network in CIDR format X.X.X.X/24},
            Accept Defaults,
            localhost
  :no_key_title:
  :no_section:
  :no_launch:

.. code-block:: bash
  :caption: **0644 root root** ``/etc/default/saslauthd``

  START=yes

.. code-block:: bash
  :caption: Enable SASL and Add Options.

  sudo service saslauthd start
  sudo postconf -e “myhostname = example.com”
  sudo postconf -e “mydestination = localhost, mail.example.com, example.com, example2.com, mail.example2.com, localhost.localdomain”
  sudo postconf -e “mynetworks = 127.0.0.0/8 [::ffff:127.0.0.0]/104 [::1]/128 X.X.X.X/24”
  sudo postconf -X “alias_maps”
  sudo postconf -e “virtual_alias_maps = hash:/etc/postfix/virtual”
  sudo postconf -e “home_mailbox = Maildir/”
  sudo postconf -e “mailbox_command = “

.. code-block:: bash
  :caption: **0644 root root** ``/etc/postfix/master.cf``

  smtps  inet  n       -       -       -       -       smtpd

.. note::
  Uncomment this line in the first section of the master.cf file; enables
  ``smtps/465`` for MUA's.

  On newer versions of postfix, you might get a chroot warning. This is because
  it was not specified originally. Set all of these to **n**, unless explicitly
  **y**.

`Configuring email Aliases for Users`_
**************************************
.. code-block:: bash
  :caption: **0644 root root** ``/etc/postfix/virtual``

  alias1@example.com user
  alias2@example.com user
  alias1@example2.com user
  alias3@example.com blackhole@localhost
  @example.com user

.. note::
  ``blackhole@localhost`` will accept mail for specific address, and deliver
  locally to ``/dev/null``.

  ``@example.com user`` is a `catchall for domains`_ and delivers to user.

.. code-block:: bash
  :caption: **0644 root root** ``/etc/aliases``

  blackhole:/dev/null

.. note::
  Add at end of file. See `blackhole an entire domain`_.

.. code-block:: bash
  :caption: Regenerate aliases and restart postfix to pickup changes.

  sudo newaliases
  sudo postmap /etc/postfix/virtual
  sudo service postfix restart

.. note::
  ``postmap`` creates a db from the virtual file used to process mail.

`Testing Initial postfix Setup`_
********************************
.. code-block:: bash
  :caption: Telnet to postfix to test sending an email.

  telnet localhost 25
  ehlo localhost
  mail from: root@localhost
  rcpt to: user@localhost
  data
  Subject: postfix text
  testing mail from postfix
  .
  quit

* Should receive ``220`` from the server if working when initially connecting.
* type ``.``, {ENTER}, then ``quit`` to send mail.
* Verify email sent is received (``mail`` command works here).
* Send email from another account (like gmail), verify received again. This
  should use one of the aliases created, also ensure ports are opened.

`Installing postgrey`_
**********************
Postgrey will graylist senders (e.g. will initially reject non-certified MTA
senders and wait for them to reconnect). This will remove a bunch of spammers
that will only connect once and move on.

.. code-block:: bash
  :caption: **0644 root root** ``/etc/default/postgrey``

  POSTGREY_OPTS="--inet=10023 --delay=60"

.. note::
  Reduce default graylist from ``300`` seconds to ``60``. Can verify ports by
  checking ``/var/log/mail.log``.

.. code-block:: bash
  :caption: Add postgrey to postfix configuration and reload.

  sudo postconf -e 'smtpd_recipient_restrictions = permit_sasl_authenticated,permit_mynetworks,reject_unauth_destination,check_policy_service inet:127.0.0.1:10023'
  sudo service postfix reload
  sudo service postgrey restart
  sudo tail -F /var/log/mail.log

.. note::
  Ports should match port defined in ``/etc/default/postgrey``. Greylisting is
  logged in ``/var/log/mail.log``.

`Installing Sender Policy Framework (SPF) Validation`_
******************************************************
This will enable our MTA to verify that the sending MTA is from an authorized
host for that domain, via DNS.

.. code-block:: bash
  :caption: Set a hard upper limit of one hour.

  sudo postconf -e “policy-spf_time_limit = 3600s”

.. code-block:: bash
  :caption: **0644 root root** ``/etc/postfix/master.cf``

  # Enable SPF validation for receiving email
  policy-spf  unix  -       n       n       -       -       spawn
       user=nobody argv=/usr/bin/policyd-spf

.. note::
  Place this command in the first section of services near the bottom, before
  the *Interfaces to non-Postfix* software section.

  Make sure to use a newline and two spaces for ``user=`` line.

.. code-block:: bash
  :caption: Enable SPF and reload.

  sudo postconf -e 'smtpd_recipient_restrictions = permit_sasl_authenticated,permit_mynetworks,reject_unauth_destination,check_policy_service inet:127.0.0.1:10023,check_policy_service unix:private/policy-spf'
  sudo service postfix reload
  sudo tail -F /var/log/mail.log

.. note::
  * ``check_policy_service`` needs to appear after ``permit_mynetworks`` to
    enable local non-SPF validated local email to send.
  * Send a test mail to a hosted domain and from a hosted domain.
  * SPF validation will appear as ``policyd-spf[PID]:`` with pass, none or fail
    if working properly.

`Installing spamassassin`_
**************************
This will automatically filter detected spam and deal with it how you wish. In
this setup, it is sent to the users spam folder, which is used to train
spamassassin for better future accuracy.

Learning (training) is accomplished via the `sa-learn utility`_.

.. code-block:: bash
  :caption: Add spamassassin user.

  sudo groupadd spamd
  sudo useradd -g spamd -s /bin/false -d /var/log/spamassassin spamd
  mkdir /var/log/spamassassin
  chown spamd:spamd /var/log/spamassassin

.. literalinclude:: source/spamassassin
  :caption: **0644 spamd spamd** ``/etc/default/spamassassin``

.. code-block:: bash
  :caption: **0644 spamd spamd** ``/etc/spamassassin/local.cf``

  # Set the threshold at which a message is considered spam (default: 5.0)
  #
  required_score 3.0

.. note::
  This is the only changed line in this file.

.. code-block:: bash
  :caption: Start spamassassin service.

  sudo service spamassassin start
  sudo systemctl enable spamassassin.service

.. code-block:: bash
  :caption: **0644 root root** ``/etc/postfix/master.cf``

  smtp      inet  n       -       -       -       -       smtpd
          -o content_filter=spamassassin

.. note::
  This is the first line in the ``master.cf`` configuration file.

  Make sure to use a newline and two spaces for ``-o`` line.

.. code-block:: bash
  :caption: **0644 root root** ``/etc/postfix/master.cf``

  spamassassin unix -     n       n       -       -       pipe
          user=spamd argv=/usr/bin/spamc -f -e
          /usr/sbin/sendmail -oi -f ${sender} ${recipient}

.. note::
  This is the last line in the ``master.cf`` configuration file.

  Make sure to use a newline and two spaces for additional lines.

.. code-block:: bash
  :caption: Reload postfix and train spamassassin.

  sudo postfix reload
  sudo sa-learn --spam -u spamd --dir /home/user/Maildir/.spam/* -D
  sudo sa-learn --ham -u spamd --dir /home/user/Maildir/.some_valid_mails/* -D
  sudo tail -f /var/log/mail.log

.. note::
  * ``--spam`` will do initial training for spamassassin on known spam mail.
  * ``--ham`` will do initial training for spamassassin on known good mail.
  * In the logs, you should see ``relay=spamassassin`` for messages coming in,
    which means it is sending it to spamassassin correctly (sending a test mail
    from an external account works well).

.. tip::
  ``sa-learn --backup > backup.txt; sa-learn --restore backup.txt`` to backup
  database and restore it.

Disable Login Notifications for Email
*************************************
Remove *you have new mail.* when you login to the mail host.

.. code-block:: bash
  :caption: **0644 root root** ``/etc/pam.d/login``

  session  optional  pam_mail.so nopen

.. code-block:: bash
  :caption: **0644 root root** ``/etc/pam.d/sshd``

  session  optional  pam_mail.so nopen noenv # [1]


.. _Postfix Setup: https://help.ubuntu.com/community/PostfixBasicSetupHowto
.. _Configuring email Aliases for Users: http://postfix.1071664.n5.nabble.com/How-to-delete-a-key-via-postconf-td3692.html
.. _catchall for domains: http://www.cyberciti.biz/faq/howto-setup-postfix-catch-all-email-accounts/
.. _blackhole an entire domain: http://madphilosopher.ca/2006/09/how-to-send-an-entire-domain-to-dev-null-in-postfix/
.. _Testing Initial postfix Setup: https://qmail.jms1.net/test-auth.shtml
.. _Installing postgrey: https://help.ubuntu.com/community/PostfixGreylisting
.. _Installing Sender Policy Framework (SPF) Validation: https://help.ubuntu.com/community/Postfix/SPF
.. _Installing spamassassin: http://www.debuntu.org/postfix-and-spamassassin-how-to-filter-spam/
.. _sa-learn utility: https://spamassassin.apache.org/full/3.1.x/doc/sa-learn.html