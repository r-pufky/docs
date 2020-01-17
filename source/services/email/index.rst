.. _service-email:

Email
#####
Self-hosted complete postfix email stack.

This setup will focus on creating a docker-based postfix/dovecot email stack,
hosting email for multiple domains using Let's Encrypt.

You must be able to setup DNS for your domain to use the security options.

See `Email Docker and Documentation`_.

For more in-depth configuration (or non-docker email stack) see
:ref:`service-postfix` and :ref:`service-dovecot` detailed configuration.

.. _service-mail-ports:

.. gport:: Ports (Email)
  :port:     25,
             587,
             993
  :protocol: TCP,
             TCP,
             TCP
  :type:     Exposed,
             Exposed,
             Exposed
  :purpose:  SMTP Mail Relay.,
             SMTP Mail Submission Port.,
             IMAPS Port.
  :no_key_title:
  :no_caption:
  :no_launch:

.. gflocation:: Important File Locations (Email)
  :file:    /var/mail,
            /var/mail-state,
            /var/log/mail,
            /tmp/docker-mailserver,
            /etc/letsencrypt
  :purpose: Email storage location.,
            Mail server state.,
            Mail logs.,
            Mail configuration files.,
            Let's Encrypt certificates to use for SSL.
  :no_key_title:
  :no_caption:
  :no_launch:

Docker Creation
***************
Run a simple email stack that will pass email server legitimacy tests.

.. code-block:: yaml
  :caption: Docker Compose

  mail:
    image: tvial/docker-mailserver:latest
    hostname: mail
    domainname: {DOMAIN}
    container_name: mail
    stop_grace_period: 1m
    cap_add:
      - SYS_PTRACE
    restart: unless-stopped
    ports:
      - "25:25"
      - "587:587"
      - "993:993"
    environment:
      - HOSTNAME=mail
      - DOMAINNAME={DOMAIN}
      - CONTAINER_NAME=mail
      - DMS_DEBUG=0
      - ONE_DIR=1
      - POSTMASTER_ADDRESS=postmaster@{DOMAIN}.com
      - PERMIT_DOCKER=host
      - TLS_LEVEL=modern
      - SPOOF_PROTECTION=1
      - ENABLE_SRS=0
      - ENABLE_POP3=0
      - ENABLE_CLAMAV=0
      - RELAY_HOST=''
      - ENABLE_ELK_FORWARDER=0
      # If enabled, requires NET_ADMIN.
      - ENABLE_FAIL2BAN=0
      - ENABLE_MANAGESIEVE=1
      - POSTSCREEN_ACTION=enforce
      - SSL_TYPE=letsencrypt
      - POSTFIX_MAILBOX_SIZE_LIMIT=0
      - POSTFIX_MESSAGE_SIZE_LIMIT=10480000
      - REPORT_RECIPIENT=0
      - REPORT_INTERVAL=daily
      - ENABLE_SPAMASSASSIN=1
      - SA_TAG=3.0
      - SA_TAG2=6.31
      - SA_KILL=6.31
      - SA_SPAM_SUBJECT=***SPAM*****
      - ENABLE_FETCHMAIL=0
      - ENABLE_LDAP=0
      - ENABLE_POSTGREY=1
      - POSTGREY_DELAY=300
      - POSTGREY_MAX_AGE=35
      - POSTGREY_TEXT=Delayed by postgrey
      - POSTGREY_AUTO_WHITELIST_CLIENTS=0
      - ENABLE_SASLAUTHD=1
      - SASLAUTHD_MECHANISMS=dovecot
      - SRS_SENDER_CLASSES=envelope_sender,header_sender
      - TZ=TZ=America/Los_Angeles
    volumes:
      - /data/mail/data:/var/mail
      - /data/mail/state:/var/mail-state
      - /data/mail/logs:/var/log/mail
      - /data/mail/config/:/tmp/docker-mailserver/
      - /data/letsencrypt:/etc/letsencrypt:ro
      - /etc/localtime:/etc/localtime:ro

