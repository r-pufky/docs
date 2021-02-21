.. _service-email-mta-setup:

Setup
#####
The :term:`MTA` handles the transmission of email to and from the system, while
the :term:`MDA` handles delivery of email on that system.

In this configuration, *postfix* is the MTA and *dovecot* is the MDA.

See `Email Docker and Documentation`_.

.. _service-email-ports:

Ports
*****
.. ports:: Email Ports
  :value0:  25, {TCP},  {PUBLIC}, :term:`MTA` SMTP Mail Relay (Recieve mail from
                                  other mail servers)
  :value1: 110, {TCP}, {DISABLE}, POP3 plaintext client
  :value2: 143, {TCP}, {DISABLE}, StartTLS IMAP client
  :value3: 465, {TCP}, {DISABLE}, SSL MUA email submission (defacto standard)
  :value4: 587, {TCP}, {EXPOSED}, TLS MUA email submission (RFC 2476)
  :value5: 993, {TCP}, {EXPOSED}, TLS/SSL IMAP client
  :value6: 995, {TCP}, {DISABLE}, TLS/SSL POP3 client
  :open:

  .. note::
    POP3 and non TLS/SSL connections should be considered compromised by
    default. If enabling remote :term:`MUA` connections, Use **TLS/SSL IMAP**.

    Port ``465`` is a defacto standard for client email submissions before the
    creation of `RFC 2476`_. It is safe to disable this unless you are forcing
    connections to this port. Read `more about ports here`_.

Files
*****
.. files:: Email Files
  :value0: /var/mail, Email storage location
  :value1: /var/mail-state, Mail server state
  :value2: /var/log/mail, Mail logs
  :value3: /tmp/docker-mailserver, Mail configuration files
  :value4: /etc/letsencrypt, Let's Encrypt certificates to use for SSL
  :open:

.. note::
  Documentation assumes the following DNS preferences:

  * ``mail.{DOMAIN}`` resolves to the mail server IP, MX records (e.g.
    mail.example.com).
  * Mail accounts are ``{USER}@{DOMAIN}``.

.. _service-email-mta-docker:

Docker Creation
***************
.. warning::
  Create the compose file but do **not** start the docker container.
  Pre-existing configurations can be started normally.

  Initial configuration must be done before launching the conatiner so that
  all auto-generated setup for domains, accounts, aliases and SPF/DKIM/SSL are
  generated and configured correctly.

  See :ref:`service-email-mta-configuration`.

  Delete configuration files to reset if started without configuration.

* Mail containers should be placed on a separate isolated network as the is
  exposed to the world.
* See `Docker options`_ for detailed docker environment setup. Explicit options
  set even if default to remain consistent if any changes do occur.
* Dovecot manages SASL authentication, so ``SASLAUTHD`` is disabled.

