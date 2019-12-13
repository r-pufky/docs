.. _service-dovecot-setup:

`Dovecot Setup`_
################
This will configure dovecot as an IMAPS server, disabling POP and non-SSL
connections. Accounts are based off of local accounts, using non-local passwords
for authentication.

Sieve is used to do server-side mailbox filtering, in additional to what the MTA
already does. This allows for vacation messages as well as custom filtering and
responses.

.. code-block:: bash
  :caption: Install core packages.

  sudo apt remove --purge dovecot-core dovecot-imapd
  sudo rm -rfv /etc/dovecot
  sudo apt install dovecot-core dovecot-imapd dovecot-sieve dovecot-managesieved

.. note::
  Create SSL certificate; use your {HOST}.

.. code-block:: bash
  :caption: **0644 root root** ``/etc/postfix/main.cf``

  mailbox_command = /usr/lib/dovecot/deliver

.. literalinclude:: source/10-master.conf
  :caption: **0644 root root** ``/etc/dovecot/conf.d/10-master.conf``

.. code-block:: bash
  :caption: **0644 root root** ``/etc/dovecot/conf.d/10-auth.conf``

  auth_mechanisms = plain login
  #!include auth-system.conf.ext
  !include auth-passwdfile.conf.ext

.. code-block:: bash
  :caption: **0644 root root** ``/etc/dovecot/conf.d/10-mail.conf``

  mail_location: maildir:/home/%u/Maildir

.. code-block:: bash
  :caption: **0644 root root** ``/etc/dovecot/conf.d/10-ssl.conf``

  ssl = required
  ssl_cert = </etc/dovecot/dovecot.pem
  ssl_key = </etc/dovecot/private/dovecot.pem

.. note::
  These certs can be the same as postfix, useful when you get valid certs.

  The ``</`` is not a mistake, it is required to specify file location.

.. code-block:: bash
  :caption: **0644 root root** ``/etc/dovecot/conf.d/15-lda.conf``

  postmaster_address = postmaster@%d
  Protocol lda {
    mail_plugins = $mail_plugins
  }

.. code-block:: bash
  :caption: **0644 root root** ``/etc/dovecot/conf.d/20-imap.conf``

  protocol imap {
    imap_client_workarounds = tb-extra-mailbox-sep
  }

.. code-block:: bash
  :caption: **0644 root root** ``/etc/dovecot/conf.d/auth-passwdfile.conf.ext``

  passdb {
    driver = passwd-file
    args = scheme=SHA512-CRYPT username_format=%u /etc/imap.passwd
  }

  userdb {
    driver = passwd-file
    args = username_format=%u /etc/imap.passwd
  }

See `Dovecot password schemes`_.

.. code-block:: bash
  :caption: Create passwd DB and enable Dovecot.

  sudo touch /etc/imap.passwd
  sudo chown dovecot:dovecot /etc/imap.passwd
  sudo chmod 0400 /etc/imap.passwd
  sudo postconf -e 'smtpd_sasl_type = dovecot'
  sudo postconf -e 'smtpd_sasl_auth_enable = yes'
  sudo postconf -e 'smtpd_recipient_restrictions = permit_sasl_authenticated,permit_mynetworks,reject_unauth_destination'
  sudo postconf -e 'smtpd_sasl_path = private/auth'
  sudo service postfix restart
  sudo service dovecot restart

* Restarting postfix will pickup dovecot as the MDA instead of postfix/maildir
  (dovecot still delivers to maildir).
* LDA (local delivery agent) is what dovecot uses for it’s MDA; it also provides
  IMAPS.
* Tailing ``mail.log`` and watching for incoming message delivery, should be
  sent to ``/usr/lib/dovecot/deliver`` and appear in your maildir.

.. rubric:: References

#. `Postfix + Dovecot + SASL <https://help.ubuntu.com/community/PostfixDovecotSASL>`_
#. `Spamassassin with Dovecot <http://www.townx.org/index.php?q=blog/elliot/simple_spamassassin_setup_with_postfix_and_dovecot_on_ubuntu_breezy>`_

.. _Dovecot Setup: https://www.binarytides.com/install-postfix-dovecot-debian/
.. _Dovecot password schemes: https://wiki.dovecot.org/Authentication/PasswordSchemes