* Docker container should be run in an isolated network given the sensitive and
  exposes nature of the data and service.
* Do **not** start docker until accounts, aliases and SPF/DKIM/SSL are
  configured.

Initial Setup
*************
A `detailed step-by-step setup guide`_ walks through all of the following
configuration with more and options.

Only start the mailserver after all initial configuration has been completed,
and sufficient time has passed for DNS entries to update.

.. important::
  DNS changes should be applied to all domains on which the mail server will be
  hosting
.
Add Initial User Accounts
=========================
Actual email accounts for users. These are accounts that will be logged into.

.. code-block:: bash
  :caption: Create email accounts for initial users (can use multiple domains).

  docker run --rm -e MAIL_USER={EMAIL} -e MAIL_PASS={PASS} -ti tvial/docker-mailserver:latest /bin/sh -c 'echo "$MAIL_USER|$(doveadm pw -s SHA512-CRYPT -u $MAIL_USER -p $MAIL_PASS)"' >> /data/mail/config/postfix-accounts.cf

.. note::
  If the docker container is already running, these can be added dynamically
  using the `setup helper script`_.

  .. code-block:: bash
    :caption: Add user account to running mailserver.

    ./setup.sh email add {EMAIL} {PASS}

Add Aliases
===========
Local system aliases for mail delivery.

.. code-block:: bash
  :caption: **0600 root root** ``/data/mail/config/postfix-aliases.cf``

  blackhole: /dev/null

.. note::
  Only a `blackhole alias`_ is made to redirect specific mail to ``/dev/null``.

Add Virtual Mailboxes
=====================
Maps additional email addresses to accounts on the system. This enables a single
user to have multiple email addresses, as well as catch-alls and blackholing
known compromised email addresses.

.. literalinclude:: source/postfix-virtual.cf
  :caption: **0600 root root** ``/data/mail/config/postfix-virtual.cf``
  :emphasize-lines: 4, 7, 10

.. note::
  If the docker container is already running, these can be added dynamically
  using the `setup helper script`_.

  .. code-block:: bash
    :caption: Add additional virtual email aliases.

    ./setup.sh alias add {EMAIL} {RECIPIENT}

.. _service-mail-dkim:

Generate :term:`DKIM` Config
============================
:term:`DKIM` provides a method for validating a domain name identity that is
associated with an email message through cryptographic authentication.

.. code-block:: bash
  :caption: Generate DKIM Keys for mailserver.

  docker run --rm -v /data/mail/config:/tmp/docker-mailserver -ti tvial/docker-mailserver:latest generate-dkim-config

.. gtable:: DKIM DNS Entry
  :header: Key,
           Value
  :c0:     Record,
           Name,
           Target/Value/Data,
           TTL
  :c1:     TXT,
           mail._domainkey_.{DOMAIN}.,
           "v=DKIM1; k=rsa; " "p=AZER..." "aUIOPQSDF...",
           5 seconds
  :no_key_title:
  :no_caption:
  :no_headers:
  :no_launch:

.. note::
  The `DKIM data must be quoted`_ for it to be properly stored. The generated
  data *may* be broken across multiple lines. Just use the **content** within
  the parentheses and separate quote data with a single space. This allows the
  public key to be properly re-assembled for services that do not support large
  TXT data.

.. _service-mail-spf:

Setup :term:`SPF` Policy
========================
Setup soft-failing for SPF policy enforcment.

.. gtable:: SPF DNS Entry
  :header: Key,
           Value
  :c0:     Record,
           Name
           Target/Value/Data,
           TTL
  :c1:     TXT,
           mail.{DOMAIN}.,
           "v=spf1 mx ~all",
           300 seconds
  :no_key_title:
  :no_caption:
  :no_headers:
  :no_launch:

.. note::
  The ``MX`` for ``mail.{DOMAIN}`` must exist for this to work. see
  :ref:`service-email-dns` for all DNS entries required for functioning service.

.. tip::
  Once server is verified to work, the policy may be switched to ``enforce`` by
  changing the DNS record to: ``v-spf1 mx -all``.