.. code-block:: yaml
  :caption: Docker Compose

  mail:
    image: tvial/docker-mailserver:latest
    hostname: mail
    domainname: {DOMAIN}
    stop_grace_period: 1m
    restart: unless-stopped
    ports:
      - "25:25"
      - "587:587"
      - "993:993"
    environment:
      - DEFAULT_RELAY_HOST=''
      - DMS_DEBUG=0
      - DOVECOT_MAILBOX_FORMAT=maildir
      - ENABLE_CLAMAV=1
      - ENABLE_ELK_FORWARDER=0
      - ENABLE_FAIL2BAN=0
      - ENABLE_FETCHMAIL=0
      - ENABLE_LDAP=''
      - ENABLE_MANAGESIEVE=1
      - ENABLE_POP3=0
      - ENABLE_POSTFIX_VIRTUAL_TRANSPORT=''
      - ENABLE_POSTGREY=1
      - ENABLE_SASLAUTHD=0
      - ENABLE_SPAMASSASSIN=1
      - ENABLE_SRS=1
      - LOGROTATE_INTERVAL=weekly
      - LOGWATCH_INTERVAL=weekly
      - ONE_DIR=1
      - PERMIT_DOCKER=host
      - PFLOGSUMM_TRIGGER=logrotate
      - POSTFIX_DAGENT=''
      - POSTFIX_MAILBOX_SIZE_LIMIT=0
      - POSTFIX_MESSAGE_SIZE_LIMIT=10480000
      - POSTGREY_AUTO_WHITELIST_CLIENTS=0
      - POSTGREY_DELAY=300
      - POSTGREY_MAX_AGE=35
      - POSTGREY_TEXT=Delayed by postgrey
      - POSTMASTER_ADDRESS=postmaster@{DOMAIN}
      - POSTSCREEN_ACTION=enforce
      - RELAY_HOST=''
      - SA_KILL=6.31
      - SA_SPAM_SUBJECT=***SPAM***
      - SA_TAG2=6.31
      - SA_TAG=3.0
      - SASL_PASSWD=''
      - SASLAUTHD_MECH_OPTIONS=''
      - SASLAUTHD_MECHANISMS=''
      - SMTP_ONLY=''
      - SPOOF_PROTECTION=1
      - SRS_EXCLUDE_DOMAINS=''
      - SRS_SENDER_CLASSES=envelope_sender,header_sender
      - SSL_TYPE=letsencrypt
      - TLS_LEVEL=modern
      - TZ=America/Los_Angeles
      - VIRUSMAILS_DELETE_DELAY=7
    volumes:
      - /data/mail:/var/mail
      - /data/mail/server/state:/var/mail-state
      - /var/log/mail:/var/log/mail
      - /data/mail/server/config:/tmp/docker-mailserver
      - /data/letsencrypt:/etc/letsencrypt:ro
      - /etc/localtime:/etc/localtime:ro

.. note::
  ``NET_ADMIN`` capability is required if ``fail2ban`` is run within the
  container. Alternatively, the mail logs can be mounted externally and
  ``fail2ban`` run in an isolated container.
  See :ref:`service-fail2ban-system`.

  ``SYS_PTRACE`` capability is required for debugging as well as detecting
  a hung procress; disabling might allow container processes to die and not
  restart.

  The `security vulnerability with SYS_PTRACE`_ is patched for all **4.8+**
  Linux kernels.

fail2ban Setup
**************
Enable fail2ban for :term:`MTA` and :term:`MDA` services.

Use :ref:`service-fail2ban-system` for the base fail2ban service setup.

.. code-block:: yaml
  :caption: Add read-only mail logs to Docker Compose (f2b-system)

  f2b-system:
    volumes:
      - /var/log/mail:/var/log/mail:ro

Custom filters generated by `extracting them from the mail docker image`_ and
adding as additional rules for the separate fail2ban container.

.. literalinclude:: source/mail-dovecot.conf
  :caption: **0644 root root** ``/data/filter.d/mail-dovecot.conf``
  :emphasize-lines: 13

.. note::
  Dovecot filter needs to be adjusted to use the ``<HOST>`` as the default
  filter will fail by default.

  Patched, pending release: https://github.com/tomav/docker-mailserver/pull/1388

.. literalinclude:: source/mail-postfix.conf
  :caption: **0644 root root** ``/data/filter.d/mail-postfix.conf``

.. literalinclude:: source/mail-postfix-rbl.conf
  :caption: **0644 root root** ``/data/filter.d/mail-postfix-rbl.conf``

.. literalinclude:: source/mail-postfix-sasl.conf
  :caption: **0644 root root** ``/data/filter.d/mail-postfix-sasl.conf``

.. literalinclude:: source/dovecot.conf
  :caption: **0644 root root** ``/data/jail.d/dovecot.conf``

.. literalinclude:: source/postfix.conf
  :caption: **0644 root root** ``/data/jail.d/postfix.conf``

* Restart ``f2b-system``.

.. _Email Docker and Documentation: https://hub.docker.com/r/tvial/docker-mailserver/
.. _RFC 2476: https://tools.ietf.org/html/rfc2476
.. _Docker options: https://github.com/tomav/docker-mailserver/blob/master/README.md
.. _security vulnerability with SYS_PTRACE: https://github.com/tomav/docker-mailserver/issues/1057
.. _more about ports here: https://blog.mailtrap.io/smtp-ports-25-465-587-used-for/
.. _extracting them from the mail docker image: https://github.com/tomav/docker-mailserver/tree/master/target/fail2ban
