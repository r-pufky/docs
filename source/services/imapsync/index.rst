.. _service-imapsync:

`imapsync`_
###########
Sync gmail to local imap server.

Uses :ref:`1804-server-base-install`.

imapsync Setup
**************
.. code-block:: bash
  :caption: Clone imapsync repo.

  git clone https://github.com/imapsync/imapsync

.. code-block:: bash
  :caption: Install perl dependencies.

  apt install libio-tee-perl libmail-imapclient-perl libterm-readkey-perl libunicode-string-perl libcrypt-openssl-rsa-perl libdata-uniqid-perl libjson-perl liblwp-online-perl libreadonly-perl libfile-copy-recursive-perl libio-socket-inet6-perl libsys-meminfo-perl libregexp-common-perl libfile-tail-perl libauthen-ntlm-perl libcgi-pm-perl libclass-load-perl libcrypt-ssleay-perl libdigest-hmac-perl libdist-checkconflicts-perl libencode-imaputf7-perl libio-compress-perl libio-socket-ssl-perl libmodule-scandeps-perl libnet-dbus-perl libnet-ssleay-perl libpar-packer-perl libtest-fatal-perl libtest-mock-guard-perl libtest-mockobject-perl libtest-pod-perl libtest-requires-perl libtest-simple-perl liburi-perl libtest-nowarnings-perl libtest-deep-perl libtest-warn-perl libjson-webtoken-perl cpanminus make

.. note::
  Meeting prerequisites can be determined by running
  ``./INSTALL.d/prerequisities_imapsync``.

.. code-block:: bash
  :caption: Create secured password files, enter passwords.

  touch .ssh/imapsync_{personal,gmail}
  chmod 0600 .ssh/imapsync_{personal,gmail}

.. note::
  * Remote server is gmail, uses application specific password. `Setup here`_.
  * Local server is your personal IMAP server. Use IMAP password.
  * Use ``.ssh`` directory here since it's already secured.

.. code-block:: bash
  :caption: Set password files readonly.

  chmod 0400 .ssh/imapsync_{personal,gmail}

Testing
*******
.. code-block:: bash
  :caption: Test sync to ensure connecting properly.

  ./imapsync --dry \
  --host1 imap.gmail.com --port1 993 --user1 {GMAIL EMAIL USER} --passfile1 ~/.ssh/imapsync_gmail --ssl1 \
  --host2 {YOUR IMAP SERVER} --port2 993 --user2 {YOUR IMAP USER} --passfile2 ~/.ssh/imapsync_personal --ssl2 \
  --subfolder2 gmail-archive --minage 30 --exitwhenover 2500000000 --delete --expunge1

* This will sync mail older than 30 days, and remove it from `gmail`_.
* Gmail has a download limit of 2.5GB's a day, this will safetly exit when
  reached.
* Ensure connections work, folders are identified, and local folder is set
  properly.

Install Service
***************
.. code-block:: bash
  :caption: Install imapsync to ``/opt/imapsync``.

  sudo git checkout-index -a -f --prefix=/opt/imapsync/

* Set ``/opt/imapsync`` permissions according to your system, ensure
  ``imapsync`` is executable.

.. code-block:: bash
  :caption: Create bash script using ``/opt/imapsync``, typically in ``~/bin``.

  #!/bin/bash

  /opt/imapsync/imapsync \
  --host1 imap.gmail.com --port1 993 --user1 {GMAIL EMAIL USER} --passfile1 ~/.ssh/imapsync_gmail --ssl1 \
  --host2 {YOUR IMAP SERVER} --port2 993 --user2 {YOUR IMAP USER} --passfile2 ~/.ssh/imapsync_personal --ssl2 \
  --subfolder2 gmail-archive --minage 30 --exitwhenover 2500000000 --delete --expunge1 \
  --nolog &>/dev/null

Add to `local crontab`_ to run nightly.

.. code-block:: bash
  :caption: ``crontab -e``

  * 3 * * * ~/bin/gmail_to_imap_sync

Removing Duplicates On Local Maildir
************************************
When sync'ing imap servers, you may end up `with duplicates`_ (e.g. if you have
copied a message to multiple accounts and they are now all synced to one
account.)

.. code-block:: bash
  :caption: Generate a list of duplicates.

  sudo apt install fdupes
  find USER_MAIL -type d -name cur -print0 | xargs -0 /usr/bin/fdupes -n > out

.. code-block:: bash
  :caption: Download / configure / run ``imap-de-dupe.go``.

  go get github.com/r-rpufky/docs/services/imapsync/imap-de-dupe.go
  go build src/github.com/r-rpufky/doc/services/imapsync/imap-de-dupe.go
  ./imap-de-dupe.go

:download:`imap-de-dupe.go <source/imap-de-dupe.go>`

.. rubric:: References

#. `Error installing imapsync <https://askubuntu.com/questions/539102/error-install-imapsync>`_

.. _imapsync: https://github.com/imapsync/imapsync
.. _gmail: http://imapsync.lamiral.info/FAQ.d/FAQ.Gmail.txt
.. _Setup here: https://security.google.com/settings/security/apppasswords
.. _local crontab: https://en.wikipedia.org/wiki/Cron
.. _with duplicates: https://blog.christosoft.de/2015/03/maildir-remove-duplicates/