.. _service-mail-dmarc:

Setup :term:`DMARC` Policy
==========================
Protects from phishing attacks by validating From fields. `Setup DMARC`_ for
quarantine of flagged emails. The mailserver will automatically configure DMARC
using the ``POSTMASTER_ADDRESS`` in the docker compose definition.

.. gtable:: DMARC DNS Entry
  :header: Key,
           Value
  :c0:     Record,
           Name
           Target/Value/Data,
           TTL
  :c1:     TXT,
           _dmarc.{DOMAIN}.,
           "v=DMARC1; p=quarantine; rua=mailto:postmaster@{DOMAIN}",
           300 seconds
  :no_key_title:
  :no_caption:
  :no_headers:
  :no_launch:

.. note::
  Use ``p=none`` to test and ensure everything is working correctly.

  ``p=reject`` is the most strict but you must ensure everything is working
  properly; this should be the default when service is live.

  All `DMARC policies`_.

Setup SSL Certificates
======================
The container will automticall setup all services correctly if provided the
appropriate Let's Encrypt certificates.

.. note::
  Explicit FQDN certificates should be created for the mail server DNS name, and
  exist in the ``letsencrypt/live``. See :ref:`service-letsencrypt-domains`
  before proceeding.

.. code-block:: yaml
  :caption: Docker Compose

  mail:
    volumes:
      - /data/letsencrypt:/etc/letsencrypt:ro

Just add the letsencrypt live directory in read-only to enable SSL connections.

Disable Unsecured Services
==========================
POP3 should not be used, and unencrypted IMAP should be disabled.

.. literalinclude:: source/dovecot.cf
  :caption: **600 root root** ``/data/mail/config/dovecot.cf``
  :emphasize-lines: 3, 6, 13, 16

.. _service-email-dns:

Setup Mail DNS Entries
======================
Setup DNS entries to allow for properly resolution of mail server. Redirect
{DOMAIN} to mail.{DOMAIN} for mail inquries.

.. gtable:: Root Domain Mail Redirect MX DNS Entry
  :header: Key,
           Value
  :c0:     Record,
           Name
           Target/Value/Data,
           TTL
  :c1:     MX,
           DOMAIN},
           10 mail.{DOMAIN}.,
           300 seconds
  :no_key_title:
  :no_caption:
  :no_headers:
  :no_launch:

.. gtable:: Mail subdomain MX DNS Entry
  :header: Key,
           Value
  :c0:     Record,
           Name
           Target/Value/Data,
           TTL
  :c1:     MX,
           {DOMAIN},
           10 {IP}.,
           300 seconds
  :no_key_title:
  :no_caption:
  :no_headers:
  :no_launch:

.. gtable:: Mail subdomain A DNS Entry
  :header: Key,
           Value
  :c0:     Record,
           Name
           Target/Value/Data,
           TTL
  :c1:     A,
           mail.{DOMAIN}.,
           10 {IP}.,
           300 seconds
  :no_key_title:
  :no_caption:
  :no_headers:
  :no_launch:

.. gtable:: Wildcard subdomain MX DNS Entry
  :header: Key,
           Value
  :c0:     Record,
           Name
           Target/Value/Data,
           TTL
  :c1:     MX,
           @.{DOMAIN}.,
           10 mail.{DOMAIN}.,
           21600 seconds
  :no_key_title:
  :no_caption:
  :no_headers:
  :no_launch:

* Ensure DKIM DNS entry exists. See :ref:`service-mail-dkim`.
* Ensure SPF DNS entry exists. See :ref:`service-mail-spf`.
* Ensure DMARC DNS entry exists. See :ref:`service-mail-dmarc`.

Test Mail Delivery
******************
Before exposing ports and validating DNS settings in
:ref:`service-mail-validation`, ensure mail server is working.

Verify Services Locked Down
===========================
.. code-block:: bash
  :caption: Test SASL service.

  telnet localhost 25
  ehlo localhost

