.. _service-mail-manual-testing:

Manual Testing
##############

Verify Services Locked Down
***************************
.. code-block:: bash
  :caption: Test SASL service.

  telnet localhost 25
  ehlo localhost

.. note::
  Should see ``250 auth plain login`` after issuing the ``ehlo`` command. This
  means that SASL dovecot is setup correctly.

  Press :cmdmenu:`ctrl + ]` to quit.

.. code-block:: bash
  :caption: Verify non-encrypted connections fail.

  telnet localhost 143
  telnet localhost 110
  telnet localhost 995

.. note::
  All unencrypted connections should fail with:

  .. pull-quote::
    Unable to connect to remote host: Connection refused.

  IMAP uses port 143.

  POP uses ports 110, 995.

.. code-block:: bash
  :caption: Verify IMAPS connections succeed.

  openssl s_client -connect localhost:993

.. note::
  Should get a ``* OK [{CAPABILITY LIST}] Dovecot ready``. Verify the
  ceritificate listed is the correct Let's Encrypt certificate for the domain
  used.

  :cmdmenu:`C logout {ENTER}` to quit.

.. code-block:: bash
  :caption: Verify encrypted SMTP connections succeed.

  openssl s_client -starttls smtp -crlf -connect localhost:587

.. note::
  Verify the certificate listed is the correct Let's Encrypt certificate for
  the domain used.

  :cmdmenu:`crtl + c` to quit.

Test Email Delivery
*******************
Ensure that users can receive mail. Test for users and alias cases.

.. note::
  ``{USER}`` and ``{PASS}`` should be `base64 encoded
  <https://www.base64decode.org/>`_. Use a local utility if testing actual
  passwords.

.. note::
  See `testing outbound email via command line <https://support.sugarcrm.com/Knowledge_Base/Email/Testing_Outbound_Email_Using_Command_Line/>`_
  for additional instructions.

.. code-block:: bash
  :caption: Telnet SMTP and send test emails.

  telnet localhost 25
  ehlo localhost
  auth login
  VXNlcm5hbWU6
  {USER}
  UGFzc3dvcmQ6
  {PASS}
  mail from: root@localhost
  rcpt to: {USER}@{DOMAIN}
  data
  Subject: postfix text
  testing mail from postfix
  .
  quit

.. code-block:: bash
  :caption: Verify SSL/TLS SMTP can send.

  openssl s_client -starttls smtp -crlf -connect mail.{DOMAIN}:587
  ehlo mail.{DOMAIN}
  auth login
  VXNlcm5hbWU6
  {USER}
  UGFzc3dvcmQ6
  {PASS}
  mail from: root@localhost
  rcpt to: {USER}@{DOMAIN}
  data
  Subject: postfix text
  testing mail from SSL/TLS SMTP
  .
  quit

* Should receive ``220`` from the server if working when initially connecting.
* type ``.``, {ENTER}, then ``quit`` to send mail.
* Verify email sent is received (``mail`` command works here). May also be
  verified by looking at the user's maildir:
  ``/data/mail/data/{DOMAIN}/{USER}/new``.
* Also test email aliases and virtual addresses.

Verify Proper Mail Configuration
********************************
Tests must be green or the mail server will be blacklisted by major email
services.

Use https://mxtoolbox.com to validate settings and ensure ports (25,587) are
exposed for testing.

* Test ``{DOMAIN}`` and ``mail.{DOMAIN}`` MX records.

   * All results **must** be green.
   * The correct IP must be shown.

* :cmdmenu:`SMTP Test` after looking up the MX record.

   * All results **must** be green, except ``PTR`` lookup.

.. note::
  The ``PTR`` record maps an IP address to a DNS name. This is used by **other**
  mail servers to verify mail received from your server is a valid email.

  This **must** be green if there is **any** intent to send mail to other
  services. Your ISP generally controls this, which implies that you have your
  ISP set this up for you or setup a hosted solution where you control the IP
  space.

`PTR <https://community.spiceworks.com/topic/405534-dns-ptr-record-issues>`_
DNS Entry

+-------------------+------------------------------------+
| Record            | PTR                                |
+===================+====================================+
| Name              | {REVERSED IP OCTETS}.in-addr.arpa. |
+-------------------+------------------------------------+
| Target/Value/Data | mail.{DOMAIN}.                     |
+-------------------+------------------------------------+
| TTL               | 300 seconds                        |
+-------------------+------------------------------------+
