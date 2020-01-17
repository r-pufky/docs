.. _service-email-mta-configuration:

Configuration
#############
A `detailed step-by-step setup guide`_ walks through all of the following
configuration with more and options.

Only start the mailserver after all initial configuration has been completed,
and sufficient time has passed for DNS entries to update.

.. important::
  DNS changes should be applied to all domains on which the mail server will be
  hosting.

  Hosting multiple domains will generate different keys for each domain. Use the
  correct keys.

Add Initial User Accounts
*************************
Actual email accounts for users. These are accounts that will be logged into.

.. warning::
  These passwords should be unique for the user.

.. code-block:: bash
  :caption: Create email accounts for initial users (can use multiple domains).

  docker run --rm -e MAIL_USER={EMAIL} -e MAIL_PASS={PASS} -ti tvial/docker-mailserver:latest /bin/sh -c 'echo "$MAIL_USER|$(doveadm pw -s SHA512-CRYPT -u $MAIL_USER -p $MAIL_PASS)"' >> /data/mail/server/config/postfix-accounts.cf

.. note::
  If the docker container is already running, these can be added dynamically
  using the `setup helper script`_.

  .. code-block:: bash
    :caption: Add user account to running mailserver.

    ./setup.sh email add {EMAIL} {PASS}

Add Aliases
***********
Local system aliases for mail delivery.

.. code-block:: bash
  :caption: **0600 root root** ``/data/mail/config/postfix-aliases.cf``

  blackhole: /dev/null

.. note::
  `blackhole alias`_ is made to redirect specific mail to ``/dev/null``
  (discard).

Add Virtual Mailboxes
*********************
Maps additional email addresses to accounts on the system. This enables a single
user to have multiple email addresses, as well as catch-alls and blackhole
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

.. _service-email-dkim:

Use Dovecot for SMTP Authentication
***********************************
Set Dovecot to handle SMTP authentication for sending email. See
`SASL SMTP postfix options`_.

.. literalinclude:: source/postfix-main.cf
  :caption: **0600 root root** ``/data/mail/config/postfix-main.cf``

Set Global Sieve Filters (Optional)
***********************************
Apply global mail filtering rules before delivering mail.

See `configure sieve filters`_. In this example, enable vacation messages (even
for non-existing addresses to cover aliases) and send a message requesting the
sender to update email address.

.. literalinclude:: source/90-sieve.conf
  :caption: **0600 root root** ``/data/mail/config/90-sieve.conf``
  :emphasize-lines: 16

.. note::
  ``90-sieve.conf`` can be copied from the server to use as a base template.

  ``docker cp mail:/etc/dovecot/conf.d/90-sieve.conf .``

.. code-block:: yaml
  :caption: Docker Compose

  services:
    mail:
      volumes:
        - /data/mail/config/90-sieve.conf:/etc/dovecot/conf.d/90-sieve.conf

.. literalinclude:: source/before.dovecot.sieve
  :caption: **0644 root root** ``/data/mail/config/before.dovecot.sieve``

Generate :term:`DKIM` Config
****************************
:term:`DKIM` provides a method for validating a domain name identity that is
associated with an email message through cryptographic authentication.

.. code-block:: bash
  :caption: Generate DKIM Keys for mailserver.

  docker run --rm -v /data/mail/config:/tmp/docker-mailserver -ti tvial/docker-mailserver:latest generate-dkim-config

.. note::
  Regenerate when new domains are added to the mail server.

  Data is saved to ``/data/mail/config/opendkim/keys``

.. gtable:: DKIM DNS Entry
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
  :no_section:
  :no_launch:

.. note::
  The `DKIM data must be quoted`_ for it to be properly stored. The generated
  data *may* be broken across multiple lines. Just use the **content** within
  the parentheses and separate quoted data with a single space. This allows the
  public key to be properly re-assembled for services that do not support large
  TXT record data.

.. _service-email-spf:

Setup :term:`SPF` Policy
************************
Setup soft-failing for SPF policy enforcment.

.. gtable:: SPF DNS Entry
  :c0:     Record,
           Name,
           Target/Value/Data,
           TTL
  :c1:     TXT,
           mail.{DOMAIN}.,
           "v=spf1 mx ~all",
           300 seconds
  :no_key_title:
  :no_caption:
  :no_section:
  :no_launch:

