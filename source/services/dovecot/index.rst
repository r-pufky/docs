.. _service-dovecot:

Dovecot
#######
Mail Delivery Agent (MDA) Setup.

Uses :ref:`1804-server-base-install`.

* Disable ports **25/465/993** on firewall until configuration is final
  otherwise you may get email delivered while you are configuring server.
* example.com = your primary domain.
* example2.com = your secondary domain, if applicable.
* X.X.X.X/24 = your server subnet (this is defaulting to a class C CIDR).
* user = a local linux user account.
* alias@example.com = an email address (alias) for a given domain.

See :ref:`service-dovecot-glossary` for mail terms.

#. :ref:`service-dovecot-setup`.
#. :ref:`service-dovecot-testing`.
#. :ref:`service-dovecot-account`.
#. :ref:`service-dovecot-sieve`.

.. toctree::
   :hidden:
   :maxdepth: -1

   setup
   testing
   account
   sieve
   migration
   glossary