.. note::
  Should see a ``250 auth plain login`` after issuing the ``ehlo`` command. If
  so then SASL dovecot is setup for postfix correctly.

  Press :guimenu:`ctrl + ]` to quit.

.. code-block:: bash
  :caption: Verify non-encrypted connections fail.

  telnet localhost 143
  telnet localhost 110
  telnet localhost 995

.. note::
  All unencrypted connections should fail with:

  .. pull-quote::
    Unable to connect to remote host: Connection refused.

  POP uses ports 110, 995.
  IMAP uses port 143.

.. code-block:: bash
  :caption: Verify IMAPS connections succeed.

  openssl s_client -connect localhost:993

.. note::
  Should get a ``* OK [{CAPABILITY LIST}] Dovecot ready``. Verify the
  ceritificate listed is the correct Let's Encrypt certificate for the domain
  used.

  Type ``C logout {ENTER}`` to quit.

.. code-block:: bash
  :caption: Verify encrypted SMTP connections succeed.

  openssl s_client -starttls smtp -crlf -connect localhost:587

.. note::
  Verify the ceritificate listed is the correct Let's Encrypt certificate for
  the domain used.

  :guimenu:`crtl + c` to quit.

Test Postfix Delivery
=====================
Ensure that users can receive mail. Test for users and alias cases.

.. code-block:: bash
  :caption: Telnet to postfix and send test emails.

  telnet localhost 25
  ehlo localhost
  mail from: root@localhost
  rcpt to: {USER}@{DOMAIN}
  data
  Subject: postfix text
  testing mail from postfix
  .
  quit

* Should receive ``220`` from the server if working when initially connecting.
* type ``.``, {ENTER}, then ``quit`` to send mail.
* Verify email sent is received (``mail`` command works here). May also be
  verified by looking at the user's maildir:
  ``/data/mail/data/{DOMAIN}/{USER}/new``.
* Also test emai aliases and virtual addresses.

.. _service-mail-validation:

Verify Proper Mail Configuration
================================
Tests must be green or the mail server is likely to be blacklisted by major
email services from receiving mail.

Use https://mxtoolbox.com to validate settings and ensure
:ref:`service-mail-ports` are forwarded on router.

* Test ``{DOMAIN}`` and ``mail.{DOMAIN}`` MX records.
   * All results **must** be green.
   * The correct IP must be shown.

* :guimenu:`SMTP Test` after looking up the MX record.
   * All results **must** be green, except ``PTR`` lookup.

.. note::
  The ``PTR`` record maps an IP address to a DNS name. This is used by **other**
  mail servers to verify mail received from your server is a valid email.

  This **must** be green (setup) if there is any intent to send mail to other
  services. Your ISP generally controls this, which implies that you have your
  ISP set this up for you or setup a hosted solution where you control the IP
  space.

  .. gtable:: `PTR`_ DNS Entry
    :header: Key,
             Value
    :c0:     Record,
             Name
             Target/Value/Data,
             TTL
    :c1:     PTR,
             {REVERSED IP OCTETS}.in-addr.arpa.,
             mail.{DOMAIN}.,
             300 seconds
    :no_key_title:
    :no_caption:
    :no_headers:
    :no_launch:

.. _PTR: https://community.spiceworks.com/topic/405534-dns-ptr-record-issues
.. _Setup DMARC: https://easydmarc.com/blog/how-to-fix-no-dmarc-record-found/
.. _detailed step-by-step setup guide: https://github.com/tomav/docker-mailserver/wiki/Configure-Accounts
.. _Email Docker and Documentation: https://hub.docker.com/r/tvial/docker-mailserver/
.. _setup helper script: https://github.com/tomav/docker-mailserver/blob/master/setup.sh
.. _DKIM data must be quoted: https://github.com/tomav/docker-mailserver/wiki/Configure-DKIM
.. _DMARC policies: https://help.returnpath.com/hc/en-us/articles/222438007-What-are-the-different-types-of-DMARC-policies-
.. _blackhole alias: http://madphilosopher.ca/2006/09/how-to-send-an-entire-domain-to-dev-null-in-postfix/