.. note::
  The ``MX`` for ``mail.{DOMAIN}`` must exist for this to work. see
  :ref:`service-email-dns` for all DNS entries required for functioning service.

.. tip::
  Once server is verified to work, switch to ``enforce`` by changing the DNS
  record to: ``v-spf1 mx -all``.

.. _service-email-dmarc:

Setup :term:`DMARC` Policy
**************************
Protects from phishing attacks by validating ``From`` fields. `Setup DMARC`_ for
quarantine of flagged emails. The mailserver will automatically configure DMARC
using the ``POSTMASTER_ADDRESS`` in the docker compose definition.

.. gtable:: DMARC DNS Entry
  :c0:     Record,
           Name,
           Target/Value/Data,
           TTL
  :c1:     TXT,
           _dmarc.{DOMAIN}.,
           "v=DMARC1; p=quarantine; rua=mailto:postmaster@{DOMAIN}",
           300 seconds
  :no_key_title:
  :no_caption:
  :no_section:
  :no_launch:

.. note::
  Use ``p=none`` to test and ensure everything is working correctly.

  ``p=reject`` is the most strict but you must ensure everything is working
  properly; this should be the default when service is live.

  All `DMARC policies`_.

Setup SSL Certificates
**********************
The container will automtically setup all services correctly if provided the
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
**************************
POP3 should not be used, and unencrypted IMAP should be disabled.

.. literalinclude:: source/dovecot.cf
  :caption: **600 root root** ``/data/mail/config/dovecot.cf``
  :emphasize-lines: 3, 6, 13, 16

.. _service-email-dns:

Setup Mail DNS Entries
**********************
Setup DNS entries to allow for properly resolution of mail server. Redirect
{DOMAIN} to mail.{DOMAIN} for mail inquries.

.. gtable:: Root Domain Mail Redirect MX DNS Entry
  :c0:     Record,
           Name,
           Target/Value/Data,
           TTL
  :c1:     MX,
           {DOMAIN},
           10 mail.{DOMAIN}.,
           300 seconds
  :no_key_title:
  :no_caption:
  :no_section:
  :no_launch:

.. gtable:: Mail subdomain MX DNS Entry
  :c0:     Record,
           Name,
           Target/Value/Data,
           TTL
  :c1:     MX,
           {DOMAIN},
           10 {IP}.,
           300 seconds
  :no_key_title:
  :no_caption:
  :no_section:
  :no_launch:

.. gtable:: Mail subdomain A DNS Entry
  :c0:     Record,
           Name,
           Target/Value/Data,
           TTL
  :c1:     A,
           mail.{DOMAIN}.,
           10 {IP}.,
           300 seconds
  :no_key_title:
  :no_caption:
  :no_section:
  :no_launch:

.. gtable:: Wildcard subdomain MX DNS Entry
  :c0:     Record,
           Name,
           Target/Value/Data,
           TTL
  :c1:     MX,
           @.{DOMAIN}.,
           10 mail.{DOMAIN}.,
           21600 seconds
  :no_key_title:
  :no_caption:
  :no_section:
  :no_launch:

* Ensure DKIM DNS entry exists. See :ref:`service-email-dkim`.
* Ensure SPF DNS entry exists. See :ref:`service-email-spf`.
* Ensure DMARC DNS entry exists. See :ref:`service-email-dmarc`.

.. _Setup DMARC: https://easydmarc.com/blog/how-to-fix-no-dmarc-record-found/
.. _detailed step-by-step setup guide: https://github.com/tomav/docker-mailserver/wiki/Configure-Accounts
.. _setup helper script: https://github.com/tomav/docker-mailserver/blob/master/setup.sh
.. _DKIM data must be quoted: https://github.com/tomav/docker-mailserver/wiki/Configure-DKIM
.. _DMARC policies: https://help.returnpath.com/hc/en-us/articles/222438007-What-are-the-different-types-of-DMARC-policies-
.. _blackhole alias: http://madphilosopher.ca/2006/09/how-to-send-an-entire-domain-to-dev-null-in-postfix/
.. _SASL SMTP postfix options: http://www.postfix.org/SASL_README.html
.. _configure sieve filters: https://github.com/tomav/docker-mailserver/wiki/Configure-Sieve-filters
