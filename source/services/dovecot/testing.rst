.. _service-dovecot-testing:

Testing Dovecot
###############
Basic tests to ensure dovecot is working properly as an IMAPS MDA.

.. code-block:: bash
  :caption: Test SASL service.

  telnet localhost 25
  ehlo localhost

.. note::
  Should see a ``250 auth plain login``, if so then SASL dovecot is setup for
  postfix correctly.

.. code-block:: bash
  :caption: Verify IMAP service.

  telnet localhost imap2
  C logout

.. note::
  Should get a ``* OK [list of capabilities] Dovecot (ubuntu) ready``.

  ``C logout`` to quit.

.. code-block:: bash
  :caption: Verify non-encrypted connections fail, encrypted connections succeed.

  telnet localhost 143
  telnet localhost 110
  telnet localhost 995
  openssl s_client -connect localhost:993
  openssl s_client -starttls smtp -crlf -connect localhost:465

.. note::
  ``telnet`` (non-encrypted) logins should fail (imap, pop3, pop3s). ``openssl``
  logins should present certificate, connection (imaps).

  ``C logout`` to quit.