.. _service-dovecot-sieve:

Server-Side Mail Filtering (`sieve`_)
#####################################
This will enable users to setup server-side per-mailbox filters that are applied
automatically when email is `delivered by the MDA`_, which removes the need for
the user to setup a filtering on each MUA they use. This is in addition to any
filtering already applied at the MTA level.

Sieve filtering uses a `standard mail filtering language`_ and is `fairly easy
to learn`_.

.. code-block:: bash
  :caption: **0644 root root** ``/etc/dovecot/conf.d/15-lda.conf``

  postmaster_address = postmaster@%d
  Protocol lda {
    mail_plugins = $mail_plugins sieve
  }

.. code-block:: bash
  :caption: **0644 root root** ``/etc/dovecot/conf.d/90-sieve.conf``

  Plugin {
    sieve = file:~/sieve;active=~/.dovecot.sieve
    sieve_default = /var/lib/dovecot/sieve/default.sieve
    # Disable implicit recipient validation before responding to vacation messages
    # otherwise, vacation messages are not sent, as there are multiple emails to
    # a given email account in this example. You should have this disabled unless
    # needed.
    sieve_vacation_dont_check_recipient = yes
  }

.. code-block:: bash
  :caption: Create sieve location.

  sudo mkdir -p /var/lib/dovecot/sieve
  sudo chown -R dovecot:dovecot /var/lib/dovecot
  sudo chmod 755 /var/lib/dovecot /var/lib/dovecot/sieve

.. literalinclude:: source/default.sieve
  :caption: **0644 dovecot dovecot** ``/var/lib/dovecot/sieve/default.sieve``

.. note::
  This is an example sieve filter that will allow certain emails through to that
  user, and reject all others with an autoresponder. Any emails not sent to a
  specific email address are filtering into an alternative inbox.

  Run ``sievec`` to compile script for sieve to use (will expose any errors in
  script).

.. code-block:: bash
  :caption: Compile default.sieve for use.

  sudo sievec /var/lib/dovecot/sieve/default.sieve

.. note::
  You should see sieve entries on incoming mail in the ``/var/log/mail.log``.

.. _sieve: http://dikant.de/2012/05/21/setting-up-server-side-mail-filtering/
.. _delivered by the MDA: http://wiki2.dovecot.org/Pigeonhole
.. _standard mail filtering language: https://easyengine.io/tutorials/mail/server/sieve-filtering/
.. _fairly easy to learn: https://tty1.net/blog/2011/sieve-tutorial_en.html